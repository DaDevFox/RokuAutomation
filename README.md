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

