
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets



class ScanDialog(QtWidgets.QDialog):

    def setupUi(self):
        self.setObjectName("Scan")
        self.setWindowTitle("Scan Token")
        self.setEnabled(True)
        self.resize(300, 100)
        self.setMinimumSize(QtCore.QSize(300,100))
        self.setMaximumSize(QtCore.QSize(300,100))

        self.layout = QtWidgets.QVBoxLayout()

        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttonBox)
        self.buttonBox.rejected.connect(self.reject)
        self.setLayout(self.layout)
        self.qrToken = ""    
        
    def keyPressEvent(self, event):
        if event.key() < 255:
            self.qrToken += event.text()
        if event.key() == QtCore.Qt.Key_Return:
            self.accept()


app = QApplication(sys.argv)
window = QDialog()

scan = ScanDialog()
scan.setupUi()
scan.grabKeyboard()
scan.exec_()
scan.releaseKeyboard()
print(scan.qrToken)

window.show()

sys.exit(app.exec_())
