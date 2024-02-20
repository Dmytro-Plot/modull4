import colorama
import pathlib
import sys
colorama.init(autoreset=True)
path=sys.argv[1]
def listdir(path,tab=0):
    p=pathlib.Path(path) #задаємо шлях
    lst=p.iterdir() #отримуємо список елементів
    for el in lst:
        if el.is_dir(): 
            print(colorama.Fore.GREEN+(tab*' ')+"\\"+el.name)#якщо деректорія друкуємо зеленим
            listdir(path=el,tab=tab+1)
        else:
            print(colorama.Fore.LIGHTBLUE_EX+(tab*' ')+"|"+el.name)#файли друкуємо синім кольором з відступом

listdir(path=path)