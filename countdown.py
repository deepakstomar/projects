import time
t = int(input('Enter time to start timer: '))
while t:
    mins, secs = divmod(t, 60)
    print(f"{mins:02d}:{secs:02d}", end = '\r')
    time.sleep(1)
    t -=1   