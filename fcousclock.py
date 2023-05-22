import time, os

def countdown(t):
    while t > 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer + " remaining.", end="\r")
        time.sleep(1)
        t -= 1

    print("Time's up!")
    os.system('afplay /System/Library/Sounds/Ping.aiff')

countdown(1500) # 1500 seconds = 25 minutes
