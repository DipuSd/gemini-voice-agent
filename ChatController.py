import pyaudio
from Agent import VoiceAgent
from mic_stream import MicStream
from google.adk.agents.live_request_queue import LiveRequestQueue

class ChatController:
    def __init__(self, view):
        self.view = view
        self.agent = VoiceAgent()
        self.agent.start()
        self.mic = MicStream(self.agent.live_queue)
        self.state = "LISTENING"
        self.ai_speaking = False

        self.pa = pyaudio.PyAudio()
        self.audio_out = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=24000,
            output=True
        )
        self.view.toggle_session_requested.connect(self.toggle_mic)
        self.agent.signal_text.connect(self.view.display_message)
        self.agent.signal_status.connect(self.view.update_status)

    def toggle_mic(self, active):
        if active:
            self.state = "LISTENING"
            print("mic active")
            self.view.update_status("🎤 Listening...")
            self.mic.start()
        else:
            self.mic.stop()
            self.state = "IDLE"
            self.view.update_status("Stopped")


