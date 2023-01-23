from datetime import datetime
import math
import numpy as np
import random as rd

def anchor(year):
    century = math.floor(year/100)
    century_anchor = (5*(century%4))%7+2
    decade = year-century*100
    if decade%2 != 0: decade += 11
    decade /= 2
    if decade%2 != 0: decade += 11
    decade_anchor = 7-(decade%7)
    return int((decade_anchor+century_anchor)%7)

def is_leap(year):
    if year%4 != 0:
        return False
    if year%100 == 0 and year%400 != 0:
        return False
    return True

def rd_date(min_year, max_year):
    rd_year = rd.randint(min_year, max_year)
    rd_month = rd.randint(1,12)
    offset = 0
    if is_leap(rd_year):
        offset = 1
    if rd_month in [1, 3, 5, 7, 8, 10, 12]:
        rd_day = rd.randint(1,31)
    if rd_month in [4, 6, 9, 11]:
        rd_day = rd.randint(1,30)
    if rd_month == 2:
        rd_day = rd.randint(1, 28+offset)
    return [rd_day, rd_month, rd_year]

def print_date(date):
    print(str(date[0])+"."+str(date[1])+"."+str(date[2]))

def weekday(date):
    date = datetime(date[2], date[1], date[0])
    return date.weekday()

def get_seconds(time):
    time_digits = list(str(time))
    return int(time_digits[0])*60*60+int(time_digits[2])*10*60+int(time_digits[3])*60+int(time_digits[5])*10+int(time_digits[6])+int(time_digits[8])*0.1+int(time_digits[9])*0.01

def ask_date(min_year, max_year, max_attempts):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    times = []
    print("Push ENTER to start the timer!")
    inp = input()
    if len(inp) == 0:
        start_global = datetime.now()
        count = 0
        global_count = 0
        for i in range(max_attempts):
            date = rd_date(min_year, max_year)
            start = datetime.now()
            print_date(date)
            inp = input()
            try:
                test_int = int(inp)
            except:
                print("Attempt abortet! The correct weekday would have been:", weekdays[weekday(date)]+".", "Anchor:", str(anchor(date[2]))+".")
                break
            if int(inp) > 7 or int(inp) < 0:
                print("Attempt abortet! The correct weekday would have been:", weekdays[weekday(date)]+".", "Anchor:", str(anchor(date[2]))+".")
                break
            if int(inp)%7 == (weekday(date)+1)%7:
                stop = datetime.now()
                count += 1
                global_count += 1
                times.append(round(get_seconds(stop-start),2))
                print("Correct! It is a", weekdays[weekday(date)]+".", "You took:", round(get_seconds(stop-start),2), "seconds.", "Anchor:", str(anchor(date[2]))+".")
            else:
                stop = datetime.now()
                global_count += 1
                times.append("DNF")
                print("Wrong! The correct weekday is:", weekdays[weekday(date)]+".", "You took:", round(get_seconds(stop-start),2), "seconds.", "Anchor:", str(anchor(date[2]))+".")
        stop_global = datetime.now()
        print("\n")
        print("You got", count, "of", global_count, "correct in", stop_global-start_global)
        if count > 1:
            print("Ratio:", round(get_seconds(stop_global-start_global)/count, 2), "Seconds/Date")
            print("Average of", len(times), "is:", average(times))
    else: return print("Attempt aborted!")

def give_weekday(day, month, year):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date = datetime(year, month, day)
    print("The", str(day)+"."+str(month)+"."+str(year), "is a", str(weekdays[date.weekday()])+".")

def count_list(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count += 1
    return count
    
def average(values):
    length = len(values)
    number = math.ceil(0.05*length)
    num_dnf = count_list(values, "DNF")
    if num_dnf > number:
        return "DNF"
    if len(values) <= 2:
        return "To short for average."
    num_bad = number - num_dnf
    for i in range(num_dnf):
        values.remove("DNF")
    values.sort()
    for i in range(num_bad):
        values.pop(-1)
    for i in range(number):
        values.pop(0)
    return round(sum(values)/len(values),2)

#give_weekday(3,7,2025)

ask_date(1600, 2300, 5)