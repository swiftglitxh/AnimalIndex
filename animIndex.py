import requests
from time import sleep
from bs4 import BeautifulSoup
import os
os.system('cls')
options = {"1": "Search Animal", "2": "Search Aniaml By Locations","3":"List Animals By Letter"}
# Banner
def banner():
    print('''\033[31m
                                 xXXXX   xXXX
                                XXXXXXX XXXXXX
                                "XXXXXX XXXXXX
                                 XXXXX  XXXXX xXx
                             XXXx XXXXX  XX" XXXX
                             XXXXx "XX"  "  XXXXXX
                              XXXXX   xXx  XXXXX"
                               """  xXXXXXx "XX"
                                   XXXXXXXXXX
                                xXXXXXXXXXXXXXx
                                XXXXXXXXXXXXXXX
                                 """"  """"""" \033[37m

                 _                 _ _____           _           
     /\         (_)               | |_   _|         | |          
    /  \   _ __  _ _ __ ___   __ _| | | |  _ __   __| | _____  __
   / /\ \ | '_ \| | '_ ` _ \ / _` | | | | | '_ \ / _` |/ _ \ \/ /
  / ____ \| | | | | | | | | | (_| | |_| |_| | | | (_| |  __/>  < 
 /_/    \_\_| |_|_|_| |_| |_|\__,_|_|_____|_| |_|\__,_|\___/_/\_\\ \n
           *** Like a Pokedex but for real life animals *** \n''')

while True:
    banner()
    for key in options:
        print(" ("+key + ") " + options[key])
    url = "https://a-z-animals.com/animals/"
    choice = input('\n [?] Select an option >> ')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def check():
        search = input("\n[+] Search For A Animal: ").lower()
        if search == '':
            print('Please Enter a animal')
            sleep(2)
            os.system('cls')
        else:
            r = requests.get(url+search+"/",headers=headers)
            sleep(0.8)
            print("[+] Checking database ...")
            sleep(1)
            if r.status_code == 200:
                print(f"\n[!] A \033[32m{search}\033[37m is an animal")
                input('Press Enter to continue ...')
                os.system('cls')
            else:
                print(f"\n[X] A \033[31m{search}\033[37m is not an animal")
                sleep(3)
                os.system('cls')

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
        
        if location == "1":
            country_choice = "Africa"
            loc(country_choice)
        elif location == "2":
            country_choice = "Asia"
            loc(country_choice)
        elif location == "3":
            country_choice = "Central America"
            loc(country_choice)
        elif location == "4":
            country_choice = "Eurasia"
            loc(country_choice)
        elif location == "5":
            country_choice = "Europe"
            loc(country_choice)
        elif location == "6":
            country_choice = "North America"
            loc(country_choice)
        elif location == "7":
            country_choice = "Ocean Locations"
            loc(country_choice)
        elif location == "8":
            country_choice = "Oceania"
            loc(country_choice)
        elif location == "9":
            country_choice = "South America"
            loc(country_choice)
        elif location == location:
            country_choice = location 
            loc(country_choice)

            

    def loc(country_choice):
        site = f"https://a-z-animals.com/animals/location/{country_choice}"
        url = requests.get(site, headers=headers)
        soup = BeautifulSoup(url.text, 'html.parser')
        try:
            links = soup.find('ul',{'class':'list-unstyled'})
            a = links.find_all('li',{'class':'list-item'})
        except:
            print(f' [!] Could not find anywhere called { country_choice}')
            sleep(3)
            os.system('cls')
            exit()
        print(f'\n [+] Gathering Countries in {country_choice}\n')
        sleep(1)
        number = 0
        for link in a:
            number += 1
            print(f" [{number}] {link.text}")
            sleep(0.1)
        place = input("\n (Q) What Country would you like to check?: ")
        if place == place:
            country(country_choice,place)

    def country(country_choice,place):
        site = f"https://a-z-animals.com/animals/location/{country_choice}/{place}/"
        url = requests.get(site, headers=headers)
        soup = BeautifulSoup(url.text, 'html.parser')
        animals = soup.find_all('h5')
        print(f'\n [+] Scanning database for animals in {country_choice}\n')
        sleep(1)
        i = 0 
        x = len(animals) - 14
        number = 0
        print(f" [+] \033[32m{x}\033[37m: Found In database")
        for animal in animals:
            i +=1
            number += 1
            print(f" [{number}] Animal Found: {animal.text}")
            
            if i == x:
                break
        input('Press Enter to continue ...')
        os.system('cls')
            
    def letter():
        letter = input(" (Q) What letter of animals would you like to search for?: ")
        site = f"https://a-z-animals.com/animals/animals-that-start-with-"+letter
        url = requests.get(site, headers=headers)
        soup = BeautifulSoup(url.text, 'html.parser')
        letters = soup.find_all('li',{'class':'list-item'})
        x = len(letters)
        print(f" [+] \033[32m{x}\033[37m: Found In database")
        sleep(0.5)
        print(f'\n [+] Scanning database for animals starting with {letter}\n')
        sleep(1)
        for letter in letters:
            print(" [+] ",letter.text)
        input("\nPress Enter to continue ...")
        os.system('cls')


    if choice == "1":
        print("- You selected \033[31m" + options[choice] + "\033[37m")
        check()
    elif choice == "2":
        print("- You selected \033[31m" + options[choice] + "\033[37m")
        location()
    elif choice == "3":
        print("- You selected \033[31m" + options[choice] + "\033[37m")
        letter()
    else:
        os.system('cls')
