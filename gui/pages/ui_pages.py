# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'pagesWSFxJM.ui'
##
# Created by: Qt User Interface Compiler version 6.6.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(1097, 689)
        self.watch_list = QWidget()
        self.watch_list.setObjectName(u"watch_list")
        self.verticalLayout_6 = QVBoxLayout(self.watch_list)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.watch_list)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout_6.addWidget(self.label_5)

        StackedWidget.addWidget(self.watch_list)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.home_page)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_spacer = QSpacerItem(
            20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.top_spacer)

        self.title = QLabel(self.home_page)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout.addWidget(self.title)

        self.verticalSpacer = QSpacerItem(
            20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_1 = QFrame(self.home_page)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setEnabled(True)
        self.btn_1.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        self.btn_1.setFont(font1)
        self.btn_1.setFrameShape(QFrame.NoFrame)  # type: ignore
        self.btn_1.setFrameShadow(QFrame.Raised)  # type: ignore
        self.btn_1.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.btn_1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(
            QLayout.SetDefaultConstraint)  # type: ignore
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.watch_list_btn = QPushButton(self.btn_1)
        self.watch_list_btn.setObjectName(u"watch_list_btn")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.watch_list_btn.sizePolicy().hasHeightForWidth())
        self.watch_list_btn.setSizePolicy(sizePolicy)
        self.watch_list_btn.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        self.watch_list_btn.setFont(font2)

        self.horizontalLayout.addWidget(self.watch_list_btn)

        self.verticalLayout.addWidget(self.btn_1)

        self.btn_2 = QFrame(self.home_page)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(0, 0))
        self.btn_2.setFrameShape(QFrame.NoFrame)  # type: ignore
        self.btn_2.setFrameShadow(QFrame.Raised)  # type: ignore
        self.horizontalLayout_2 = QHBoxLayout(self.btn_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.metas_btn = QPushButton(self.btn_2)
        self.metas_btn.setObjectName(u"metas_btn")
        sizePolicy.setHeightForWidth(
            self.metas_btn.sizePolicy().hasHeightForWidth())
        self.metas_btn.setSizePolicy(sizePolicy)
        self.metas_btn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.metas_btn)

        self.verticalLayout.addWidget(self.btn_2)

        self.btn_3 = QFrame(self.home_page)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(0, 0))
        self.btn_3.setFrameShape(QFrame.NoFrame)  # type: ignore
        self.btn_3.setFrameShadow(QFrame.Raised)  # type: ignore
        self.horizontalLayout_3 = QHBoxLayout(self.btn_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.training_btn = QPushButton(self.btn_3)
        self.training_btn.setObjectName(u"training_btn")
        sizePolicy.setHeightForWidth(
            self.training_btn.sizePolicy().hasHeightForWidth())
        self.training_btn.setSizePolicy(sizePolicy)
        self.training_btn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.training_btn)

        self.verticalLayout.addWidget(self.btn_3)

        self.btn_4 = QFrame(self.home_page)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(0, 0))
        self.btn_4.setFrameShape(QFrame.NoFrame)  # type: ignore
        self.btn_4.setFrameShadow(QFrame.Raised)  # type: ignore
        self.horizontalLayout_4 = QHBoxLayout(self.btn_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.finance_btn = QPushButton(self.btn_4)
        self.finance_btn.setObjectName(u"finance_btn")
        sizePolicy.setHeightForWidth(
            self.finance_btn.sizePolicy().hasHeightForWidth())
        self.finance_btn.setSizePolicy(sizePolicy)
        self.finance_btn.setFont(font2)

        self.horizontalLayout_4.addWidget(self.finance_btn)

        self.verticalLayout.addWidget(self.btn_4)

        self.btn_5 = QFrame(self.home_page)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(0, 0))
        self.btn_5.setFrameShape(QFrame.NoFrame)  # type: ignore
        self.btn_5.setFrameShadow(QFrame.Raised)  # type: ignore
        self.horizontalLayout_5 = QHBoxLayout(self.btn_5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.travels_btn = QPushButton(self.btn_5)
        self.travels_btn.setObjectName(u"travels_btn")
        sizePolicy.setHeightForWidth(
            self.travels_btn.sizePolicy().hasHeightForWidth())
        self.travels_btn.setSizePolicy(sizePolicy)
        self.travels_btn.setFont(font2)

        self.horizontalLayout_5.addWidget(self.travels_btn)

        self.verticalLayout.addWidget(self.btn_5)

        self.verticalSpacer_2 = QSpacerItem(
            20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.botom_spacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.botom_spacer)

        StackedWidget.addWidget(self.home_page)
        self.finance = QWidget()
        self.finance.setObjectName(u"finance")
        self.verticalLayout_2 = QVBoxLayout(self.finance)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.finance)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout_2.addWidget(self.label)

        StackedWidget.addWidget(self.finance)
        self.training = QWidget()
        self.training.setObjectName(u"training")
        self.verticalLayout_4 = QVBoxLayout(self.training)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.training)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout_4.addWidget(self.label_3)

        StackedWidget.addWidget(self.training)
        self.metas = QWidget()
        self.metas.setObjectName(u"metas")
        self.verticalLayout_3 = QVBoxLayout(self.metas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.metas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout_3.addWidget(self.label_2)

        StackedWidget.addWidget(self.metas)
        self.travels = QWidget()
        self.travels.setObjectName(u"travels")
        self.verticalLayout_5 = QVBoxLayout(self.travels)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.travels)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout_5.addWidget(self.label_4)

        StackedWidget.addWidget(self.travels)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate(
            "StackedWidget", u"StackedWidget", None))
        self.label_5.setText(QCoreApplication.translate(
            "StackedWidget", u"Watch List", None))
        self.title.setText(QCoreApplication.translate(
            "StackedWidget", u"Home Page", None))
        self.watch_list_btn.setText(QCoreApplication.translate(
            "StackedWidget", u"Watch List", None))
        self.metas_btn.setText(QCoreApplication.translate(
            "StackedWidget", u"Metas", None))
        self.training_btn.setText(QCoreApplication.translate(
            "StackedWidget", u"Training", None))
        self.finance_btn.setText(QCoreApplication.translate(
            "StackedWidget", u"Finance", None))
        self.travels_btn.setText(QCoreApplication.translate(
            "StackedWidget", u"Travels", None))
        self.label.setText(QCoreApplication.translate(
            "StackedWidget", u"Finance", None))
        self.label_3.setText(QCoreApplication.translate(
            "StackedWidget", u"Training", None))
        self.label_2.setText(QCoreApplication.translate(
            "StackedWidget", u"Metas", None))
        self.label_4.setText(QCoreApplication.translate(
            "StackedWidget", u"Travel", None))
    # retranslateUi
