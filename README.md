# Chomp-Bot
Python script for Pi-Hole + Pimoroni Scroll-Bot kit, which plays a 'chomp' animation every time the 'ads blocked' count increases
## Instructions / dependencies

 - [Pi-Hole](https://github.com/pi-hole/pi-hole/#one-step-automated-install)
 - [scrollphathd](https://github.com/pimoroni/scroll-phat-hd#manual-install)
 - `sudo cp chompbot.service /lib/systemd/system/`
 - `sudo systemctl enable chompbot.service`
 - `sudo systemctl start chompbot.service`
