import os
import json
from lxml import etree as ET


def calc(nominal, actual):
    return actual if nominal==0 else nominal - actual


class JsonContainer:
    def __init__(self, filepath, planFolder, planId=""):
        self._jsonData = {}
        self.filepath = filepath
        self.planFolder = planFolder
        self.dialogFilepath = os.path.abspath("\\".join(["O:\\Measurement\\_resultDatabase", planId, "dialog.json"]))

        if os.path.isfile(self.dialogFilepath):
            print(f"loading {self.dialogFilepath}")
            with open(self.dialogFilepath, 'r') as inFile:
                self._jsonData = json.load(inFile)
        else:
            self._jsonData = {"Dialog" : {"name":"","MSN":"","cavNo":"","partID":planId,"WO":"","SO":"","comment":"","startRun":"", "endRun":"" ,"xOffset":"0.0000","yOffset":"0.0000","zOffset":"0.0000","operation":"default", "fileIndex":"MSN"}, 
                            "Setup":{"nominalXoffset": "0.0000","nominalYoffset": "0.0000","nominalZoffset": "0.0000"}}

    def update(self, data):
        if isinstance(data, dict):
            for item in data.keys():
                if item == "update":
                    for up in data["update"].keys():
                        print(up)
                if item == "Dialog":
                    for up in data.keys():
                        self._jsonData[up] = data[up]
                if item == "Setup":
                    for up in data.keys():
                        self._jsonData[up] = data[up]
                
    def loadXML(self, filename):
        if os.path.isfile(filename) and "dialog" in filename:
            tree = ET.parse(filename)
            root = tree.getroot()
            dialog = root.find("dialog")
            dialogEntries = {}
            for dia in dialog.iter():
                dialogEntries.update({dia.tag:dia.text})
            setup = root.find("Setup")
            setupEntries = {}
            for se in setup.iter():
                setupEntries.update({se.tag:se.text})

            return {"Dialog": dialogEntries, "Setup":setupEntries}
            
    def saveXML(self):
        jsonDialogData = self._jsonData['Dialog']
        jsonSetupData = self._jsonData['Dialog']
        xmlData = f'''<?xml version="1.0" encoding="UTF-8"?>
<cmmApp>
    <dialog>
        <name>{jsonDialogData.get('name')}</name>
        <partID>{jsonDialogData.get('partID')}</partID>
        <MSN>{jsonDialogData.get('MSN')}</MSN>
        <cavNo>{jsonDialogData.get('cavNo')}</cavNo>
        <operation>{jsonDialogData.get('operation')}</operation>
        <xOffset>{jsonDialogData.get('xOffset')}</xOffset>
        <yOffset>{jsonDialogData.get('yOffset')}</yOffset>
        <zOffset>{jsonDialogData.get('zOffset')}</zOffset>
        <WO>{jsonDialogData.get('WO')}</WO>
        <comment>{jsonDialogData.get('comment')}</comment>
    </dialog>
    <Setup>
        <nominalXoffset>{jsonSetupData.get('nominalXoffset')}</nominalXoffset>
        <nominalYoffset>{jsonSetupData.get('nominalYoffset')}</nominalYoffset>
        <nominalZoffset>{jsonSetupData.get('nominalZoffset')}</nominalZoffset>
    </Setup>
</cmmApp>'''

        with open(self.filepath+"/dialog.xml", 'w') as file:
            file.write(xmlData)
            
    def save(self):
        xOffset = float(self._jsonData.get('Dialog').get('xOffset'))
        yOffset = float(self._jsonData.get('Dialog').get('yOffset'))
        zOffset = float(self._jsonData.get('Dialog').get('zOffset'))
        
        nominalXOffset = float(self._jsonData.get('Setup').get('nominalXoffset'))
        nominalYOffset = float(self._jsonData.get('Setup').get('nominalYoffset'))
        nominalZOffset = float(self._jsonData.get('Setup').get('nominalZoffset'))

        with open(self.planFolder + "/inspection_start_pcm.txt", "w") as ispFile:
            ispFile.write(f'xOffset = {round(calc(nominalXOffset, xOffset), 4)}\n')
            ispFile.write(f'yOffset = {round(calc(nominalYOffset, yOffset), 4)}\n')
            ispFile.write(f'zOffset = {round(calc(nominalZOffset, zOffset), 4)}\n')
            ispFile.write(f'setRecordHead("order","{self._jsonData.get("Dialog").get("MSN")}")')

        with open(self.dialogFilepath, 'w') as file:
            json.dump(self._jsonData, file, indent=2)

    def readJson(self, data):
        j = json.loads(data)
        for x in j:
            self._jsonData[x] = j[x]
        return self._jsonData

    def getData(self):
        return self._jsonData
