import sys, os, json, time
from PyQt5.QtWidgets import QApplication, QDialog
from gui import Ui_Dialog
from setup import SetupDialog
from jsonContainer import JsonContainer
import time

def saveDialog(jsonData, data):
    jsonData.update(data.getData())
    jsonData.save()
    jsonData.saveXML()

    
def setupDialog(jsonData):
    setup = SetupDialog()
    setup.setupUi()
    setup.setData(jsonData)
    if setup.exec_():
        jsonData.update(setup.getData())


resultFolder = "O:/Measurement/Results/"

if __name__ == "__main__":
    print("sys.argv " + " ".join(sys.argv))
    for x, arg in enumerate(sys.argv):
        if "-pd" in arg:
            currentPlanFolder = sys.argv[x+1]
            print("current Plan Folder " + currentPlanFolder)

        if "-f" in arg:
            planid = sys.argv[x+1]
            print("current Plan ID " + planid)

    dialogPath = os.path.abspath(resultFolder + planid)
    if not os.path.exists(dialogPath):
        os.makedirs(dialogPath)


    jsonData = JsonContainer(dialogPath, currentPlanFolder, planId=planid)

    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)
    ui.setOperations(["default", "Setup", "EDM","EDM Ingersol 781","EDM Ingersol 782","EDM Charmilles 550","WireEDM","WireEDM Cut 2000","WireEDM Charmilles 440", "HSC","Grinding","Jig-Grinding","Cylindrical Grinding","Turning","Milling", "Electrode","Polishing","Assembly","Repair", "Valve Pin", "Incomming Measurement","Final Measurement" ])
    ui.update(jsonData.getData())
    ui.buttonBox.accepted.connect(lambda: saveDialog(jsonData, ui))
    ui.toolButton.pressed.connect(lambda: setupDialog(jsonData))

    window.show()
    
    sys.exit(app.exec_())
    