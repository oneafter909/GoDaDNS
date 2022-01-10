from datetime import datetime
import os
from threading import Thread
import time
Exec="updateDNS" #The SH file name
#Check every hour
resetTime = datetime(year = datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour, minute=0)


def checkTime():
    while(not False):
        print("CHECK DNS")
        now = datetime.now()
        if(now.hour == resetTime.hour and now.minute == resetTime.minute):
            os.system("bash updateDNS yourdomain.com @")
            print("UPDATE DNS")
        time.sleep(60)

def oneTimeStart():
    os.system("bash updateDNS yourdomain.com @")
    print("UPDATE DNS")


def main():
    oneTimeStart()
    t = Thread(target=checkTime, args="")
    t.name = "Checker thread"
    t.start()

main()
