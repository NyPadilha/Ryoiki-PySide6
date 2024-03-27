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

# qt core
from qt_core import *
from gui.pages.ui_pages import Ui_StackedWidget


# main window
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # initial parameters
        parent.setMinimumSize(700, 400)
        parent.showMaximized()

        # central widget
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #333")

        # main layout
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # title bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)

        # content
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #444")

        # content layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 20px; color: #FFF")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.home_page)

        # add widgets to content layout
        self.content_layout.addWidget(self.pages)

        # add widgets to main layout
        self.main_layout.addWidget(self.top_bar)
        self.main_layout.addWidget(self.content)

        # set central widget
        parent.setCentralWidget(self.central_frame)
