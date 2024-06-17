import os
import subprocess

def findmyip():
    public_ip = ('curl ifconfig.me')
    print("")
    print("This is your public IP")
    print(os.system(public_ip))
    
    print("")
    print("------------------------------------------------------------------------------------")
    networkinterfaces = ("ifconfig")
    print("")
    print('Theses are all your avaiable network interfaces')
    print("")
    print(os.system(networkinterfaces))
    
    

findmyip()