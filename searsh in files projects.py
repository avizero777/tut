from colorama import Fore, Style

file1 = input('enter name of the file :')

from pathlib import Path
path_to_file = file1
path = Path(path_to_file)

if path.is_file():
    print(Fore.LIGHTGREEN_EX +'The file exist')
    print(Style.RESET_ALL)
else:
    print(Fore.RED +'The file does not exist')
    print(Style.RESET_ALL)
    quit()

while True:
    myWord = input('enter the word :')
    file = open(file1, "r")
    data = file.read()
    times = data.count(myWord)
    if times == 0 :
        print(Fore.RED +'the word not found ')
        print(Style.RESET_ALL)
    else:
        print(f'{Fore.LIGHTGREEN_EX}number of ocurences of the word is :{times}')
        print(Style.RESET_ALL)
    file.close()
