# Python program to create a Countdown Timer
# In this Example, you will learn to create countdown timer.

# Python while loop, python divmod(), python time module
'''import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -=1
    print("STOP!!!")
countdown(60)'''