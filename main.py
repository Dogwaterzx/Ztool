
import random
import time
import colorama
import sys
from os import system, name
from time import sleep
from colorama import Fore, Back, Style
colorama.init()
import time
import random

    #functions
def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result
print(Fore.CYAN + " ▄· ▄▌▄▄▄▄▄·▄▄▄▄•    ▄▄ • ▄▄▄ . ▐ ▄ ")
print("▐█▪██▌•██  ▪▀·.█▌   ▐█ ▀ ▪▀▄.▀·•█▌▐█")
print("▐█▌▐█▪ ▐█.▪▄█▀▀▀•   ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌")
print(Fore.MAGENTA + " ▐█▀·. ▐█▌·█▌▪▄█▀   ▐█▄▪▐█▐█▄▄▌██▐█▌")
print("(Mobile)")

print()
print()

print("Made by, ytz!#0001")
print("Thanks for buying ;)")
print()
print()
print(Fore.LIGHTMAGENTA_EX)

print("What gen do you want to launch?")
print("1) Amazon Store Card Gen")
print("2) Discord Nitro Gen + Checker")
print("3) Netflix Gift Code Gen")  
print("4) Xbox Gift Card Gen")
print("5) Playstation Gift Card Gen")
print("6) Other")

choice  = int(input("Choice=  "))

if choice == 1:
    import random
    import time
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()

    class validator():

        def __init__(self):
            self.cardNumber = None
            self.Brand = None

        def __findBrand(self):
            if self.cardNumber[:2] in ['34', '37']:
                self.Brand = 'American Express'
            elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
                self.Brand = 'Diners Club - Carte Blanche'
            elif self.cardNumber[:2] in ['36']:
                self.Brand = 'Diners Club - International'
            elif self.cardNumber[:2] in ['54']:
                self.Brand = 'Diners Club - USA & Canada'
            elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
                '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
                self.Brand = 'Discover'
            elif self.cardNumber[:3] in ['637', '638', '639']:
                self.Brand = 'InstaPayment'
            elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
                self.Brand = 'JCB'
            elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
                self.Brand = 'Maestro'
            elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
                self.Brand = 'MasterCard'
            elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
                self.Brand = 'VISA Electron'
            elif self.cardNumber[0] in ['4']:
                self.Brand = 'VISA'
            else:
                self.Brand = 'Unknown Brand'

        def validate(self, number):
            """
            number: str or int credit card number
            """
            if number is None: return 'Not a valid Credit Card Number'
            if number is bool: return 'Not a valid Credit Card Number'
            if number is float: return 'Not a valid Credit Card Number'
            number = ''.join(x for x in str(number).strip().split())
            if number.isdigit() and 13 <= len(number) <= 19:
                # Identify Brand
                self.cardNumber = number
                self.__findBrand()
                # Luhn's Algorithm
                lastDigit = int(number[-1])
                base = [int(x) for x in reversed(number[:-1])]
                base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
                base = [x if x <= 9 else x - 9 for x in base]
                base = sum(base)
                base = (base * 9) % 10
                if base == lastDigit:
                    print(Fore.GREEN)
                    return f'[!] {self.cardNumber} is a valid Store Card!'
                    file = open("cards.txt", "w")
                    number = repr(number)
                    file.write(number)
                    file.close()
                else:
                    print(Fore.RED)
                    return f'[!] {self.cardNumber} is not a valid Store Card!'
            else:
                return 'Not a valid Credit Card Number'


    print(" ")
    print(Fore.LIGHTMAGENTA_EX + " ")
    print("1. 1k Card")
    print("2. 2k Card")
    print("3. 5k Card")
    print("4. 10k Card")
    print(" ")
    whatcard = input("[?] What Card Do You Want To Generate? (1, 2, 3 or 4) ")
    print(" ")
    whatcard = int(whatcard)
    randomnums = "0123456789"

    if whatcard == 1:
        howmany = input("[?] How Many Cards Do You Want? ")
        time.sleep(0.8)
        print("           [/] Starting")
        time.sleep(0.8)
        howmany = int(howmany)

        for x in range(howmany):
            bin = "60457811425"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
            print(validator().validate(int(cc)))

    if whatcard == 2:
        howmany = input("[?] How Many Cards Do You Want? ")
        time.sleep(0.8)
        print("[/] Starting")
        time.sleep(0.8)
        howmany = int(howmany)
        for x in range(howmany):
            bin = "604578114"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            ff6 = random.choice(randomnums)
            ff7 = random.choice(randomnums)
            cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
            print(validator().validate(int(cc)))

    if whatcard == 3:
        howmany = input("How Many Cards Do You Want? ")
        howmany = int(howmany)
        for x in range(howmany):
            bin = "604578118"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            ff6 = random.choice(randomnums)
            ff7 = random.choice(randomnums)
            cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)+str(ff7)
            print(validator().validate(int(cc)))

    if whatcard == 4:
        howmany = input("[?] How Many Cards Do You Want? ")
        time.sleep(0.8)
        print("[/] Starting")
        time.sleep(0.8)
        howmany = int(howmany)
        for x in range(howmany):
            bin = "6045781123"
            ff1 = random.choice(randomnums)
            ff2 = random.choice(randomnums)
            ff3 = random.choice(randomnums)
            ff4 = random.choice(randomnums)
            ff5 = random.choice(randomnums)
            ff6 = random.choice(randomnums)
            cc = str(bin)+str(ff1)+str(ff2)+str(ff3)+str(ff4)+str(ff5)+str(ff6)
            print(validator().validate(int(cc)))

elif choice == 2:
    import os
    import ctypes
    import requests
    import random
    import string
    import time
    print("")

    print("███╗░░██╗██╗████████╗██████╗░░█████╗░░ ██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
    print("████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗ ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
    print("██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║ ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
    print("██║╚████║██║░░░██║░░░██╔══██╗██║░░██║ ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
    print("██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝ ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
    print("╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░ ╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")


    num = int(input('Input How Many Codes to Generate and Check: '))

    with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
        print("Your nitro codes are being generated, be patient!")

        start = time.time()

        for i in range(num):
            code = "".join(random.choices(
                string.ascii_uppercase + string.digits + string.ascii_lowercase,
                k = 19
            ))

            file.write(f"https://discord.gift/{code}\n")

        print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

    with open("Nitro Codes.txt") as file:
        for line in file.readlines():
            nitro = line.strip("\n")
    
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

            r = requests.get(url)

            if r.status_code == 200:
                print(f" Valid | {nitro} ")
                break
            else:
                print(f" Invalid | {nitro} ")

    time.sleep(0.2)

    print("Valid codes will be in Valid Codes.txt - if there none then keep generating :)")

elif choice == 3:
    import colorama
    import random, string
    
    upper_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letter = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'

    amount = int(input("Gift Code Amount : "))
    for i in range(amount):
        code = "https://www.netflix.com/redeem/" + "".join(random.choices(string.ascii_uppercase + string.digits, k=11))
        print("[GENERATED] " + code)
        giftcode = open('netflixcodes.txt', 'a')
        giftcode.write(code + "\n")

elif choice == 4:
  import requests
  print("Checked Xbox Gift Codes ;)")
  print("")
  print("How many of them?")
  nn = input(">")
  print("")
  n = int(nn)
  for x in range(n):
        print("")   
        v = g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)+"-"+g(5)
        url = "https://microsoft.com/api/entitlements/redeem/" + v

        s = requests.get(url)

        if s == 200:
                print(f" Valid | {v} ")
                break
        else:
                print(f" Invalid | {v} ")
      
  print("Done!")

elif choice == 5:
    import requests
    print("Checked PS codes")
    print("")
    print("How many of them?")
    nn = input(">")
    print("")
    n = int(nn)
    for x in range(n):
        print("")
        v = (g(4)+"-"+g(4)+"-"+g(4))
        url = "https://playstation.com/api/redeem/" + v

        s = requests.get(url)

        if s == 200:
                print(f" Valid | {v} ")
                break
        else:
                print(f" Invalid | {v} ")

elif choice == 6:
    #interface
    print("JUST SO YOU KNOW THESE ARE UNCHECKED SO YOU'RE GONNA HAVE TO GO FIND A CHECKER FOR YOUR CODES")
    print("Multiple Gift Card Generator")
    print("")
    print("What Giftcard you need to generate?")

    tt = input("\n[-] Amazon\n[-] Roblox\n[-] Fortnite\n[-] Ebay\n[-] iTunes\n[-] Paypal\n[-] Visa\n[-] Playstation\n[-] Steam\n[-] Xbox\n[-] PlayStore\n[-] Minecraft\n\n>")

    t = tt.lower()
    print("")
    print("How many of them?")
    nn = input(">")
    print("")
    n = int(nn)
    if t == "minecraft":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(4)+"-"+g(4))
		
    if t == "paypal":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(4)+"-"+g(4))
			
    if t == "amazon":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(6)+"-"+g(4))
		
    if t == "netflix":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(6)+"-"+g(4))
		
    if t == "steam":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(6)+"-"+g(5))
		
    if t == "fortnite":
	    for x in range(n):
		    print("")
		    print(g(5)+"-"+g(4)+"-"+g(4))
		
    if t == "roblox":
	    for x in range(n):
		    print("")
		    print(g(3)+"-"+g(3)+"-"+g(4))
		
    if t == "itunes":
	    for x in range(n):
		    print("")
		    print(g(16))
		
    if t == "ebay":
	    for x in range(n):
		    print("")
		    print(g(10))
			
    if t == "playstore":
	    for x in range(n):
		    print("")
		    print(g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4)+"-"+g(4))
		
    print("")
    print("-----Generation completed-----")
    time.sleep(360)
