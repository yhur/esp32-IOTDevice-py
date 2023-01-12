# ESP32 IOTDevice Library

This consists of two modules. the ComMgr and the IOTDevice.

## IOTDevice
```
        This creates the IOTDevice. It can be called with either a configuration option or all parameters
        1. With all parameters
            device=Device(
                devId = 'mydevice',
                devType = 'mytype',
                broker = '192.168.1.9',
                token = 'mytoken'
            )
        
        2. With option.
            option = {
                devId : 'mydevice',
                devType : 'mytype',
                broker : '192.168.1.9',
                token : 'mytoken'
            }
            device = Device(cfg = option)

        This can be especially usefull when the configuration is stored in a file
            f = open('device.cfg', 'w')
            option = json.loads(f.read())
            device = Device(cfg = option)
```

## ESP32 CommMgr.py

This Micropython code has the BLE and WiFi connection function.


The included boot.py shows the basic usage of this component with webrepl
