# 3d-printer-dashboard
---
In the 3D printer project we are working with the 3D printers in the computer science lab and our goal is to read information from the printer and be able to display it. The printers have many characteristics that we can get information from, such as the temperature of the beds, the current item being printed, what printer is being used, etc. We are using the printers' API to get all of this information. We are utilizing a framework called Smashing to display a dashboard on our computer, and to be able to get the information formatted in a readable way.


# Production Setup
---
* Image an SD card with [Screenly OSE] (https://www.screenly.io/ose/) (use [Etcher] (https://www.balena.io/etcher/))
* Create a file `/boot/ssh` on the SD card (see #3 from the [SSH page] (https://www.raspberrypi.org/documentation/remote-access/ssh/README.md))
* Boot the Pi. Screenly will launch to a screen that shows the IP
* Connect using the IP: `ssh pi@<IP>`. Password is `raspberry`
* Change the password: `sudo passwd pi`
* Update the package manager: `sudo apt-get update`
* Install pip3: `sudo apt-get install python3-pip`
* Install [Apache] (https://www.apache.org/): `sudo apt-get install apache2 -y`
* Install [PHP] (http://www.php.net/): `sudo apt-get install php -y`
* Install [MySQL] (README.md): `sudo apt-get install mysql-server php-mysql -y`
* Initialize MySQL database: `???`
* Install [gunicorn] (https://gunicorn.org/): `sudo pip3 install gunicorn`
* Clone this repo to the Pi (and go into the directory)
* Install the dependencies (as root): `sudo pip3 install -r requirements.txt`
* Create a file named .env that contains `GITHUB_TOKEN=<TOKEN>` (replace `<TOKEN>` with a [GitHub Personal Access Token] (https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) with `repo` access)
* Note the name of the directory: `pwd`
* Edit `etc/rc.local` and add the following *above* `exit 0`: (Replace `<repo dir>` with the absolute path and note the `&` at the end of each line!) <br/>
`python <repo dir>/home/pi/3d-printer-collecter/api.py &` </br> `python <repo dir>/home/pi/3d-printer-collecter/main.py &` </br>
