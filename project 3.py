import time
import datetime
from datetime import datetime, timedelta

ch='y'

while ch!='n':
    try:
        est_date_dept = input("Esimated date of departure (YYYY-MM-DD):")
     
        est_time_dept = input("Estimated time of departure (HH:MM AM/PM):")
        dist = int(input("Enter Miles:"))
        speed = int(input("Enter miles per hour:"))

        travel_time = float(dist)/speed

        t=timedelta(hours=travel_time)
        t=str(t)

        t=t.split(":")

        if t[2] > "00":
            t[1]=int(t[1])+1
            travel_time+=.01

        time = datetime.strptime(est_time_dept, "%I:%M %p")

        est_time_dept = datetime.strftime(time, "%H:%M")
        est_date_dept = est_date_dept+" "+est_time_dept

        arr_date_time = datetime.strptime(est_date_dept, "%Y-%m-%d %H:%M")

        arr_date_time += timedelta(hours=travel_time)

        est_arr = arr_date_time.strftime("%Y-%m-%d %I:%M %p")

        est_arr=str(est_arr)

        est_arr=est_arr.split()

        print("Estimated travel time")
        print("Hours:",t[0],"Minutes:", t[1])

        print("Estimated date of arrival:",est_arr[0])

        print("Estimated time of arrival:", est_arr[1], est_arr[2])

        ch = input("Continue? (y/n):")
        break
    except:
        continue
