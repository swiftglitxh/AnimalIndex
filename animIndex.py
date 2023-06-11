import requests
from time import sleep
from bs4 import BeautifulSoup
import os
from enum import Enum

class Options(Enum):
    SEARCH_ANIMAL = 1
    SEARCH_ANIMAL_BY_LOCATIONS = 2
    LIST_ANIMALS_BY_LETTER = 3

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Banner
def banner():
    print('''
                 _                 _ _____           _           
     /\         (_)               | |_   _|         | |          
    /  \   _ __  _ _ __ ___   __ _| | | |  _ __   __| | _____  __
   / /\ \ | '_ \| | '_ ` _ \ / _` | | | | | '_ \ / _` |/ _ \ \/ /
  / ____ \| | | | | | | | | | (_| | |_| |_| | | | (_| |  __/>  < 
 /_/    \_\_| |_|_|_| |_| |_|\__,_|_|_____|_| |_|\__,_|\___/_/\_\\ \n
           *** Like a Pokedex but for real life animals *** \n''')

def brute_force_url(base_url, wordlist):
    clear()
    banner()

    for option in Options:
        print(f" ({option.value}) {option.name.replace('_', ' ')}")

    url = "https://a-z-animals.com/animals/"
    choice = input('\n [?] Select an option >> ')

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def check():
        search = input("\n[+] Search For An Animal: ").lower()
        if not search:
            print('Please Enter an animal')
            sleep(2)
            clear()
        else:
            r = requests.get(url + search + "/", headers=headers)
            sleep(0.8)
            print("[+] Checking database ...")
            sleep(1)
            if r.status_code == 200:
                print(f"\n[!] A \033[32m{search}\033[37m is an animal")
                input('Press Enter to continue ...')
                clear()
            else:
                print(f"\n[X] A \033[31m{search}\033[37m is not an animal")
                sleep(3)
                clear()

    def location():
        site = "https://a-z-animals.com/animals/location/"
        url = requests.get(site, headers=headers)
        soup = BeautifulSoup(url.text, 'html.parser')
        links = soup.find_all('h3')
        number = 0
        print('\n [Presets]')
        for link in links:
            number += 1
            print(f" [{number}] {link.text}")
        location = input("\n [+] Please select one of the options: ")

        # Rest of the code...

    # Rest of the code...

    if choice == str(Options.SEARCH_ANIMAL.value):
        print("- You selected \033[31m" + Options.SEARCH_ANIMAL.name.replace('_', ' ') + "\033[37m")
        check()
    elif choice == str(Options.SEARCH_ANIMAL_BY_LOCATIONS.value):
        print("- You selected \033[31m" + Options.SEARCH_ANIMAL_BY_LOCATIONS.name.replace('_', ' ') + "\033[37m")
        location()
    elif choice == str(Options.LIST_ANIMALS_BY_LETTER.value):
        print("- You selected \033[31m" + Options.LIST_ANIMALS_BY_LETTER.name.replace('_', ' ') + "\033[37m")
        letter()
    else:
        clear()

# Start the program
brute_force_url()
