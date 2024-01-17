import math

print("*"*25)
print("*"," "*4, "Taylorreihe"," "*4, "*")
print("*", " "*4, "Khoala Agob",  " "*4, "*")
print("*"," "*6, "App16a2", " "*6,"*")
print("*"*25)

def reihe(x, n):
    ergebnis = 0 
    for i in range(0, n+1):
        ergebnis += (x**i)/math.factorial(i)
    return ergebnis
    
def absF(xa1, xr1):
    absolutFehler = xa1 - xr1
    return absolutFehler

def relF(xa2, xr2):
    relativFehler = ((xa2-xr2) / xa2)
    return relativFehler
    
lf = int(input("Geben Sie n ein: "))
exp = int(input("Geben Sie x ein: "))

#e^x = 1 + x + x2/2! + x3/3! + x4/4! + x5/5! + ...

xr = reihe(exp, lf)
xa = math.exp(exp)

F = absF(xa, xr)
Fr = relF(xa, xr)


print("\n")

table = [
    ["n","xa","xr","F","Fr"],
    ["========================================"],
    ]
for row in table: 
    print("\t".join(map(str, row)))

for lf in range(lf+1):
    xr = reihe(exp,lf)  
    xa = math.exp(exp)
    F = absF(xa, xr)
    Fr = relF(xa, xr)
    print(lf, end="\t")
    print(round(xa,3), end="\t")
    print(round(xr, 3), end="\t")
    print(round(F, 3), end="\t") 
    print(round(Fr, 3))

