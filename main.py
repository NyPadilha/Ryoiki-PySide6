# ///////////////////////////////////////////////////////////////
#
# BY: NyPadilha
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 0.0.1
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# imports
import sys
# import os
from qt_core import *
from gui.windows.main_window.ui_main_window import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ryoiki")

        # setup main window
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
