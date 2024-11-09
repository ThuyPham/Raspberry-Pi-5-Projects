# author: Thuy.PX
# email: thuypx.tech.mlab@gmail.com
# Use button control led and cleanup gpio with python lib: gpiozero, run on Raspberry Pi 5

from gpiozero import Button
from gpiozero import LED
from time import sleep

btn = Button(4)
led = LED(17)

def main():
	# prev_value = None

	# Initial state for LEDs:
	led.off()
	print("Starting demo now! Press CTRL+C to exit")
	try:
		while True:
			btn.when_pressed = led.on
			btn.when_released = led.off
	except KeyboardInterrupt:
		print("\nProgram terminated by user Ctrl+C.")
		print("Cleanup is automatically.")
	finally:
		print("\nButton - LED Finish.")

if __name__ == '__main__':
    main()
