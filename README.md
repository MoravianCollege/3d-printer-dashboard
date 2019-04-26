# 3d-printer-dashboard
In the 3D printer project we are working with the 3D printers in the computer science lab and our goal is to read information from the printer and be able to display it. The printers have many characteristics that we can get information from, such as the temperature of the beds, the current item being printed, what printer is being used, etc. We are using the printers' API to get all of this information. We are utilizing a Python framework called Dash to display a dashboard on our computer, and to be able to get the information formatted in a readable way.


# Production Setup
* Image an SD card with [Screenly OSE] (https://www.screenly.io/ose/) (use [Etcher] (https://www.balena.io/etcher/))
* Create a file `/boot/ssh` on the SD card (see #3 from the [SSH page] (https://www.raspberrypi.org/documentation/remote-access/ssh/README.md))
* Boot the Pi. Screenly will launch to a screen that shows the IP
* Connect using the IP: `sudo ssh pi@<IP>`. Password for the Pi is `raspberry`
* Change the password: `sudo passwd pi`
* Update the package manager: `sudo apt-get update`
* Install pip3: `sudo apt install python3-pip`
* Install [MySQL] (README.md): `sudo apt-get install mysql-server`
* Set MySQL password and create `printer` database:
	* Access MySQL: `sudo mysql -u root`
	* Use correct database (once inside MySQL): `use mysql;`
	* Change password: `UPDATE	 user SET authentication_string=PASSWORD("3dprinting") WHERE User='root';`
	* Update native password plugin: `update user set plugin="mysql_native_password" where User='root';`
	* Flush privileges: `FLUSH PRIVILEGES`
	* Create database for printer stats: `CREATE DATABASE printer;`
	* Leave MySQL: `\q`
* Clone this repo to the Pi (and go into the directory)
* Note the name of the directory: `pwd` (referred to as`<repo-dir>` below)
* Install the dependencies (as root): `sudo pip3 install -r requirements.txt`
* Set SQL database to be used for printer stats:
	* Go to collector directory: `cd <repo-dir>/3d-printer-collector`
	* Source .sql file to be used with printer database: `mysql -u root -p printer < 3d_printer_table.sql`
* Edit `etc/rc.local` and add the following *above* `exit 0`: (Replace `<repo dir>` with the absolute path and note the `&` at the end of each line!) <br/>
`python3 <repo dir>/3d-printer-collecter/main.py &` </br>
`gunicorn -b 127.0.0.1:5000 api:app &` </br>
`python3 <repo dir>/3d-printer-collecter/client.py &` </br>
* Reboot the Pi: `sudo reboot`
* Add a new asset to Screenly in the form `http://<IP>:8050`
