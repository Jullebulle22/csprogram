static double BeräknaMedelvärde(int[] fält)
{
    if (fält.Length == 0)
    {
        return 0;
    }
    
    int summa = 0;
    foreach (int värde in fält)
    {
        summa += värde;
    }
    
    return (double)summa / fält.Length;
}

static void VisaResultat(int[] fält, string namn)
{
    Console.Write($"{namn}: [");
    for (int i = 0; i < fält.Length; i++)
    {
        Console.Write(fält[i]);
        if (i < fält.Length - 1)
        {
            Console.Write(", ");
        }
    }
    Console.WriteLine("]");
    
    double medelvärde = BeräknaMedelvärde(fält);
    Console.WriteLine($"Medelvärde: {medelvärde:F2}\n");
}

Console.WriteLine("=== Beräkning av medelvärden ===\n");

int[] fält1 = { 5, 10, 15, 20, 25 };
VisaResultat(fält1, "Fält 1");

int[] fält2 = { -10, 5, -3, 8, 12, -7 };
VisaResultat(fält2, "Fält 2");

int[] fält3 = { 100, 200, 300, 400, 500, 600, 700 };
VisaResultat(fält3, "Fält 3");
