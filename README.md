# Voice Agent with Google ADK & Qt6

A lightweight **voice assistant** built with **Google ADK** and **Qt6**, capable of transcribing speech and displaying AI-generated responses in real time.

---

## Features

* **Toggleable Microphone:** Enable or disable live voice input directly from the UI.
* **Transcription & Responses:** Displays AI responses in a chat-style interface.
* **Continuous Agent Thread:** Agent logic runs in a dedicated Qt thread.
* **Background Mic Daemon:** Microphone streams audio in a separate daemon thread for real-time processing.
* **Powered by Gemini Live Model:** Uses Google’s Gemini Live model for speech-to-text and AI responses.

---

## Architecture

* **Main Qt Loop:** Handles UI events and user interactions.
* **Agent Thread (Qt Thread):** Continuously runs AI logic and generates responses.
* **Mic Daemon Thread:** Keeps the microphone live and streams audio to the agent.

The design is modular and ready for future enhancements like **manual Voice Activity Detection** and **interruptible responses**.

---

## Future Improvements

* **Manual Voice Activity Detection:** Currently relies on Gemini Live built-in VAD.
* **Interruptible Responses:** Allow the user to interrupt the agent during response generation.

---

## Getting Started

### Prerequisites

* Python 3.11+
* [UV]() (Python package manager)

### Setup

1. Create a `.env` file from the example:

   <pre class="overflow-visible! px-0!" data-start="1697" data-end="1731"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="w-full overflow-x-hidden overflow-y-auto pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>cp .env.example .env</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

   Add your Google Ai Api Key.
2. Sync dependencies:

   <pre class="overflow-visible! px-0!" data-start="1804" data-end="1825"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="w-full overflow-x-hidden overflow-y-auto pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>uv sync</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>
3. Run the application:

   <pre class="overflow-visible! px-0!" data-start="1854" data-end="1882"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="w-full overflow-x-hidden overflow-y-auto pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python main.py</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* Use the **UI toggle** to enable or disable the microphone.
* Speak into the mic to see your transcribed text and AI response in the chat panel.
