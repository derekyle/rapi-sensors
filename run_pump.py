from gpiozero import OutputDevice, Button
from time import sleep
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--time", help="Number of seconds to run pump.", default=15, type=int)
args = parser.parse_args()

relay1 = OutputDevice(
    pin=16,
    active_high=False
    )

print("Turning on pump for ",args.time," seconds...")
relay1.on()
sleep(args.time)
print("Turning pump off.")
relay1.off()