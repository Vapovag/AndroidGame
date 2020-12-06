from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from Cours import *

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    """def findClass(self):
        found = False
        num = 0
        h = hour
        semaine = ""
        if year == 2020:
            if week_of_year % 2 == 0:
                semaine = "A"
            else:
                semaine = "B"
        elif year == 2021:
            if week_of_year % 2 == 0:
                semaine = "B"
            else:
                semaine = "A"
        if minute >= 15:
            h += 1
        C1 = None
        C2 = None
        while C1 is None:
            C = listeCours[num]
            if day_of_week >= 6:
                if semaine == "A":
                    C1 = c1
                    C2 = c2
                else:
                    C1 = c2
                    C2 = c3
            else:
                if day_of_week == 4:
                    if hour == 9 and minute < 15:
                        C1 = c27
                        C2 = c28
                    elif hour == 10 and minute < 40:
                        C1 = c27
                        C2 = c28
                if C.jour == day_of_week:
                    if C.heure == h:
                        if C.semaine == "AB" or C.semaine == semaine:
                            C1 = C
                elif C.jour > day_of_week:
                    if C.semaine == "AB" or C.semaine == semaine:
                        C1 = C
                num += 1
        while C2 is None:
            break
        return C1"""

    def findClass(self):
        num = 0
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
            if num + 1 > len(order[0]): #si l'algorythme n'a rien trouvé
                CoursN1 = order[1][0] #le premier cours de la semaine d'après
                CoursN2 = order[1][1] #le second cours de la semaine d'après
                stop = True #stop la boucle
            elif order[0][num].jour == day_of_week: #si le jour correspond au jour du cours sélectionné
                if order[0][num].heure >= hour: #si l'heure du cours est supérieure à l'heure (le 1er cours sera le bon)
                    CoursN1 = order[0][num]
                    if num + 1 == len(order[0]):
                        CoursN2 = order[1][0]
                    else:
                        CoursN2 = order[0][num + 1]
                    stop = True
            elif order[0][num].jour > day_of_week:
                CoursN1 = order[0][num]
                CoursN2 = order[0][num+1]
                stop = True
            num += 1
        return [CoursN1, CoursN2]

    def getColor(self, cl):
        colorsClass = {"Mathématiques": "#CE0000", "Français":"#FFD200", "Anglais":"#000BFF", "Allemand":"#464646",
                       "Histoire-Géo":"#794016", "Latin":"#6430A6", "Sport":"#FF00E9", "HG Anglais": "#905E38",
                       "Acc. Perso":"#FFA2A2", "SES":"#80CAFF", "SNT":"#6389BA", "EMC":"#644B39",
                       "Physique-Chimie":"#DD4E7F", "SVT":"#18CF00"}
        cFontClass = {"Mathématiques": "#000000", "Français": "#000000", "Anglais":"#000000", "Allemand":"#FFFFFF",
                       "Histoire-Géo":"#000000", "Latin":"#000000", "Sport":"#000000", "HG Anglais": "#000000",
                       "Acc. Perso":"#000000", "SES":"#000000", "SNT":"#000000", "EMC":"#000000",
                       "Physique-Chimie":"#000000", "SVT":"#000000"}
        return [colorsClass[cl.nom], cFontClass[cl.nom]]

    def getImage(self, cl):
        imgClass = {"Mathématiques": "Sprites/Maths.png", "Français": "Sprites/None_.png", "Anglais": "Sprites/Anglais.png",
                    "Allemand": "Sprites/Allemand.png", "Histoire-Géo": "Sprites/HG.png", "Latin": "Sprites/None_.png",
                    "Sport": "Sprites/Sport.png", "HG Anglais": "Sprites/None_.png", "Acc. Perso": "Sprites/None_.png",
                    "SES": "Sprites/None_.png", "SNT": "Sprites/SNT.png", "EMC": "Sprites/None_.png",
                    "Physique-Chimie": "Sprites/Physique-Chimie.png", "SVT": "Sprites/SVT.png"}
        return imgClass[cl.nom]

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class VappovagApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    VappovagApp().run()
