from gpiozero import OutputDevice
from time import sleep

relay1 = OutputDevice(
    pin=2,
    active_high=False
    )
relay2 = OutputDevice(
    pin=3,
    active_high=False
    )
relay3 = OutputDevice(
    pin=4,
    active_high=False
    )
#relay4 = OutputDevice(
#    pin=14,
#    active_high=False
#    )
#relay5 = OutputDevice(
#    pin=15,
#    active_high=False
#    )

while True:
    relay1.on()
    sleep(1)
    relay1.off()
    sleep(1)
    relay2.on()
    sleep(1)
    relay2.off()
    sleep(1)
    relay3.on()
    sleep(1)
    relay3.off()
    sleep(1)
#    relay4.on()
#    sleep(1)
#    relay4.off()
#    sleep(1)
#    relay5.on()
#    sleep(1)
#    relay5.off()
#    sleep(1)
