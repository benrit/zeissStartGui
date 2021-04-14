from PyQt5.QtWidgets import QLineEdit, QComboBox
import re

class NumberEdit(QLineEdit):
    def __init__(self, steps=5, *args, **kwargs):
        super(NumberEdit, self).__init__(*args, **kwargs)
        self.textChanged.connect(self.valueChanged)
    
    def focusOutEvent(self, e):
        try:
            number = float(self.text())
            self.setText('%.4f' % number)
        except:
            self.setText(self.text())

        super(NumberEdit, self).focusOutEvent(e)
    
    def valueChanged(self):
        try:
            float(self.text())
            self.setStyleSheet("background-color: white;")
        except:
            self.setStyleSheet("background-color: red;")


class MSNEdit(QLineEdit):
    def __init__(self, steps=5, *args, **kwargs):
        super(MSNEdit, self).__init__(*args, **kwargs)
        self.textChanged.connect(self.valueChanged)

    def valueChanged(self):
        if re.findall(r'[\\|\/|%]', self.text()):
            self.setStyleSheet("background-color: red;")
        else:
            self.setStyleSheet("background-color: white;")
            



class ComboBox(QComboBox):
    def __init__(self, steps=5, *args, **kwargs):
        super(ComboBox, self).__init__(*args, **kwargs)
        self.currentIndexChanged.connect(self.valueChanged)

    def valueChanged(self, index):
        if self.itemText(index) == "Setup":
            self.setStyleSheet("QComboBox { color: white; background-color: red;  border-radius: 2px; }")
        elif self.itemText(index) == "Final Measurement":
            self.setStyleSheet("QComboBox { color: black; background-color: rgb(0,255,0);  border-radius: 2px; }")
        elif self.itemText(index) == "default":
            self.setStyleSheet("QComboBox { color: white; background-color: rgb(0,0,255);  border-radius: 2px; }")
        else:
            self.setStyleSheet("QComboBox { color: black; background-color: lightgray;  border-radius: 2px; }")
