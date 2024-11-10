'''Készíts egy programot, amely a felhasználó által megadott mondatról
a mondatvégi jel alapján eldönti milyen fajtájú! (kijelentő, kérdő, felkiáltó / felszólító / óhatjtó)'''
print("írj be egy mondatot aminek a végére mondatvégi jelet teszel.")


mondat=input("Adjon meg egy mondatot.")
if len(mondat) > 0:
    utolso_karakter = mondat[-1]

if utolso_karakter == ".":
    print("Kijelentő mondat")
elif utolso_karakter == "?":
    print("Kérdő mondat")
elif utolso_karakter == "!":
    print("Felszólító, óhajtó vagy felkiáltó mondat")

else:
    print("A mondat nem tartalmaz írásjelet")

