import time
import colorama
print("Kalkulačka se vzorcy")
print("BY: larisek")
print("Github: https://github.com/larisek")
input("Start")
print("1.Newtonovy gravitační zákony")
print("2.Práce")
print("3.Přibližná smrt")
print("0.Klasická kalkulačka")
choose = int(input("Vyber co chceš počítat: "))
if choose == 1:  
#Newtonovy gravitační zákony
    print("newtonovy gravitační zákony:  ")
    print("co chceš spočítat(Pokud počítáš gravitační zrychlení tak místo síly napiš 9.81)")
    print("1. zrychlení")
    print("2. hmotnost")
    print("3. sílu")
    dev = input("Zadej číslo:  ")
    if float(dev) == 1:
        F = input("Síla (N): ")
        m = input("Váha (KG): ")
        propočet = float(F) / float(m) 
        print("zrychlení je ", propočet, "m/s^2")
    elif float(dev) == 2:
        F = input("Síla(N):  ")
        a = input("Zrychlení(m/s^2):  ")
        propočet = float(F)/float(a) 
        print("Hmotnost tělesa je", propočet, "KG")
    elif float(dev) == 3:
        a = input("zrychlení (m/s^2): ")
        m = input("Váha (KG): ")
        F = float(a)*float(m)
        print("Síla je", F, "Newtonů" )
    else:
        print("Špatně zadaná syntaxe.")
#Práce
elif choose == 2:
    print("Práce/Výkon")
    print("1. Práce")
    print("2. Výkon")
    print("3. dráha")
    print("4. čas")
    print("5. váha")
    PVset = int(input("Co chceš vypočítat: "))
    if PVset == 1:
        print("Výpočet práce")
        mass = int(input("Váha v kg: "))
        trail = int(input("Dráha v m: "))
        solve = mass * 10 * trail
        print(f"Výsledek je {solve} J")
    elif PVset == 2:
        print("Výpočet výkonu")
        work = int(input("Vykonaná práce v KJ: "))
        time = int(input("Čas v s: "))
        solve = work / time
        print(f"Výsledek je {solve} W")
    elif PVset == 3:
        print("Výpočet dráhy")
        work = int(input("Práce v KJ: "))
        mass = int(input("Váha v kg: "))
        solve = mass * 10 / work
        print(f"Výsledek je {solve} m")
    elif PVset == 4:
        print("Výpočet času")
        power = int(input("Výkon ve W: "))
        work = int(input("Práce v KJ: "))
        solve = work * power
        print(f"Výsledek je {solve} s")
    elif PVset == 5:
        trail = int(input("Dráha v m: "))
        work = int(input("Práce v KJ: "))
        solve = trail * 10 / work
        print(solve)
    else:
        print("Špatně zadaná syntaxe.")
#Klasická kalkulačka
elif choose == 0:
    print("Kalkulačka")
    num1 = float(input("Vyber první číslo:  "))
    num2 = float(input("Vyber druhé číslo:  "))
    print("1. Násobení")
    print("2. Dělení")
    print("3. Sčítání")
    print("4. Odčítání")
    oper = int(input("Vyber početní operaci:  "))
    if oper == 1:
        x = num1 * num2
        print(f"výsledek je : {x}")
    elif oper == 2:
        x = num1 / num2
        print(f"výsledek je : {x}")
    elif oper == 3:
        x = num1 + num2
        print(f"výsledek je : {x}")
    elif oper == 4:
        x = num1 - num2
        print(f"výsledek je : {x}")
    while True:
        print("Chcete pokračovat?")
        print("1.Ano")
        print("2.Ne")
        chs = int(input())
        if chs == 2:
            break
        elif chs == 1:
            print(f"První číslo je {x}")
            num2 = int(input("druhé číslo:  "))
            print("1. Násobení")
            print("2. Dělení")
            print("3. Sčítání")
            print("4. Odčítání")
            oper = int(input(""))
            if oper == 1:
                x = x * num2
                print(f"První číslo je {x}")
                print(f"výsledek je : {x}")
            elif oper == 2:
                x = x / num2
                print(f"První číslo je {x}")
                print(f"výsledek je : {x}")
            elif oper == 3:
                x = x + num2
                print(f"První číslo je {x}")
                print(f"výsledek je : {x}")
            elif oper == 4:
                x = x - num2
                print(f"První číslo je {x}")
                print(f"výsledek je : {x}")
            else:
                print("Špatně zadaná syntaxe.")
        else:
            print("Špatně zadaná syntaxe.")
#Kalkulačka života
elif choose == 3:
    print("Klakulačka života")
    print("Piš pouze čísla")
    print("Zadej své datum narození:")
    day = int(input("Den: "))
    month = int(input("Měsíc: "))
    year = int(input("Rok: "))
    deathdate = year + 90
    print("Zadej dnešní datum:")
    tday = int(input("Den: "))
    tmonth = int(input("Měsíc: "))
    tyear = int(input("Rok: "))
    propočet1 = tday - day
    propočet2 = tmonth - month
    propočet3 = tyear - year
    x = 0
    y = 0
    if propočet1 <= 0:
        x + 1
        propočet2 - x
        propočet1 *= -1
    if propočet2 <= 0:
        y + 1
        propočet3 - y
        propočet2 *= -1
    propočet4 = 90 - propočet3 
    
    print(f"Do konce života ti zbývá asi {propočet4} let, {propočet2} měsíců a {propočet1} dní")
    print(f"Tvé datum smrti bude nejspíš {day}.{month}.{deathdate}")
    print("Chceš přesnější dobu tvé smrti?")
    print("1.ano")
    print("2.ne")
    sol = int(input("Vaše odpověď: "))
    if sol == 1:
        prop = propočet4 * 365 + propočet2 * 29 + propočet1
        prop2 = prop * 24 * 3600
        n = prop2
        while True:
            n = n - 1
            print(f"Do konce tvého života zbývá {n} sekundy")
            time.sleep(1)
            if n == 0:
                break
else:
    print("Špatně zadaná syntaxe")
print("Konec programu")
