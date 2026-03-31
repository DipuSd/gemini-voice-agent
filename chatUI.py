from PySide6.QtWidgets import (
    QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QApplication)
from PySide6.QtCore import Qt,Signal
import sys

class ChatUI(QMainWindow):
    toggle_session_requested = Signal(bool)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Voice agent AI")
        self.resize(450, 600)

        layout = QVBoxLayout()

        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.mic_button = QPushButton("🎤 Start Session")
        self.mic_button.setCheckable(True)
        self.mic_button.setFixedHeight(60)
        self.mic_button.clicked.connect(self._on_mic_clicked)

        layout.addWidget(self.status_label)
        layout.addWidget(self.chat_area)
        layout.addWidget(self.mic_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def _on_mic_clicked(self):
        is_active = self.mic_button.isChecked()
        self.toggle_session_requested.emit(is_active)
        self.mic_button.setText("🛑 Stop" if is_active else "🎤 Start Session")

    def display_message(self, role, text):
        color = "#2980b9" if role == "You" else "#27ae60"
        self.chat_area.append(f"<b style='color:{color}'>{role}:</b> {text}")

    def update_status(self, text):
        self.status_label.setText(text)
        


