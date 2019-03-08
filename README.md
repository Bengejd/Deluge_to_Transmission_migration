# Deluge_to_Transmission_migration
This python project helps you navigate the horror of migrating from Deluge torrent client to Transmission torrent client on Linux.

## Important Note:
This only coppies over magnet links, but no other meta data. This is to be used when Deluge is clear of any currently active torrents, as Transmission might re-download them on submission. I created this because I supidly forgot to check "Make a copy of torrents" in Deluge before adding some odd 200+ torrents, and didn't want to add them all back manually in Transmission (my new client). 

This also assumes that the machine that you're running this on, is the one with the Deluge & Transmission client on it already. Deluge should be closed (ideally), but Transmission **MUST BE RUNNNING** in order to properly add them via the web interface.

# Getting Started
When you get to **step 5** you will be required to enter your transmission username and password. The username and password is: `transmission`, if you didn't change the default. You have 15 seconds to input this information and click enter. There is no way that I could find to automate this step, as it's not something I could target using selenium. 

1. Download & Unzip this project.
2. Copy this file: `cp ~/.config/deluge/state/torrents.state ~/LOCATION_OF_THIS_PROJECT`
3. cd into this project directory, e.g: `cd ~/home/downloads/Deluge_to_Transmission_migration` 
4. Run `pip install selenium`
5. Run `python start.py`

# Sit back and wait.
The last step will take a few minutes, depending on the amount of torrents you are planning on adding. Please remember, that this does not add any meta data from Deluge to Transmission, it simply copies the magnet link into the transmission browser.

Once the script is finished running, it will close the browser that it opened, and you can log back into transmission to see the results.
