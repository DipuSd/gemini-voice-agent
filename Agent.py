import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.agents import LiveRequestQueue
from voice_agent.agent import voice_agent
from google.genai import types
from google.adk.runners import RunConfig
from PySide6.QtCore import Signal, QThread
import pyaudio

load_dotenv()

class VoiceAgent(QThread):
    signal_text = Signal(str, str)
    signal_status = Signal(str)
    signal_speaking = Signal(bool)

    def __init__(self):
        super().__init__()
        self.loop = None

        self.session_service = InMemorySessionService()
        self.app_name = "Voice_assistant_app"
        self.user_id = "test_user"
        self.session_id = str(uuid.uuid4())
        self.live_queue = LiveRequestQueue()
        self.pa = pyaudio.PyAudio()
        self.audio_out = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=24000,
            output=True
        )

    def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self._start())



    async def _start(self):
        await self.session_service.create_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=self.session_id
        )
        runner = Runner(
            agent=voice_agent,
            app_name=self.app_name,
            session_service=self.session_service
        )
        speech = types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Puck"
                )
            )
        )
        config = RunConfig(
            response_modalities=[types.Modality.AUDIO],
            speech_config=speech,
            output_audio_transcription=types.AudioTranscriptionConfig()

        )
        connection = runner.run_live(
            user_id=self.user_id,
            session_id=self.session_id,
            live_request_queue=self.live_queue,
            run_config=config
        )

        async for event in connection:
            await self._handle_event(event)


    async def _handle_event(self, event):
        print(event)
        if event.content:
            for part in event.content.parts:
                if hasattr(part, "inline_data") and part.inline_data:
                    self.signal_speaking.emit(True)
                    audio_bytes = part.inline_data.data
                    self.audio_out.write(audio_bytes)
                    self.signal_speaking.emit(False)
        if event.output_transcription and event.output_transcription.finished:
            text = event.output_transcription.text
            role = "AI" if event.author != "user" else "You"
            self.signal_text.emit(role, text)


    def send_text(self, text):
        content = types.Content(
            role="user",
            parts=[types.Part(text=text)]
        )
        self.live_queue.send_content(content)










