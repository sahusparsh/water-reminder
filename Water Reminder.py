import time

import win32com.client as s

import winsound

from win10toast import ToastNotifier

a = s.Dispatch("SAPI.SpVoice")

a.Voice = a.getVoices("gender=male").Item(0) # <--Change voice

frequency=8000

duration=500

print("                                 *** WATER REMINDER ***  ")

while True:

    try:

        d = float(input("* ENTER HOW MANY MINUTES LATER YOU WANT WATER ::-> "))

        break

    except ValueError:

        a.Speak(" SORRY , ENTER NUMBER ONLY !! ")

        print("ENTER NUMBER ONLY !! ")

def notification(title, message):

    c = ToastNotifier()

    c.show_toast(title, message, duration=15)

if __name__ == "__main__":

    title = " NOTIFICATION MESSAGE "

    b = time.strftime("%H hr: %M min: %S sec")

    message = f"!! Hey, it's {b}. Time to drink water :) !!\n                           KEEP HYDRATED :) "

    time.sleep(d*60)

    a.Speak(" It's Time To Drink Water !!! ")

    print(" !! DRINK WATER !!  >",end='', flush=True)

    time.sleep(0.65)

    print(" !! DRINK WATER !!  >",end='', flush=True)

    time.sleep(0.40)

    print(" !! DRINK WATER !!", flush=True)

    a.Voice = a.getVoices("gender=female").Item(0) # <--Change voice

    a.Speak(" Keep hydrated ")

    winsound.Beep(frequency, duration)

    print("|--------------------------------------------------------------------------|")

    notification(title, message)
