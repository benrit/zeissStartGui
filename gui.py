# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "startBox.ui"
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mWitgets import NumberEdit

import time, json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(850, 350)
        Dialog.setMinimumSize(QtCore.QSize(850, 350))
        Dialog.setMaximumSize(QtCore.QSize(850, 350))
        Dialog.setBaseSize(QtCore.QSize(0, 0))
        Dialog.setWindowOpacity(1.0)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.labelName = QtWidgets.QLabel(self.groupBox)
        self.labelName.setMinimumSize(QtCore.QSize(80, 0))
        self.horizontalLayout.addWidget(self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout.addWidget(self.lineEditName)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.labelMSN = QtWidgets.QLabel(self.groupBox)
        self.labelMSN.setMinimumSize(QtCore.QSize(80, 0))
        self.horizontalLayout_2.addWidget(self.labelMSN)
        self.lineEditMSN = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout_2.addWidget(self.lineEditMSN)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.labelCav = QtWidgets.QLabel(self.groupBox)
        self.labelCav.setMinimumSize(QtCore.QSize(80, 0))
        self.horizontalLayout_3.addWidget(self.labelCav)
        self.lineEditCav = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout_3.addWidget(self.lineEditCav)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.labelPartId = QtWidgets.QLabel(self.groupBox)
        self.labelPartId.setMinimumSize(QtCore.QSize(80, 0))
        self.horizontalLayout_4.addWidget(self.labelPartId)
        self.lineEditPartId = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.lineEditPartId)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.labelWO = QtWidgets.QLabel(self.groupBox)
        self.labelWO.setMinimumSize(QtCore.QSize(80, 0))
        self.horizontalLayout_5.addWidget(self.labelWO)
        self.lineEditWO = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout_5.addWidget(self.lineEditWO)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.labelSO = QtWidgets.QLabel(self.groupBox)
        self.labelSO.setMinimumSize(QtCore.QSize(80, 0))
        self.horizontalLayout_8.addWidget(self.labelSO)
        self.lineEditSO = QtWidgets.QLineEdit(self.groupBox)
        self.horizontalLayout_8.addWidget(self.lineEditSO)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.labelOperation = QtWidgets.QLabel(self.groupBox)
        self.labelOperation.setMinimumSize(QtCore.QSize(80, 0))
        self.labelOperation.setMaximumSize(QtCore.QSize(80, 16777215))
        self.horizontalLayout_6.addWidget(self.labelOperation)
        self.comboBoxOperation = QtWidgets.QComboBox(self.groupBox)
        self.horizontalLayout_6.addWidget(self.comboBoxOperation)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.labelXOffset = QtWidgets.QLabel(self.groupBox)
        self.horizontalLayout_10.addWidget(self.labelXOffset)
        self.lineEditXOffset = NumberEdit(self.groupBox)
        self.lineEditXOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditXOffset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout_10.addWidget(self.lineEditXOffset)
        self.labelYOffset = QtWidgets.QLabel(self.groupBox)
        self.horizontalLayout_10.addWidget(self.labelYOffset)
        self.lineEditYOffset = NumberEdit(self.groupBox)
        self.lineEditYOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditYOffset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout_10.addWidget(self.lineEditYOffset)
        self.labelZOffset = QtWidgets.QLabel(self.groupBox)
        self.horizontalLayout_10.addWidget(self.labelZOffset)
        self.lineEditZOffset = NumberEdit(self.groupBox)
        self.lineEditZOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditZOffset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.horizontalLayout_10.addWidget(self.lineEditZOffset)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.labelTags = QtWidgets.QLabel(self.groupBox)
        self.horizontalLayout_11.addWidget(self.labelTags)
        self.lineEditTags = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditTags.setMinimumSize(QtCore.QSize(100, 0))
    
        self.horizontalLayout_11.addWidget(self.lineEditTags)
        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_7.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.toolButton = QtWidgets.QPushButton(Dialog)
        self.toolButton.setMaximumSize(QtCore.QSize(100, 25))
        self.horizontalLayout_9.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditName, self.lineEditMSN)
        Dialog.setTabOrder(self.lineEditMSN, self.lineEditCav)
        Dialog.setTabOrder(self.lineEditCav, self.lineEditPartId)
        Dialog.setTabOrder(self.lineEditPartId, self.lineEditWO)
        Dialog.setTabOrder(self.lineEditWO, self.lineEditSO)
        Dialog.setTabOrder(self.lineEditSO, self.comboBoxOperation)
        Dialog.setTabOrder(self.comboBoxOperation, self.lineEditZOffset)
        Dialog.setTabOrder(self.lineEditZOffset, self.lineEditYOffset)
        Dialog.setTabOrder(self.lineEditYOffset, self.lineEditXOffset)
        Dialog.setTabOrder(self.lineEditXOffset, self.lineEditTags)
        Dialog.setTabOrder(self.lineEditTags, self.toolButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Run Info"))
        self.labelName.setText(_translate("Dialog", "Name:"))
        self.labelMSN.setText(_translate("Dialog", "MSN:"))
        self.labelCav.setText(_translate("Dialog", "CAV:"))
        self.labelPartId.setText(_translate("Dialog", "PartID:"))
        self.labelWO.setText(_translate("Dialog", "Work Order#:"))
        self.labelSO.setText(_translate("Dialog", "Sales Order#:"))
        self.labelOperation.setText(_translate("Dialog", "Operation"))
        self.labelXOffset.setText(_translate("Dialog", "X Offset:"))
        self.labelYOffset.setText(_translate("Dialog", "Y Offset:"))
        self.labelZOffset.setText(_translate("Dialog", "Z Offset:"))
        self.labelTags.setText(_translate("Dialog", "Tags"))
        self.groupBox_2.setTitle(_translate("Dialog", "Comments"))
        self.toolButton.setText(_translate("Dialog", "Setup"))

    def setOperations(self, data):
        for item in data:
            self.comboBoxOperation.addItem(item)

    def getData(self):
        data = {"Dialog":{
                        "name": self.lineEditName.text(),
                        "partID": self.lineEditPartId.text(),
                        "MSN": self.lineEditMSN.text(),
                        "cavNo": self.lineEditCav.text(),
                        "xOffset": self.lineEditXOffset.text(),
                        "yOffset": self.lineEditYOffset.text(),
                        "zOffset": self.lineEditZOffset.text(),
                        "WO": self.lineEditWO.text(),
                        "SO": self.lineEditSO.text(),
                        "comment": self.textEdit.toPlainText(),
                        "startRun": time.time(),
                        "endRun": "",
                        "operation": self.comboBoxOperation.currentText(),
                        "tags": self.lineEditTags.text(),
                        "fileIndex": "MSN",
                        "status": "ok"
                        }
                }
        return data

    def update(self, data):
        for x in data:
            if x == "Dialog":
                self.lineEditName.setText(data["Dialog"].get("name"))
                self.lineEditMSN.setText(data["Dialog"].get("MSN"))
                self.lineEditCav.setText(data["Dialog"].get("cavNo"))
                self.lineEditPartId.setText(data["Dialog"].get("partID"))
                self.lineEditWO.setText(data["Dialog"].get("WO"))
                self.lineEditSO.setText(data["Dialog"].get("SO"))
                self.textEdit.setText(data["Dialog"].get("comment"))
                self.lineEditTags.setText(data["Dialog"].get("tags"))
                self.lineEditXOffset.setText(data["Dialog"].get("xOffset"))
                self.lineEditYOffset.setText(data["Dialog"].get("yOffset"))
                self.lineEditZOffset.setText(data["Dialog"].get("zOffset"))
                index = self.comboBoxOperation.findText(data["Dialog"].get("operation"))
                if index > -1:
                    self.comboBoxOperation.setCurrentIndex(index)
            
            if x == "updateWO":
                print(data)
                self.lineEditWO.setText(data["updateWO"].get("WO"))
                self.lineEditSO.setText(data["updateWO"].get("SO"))
