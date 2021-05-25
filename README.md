# LedSurf


### Logs directory
Is used as folder where failing to run the script on startup of the raspberry pi
information is given. So should remain empty. This site gives more info: https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/.

Add this at the first time to make the script start upon startup:
Step 1: Make the files executables and test it with the second line:
chmod 755 launcher.sh
sh launcher.sh

Step 2: To add let it work on startup:
sudo crontab -e
\@reboot sh /home/pi/bbt/launcher.sh >/home/pi/logs/cronlog 2>&1
