import pyaudio
import time

class AudioPlayer:
    def __init__(self, channel=1, rate=16000):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=channel,
            rate=rate,
            output=True
        )

    def play(self, audio_data):
        self.stream.write(audio_data)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()