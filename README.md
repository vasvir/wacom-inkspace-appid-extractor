# wacom-inkspace-appid-extractor
Extracts the AppID from inkspace settings so that it can be used as tuhi UUID.

This eliminates the needs of registrations whenever you want to switch
between inkspace and tuhi

Pairing is still required though.

## Dependencies

* plyvel
```
   sudo apt install python3-plyvel
```

## Usage
```
  ./wacom-inkspace-appid-extractor.py {directory of electron app index db}
```

The db dir is located in windows somewhere here:
```
    C:\Users\\${USER}\AppData\Local\Packages\D91E29CF.InkspaceApp_38kynpdw5g1aw\LocalState\db
```
You can copy it to your python (linux) machine and extract the appID/UUID there.

The output is something like that:
   appID: 256484a96358

Now you can put the hex output as your UUID in ~/.local/share/tuhi/${BLUETOOTH_ADDRESS}/settings.ini
