# author: Thuy.PX
# email: thuypx.tech.mlab@gmail.com
# Blink led and cleanup gpio with python lib: gpiozero, run on Raspberry Pi 5

from gpiozero import LED
from time import sleep

led = LED(17)

try:
    print("Starting demo now! Press CTRL+C to exit")
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
except KeyboardInterrupt:
    print("\nProgram terminated by user Ctrl+C.")
    print("Cleanup is automatically.")
finally:
    print("\nBlink LED Finish.")

# In GPIO Zero, cleanup is automatically performed on every pin used, at the end of the script.
# Note that cleanup only occurs at the point of normal termination of the script. 
# If the script exits due to a program error, cleanup will not be performed. To ensure that cleanup is performed after an exception is raised, the exception must be handled.
# the exception: Keyboard Interrupt Ctrl+C
