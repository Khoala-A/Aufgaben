import math

print("*"*25)
print("* Quadratisch Gleichung *")
print("*", " "*4, "Khoala Agob",  " "*4, "*")
print("*"*25)

def kleine_loesung():
    if diskriminate > 0:
        print("x²+ {}x + {} = 0".format(p, q))
        print("x₁ = {:.3f}".format(gleichung+math.sqrt(diskriminate)))
        print("x₂ = {:.3f}".format(gleichung-math.sqrt(diskriminate)))

    elif diskriminate == 0: 
        print("x²+ {}x + {} = 0".format(p, q))
        print("x₁ = {:.3f}".format(gleichung+math.sqrt(diskriminate)))
        print("x₂ = {:.3f}".format(gleichung-math.sqrt(diskriminate)))

    elif diskriminate < 0:
        print("x²+ {}x + {} = 0".format(p, q))
        print("x₁ = ", gleichung,"+ i {:.3f}".format(math.sqrt(-1*diskriminate)))
        print("x₂ = ", gleichung,"- i {:.3f}".format(math.sqrt(-1*diskriminate)))
    
def große_loesung():
    if diskriminate1 > 0: 
        print("{}x² + {}x + {} = 0".format(a, b, c))
        print("x₁ = {:.3f}".format((gleichung1+math.sqrt(diskriminate1))/gleichung2))
        print("x₂ = {:.3f}".format((gleichung1-math.sqrt(diskriminate1))/gleichung2))

    elif diskriminate1 == 0: 
        print("{}x² + {}x + {} = 0".format(a, b, c))
        print("x₁ = {:.3f}".format((gleichung1+math.sqrt(diskriminate1))/gleichung2))
        print("x₂ = {:.3f}".format((gleichung1-math.sqrt(diskriminate1))/gleichung2))

    elif diskriminate1 < 0:
        print("{}x² + {}x + {} = 0".format(a, b, c))
        print("x₁ = {:.3f}".format((gleichung1/gleichung2)),"+ i {:.3f}".format(math.sqrt(-1*diskriminate1)/gleichung2))
        print("x₂ = {:.3f}".format((gleichung1/gleichung2)),"- i {:.3f}".format(math.sqrt(-1*diskriminate1)/gleichung2))


formel = int(input("Mit welchen Gleichung möchten Sie berechnen? 1. Kleine Gleichung oder 2. Große Gleichung: "))

if formel == 1: 
    print("x²+px+q=0")
    p = float(input("Bitte Geben Sie p ein: "))
    q = float(input("Bitte Geben Sie q ein: "))
    print("\n")

    gleichung = -p/2 
    diskriminate = (p*p)/4-q 

    kleine_loesung()

elif formel == 2: 
    print("Ax² + Bx + C = 0")
    a = float(input("Bitte Geben Sie a ein: "))
    b = float(input("Bitte Geben Sie b ein: "))
    c = float(input("Bitte Geben Sie c ein: "))
    print("\n")
    
    diskriminate1 = (b*b)-4*a*c
    gleichung1 = -b
    gleichung2 = 2*a
    
    große_loesung()

print("\n")
weitermachen = input("Weitere Berechnungen? Ja oder Nein: ")
print("\n")

while weitermachen == "Ja" or weitermachen == "J" or weitermachen == "ja" or weitermachen == "j" or weitermachen == "JA": 
   formel1 = int(input("Mit welchen Gleichung möchten Sie berechnen? 1. Kleine Gleichung oder 2. Große Gleichung: "))
   
   if formel1 == 1:
        print("x²+px+q=0")
        p = float(input("Bitte Geben Sie p ein: "))
        q = float(input("Bitte Geben Sie q ein: "))
        print("\n")
        
        gleichung = -p/2 
        diskriminate = (p*p)/4-q 
        
        kleine_loesung()
        print("\n")
        weitermachen = input("Weitere Berechnungen? Ja oder Nein: ")
    
    
   elif formel1 == 2:
       print("Ax² + Bx + C = 0")
       a = float(input("Bitte Geben Sie a ein: "))
       b = float(input("Bitte Geben Sie b ein: "))
       c = float(input("Bitte Geben Sie c ein: "))
       print("\n")
       
       diskriminate1 = (b*b)-4*a*c
       gleichung1 = -b
       gleichung2 = 2*a
       
       große_loesung()
       print("\n")
       weitermachen = input("Weitere Berechnungen? Ja oder Nein: ")

