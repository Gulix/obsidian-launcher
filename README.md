# Obsidian Launcher
GUI to launch existing Obsidian vaults.

This utility enables the user to select a vault to open on Obsidian startup. Currently when launching Obsidian, the most recent vault is opened. There is not yet a setting to override this behavior.

Hopefully, Obsidian will get an option to have the native launcher exhibit this behavior.
I have a few vaults for work and personal and have to go through the extra process of switching to and closing the most recently used vault after I opened the desired vault.

![App Screenshot](/app screenshot.png?raw=true "App Screenshot")

# How to Install and/or Run
Run `pip install -r requirements.txt` to install requirements.  
*wxpython is the only nonstandard library package required.*

main.py can then be ran directly from py or pyw

Alternatively (On Windows), I used the pyinstaller package to create a single executable folder.
This enables me to pin the executable my taskbar with the correct icon.

To compile, ensure [pyinstaller](https://pyinstaller.org/en/stable/) is installed.

# How It Works
The GUI is built with wxpython.

1. The available vaults (by name) are obtained from the obsidian configuration file.
Obsidian keeps a record available vaults in a json file.
On Windows, this file is located in:
~\\AppData\\Roaming\\obsidian\\obsidian.json

2. The [Obsidian URI protocol](https://help.obsidian.md/Advanced+topics/Using+Obsidian+URI) is used to open the vault. Using the URI has the benefit of simplicity. 
The system call looks something like this:
"obsidian://open/?vault=" + vault_name

# Needs
I haven't designed obsidian-launcher to work on Mac. I only have Windows computers. Feel free to pull request with platform supported changes.
