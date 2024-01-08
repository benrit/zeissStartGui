# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file "startBox.ui"
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mWitgets import NumberEdit, ComboBox, MSNEdit
import random
import string

import time, json

def createTextBox(label:str, layout: QtWidgets.QBoxLayout, parent:QtWidgets.QWidget, editBox: QtWidgets.QWidget = QtWidgets.QLineEdit):

    horizontalLayout = QtWidgets.QHBoxLayout()
    labelName = QtWidgets.QLabel(parent)
    labelName.setText(label)
    labelName.setMinimumSize(QtCore.QSize(60, 0))
    horizontalLayout.addWidget(labelName)
    lineEdit = editBox(parent)
    horizontalLayout.addWidget(lineEdit)
    layout.addLayout(horizontalLayout)
    
    return lineEdit

def createNumberBox(label:str, layout: QtWidgets.QBoxLayout, parent:QtWidgets.QWidget):
    
    labelOffset = QtWidgets.QLabel(parent)
    labelOffset.setText(label)
    layout.addWidget(labelOffset)
    lineEditOffset = NumberEdit(parent)
    lineEditOffset.setMinimumSize(QtCore.QSize(100, 0))
    lineEditOffset.setMaximumSize(QtCore.QSize(100, 16777215))
    layout.addWidget(lineEditOffset)

    return lineEditOffset


class Ui_Dialog(object):
    coatingCheckBox = None
    coatingEnabled = None

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

        self.lineEditName = createTextBox("Name:", self.verticalLayout, self.groupBox)
        self.lineEditMSN = createTextBox("MSN:", self.verticalLayout, self.groupBox, editBox=MSNEdit)
        self.lineEditCav = createTextBox("CAV:", self.verticalLayout, self.groupBox)

        self.lineEditPartId = createTextBox("PartID:", self.verticalLayout, self.groupBox)
        self.lineEditPartId.setReadOnly(True)
        
        self.lineEditWO = createTextBox("WO:", self.verticalLayout, self.groupBox)
        self.lineEditSO = createTextBox("SO:", self.verticalLayout, self.groupBox)


        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.labelOperation = QtWidgets.QLabel(self.groupBox)
        self.labelOperation.setMinimumSize(QtCore.QSize(60, 0))
        self.labelOperation.setMaximumSize(QtCore.QSize(60, 16777215))
        self.horizontalLayout_6.addWidget(self.labelOperation)
        self.comboBoxOperation = ComboBox(self.groupBox)
        self.horizontalLayout_6.addWidget(self.comboBoxOperation)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()

        self.lineEditXOffset = createNumberBox("X Offset:", self.horizontalLayout_10, self.groupBox)
        self.lineEditYOffset = createNumberBox("Y Offset:", self.horizontalLayout_10, self.groupBox)
        self.lineEditZOffset = createNumberBox("Z Offset:", self.horizontalLayout_10, self.groupBox)

        self.verticalLayout.addLayout(self.horizontalLayout_10)
        
        self.lineEditTags = createTextBox("Tags:", self.verticalLayout, self.groupBox)
        
        # self.coatingWidget = QtWidgets.QWidget()
        # self.verticalLayout.addWidget(self.coatingWidget)

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
        self    .buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.horizontalLayout_9.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        # self.generateRandomNumberButton.clicked.connect(self.generateRandomNumber)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditName, self.lineEditMSN)
        Dialog.setTabOrder(self.lineEditMSN, self.lineEditCav)
        Dialog.setTabOrder(self.lineEditCav, self.lineEditWO)
        Dialog.setTabOrder(self.lineEditWO, self.lineEditSO)
        Dialog.setTabOrder(self.lineEditSO, self.comboBoxOperation)
        Dialog.setTabOrder(self.comboBoxOperation, self.lineEditZOffset)
        Dialog.setTabOrder(self.lineEditZOffset, self.lineEditYOffset)
        Dialog.setTabOrder(self.lineEditYOffset, self.lineEditXOffset)
        Dialog.setTabOrder(self.lineEditXOffset, self.lineEditTags)
        Dialog.setTabOrder(self.lineEditTags, self.toolButton)


    def enableCoating(self, enable):
        self.coatingEnabled = enable
        if enable:
            if not self.coatingCheckBox:
                self.coatingCheckBox = QtWidgets.QCheckBox("Coated")
                self.coatingCheckBox.setFont(QtGui.QFont("Sans Sarif", 12))
                self.verticalLayout.addWidget(self.coatingCheckBox)
                self.verticalLayout.update()
        else:
            if self.coatingCheckBox:
                self.coatingCheckBox.deleteLater()
                self.verticalLayout.update()
                self.coatingCheckBox = None


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Run Info"))
        self.labelOperation.setText(_translate("Dialog", "Operation"))
        self.groupBox_2.setTitle(_translate("Dialog", "Comments"))
        self.toolButton.setText(_translate("Dialog", "Setup"))


    def setOperations(self, data):
        for index, item in enumerate(data):
            self.comboBoxOperation.addItem(item)
            if item == "Setup":
                idx = self.comboBoxOperation.model().index(index, 0)
                self.comboBoxOperation.model().setData(idx, QtGui.QColor(255,0,0), QtCore.Qt.BackgroundRole)
                self.comboBoxOperation.model().setData(idx, QtGui.QColor(255, 255, 255), QtCore.Qt.TextColorRole)

            if item == "Final Measurement":
                idx = self.comboBoxOperation.model().index(index, 0)
                self.comboBoxOperation.model().setData(idx, QtGui.QColor(0,255,0), QtCore.Qt.BackgroundRole)

            if item == "default":
                idx = self.comboBoxOperation.model().index(index, 0)
                self.comboBoxOperation.model().setData(idx, QtGui.QColor(0,0,255), QtCore.Qt.BackgroundRole)
                self.comboBoxOperation.model().setData(idx, QtGui.QColor(255,255,255), QtCore.Qt.TextColorRole)

    def getData(self):
        
        coating = False
        if self.coatingEnabled:
            coating = self.coatingCheckBox.isChecked() 

        data = {"Dialog":{
                        "name": self.lineEditName.text(),
                        "partID": self.lineEditPartId.text(),
                        "MSN": self.lineEditMSN.text(),
                        "CAV": self.lineEditCav.text(),
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
                        "coating": coating,
                        "status": "measured"
                        }
                }
        return data

    def update(self, data):
        for item in data:
            if item == "Dialog":
                self.lineEditName.setText(data["Dialog"].get("name"))
                self.lineEditMSN.setText(data["Dialog"].get("MSN"))
                self.lineEditCav.setText(data["Dialog"].get("CAV"))
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

            
            if item == "Setup":
                enable = data["Setup"].get('coatingEnabled', False)
                self.enableCoating(enable)
                if enable:
                    self.coatingCheckBox.setChecked(data['Dialog'].get('coating', False))

            if item == "updateSOWO":
                print(data)
                self.lineEditWO.setText(data["updateWO"].get("WO"))
                self.lineEditWO.setText(data["updateSO"].get("SO"))
