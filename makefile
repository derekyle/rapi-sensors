init:
	sudo apt install gpiozero
	echo "dtoverlay=w1-gpio" >> /boot/config.txt
	sudo modprobe w1-gpio
	sudo modprobe w1-therm
	cd /sys/bus/w1/devices/
	ls

install_git:
	sudo apt update
	sudo apt install git -y