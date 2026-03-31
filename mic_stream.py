import threading
import pyaudio
from google.genai import types
import audioPlayer
import numpy as np
import time

class MicStream:
    def __init__(self, live_queue):
        self.live_queue = live_queue
        self.running = False
        self.pa = pyaudio.PyAudio()
        self.rate = 16000
        self.chunk = 320
        self.speaking = False
        self.silence_threshold = 500
        self.silence_time = 0.5
        self.last_speech_time = 0


    def start(self):
        if self.running:
            return
        self.running = True

        self.stream  = self.pa.open(
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

    def _loop(self):
        while self.running:
            audio = self.stream.read(self.chunk, exception_on_overflow=False)
            samples = np.frombuffer(audio, dtype=np.int16)
            energy = np.abs(samples).mean()
            now = time.time()

            if energy > self.silence_threshold:
                if not self.speaking:
                    self.live_queue.send_activity_start()
                    self.speaking = True
                    self.last_speech_time = now
            elif self.speaking and (now - self.last_speech_time) > self.silence_time:
                self.live_queue.send_activity_end()
                self.speaking = False

            audio_blob = types.Blob(
                data=audio,
                mime_type="audio/pcm;rate=16000"
            )
            self.live_queue.send_realtime(audio_blob)


            #
            # now = time.time()
            #
            # if energy > self.silence_threshold:
            #     print("speaking")
            #     self.last_speech_time = now
            #     self.speaking = True
            #
            #     audio_blob = types.Blob(
            #         data=audio,
            #         mime_type="audio/pcm;rate=16000"
            #     )
            #     self.live_queue.send_realtime(audio_blob)
            # else:
            #     if self.speaking and (now - self.last_speech_time) > self.silence_duration:
            #         self.speaking = False
            #         print("speech ended")
            #         time.sleep(0.3)
