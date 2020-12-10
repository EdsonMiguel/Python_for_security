import os 
ip_host = input("Digite o endereço ip: ")
cmd = ("ping {}".format(ip_host))
os.system(cmd)
print("-"*60)
