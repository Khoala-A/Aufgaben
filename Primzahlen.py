import math
import time

print("*"*25)
print("*"," Listen & Primzahlen ", "*")
print("*", " "*4, "Khoala Agob",  " "*4, "*")
print("*"*25)

def main(): 
    n = int(input("Maximalwert eingeben: "))
    print("\n")
    lösung = sieb(n)
    zahlen = 8
    for i in range(0, len(lösung), zahlen):
        print(*lösung[i:i + zahlen], sep="\t", end="\n")
    print("Es gibt",len(lösung),"Primazahlen, welche keiner als",n,"sind.")
    
def sieb(n):
    #Definiton der Liste
    zahlen = list(range(1, n+1))
    primzahlen = []
    #Grenze definieren
    for n in range(1, n+1):
        if n > 1:
           for i in range(2, round(math.sqrt(n))+1):
               if (n % i) == 0:
                    break
           else:
               primzahlen.append(n)
    return primzahlen
  
main()
