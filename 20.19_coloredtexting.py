# Printing Colored Text with Python
# Traditionally, printing full colour text to the terminal is accompplished by a series of escape cahracters on Linux or OS X systems. However, this will not work for Windows operating systems.Now let's see how to print coloures text with Python using the Colorama module:
'''import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.BLUE+Back.CYAN+Style.NORMAL + "Hello, we fore using colorama" + Fore.MAGENTA + Back.GREEN + "We are seeing different color effects.")
print(Fore.YELLOW + Back.BLACK + "Hi to all who learn each module one by one")'''