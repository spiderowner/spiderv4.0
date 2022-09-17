import json
from colorama import *
import ctypes
import phonenumbers
from phonenumbers import geocoder,carrier
from phonenumbers.phonenumberutil import number_type
init()
data = json.loads(open("Beta\\Australia\\data.json").read())
# 660932000059
class Info:
    valid = 0
    invalid = 0
info = Info()
def Checker(number):
    global valid,invalid
    number = number.replace("+","")
    obj = phonenumbers.parse("+"+number)
    valid = phonenumbers.is_valid_number(obj)
    if valid:
        temp = number[2:4]
        try:
            info.valid+=1
            CARRIER = data[temp]
            linetype = "mobile" if carrier._is_mobile(number_type(obj)) else "Fixed"
            print(f"{Fore.LIGHTGREEN_EX}(+) +{number} | Carrier: {CARRIER} | Line: {linetype}")
            ctypes.windll.kernel32.SetConsoleTitleW("Valid: {} | Invalid: {}".format(info.valid,info.invalid))
        except:
            info.invalid+=1
            ctypes.windll.kernel32.SetConsoleTitleW("Valid: {} | Invalid: {}".format(info.valid,info.invalid))
            pass
    elif valid == False:
        info.invalid+=1
        ctypes.windll.kernel32.SetConsoleTitleW("Valid: {} | Invalid: {}".format(info.valid,info.invalid))
    
lines = open("aus.txt").readlines()
for line in lines:
    line = line.split("\n")[0]
    Checker(line)   