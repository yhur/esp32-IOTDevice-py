# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
#		In order to enable the webrepl, you need to import this and run the setup once
#			import webrepl_setup
import CommMgr

ble = CommMgr.startBLE('esp32s3')
nic = CommMgr.startWiFi('esp32s3')

if nic:
    import esp
    import webrepl
    esp.osdebug(None)
    webrepl.start()
