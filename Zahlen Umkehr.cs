using System;
using System.Dynamic;
using System.Transactions;

public class Program
{
    public static void Main()
    {
        Console.WriteLine("Bitte geben Sie eine Zahl ein: ");
        int zahl = Convert.ToInt32(Console.ReadLine());
        int umkehr = 0; 

        while (zahl > 0)
        {
            int rest = zahl % 10;
            umkehr = (umkehr * 10) + rest;
            zahl = (zahl / 10);
        }

        Console.WriteLine(umkehr);

    }

}
