#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 07:28:44 2023

"""

print("*"*26)
print("*"," "*4,"Agob, Khoala"," "*4,"*")
print("* Temperatur umberechnen *")
print("*"*26,"\n")

abfrage = input("Was möchten Sie konvertieren? Energie (Joule) oder Temperatur? Bitte geben Sie ein: ")

if abfrage == "Temperatur" or abfrage == "T" or abfrage == "TEMPERATUR" or abfrage == "temperatur" or abfrage == "t":
    einheitt = input("Geben Sie die Einheit ein: ")

    if einheitt == "celsius" or einheitt == "c" or einheitt == "CELSIUS" or einheitt == "Celsius" or einheitt == "C":
        celsius = float(input("Geben Sie die Temparatur in Celsius ein: "))
        print(celsius,"°C ist",(celsius*9/5)+32,"°F")
        print(celsius,"°C ist",(celsius+273.15),"K")

    elif einheitt == "kelvin" or einheitt == "k" or einheitt == "K" or einheitt == "Kelvin" or einheitt == "KELVIN":   
        kelvin = float(input("Geben Sie die Temparatur in Kelvin ein: "))
        print(kelvin,"K ist",(kelvin-273.15),"°C")
        print(kelvin,"K ist",kelvin+273.15*9/5+32,"°F")

    elif einheitt == "fahrenheit" or einheitt == "F" or einheitt == "Fahrenheit" or einheitt == "f" or einheitt == "FAHRENHEIT": 
        fahrenheit = float(input("Geben Sie die Temparatur in Fahrenheit ein: "))
        print(fahrenheit,"°F ist",((fahrenheit-32)*5)/9,"°C")
        print(fahrenheit,"°F ist",(fahrenheit-32)*5/9+273.15,"K")
    
    else:
        print("Nicht erkannt")
        
elif abfrage == "Energie" or abfrage == "E" or abfrage == "energie" or abfrage == "e" or abfrage == "ENERGIE" or abfrage == "j" or abfrage == "J" or abfrage == "JOULE" or abfrage == "joule" or abfrage == "Joule":
    joule = float(input("Geben Sie die Energie in Joule ein: "))
    print("\n")
    print(joule,"J ist",joule/4.184,"cal")
    print(joule,"J ist",joule*6.242*10**18,"eV")
    print(joule,"J ist",joule/3600000,"kWh")  
    print(joule,"J ist",joule/1055,"Btu")

else:
    print("nicht erkannt")
