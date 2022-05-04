# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_control.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ControlWidget(object):
    def setupUi(self, ControlWidget):
        if not ControlWidget.objectName():
            ControlWidget.setObjectName(u"ControlWidget")
        ControlWidget.resize(400, 211)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControlWidget.sizePolicy().hasHeightForWidth())
        ControlWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(ControlWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sidesBox = QGroupBox(ControlWidget)
        self.sidesBox.setObjectName(u"sidesBox")
        sizePolicy.setHeightForWidth(self.sidesBox.sizePolicy().hasHeightForWidth())
        self.sidesBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.sidesBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sides_list = QLabel(self.sidesBox)
        self.sides_list.setObjectName(u"sides_list")

        self.verticalLayout_2.addWidget(self.sides_list)


        self.verticalLayout_3.addWidget(self.sidesBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_name_editor = QLineEdit(ControlWidget)
        self.side_name_editor.setObjectName(u"side_name_editor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_name_editor.sizePolicy().hasHeightForWidth())
        self.side_name_editor.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.side_name_editor)

        self.add_side_btn = QPushButton(ControlWidget)
        self.add_side_btn.setObjectName(u"add_side_btn")
        sizePolicy1.setHeightForWidth(self.add_side_btn.sizePolicy().hasHeightForWidth())
        self.add_side_btn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.add_side_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(ControlWidget)

        QMetaObject.connectSlotsByName(ControlWidget)
    # setupUi

    def retranslateUi(self, ControlWidget):
        ControlWidget.setWindowTitle(QCoreApplication.translate("ControlWidget", u"Form", None))
        self.sidesBox.setTitle(QCoreApplication.translate("ControlWidget", u"\u0421\u0442\u043e\u0440\u043e\u043d\u044b", None))
        self.sides_list.setText("")
        self.side_name_editor.setInputMask("")
        self.side_name_editor.setPlaceholderText(QCoreApplication.translate("ControlWidget", u"\u0418\u043c\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u0430", None))
        self.add_side_btn.setText(QCoreApplication.translate("ControlWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

