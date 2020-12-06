import datetime

class Cours:
    def __init__(self, nom, prof, salle, jour, heure, semaine):
        self.nom = nom
        self.prof = prof
        self.salle = salle
        self.jour = jour
        self.heure = heure
        self.semaine = semaine

#les cours
c1 = Cours("Histoire-Géo", "LUNDI", "210", 1, 9, "A")
c2 = Cours("Mathématiques", "LUNDI", "301", 1, 10, "AB")
c3 = Cours("Histoire-Géo", "Mme APPERE", "210", 1, 12, "B")
c4 = Cours("Allemand", "Mme JAGHOUAR", "016", 1, 12, "A")
c5 = Cours("Anglais", "M. HOLMES", "101", 1, 14, "AB")
c6 = Cours("Latin", "Mme WEILL ENGERER", "322", 1, 15, "AB")
c7 = Cours("Sport", "Mme LECARME", "015-Gymnase", 1, 16, "AB")
c8 = Cours("Sport", "Mme LECARME", "015-Gymnase", 1, 17, "AB")
#--------------------------------------------------------------
c9 = Cours("Anglais", "M. HOLMES", "101", 2, 8, "AB")
c10 = Cours("Français", "Mme POUSSARD", "323", 2, 9, "B")
c11 = Cours("Français", "Mme POUSSARD", "322", 2, 10, "A")
c12 = Cours("SES", "Mme LECLERCQ", "318", 2, 10, "B")
c13 = Cours("Mathématiques", "M. DODARD", "309", 2, 11, "AB")
c14 = Cours("Histoire-Géo", "Mme APPERE", "204", 2, 12, "AB")
c15 = Cours("Latin", "Mme WEILL ENGERER", "310", 2, 14, "AB")
c16 = Cours("Physique-Chimie", "BOUBEKEUR", "423", 2, 15, "AB")
c17 = Cours("SNT", "Mme LECLERQ", "101", 2, 16, "A")
c18 = Cours("SNT", "BOUBEKEUR", "423", 2, 17, "A")
c19 = Cours("Acc. Perso", "Mme POUSSARD", "323", 2, 16, "B")
c20 = Cours("Physique-Chimie", "BOUBEKEUR", "423", 2, 17, "B")
#--------------------------------------------------------------
c21 = Cours("Acc. Perso", "M. HOLMES", "103", 3, 8, "AB")
c22 = Cours("Anglais", "M. HOLMES", "103", 3, 9, "AB")
c23 = Cours("Allemand", "Mme JAGHOUAR", "017", 3, 10, "AB")
c24 = Cours("Français", "Mme POUSSARD", "323", 3, 11, "AB")
c25 = Cours("Français", "Mme POUSSARD", "323", 3, 12, "AB")
#--------------------------------------------------------------
c26 = Cours("SVT", "Mme DORE", "403", 4, 8, "AB")
c27 = Cours("Physique-Chimie", "BOUBEKEUR", "422", 4, 9, "AB")
c28 = Cours("Allemand", "Mme JAGHOUAR", "017", 4, 11, "AB")
c29 = Cours("Mathématiques", "M. DODARD", "302", 4, 12, "AB")
c30 = Cours("Français", "Mme POUSSARD", "323", 4, 14, "AB")
c31 = Cours("Latin", "Mme WEILL ENGERER", "317", 4, 16, "AB")
#--------------------------------------------------------------
c32 = Cours("HG Anglais", "Mme APPERE", "201", 5, 8, "AB")
c33 = Cours("Histoire-Géo", "Mme APPERE", "201", 5, 9, "AB")
c34 = Cours("Mathématiques", "M. DODARD", "301", 5, 10, "AB")
c35 = Cours("SNT", "M. DODARD", "301", 5, 11, "AB")
c36 = Cours("SES", "Mme LECLERCQ", "204", 5, 14, "A")
c37 = Cours("SES", "Mme LECLERCQ", "204", 5, 15, "A")
c38 = Cours("EMC", "Mme LECLERCQ", "204", 5, 13, "B")
#--------------------------------------------------------------

samedi = Cours("Samedi", "None", 12, 6, 8, "AB")
dimanche = Cours("Dimanche", "None", 12, 7, 8, "AB")
listeCours = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20,
              c21, c22, c23, c24, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c1, c2]
SemaineA = [c1, c2, c4, c5, c6, c7, c9, c11, c13, c14, c15, c16, c17, c18, c21, c22, c23, c24, c25, c26, c27, c28,
            c29, c30, c31, c32, c33, c34, c35, c36, c37]
SemaineB = [c2, c3, c5, c6, c7, c9, c10, c12, c13, c14, c15, c16, c19, c20, c21, c22, c23, c24, c25, c26, c27, c28,
            c29, c30, c31, c32, c33, c34, c35, c38]

class Day:
    def __init__(self, nombre, cours):
        self.nombre = nombre
        self.cours = cours
        self.firstHour = cours[0].heure
        self.lastHour = cours[len(cours)-1].heure + 1

Lundi = Day(1, [c1, c2, c3, c4, c5, c6, c7, c8])
Mardi = Day(2, [c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20])
Mercredi = Day(3, [c21, c22, c23, c24, c25])
Jeudi = Day(4, [c26, c27, c28, c29, c30, c31])
Vendredi = Day(5, [c32, c33, c34, c35, c36, c37, c38])
listeJours = [Lundi, Mardi, Mercredi, Jeudi, Vendredi, Lundi]

# la date
d = datetime.date.today()
#d = datetime.date(2020, 12, 2)
now = datetime.datetime.now()
year = d.isocalendar()[0]
week_of_year = d.isocalendar()[1]
day_of_week = d.isocalendar()[2]
hour = int(now.strftime("%H"))
#hour = 8
minute = int(now.strftime("%M"))
#minute = 0
#print(f"{hour}h{minute} - Jour: {day_of_week}, Semaine: {week_of_year}, Année: {year}")


"""def findClass():
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
    while not found:
        C = listeCours[num]
        if day_of_week >= 6:
            found = True
            return c1
        else:
            if C.jour == day_of_week:
                if C.heure == h:
                    if C.semaine == "AB" or C.semaine == semaine:
                        found = True
                        return C
            elif C.jour > day_of_week:
                if C.semaine == "AB" or C.semaine == semaine:
                    found = True
                    return C
            num += 1"""
#print(f"Prochain cours: \n{findClass().nom} en salle {findClass().salle} avec {findClass().prof}.")