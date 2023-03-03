         
                               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                            y@@@@@@@@@@@@@@@@@@@@@@KMM%%%@@@@%%%MMK@@@@@@@@@@@@@@@@@@@@@@p
                           ]@@@@@@@@@@@@@@@@@KM%@@@@@@@@@@@@@@@@@@@@@@RMK@@@@@@@@@@@@@@@@@@
                           $@@@@@@@@@@@@@@M@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@MK@@@@@@@@@@@@@@
                           $@@@@@@@@@@@M@@@@@@@@@@@@@@@@@@@KMMM%%%%%%%%%MMKK@@R@@@@@@@@@@@@
                           $@@@@@@@@@0@@@@@@@@@@@@@@@KM%%kRPPPIBR|zPww||||kkkBBBR0@@@@@@@@@
                           $@@@@@@@0@@@@@@@@@@@@@K%E|||||||||||||mw|TkBU|||kkkBBFv?@@@@@@@@
                           $@@@@@M@@@@@@@@@@@@@MkBP||||||||||mBWWPT>wIRRBmH|TBBBBBBc1@@@@@@
                           $@@@@K@@@@@@@@@@@M%kRBF||||||||||TTBBPm||||TBBRRBmBBBBBBBU?@@@@@
                           $@@@U@@@@@@@@@@MHRRRRH||||||||||||||TH||||||||TRBBBBBBBBBBFJ@@@@
                           $@@D@@@@@@@@@@HRRRRB|||||||||vTPU|||||||||TkBPw(TBBBBBBBBBBFJ@@@
                           $@M$@@@@@@@@KkRRRRF||||||||||||TH|kHzY||zPkzmBRRRBBBBBBBBBB@U1@@
                           $@U@@@@@@@@HRRRRRB|||||||||||||||||||||mkRRRRRRRRBBBBBBBBBBBB|@@
                           $@$@@@@@@@HRRRRRRB||||||||||||||||||||BRRRRRRRRRRBBBBBBBBBBB@H1@
                           $@$@@@@@@MRRRRRRRRJH|||||||||||||||zmBRRRRRRRRRRBBBBBBBBBBBBBP4@
                           $@$@@@@@@kRRRRRRRRIP||||||mPBmkBmHTRRRRRRRRRRRRRBBBBBBBBBBBBBB4@
                           $@%@@@@@HRRRRRRRRRWkH|||vBRRRRRRRBckRBRRRRRRRRRBBBBBBBBBBBBB@Ej@
                           $@&@@@@@RRRRRRRRRRRRB|||TRRRRBBRBBPBkPRRRRRRRRBBBBBBBBBBBBBB@F&@
                           $@@%@@@@RRRRRRRRRRRRRm|||TBPH|kRRRRBmIIPPBRRRBBBBBBBBBBBBBB@Bk@@
                           $@@@@@@@RRRRRRRRRRRRRRRBmmc||TPPBRRBBBBBBBBBBBBBBBBBBBBBBB@@F@@@
                           $@@@&@@@BBRRRRRRRRRRRRRRRRRBPm||BRRRRRRRBBBBBBBBBBBBBBBBB@@B&@@@
                           $@@@@&@@RBBBBRRRRRRRRRRRRRRRRRBwTBBBBFTTBFkBBRBBBBBBBBBB@@R&@@@@
                           $@@@@@@%@BBBBBBBBBRRRRRRRRRRRRRBBBBBH|kkkkkkkkkkkBBBBB@@@k@@@@@@
                           $@@@@@@@RkBBBBBBBBBBBBBBBBBBBBBBBBBBPkkkkkkkkkBBBBB@BB@B$@@@@@@@
                           $@@@@@@@@@|%BBBBBBBBBBBBBBBBBBBBBRkkkkkkkkkBBBBBB@B@BB$@@@@@@@@@
                           $@@@@@@@@@@@|TBBBBBBBBBBBBBBBBBBkkkkkkkkBBBBBB@B@BBR@@@@@@@@@@@@
                           $@@@@@@@@@@@@@@|TBBBBBBBBBBBBBBBBkBBBBBBBBB@BBBBR$@@@@@@@@@@@@@@
                           1@@@@@@@@@@@@@@@@@p}PBBBBBBBBBBBB@@BBB@BBBBBR$@@@@@@@@@@@@@@@@@@
                            %@@@@@@@@@@@@@@@@@@@@@@p@IPRBBBBBBRPP$$@@@@@@@@@@@@@@@@@@@@@@@F
                             'I%MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM%F'
                                ````````````````````````````````````````````````````````
     
                                    # Wigle-WiFi - WiFi Access Point Trilateration Tool.

This tool allows you to get the approximate location of a Wi-Fi access point (AP) using the long-awaited: Wigle.net API. The tool uses trilateration to calculate the AP's location based on its signal strength and the location of nearby access points.

## Requirements

To use this tool, you need to have Python 3 installed on your system. You also need to create a free account on Wigle.net and obtain an API key.

## Installation

- Clone this repository or download the ZIP file and extract it to a directory of your choice.
- Create a file named config.json in the same directory as wigle-Wifi and add your Wigle.net API key in the following format:

{
    "api_auth": "YOUR_API_KEY_HERE"
}

- Open a terminal or command prompt in the directory where you extracted the files and run the command 

pip3 install -r requirements.txt 

...to install the required Python libraries.

## Usage

- Open a terminal or command prompt in the directory where you extracted the files.
- Run the command: 
  
  python3 Wigle-WiFi.py 

- Choose option 1 to get the location of a Wi-Fi access point.
- Enter the MAC address of the access point when prompted.
- The tool will display the latitude and longitude of the access point's location.

### License

This tool is licensed under the MIT license. See the LICENSE file for more information.

### Acknowledgments

This tool was created using the Wigle.net API and the trilateration algorithm developed by Thomas Pototschnig. Thanks to the developers of these tools for making this project possible.
