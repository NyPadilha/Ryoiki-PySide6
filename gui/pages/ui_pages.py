# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesVZZBUk.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(1113, 809)
        self.watch_list = QWidget()
        self.watch_list.setObjectName(u"watch_list")
        self.verticalLayout_6 = QVBoxLayout(self.watch_list)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.watch_list)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.comboBox = QComboBox(self.watch_list)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_6.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.watch_list)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_6.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.watch_list)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_6.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.watch_list)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_6.addWidget(self.comboBox_4)

        self.comboBox_5 = QComboBox(self.watch_list)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_6.addWidget(self.comboBox_5)

        StackedWidget.addWidget(self.watch_list)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout = QVBoxLayout(self.home_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.home_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContents = QWidget()
        self.scrollAreaContents.setObjectName(u"scrollAreaContents")
        self.scrollAreaContents.setGeometry(QRect(0, 0, 1097, 1260))
        self.scrollAreaContents.setStyleSheet(u"background-color: rgb(58, 58, 58);\n"
"color: rgb(255, 255, 255);\n"
"font: 700 12pt \"Calibri\";")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaContents)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.cover = QFrame(self.scrollAreaContents)
        self.cover.setObjectName(u"cover")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cover.sizePolicy().hasHeightForWidth())
        self.cover.setSizePolicy(sizePolicy)
        self.cover.setMinimumSize(QSize(0, 420))
        self.cover.setMaximumSize(QSize(16777215, 420))
        self.cover.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #111111, stop:0.495 #111111, stop:0.505 #3A3A3A, stop:1 #3A3A3A);\n"
"")
        self.cover.setFrameShape(QFrame.NoFrame)
        self.cover.setFrameShadow(QFrame.Raised)
        self.cover.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.cover)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 0, 50, 0)
        self.time_frame = QFrame(self.cover)
        self.time_frame.setObjectName(u"time_frame")
        sizePolicy.setHeightForWidth(self.time_frame.sizePolicy().hasHeightForWidth())
        self.time_frame.setSizePolicy(sizePolicy)
        self.time_frame.setMinimumSize(QSize(300, 125))
        self.time_frame.setMaximumSize(QSize(300, 125))
        self.time_frame.setStyleSheet(u"background-color: rgb(17, 17, 17);\n"
"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);\n"
"box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.time_frame.setFrameShape(QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QFrame.Raised)
        self.time_frame.setLineWidth(1)

        self.horizontalLayout.addWidget(self.time_frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.profile_frame = QFrame(self.cover)
        self.profile_frame.setObjectName(u"profile_frame")
        sizePolicy.setHeightForWidth(self.profile_frame.sizePolicy().hasHeightForWidth())
        self.profile_frame.setSizePolicy(sizePolicy)
        self.profile_frame.setMinimumSize(QSize(150, 160))
        self.profile_frame.setMaximumSize(QSize(200, 210))
        self.profile_frame.setStyleSheet(u"background-color: rgb(17, 17, 17);\n"
"border: 1px solid;\n"
"border-radius: 7px;\n"
"border-color: rgb(0, 0, 0);\n"
"box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.profile_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QFrame.Raised)
        self.profile_frame.setLineWidth(1)

        self.horizontalLayout.addWidget(self.profile_frame)


        self.verticalLayout_7.addWidget(self.cover)

        self.content = QFrame(self.scrollAreaContents)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.content.setLineWidth(0)
        self.verticalLayout_8 = QVBoxLayout(self.content)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.container_1 = QFrame(self.content)
        self.container_1.setObjectName(u"container_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.container_1.sizePolicy().hasHeightForWidth())
        self.container_1.setSizePolicy(sizePolicy1)
        self.container_1.setFrameShape(QFrame.StyledPanel)
        self.container_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container_1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(100, 0, 100, 0)
        self.skills = QFrame(self.container_1)
        self.skills.setObjectName(u"skills")
        self.skills.setFrameShape(QFrame.StyledPanel)
        self.skills.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.skills)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.skills)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"font: 700 16pt;")

        self.verticalLayout_9.addWidget(self.label_6)

        self.frame = QFrame(self.skills)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(16777215, 300))
        self.frame.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.skills)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.central = QFrame(self.container_1)
        self.central.setObjectName(u"central")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.central.sizePolicy().hasHeightForWidth())
        self.central.setSizePolicy(sizePolicy2)
        self.central.setFrameShape(QFrame.StyledPanel)
        self.central.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.central)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.central)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(150, 150))
        self.frame_7.setMaximumSize(QSize(150, 150))
        self.frame_7.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_7, 2, 3, 1, 1)

        self.frame_3 = QFrame(self.central)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(150, 150))
        self.frame_3.setMaximumSize(QSize(150, 150))
        self.frame_3.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.central)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(150, 150))
        self.frame_6.setMaximumSize(QSize(150, 150))
        self.frame_6.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_6, 1, 3, 1, 1)

        self.frame_5 = QFrame(self.central)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QSize(150, 150))
        self.frame_5.setMaximumSize(QSize(150, 150))
        self.frame_5.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_5, 2, 2, 1, 1)

        self.frame_2 = QFrame(self.central)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(150, 150))
        self.frame_2.setMaximumSize(QSize(150, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 2, 1, 1, 1)

        self.frame_4 = QFrame(self.central)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(150, 150))
        self.frame_4.setMaximumSize(QSize(150, 150))
        self.frame_4.setStyleSheet(u"background-color: rgb(17, 17, 17);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)

        self.label_7 = QLabel(self.central)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setStyleSheet(u"font: 700 16pt;")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.central)


        self.verticalLayout_8.addWidget(self.container_1)

        self.container_2 = QFrame(self.content)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setFrameShape(QFrame.StyledPanel)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.container_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.container_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 500))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_8.addWidget(self.container_2)


        self.verticalLayout_7.addWidget(self.content)

        self.scrollArea.setWidget(self.scrollAreaContents)

        self.verticalLayout.addWidget(self.scrollArea)

        StackedWidget.addWidget(self.home_page)
        self.finance = QWidget()
        self.finance.setObjectName(u"finance")
        self.verticalLayout_2 = QVBoxLayout(self.finance)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.finance)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        StackedWidget.addWidget(self.finance)
        self.training = QWidget()
        self.training.setObjectName(u"training")
        self.verticalLayout_4 = QVBoxLayout(self.training)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.training)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        StackedWidget.addWidget(self.training)
        self.metas = QWidget()
        self.metas.setObjectName(u"metas")
        self.verticalLayout_3 = QVBoxLayout(self.metas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.metas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        StackedWidget.addWidget(self.metas)
        self.travels = QWidget()
        self.travels.setObjectName(u"travels")
        self.verticalLayout_5 = QVBoxLayout(self.travels)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.travels)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        StackedWidget.addWidget(self.travels)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label_5.setText(QCoreApplication.translate("StackedWidget", u"Watch List", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("StackedWidget", u"New Item", None))

        self.label_6.setText(QCoreApplication.translate("StackedWidget", u"Skills", None))
        self.label_7.setText(QCoreApplication.translate("StackedWidget", u"Central", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"Finance", None))
        self.label_3.setText(QCoreApplication.translate("StackedWidget", u"Training", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"Metas", None))
        self.label_4.setText(QCoreApplication.translate("StackedWidget", u"Travel", None))
    # retranslateUi

