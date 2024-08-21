## Use cases
### Phone remote
On iOS [iSH](https://ish.app/) runs a complete Alpine Linux distribution + accessible shell from an intuitive app interface. Scripts such as this one or entire applications can be installed and run from your phone.

### Auto-type
The native auto-type capability for most Roku applications is incredibly fast compared to typing with a remote or even the phone app -- this script leverages that in the app search capability (opens an app and searches for a show/movie). 

Additionally, some apps which do not implement native auto-type can be easily manipulated via other supported commands such as simple left/right/up/down/select's to auto-type based on a standard alphabetical keyboard layout at similar speeds (this is the case for Prime Video).

## Installation
### Ensure you have python installed:
#### Debian/Ubuntu
`apt-get install python3 python3-dev`
#### Alpine (iSH)
`apk add python3`
#### macOS and Windows
Download and install from the python [downloads page](https://www.python.org/downloads/)

### Clone the script
`git clone https://github.com/DaDevFox/RokuAutomation`

## Usage
`python main.py [TV ip address] [command] [parameters]`

### Commands
`vol_up`, `vol_down`: increases/decreases volume 1 tick

`vol_mute`: mutes/unmutes (toggles) the device

`up`, `down`, `left`, `right`: moves the selector in the specified direction

`click`: clicks the selector

`execute`: takes in a string that can specify any of the above actions in any order/repitition and executes it. Adding a number specifies how many times to perform something (e.g. 'right 2 up 4 click' goes right twice, up four times, and clicks). Also converts certain semantic phrases to commands ('move right' -> `right'; `volume up` -> `vol_up` and spelled out numbers to literal numbers)

`app_search`: takes an app name (param 1) and a query (param 2); if the app isn't already open, it is opened and navigated to the appropriate "search" feature. If it is open the script assumes the user navigated to the search page already and is on the keyboard. Then it auto-types the query and searches.

All commands power on and initialize the TV if it is not already prepared

## Contributing
This script only currently supports a few apps and commands; anyone is welcome to open a pull request!
