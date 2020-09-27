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

setup_deploy_service:
	sudo systemctl edit --force --full deploy_script.service
	sudo systemctl start deploy_script.service
	sudo systemctl restart deploy_script.service

install_ph_meter:
	tar -xvf assets/hl_install_191020B.tar.gz --overwrite
	sudo bash homelab_install.sh

#this this this

# [Unit]
# Description=My Script Service
# Wants=network-online.target
# After=network-online.target

# [Service]
# Type=simple
# User=pi
# WorkingDirectory=/home/pi
# ExecStart=/home/pi/rapi-sensors/startup_script.sh

# [Install]
# WantedBy=multi-user.target