import threading
import pyaudio
from google.genai import types
import time

class MicStream:
    def __init__(self, live_queue):
        self.live_queue = live_queue
        self.running = False
        self.pause_recording = False
        self.pa = pyaudio.PyAudio()
        self.rate = 16000
        self.chunk = 512
        self.audio_out = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=24000,
            output=True
        )

    def start(self):
        if self.running:
            return
        self.running = True

        self.stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk
        )
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()
        print("mic started")

    def stop(self):
        self.running = False

    def set_pause(self, paused: bool):
        self.pause_recording = paused

    def _loop(self):
        while self.running:
            if self.pause_recording:
                print("mic paused")
                time.sleep(0.01)
                continue
            audio = self.stream.read(self.chunk, exception_on_overflow=False)
            audio_blob = types.Blob(
                data=audio,
                mime_type="audio/pcm;rate=16000"
            )
            self.live_queue.send_realtime(audio_blob)

