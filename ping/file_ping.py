import os

with open("hosts.txt") as file:
    dump = file.read()
    dump =  dump.splitlines()
    print("-"*60)

    for ip in dump:
        os.system('ping '+ip)