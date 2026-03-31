from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini

audio_model = Gemini(
    model="gemini-2.5-flash-native-audio-preview-12-2025",
    use_interaction_api=True,
)

voice_agent=Agent(
    model=audio_model,
    name="voice_agent",
    description='A helpful voice assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge only in english',
)
