#!/usr/bin/python3

import sys
import plyvel
import json

encoding = 'utf-16'
settingsKey = 'settings'
appIDKey = 'appID'

usage = '''\
Usage: {programName} {{directory of electron app index db}}

# The db dir is located in windows somewhere here:
#    C:\\Users\\$USER\\AppData\Local\\Packages\\D91E29CF.InkspaceApp_38kynpdw5g1aw\\LocalState\\db
# You can copy it to your python (linux) machine and extract the appID/UUID there.

'''.format(programName = sys.argv[0])

if len(sys.argv) < 2:
    print(usage)
    exit(1)

dir = sys.argv[1]
db = plyvel.DB(dir)

settings = json.loads(db.get(settingsKey.encode(encoding)[2:]).decode(encoding))
appID_bytes = settings[appIDKey]

appID = "";
for byte in appID_bytes:
   appID = appID + hex(byte)[2:]

print(appIDKey + ": " + appID)

db.close()
