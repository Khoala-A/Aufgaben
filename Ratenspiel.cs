using System;
using System.Transactions;

public class Program
{
    public static void Main()
    {

        Random n = new Random();
        int computer = n.Next(1,100);

        //Console.WriteLine(computer);

        int raten = 0;

        Console.WriteLine("Geben Sie die Nummer ein, an die ich denke: ");

        while (raten != computer)
        {
            raten = Convert.ToInt32(Console.ReadLine());

            if (raten < computer)
            {
                Console.WriteLine("Leider Falsch, "+ raten + " ist zu niedrig");
            }
            else if (raten > computer)
            {
                Console.WriteLine("Leider Falsch, " + raten + " ist zu hoch");
            }

        }

        Console.WriteLine("Richtig! Meine Zahl war " + computer);
        Console.ReadLine();

    }

}
