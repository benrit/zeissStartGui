temp = rf'''str = chr(34) + "{{\" +chr(34)+ "Dialog\" + chr(34) + ": {{\" + chr(34) +"startRun\" +chr(34) + " : " + formatL (starttime, 6) + "}}}}" + chr(34)
systemCall("O:/Measurement/Scripts/json_updater/json_updater.exe " + "c:/temp/dialog.json " + str )'''

print(temp)

