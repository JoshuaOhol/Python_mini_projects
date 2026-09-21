# countdown timer program


import time
my_time = int(input("enter the time in seconds: "))

for x in range(0, my_time):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


time.sleep (1)
print("time's up")