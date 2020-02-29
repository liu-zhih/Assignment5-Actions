# import math
from datetime import date


def firstrun():
    return "success"


# def get_area(radius):
#     return round(radius*radius*math.pi)


# def get_first_and_last_ele(mylist):
#     return mylist[0], mylist[-1]


def get_days_bet_dates(date_1, date_2):
    result = date_1 - date_2
    return result.days
