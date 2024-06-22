import sys
from PySide6.QtWidgets import QApplication, QWidget
from src.view import Ui_Widget
from src.services import JsonLoader
from src.controller import NpcController

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.jsonloader = JsonLoader(self.ui)
        self.npccontroller = NpcController(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
