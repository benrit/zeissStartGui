import os
import json
from lxml import etree as ET


def calc(nominal, actual):
    return actual if nominal==0 else (nominal - actual)


class JsonContainer:
    def __init__(self, filepath, planFolder, planId=""):
        self._jsonData = {}
        self.filepath = filepath
        self.planFolder = planFolder
        self.dialogFilepath = os.path.abspath("\\".join(["O:\\Measurement\\_resultDatabase", planId]))

        if os.path.isfile(self.dialogFilepath + "\\dialog.json"):
            print(f"loading {self.dialogFilepath}")
            with open(self.dialogFilepath + "\\dialog.json", 'r') as inFile:
                self._jsonData = json.load(inFile)
        else:
            self._jsonData = {"Dialog" : {"name":"","MSN":"","CAV":"","partID": planId,"WO":"","SO":"","comment":"","startRun":"", "endRun":"" ,"xOffset":"0.0000","yOffset":"0.0000","zOffset":"0.0000","operation":"default", "status":"ok","coating": False}, 
                            "Setup":{"nominalXoffset": "0.0000","nominalYoffset": "0.0000","nominalZoffset": "0.0000", "fileIndex":"MSN", "importScan": False, "autorun": False, "coatingEnabled": False, "coatingAmount": '0.0'},
                            "Export":""}


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

    #xml is used for legacy reasons           
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
        <cavNo>{jsonDialogData.get('CAV')}</cavNo>
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
        dialog = self._jsonData.get('Dialog')
        xOffset = float(dialog.get('xOffset'))
        yOffset = float(dialog.get('yOffset'))
        zOffset = float(dialog.get('zOffset'))
        
        setup = self._jsonData.get('Setup')
        nominalXOffset = float(setup.get('nominalXoffset'))
        nominalYOffset = float(setup.get('nominalYoffset'))
        nominalZOffset = float(setup.get('nominalZoffset'))
        
        coatingAmount = 0.0
        if not dialog.get('coating', False):
            coatingAmount = float(setup.get('coatingAmount', 0.0)) 


        importScan = int(setup.get('importScan', 0))
        autorun = int(setup.get('autorun', 0))

        with open(self.planFolder + "\\inspection_start_pcm.txt", "w") as ispFile:
            ispFile.write(f'xOffset = {round(calc(nominalXOffset, xOffset), 4)}\n')
            ispFile.write(f'yOffset = {round(calc(nominalYOffset, yOffset), 4)}\n')
            ispFile.write(f'zOffset = {round(calc(nominalZOffset, zOffset), 4)}\n')
            ispFile.write(f'coating = {round(coatingAmount, 4)}\n')

            if autorun == 0:
                ispFile.write(f'setRecordHead("order","{self._jsonData.get("Dialog").get("MSN")}")\n')

            if autorun == 1:
                fileIndex = self._jsonData['Setup'].get("fileIndex", 'MSN')
                ispFile.write('planid = getRecordHead("planid")\n')
                temp = r'''str = chr(34) + "{\" + chr(34) + "Dialog\" + chr(34) + ": {\" + chr(34) +"startRun\" +chr(34) + ":\" + chr(34) + "$timestamp\" + chr(34)+"}}" + chr(34)
systemCall("O:/Measurement/Scripts/json_updater/json_updater.exe " + "O:/Measurement/_resultDatabase/" + planid + "/dialog.json " + str )
'''
                ispFile.write(temp)

                if fileIndex == 'MSN':
                    ispFile.write(f"autorun = 1\n")
                if fileIndex == 'CAV':
                    ispFile.write(f"autorun = 2\n")
                if fileIndex == 'partnb':
                    ispFile.write(f"autorun = 3\n")
            else:
                ispFile.write(f"autorun = 0\n")

        if not os.path.exists(self.dialogFilepath):
            os.makedirs(self.dialogFilepath)

        with open(self.dialogFilepath+ "\\dialog.json", 'w') as file:
            json.dump(self._jsonData, file)

    def readJson(self, data):
        j = json.loads(data)
        for x in j:
            self._jsonData[x] = j[x]
        return self._jsonData

    def getData(self):
        return self._jsonData
