from PyQt5.QtWidgets import QLineEdit


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
