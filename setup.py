# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from mWitgets import NumberEdit
import os

class SetupDialog(QtWidgets.QDialog):

    def setupUi(self):
        self.setObjectName("self")
        self.resize(600, 300)
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setMaximumSize(QtCore.QSize(600, 300))
        self.setEnabled(True)

        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelNomXOffset = QtWidgets.QLabel(self)
        self.labelNomXOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.labelNomXOffset.setObjectName("labelNomXOffset")
        self.horizontalLayout_3.addWidget(self.labelNomXOffset)
        self.lineEditNomXOffset = NumberEdit(self)
        self.lineEditNomXOffset.setObjectName("lineEditNomXOffset")
        self.horizontalLayout_3.addWidget(self.lineEditNomXOffset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelNomYOffset = QtWidgets.QLabel(self)
        self.labelNomYOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.labelNomYOffset.setObjectName("labelNomYOffset")
        self.horizontalLayout_4.addWidget(self.labelNomYOffset)
        self.lineEditNomYOffset = NumberEdit(self)
        self.lineEditNomYOffset.setObjectName("lineEditNomYOffset")
        self.horizontalLayout_4.addWidget(self.lineEditNomYOffset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelNomZOffset = QtWidgets.QLabel(self)
        self.labelNomZOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.labelNomZOffset.setObjectName("labelNomZOffset")
        self.horizontalLayout_5.addWidget(self.labelNomZOffset)
        self.lineEditNomZOffset = NumberEdit(self)
        self.lineEditNomZOffset.setObjectName("lineEditNomZOffset")
        self.horizontalLayout_5.addWidget(self.lineEditNomZOffset)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.index = QtWidgets.QLabel(self)
        self.index.setMinimumSize(QtCore.QSize(40, 0))
        
        self.horizontalLayout_6.addWidget(self.index)
        self.comboBoxIndex = QtWidgets.QComboBox(self)
        self.horizontalLayout_6.addWidget(self.comboBoxIndex)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.importScanLabel = QtWidgets.QLabel(self)
        self.importScanLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.horizontalLayout_7.addWidget(self.importScanLabel)

        self.importScanCheckBox = QtWidgets.QCheckBox(self)
        self.horizontalLayout_7.addWidget(self.importScanCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.autorunLabel = QtWidgets.QLabel(self)
        self.autorunLabel.setMinimumSize(QtCore.QSize(40, 0))
        self.horizontalLayout_8.addWidget(self.autorunLabel)
        self.autorunCheckBox = QtWidgets.QCheckBox(self)
        self.horizontalLayout_8.addWidget(self.autorunCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.coatingLabel = QtWidgets.QLabel(self)
        self.coatingLabel.setMaximumWidth(200)
        self.horizontalLayout_9.addWidget(self.coatingLabel)
        self.coatingCheckBox = QtWidgets.QCheckBox(self)
        self.horizontalLayout_9.addWidget(self.coatingCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.coatingAmountLabel = QtWidgets.QLabel(self)
        self.coatingAmountLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.horizontalLayout_10.addWidget(self.coatingAmountLabel)
        self.coutingAmount = NumberEdit(self)
        self.horizontalLayout_10.addWidget(self.coutingAmount)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout_2.addStretch()

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
    


        self.horizontalLayout_main.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel()
        # self.label.setFixedWidth(400)
        self.label.setFixedWidth(300)
        self.horizontalLayout_main.addWidget(self.label)

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelNomXOffset.setText(_translate("Dialog", "Nominal X Offset"))
        self.labelNomYOffset.setText(_translate("Dialog", "Nominal Y Offset"))
        self.labelNomZOffset.setText(_translate("Dialog", "Nominal Z Offset"))
        self.index.setText(_translate("Dialog", "Index"))
        self.importScanLabel.setText(_translate("Dialog", "Import Scan"))
        self.autorunLabel.setText(_translate("Dialog", "Autorun"))
        self.comboBoxIndex.addItems(["MSN", "CAV", "partnb"])
        self.coatingLabel.setText(_translate("Dialog", "Coating"))
        self.coatingAmountLabel.setText(_translate("Dialog", "Coating Amount"))
        
    def setData(self, data):
        jsonData = data._jsonData
        self.lineEditNomXOffset.setText(jsonData["Setup"].get("nominalXoffset", '0.0000'))
        self.lineEditNomYOffset.setText(jsonData["Setup"].get("nominalYoffset", '0.0000'))
        self.lineEditNomZOffset.setText(jsonData["Setup"].get("nominalZoffset", '0.0000'))
        self.comboBoxIndex.setCurrentText(jsonData["Setup"].get("fileIndex", "MSN"))
        self.importScanCheckBox.setChecked(jsonData['Setup'].get("importScan", False))
        self.autorunCheckBox.setChecked(jsonData['Setup'].get('autorun', False))
        self.coatingCheckBox.setChecked(jsonData['Setup'].get("coatingEnabled", False))
        self.coutingAmount.setText(jsonData['Setup'].get("coatingAmount", '0.0'))


    def setPicture(self, path):
        pixmap = QtGui.QPixmap(path)
        pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)


    def getData(self):
        return {'Setup':{
                'nominalXoffset': self.lineEditNomXOffset.text(),
                'nominalYoffset': self.lineEditNomYOffset.text(),
                'nominalZoffset': self.lineEditNomZOffset.text(),
                'fileIndex': self.comboBoxIndex.currentText(),
                'importScan': self.importScanCheckBox.isChecked(),
                'autorun': self.autorunCheckBox.isChecked(),
                'coatingEnabled': self.coatingCheckBox.isChecked(),
                'coatingAmount': self.coutingAmount.text()
            },
            "Export": ""
        }
        


