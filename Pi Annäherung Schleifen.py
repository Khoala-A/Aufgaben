import math

iteration = int(input("Bitte geben Sie die Anzahl von Iterationen ein: "))
s = 1
n = 12

for i in range(iteration):
    s = (math.sqrt(2-(math.sqrt((4-(s)**2)))))
    p = round(((1/2*n)*s),11)
    n = n * 2
    print (p)

#relative Fehler berechnen
xa = math.pi 
xr = p 
f = xa - xr 
fr = f/(xa)


