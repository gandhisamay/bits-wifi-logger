# bits-wifi-logger
Automatically connect to bits wifi without taking the hassle of entering your bits id and password everytime.

## Installation
### Linux
**If you use a window manager like i3wm, dwm etc**,

Clone the repository and edit your respective config file for the particular window manager and run the python file on startup.

**else**

Clone the repository and create a systemd.service that runs on everytime your device starts.
Check out this [blog](https://fedoramagazine.org/systemd-timers-for-scheduling-tasks/#:~:text=Systemd%20timers%20offer%20the%20best,Is%20available%20to%20all%20users) here for more help.

### Windows
Please help yourself by finding methods to run files on startup and then run the python file.
In the worst case you can create a key shortcut and then run the program using that shortcut everytime you restart your device.

### Requirements
Chromedriver (with the suitable version based on your current chrome version present on the device)



