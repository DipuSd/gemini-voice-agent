import sys
from PySide6.QtWidgets import QApplication
from chatUI import ChatUI
from Agent import VoiceAgent
from ChatController import ChatController


app = QApplication(sys.argv)

view = ChatUI()
controller = ChatController(view)

view.show()

sys.exit(app.exec())
