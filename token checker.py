import pyfiglet
import requests
from colorama import Fore,Back,Style,init
init(autoreset=True)
#
print(f"""{Fore.LIGHTBLUE_EX}
                   ███╗   ███╗██╗   ██╗████████╗██╗  ██╗██╗ ██████╗
                   ████╗ ████║╚██╗ ██╔╝╚══██╔══╝██║  ██║██║██╔════╝
                   ██╔████╔██║ ╚████╔╝    ██║   ███████║██║██║     
                   ██║╚██╔╝██║  ╚██╔╝     ██║   ██╔══██║██║██║     
                   ██║ ╚═╝ ██║   ██║      ██║   ██║  ██║██║╚██████╗
                   ╚═╝     ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝
                   {Fore.RESET}                                                             
           """)

print(f"{Fore.GREEN}Enter file name: ")
inp = input()

with open(inp + ".txt") as f:
    for line in f:
        token = line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print(Fore.LIGHTGREEN_EX + "{} is valid.".format(token))
        else:
            print(Fore.LIGHTRED_EX + "{} is invalid.".format(token))
