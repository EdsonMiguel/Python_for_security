import os 
ip_host = input("Digite o endereço Ip/Host: ")
cmd = ("ping {}".format(ip_host))
os.system(cmd)
print("-"*60)
