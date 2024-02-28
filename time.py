import time
ticks = time.time()
print("number of ticks since jan 1970: ", ticks)

localtime = time.asctime(time.localtime(ticks))
print("localtime: ", localtime)

import calendar 
cal = calendar.month(2018, 1)
print("calendar: ", cal)

print(time.strftime('%x')) #print date
print(int(time.strftime('%H%M%S'))) #print local time