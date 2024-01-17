
using System;
using System.Transactions;

public class Program
{
    public static void Main()
    {

        Console.WriteLine("Wie weit soll die Fibonacci-Folge berechnet sein: ");
        int n = Convert.ToInt32(Console.ReadLine());
        int n1 = 0;
        int n2 = 1;
        int ergebnis = 0;

        Console.WriteLine("0");

        for (int i = 0; i < n-1; i++)
        {
            n1 = n2;
            n2 = ergebnis;
            ergebnis = n1 + n2;
            Console.WriteLine(ergebnis);
        }
    }
}
