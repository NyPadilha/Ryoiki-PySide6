# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'pagesPidQHt.ui'
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
        self.verticalLayout = QVBoxLayout(self.home_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.home_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)  # type: ignore

        self.verticalLayout.addWidget(self.label_6)

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
        self.label_6.setText(QCoreApplication.translate(
            "StackedWidget", u"Home Page", None))
        self.label.setText(QCoreApplication.translate(
            "StackedWidget", u"Finance", None))
        self.label_3.setText(QCoreApplication.translate(
            "StackedWidget", u"Training", None))
        self.label_2.setText(QCoreApplication.translate(
            "StackedWidget", u"Metas", None))
        self.label_4.setText(QCoreApplication.translate(
            "StackedWidget", u"Travel", None))
    # retranslateUi
