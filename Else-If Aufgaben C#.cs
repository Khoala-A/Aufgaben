using System;
using System.Transactions;

public class Program
{
    public static void Main()
    {

        Console.WriteLine("Aufgabe 1");

        Console.WriteLine("Bitte geben Sie die Temperatur in Celsius ein: ");
        float temperatur = Convert.ToInt32(Console.ReadLine());

        if (temperatur < 0 )
        {
            Console.WriteLine("Es friert");
        } 
        else if (temperatur > 0 && temperatur < 16)
        {
            Console.WriteLine("Es ist kalt");
        }
        else if (temperatur > 15 && temperatur < 26)
        {
            Console.WriteLine("Es ist mild");
        }
        else
        {
            Console.WriteLine("Es ist heiß");
        }
    }
}

//Aufgabe 2

using System;
using System.Transactions;

public class Program
{
    public static void Main()
    {

        Console.WriteLine("Aufgabe 4");

        Console.WriteLine("Bitte geben Sie Ihre Alter ein: ");
        float alter = Convert.ToInt32(Console.ReadLine());

        if (alter < 12)
        {
            Console.WriteLine("PG");
        }
        else if (alter > 11 && alter < 17)
        {
            Console.WriteLine("PG-13");
        }
        else if (alter > 16)
        {
            Console.WriteLine("R");
        }

    }

}
