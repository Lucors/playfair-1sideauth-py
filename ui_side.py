# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_side.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SideWidget(object):
    def setupUi(self, SideWidget):
        if not SideWidget.objectName():
            SideWidget.setObjectName(u"SideWidget")
        SideWidget.resize(355, 356)
        self.gridLayout = QGridLayout(SideWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(SideWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.key_header = QLabel(self.groupBox)
        self.key_header.setObjectName(u"key_header")
        sizePolicy.setHeightForWidth(self.key_header.sizePolicy().hasHeightForWidth())
        self.key_header.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.key_header)

        self.key_value = QLineEdit(self.groupBox)
        self.key_value.setObjectName(u"key_value")

        self.verticalLayout.addWidget(self.key_value)

        self.key_apply_btn = QPushButton(self.groupBox)
        self.key_apply_btn.setObjectName(u"key_apply_btn")

        self.verticalLayout.addWidget(self.key_apply_btn)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)

        self.groupBox_3 = QGroupBox(SideWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.log_lbl = QLabel(self.groupBox_3)
        self.log_lbl.setObjectName(u"log_lbl")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.log_lbl.sizePolicy().hasHeightForWidth())
        self.log_lbl.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.log_lbl)


        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 2)

        self.groupBox_2 = QGroupBox(SideWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.side_connection = QLabel(self.groupBox_2)
        self.side_connection.setObjectName(u"side_connection")
        sizePolicy.setHeightForWidth(self.side_connection.sizePolicy().hasHeightForWidth())
        self.side_connection.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.side_connection)

        self.sides_combo = QComboBox(self.groupBox_2)
        self.sides_combo.setObjectName(u"sides_combo")

        self.verticalLayout_2.addWidget(self.sides_combo)

        self.auth_btn = QPushButton(self.groupBox_2)
        self.auth_btn.setObjectName(u"auth_btn")

        self.verticalLayout_2.addWidget(self.auth_btn)


        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.name_lbl = QLineEdit(SideWidget)
        self.name_lbl.setObjectName(u"name_lbl")
        self.name_lbl.setEnabled(False)

        self.gridLayout.addWidget(self.name_lbl, 0, 1, 1, 1)

        self.name_header = QLabel(SideWidget)
        self.name_header.setObjectName(u"name_header")

        self.gridLayout.addWidget(self.name_header, 0, 0, 1, 1)

        self.rnd_header = QLabel(SideWidget)
        self.rnd_header.setObjectName(u"rnd_header")

        self.gridLayout.addWidget(self.rnd_header, 1, 0, 1, 1)

        self.rnd_value = QLineEdit(SideWidget)
        self.rnd_value.setObjectName(u"rnd_value")
        self.rnd_value.setEnabled(False)

        self.gridLayout.addWidget(self.rnd_value, 1, 1, 1, 1)


        self.retranslateUi(SideWidget)

        QMetaObject.connectSlotsByName(SideWidget)
    # setupUi

    def retranslateUi(self, SideWidget):
        SideWidget.setWindowTitle(QCoreApplication.translate("SideWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("SideWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0430\u043b\u0433. \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.key_header.setText(QCoreApplication.translate("SideWidget", u"\u041a\u043b\u044e\u0447:", None))
        self.key_value.setText(QCoreApplication.translate("SideWidget", u"WATSON", None))
        self.key_apply_btn.setText(QCoreApplication.translate("SideWidget", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SideWidget", u"\u041b\u043e\u0433", None))
        self.log_lbl.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("SideWidget", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f", None))
        self.side_connection.setText(QCoreApplication.translate("SideWidget", u"\u0421\u0442\u043e\u0440\u043e\u043d\u0430 \u043e\u0431\u0449\u0435\u043d\u0438\u044f:", None))
        self.auth_btn.setText(QCoreApplication.translate("SideWidget", u"\u0410\u0443\u0442\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u044f", None))
        self.name_header.setText(QCoreApplication.translate("SideWidget", u"\u0418\u043c\u044f:", None))
        self.rnd_header.setText(QCoreApplication.translate("SideWidget", u"\u0421\u043b\u0443\u0447. \u0447\u0438\u0441\u043b\u043e:", None))
    # retranslateUi

