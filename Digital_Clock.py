# EGC-18 Digital Clock
import time
import snaps


#Loop that never ends
while True :

#Get the time
    current_time = time.localtime()

    hour_string = str(current_time.tm_hour)
    minute_string = str(current_time.tm_min)
    second_string = str(current_time.tm_sec)

    time_string = hour_string+ ':'+minute_string+':'+second_string
    
    print(time_string)
    time.sleep(1)

#Why does it shows an error when I import snaps 
