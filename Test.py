from Cours import *


def findClass():
    num = 0
    pogw = 0
    h = hour
    if minute >= 15:
        h += 1
    order = [SemaineB, SemaineA]
    if year == 2020:
        if week_of_year % 2 == 0:
            order = [SemaineA, SemaineB]
    elif year == 2021:
        if week_of_year % 2 == 1:
            order = [SemaineA, SemaineB]
    CoursN1 = None
    CoursN2 = None
    stop = False
    while not stop:
        if num + 1 > len(order[0]):
            CoursN1 = order[1][0]
            CoursN2 = order[1][1]
            stop = True
        elif order[0][num].jour == day_of_week:
            if order[0][num].heure >= hour:
                CoursN1 = order[0][num]
                if num + 1 == len(order[0]):
                    CoursN2 = order[1][0]
                else:
                    CoursN2 = order[0][num + 1]
                stop = True
        num += 1
    return [CoursN1, CoursN2]


print(findClass()[0].nom, findClass()[1].nom)
