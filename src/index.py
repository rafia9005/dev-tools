import time 
from src.handler.whois import index as whois
def index():
    print("1. whois")
    menu_list = {
        1: whois,
    }

    use = int(input("pilih tools : "))

    if use in menu_list:
        time.sleep(1)
        menu_list[use]()
    else:
        print("input tidak valid")
