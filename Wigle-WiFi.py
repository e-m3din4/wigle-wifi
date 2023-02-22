import requests
import json

def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print('Error: config file not found')
        return None

def get_location(netid, config):
    headers = {
        'Authorization': 'Basic ' + config['api_auth']
    }

    url = 'https://api.wigle.net/api/v2/network/search?onlymine=false&netid=' + netid
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Error: ' + response.text)
        return None

    data = response.json()

    if not data['results']:
        print('Error: no results found')
        return None

    location = (data['results'][0]['trilat'], data['results'][0]['trilong'])
    return location

def main():
    config = load_config()
    if not config:
        return

    while True:
        print('-------------------------------------------------------------')
        print('|                               . ......                    |')
        print('|                   . ,;;;;,  ..  ,;;;;;,.                  |')
        print('|               .;:: .                  ..;:;:;             |')
        print('|            .;c,.                 .......  ..:;:;          |')
        print('|           c;.            . ,:loxxdxO OO0OOkxolod;         |')
        print('|        .l;           .:dOK0OO00O0O0 OkdxO0000OxokO:       |')
        print('|      .c:.         .;dk0KKKKKKK0Ok xxO0OddkO00k oodkk      |')
        print('|     .o.          lddOKKKKKKKKK dddx0KOkkdddxkOoo oldOc    |')
        print('|    o .         odddkKKKKKKKKK K00 0KKKKK0OxdddoooolloO.   |')
        print('|   o.       .lddddOKKKKKKK0O 0K KKKKKKOkxk0kddooo ollooO   |')
        print('|  .        ,ddddx0KKKKKKKKK0 k0 0 0K0OO0kddxddoooo llld0.  |')
        print('|  c       :ddddd0KKKKKKKKKKK 00 0 00kddddd ddd oooollllkd  |')
        print('|  o,      cdddddx0KKKKKKKKKKKkKKKK Oddddd dddddo oo kkkkd0 |')
        print('|  x.     ;dddddddO0KKKKKKKKKKKKKK0k dddd ddddddooo okkkkkO |')
        print('|  d.    .ddddddddOkKKKKK0OkOOkO0  ddddd dddddddddddkkkkkkk |')
        print('|  d.    lddddddddkxk0KKKOddddd dOdddddddd ddddoooookkkkkkk |')
        print('|  o    .dddddddddddkKK0ddddd ddxxdddddddddd doooookkkkkklO |')
        print('|  .c    dddddddddddxOKKOddk0 dddxxkxdxddddddo oookkkkkccdd |')
        print('|   o   ,dddddddddddddxkOO0K0 dddddddxkxddddoooo kkkkkcclO. |')
        print('|   .o.  dddddddddddddddddxk0 0ddddddddddooooooo dddddccx.  |')
        print('|    l..oddddddddddddddddddddO ddddkOxxxddddool kkkkkcdl    |')
        print('|     .l.ooooddddddddddddddddddx xx000O00OOOOkk kkkkkcx     |')
        print('|      .codooooooodddddddddddddooo O00OOOOOOkk kxxoco       |')
        print('|         xkooooooooooooooooooooxkO OOOOOkkkkk xdodk        |')
        print('|           xkdooooooooooooooodOOOOOOO kkkkkx ddxk          |')
        print('|            .lkxokkkkkkkkkkkkkkkkkk kkxxx x dko            |')
        print('|                cxkdkkkkkkkkkkkkxkk xxdd dddk.             |')
        print('|                   .xcxxcxxdddoodxkkk  ooo                 |')
        print('|                                                           |')
        print('|-----------------------------------------------------------|')
        print('|    Wigle-WiFi --- WiFi-Access Point Trilateration Tool    |')
        print('|-----------------------------------------------------------|')
        print('|                      1. Get location                      |')
        print('|                      2. Exit                              |')
        print('|-----------------------------------------------------------|')
        choice = input('              Enter choice (1/2): ')

        if choice == '1':
            netid = input('Enter WiFi network MAC address: ')
            location = get_location(netid, config)

            if location:
                print('Location: ' + str(location))
        elif choice == '2':
            break
        else:
            print('Error: invalid choice')

if __name__ == '__main__':
    main()
