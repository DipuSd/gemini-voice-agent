from Agent import VoiceAgent
from mic_stream import MicStream

class ChatController:
    def __init__(self, view):
        self.view = view
        self.agent = VoiceAgent()
        self.agent.start()
        self.mic = MicStream(self.agent.live_queue)
        self.state = "LISTENING"
        self.view.toggle_session_requested.connect(self.toggle_mic)
        self.agent.signal_text.connect(self.view.display_message)
        self.agent.signal_status.connect(self.view.update_status)
        self.agent.signal_speaking.connect(self.mic.set_pause)

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


