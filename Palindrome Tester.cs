using System;
using System.Transactions;

public class Program
{
    public static void Main()
    {

        Console.WriteLine("Bitte geben Sie eine Wort ein: ");
        string input = Console.ReadLine();
        string umkehr = string.Empty;

        for (int i = input.Length - 1; i >= 0; i--)
        {
            umkehr += input[i];
        }

        if (input == umkehr)
        {
            Console.WriteLine(input + " ist eine Palindrome");
        }
        else
        {
            Console.WriteLine(input + " ist keine Palindrome");
        }

    }

}
