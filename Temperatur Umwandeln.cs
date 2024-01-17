using System;
using System.Transactions;

public class Program
{
    public static void Main()
    {

        Console.WriteLine("Möchten Sie Celsius nach Fahrenheit umwandeln? Bitte geben Sie 'CtoF' ein. Möchten Sie Fahrenheit nach Celsius umwandeln? Bitte geben Sie 'FtoC' ein: ");
        string antwort = Console.ReadLine();

        if (antwort == "CtoF")
        {
            Console.WriteLine("Bitte geben Sie die Temperatur in Celsius ein: ");
            float celsius = Convert.ToInt32(Console.ReadLine());

            float fahrenheit = celsius * 9 / 5 + 32;
            Console.WriteLine(celsius + "°C ist " + fahrenheit + "°F");
        }
        else if (antwort == "FtoC")
            {
            Console.WriteLine("Bitte geben Sie die Temperatur in Fahrenheit ein: ");
            float fahrenheit = Convert.ToInt32(Console.ReadLine());

            float celsius = (fahrenheit-32) * 5/9;
            Console.WriteLine(fahrenheit + "°F ist " + celsius + "°C");
        }
        else
        {
            Console.WriteLine("Eingabe nicht erkannt. Bitte versuchen Sie noch einmal.");
        }
    }
}
