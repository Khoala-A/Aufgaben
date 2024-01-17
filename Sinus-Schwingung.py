print("*"*25)
print("*"," ","Sinus-Schwingung","  ", "*")
print("*", " "*4, "Khoala Agob",  " "*4, "*"
print("*"*25)

abfrage = int(input("Was möchten Sie berechnen? 1. Frequenz oder 2. Wellenlänge?"))
c = 299792458
#Lichtsgeschwindigkeit

if abfrage == 1:
    wellenlaenge = float(input("Wellenlänge eingeben (Zwischen 0-999): "))
    if wellenlaenge < 999:
        abfrage2 = (input("Geben Sie die Einheit ein (km, m, cm, mm, µm): "))
        if abfrage2 == "km" or abfrage2 == "k":
            wellenlaenge = wellenlaenge * 10**3
        elif abfrage2 == "cm" or abfrage2 == "c":
            wellenlaenge = wellenlaenge * 10**-2
        elif abfrage2 == "mm" or abfrage2 == "m":
            wellenlaenge = wellenlaenge * 10**-3
        elif abfrage2 == "µm" or abfrage2 == "mikro":
            wellenlaenge = wellenlaenge * 10**-6
        print('\n')
        frequenz = c  / wellenlaenge
    
        praefix= ['Hz','kHz','MHz','GHz','THz']
    
        print(frequenz,"Hz")
    
        for i in praefix:
            if frequenz < 1000:
                break
            frequenz /= 1000
        
        ergebnis = str(frequenz) + " " + i
        print(ergebnis)
    else: 
        print("Error")
    
elif abfrage == 2:
    frequenz = float(input("Frequenz eingeben (Zwischen 0-999): ")) 
    if frequenz < 999:
        abfrage2 = (input("Geben Sie die Einheit ein (kHz, Hz, MHz, GHz, THz): "))
        if abfrage2 == "kHz" or abfrage2 == "khz" or abfrage2 == "k":  
            frequenz = frequenz * (10**3)
        elif abfrage2 == "MHz" or abfrage2 == "mhz" or abfrage2 == "m": 
            frequenz = frequenz * (10**6)
        elif abfrage2 == "GHz" or abfrage2 == "ghz" or abfrage2 == "g": 
            frequenz = frequenz * (10**9)
        if abfrage2 == "THz" or abfrage2 == "thz" or abfrage2 == "t": 
            frequenz = frequenz * (10**12)
    
        print('\n')
    
        wellenlänge = c  / frequenz
        print(wellenlänge,"m")
        praefix= ['km','m','cm','mm','µm','nm']
        praefix_wert= [10**3, 1, 10**-2, 10**-3, 10**-6, 10**-9]
    
        for i, j in zip(praefix,praefix_wert):
            if wellenlänge >= j: 
                wellenlänge /= j 
                präfix = i
                break
    
        ergebnis = str(wellenlänge) + " " + präfix
        print(ergebnis)
    else: 
        print("Error")    
