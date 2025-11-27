int[] tal = new int[5];

for (int i = 0; i < 5; i++)
{
    Console.Write($"Ange heltal {i + 1}: ");
    string? input = Console.ReadLine();
    
    if (int.TryParse(input, out int värde))
    {
        tal[i] = värde;
    }
    else
    {
        Console.WriteLine("Ogiltigt heltal. Ange ett heltal.");
        i--;
    }
}

Console.WriteLine("\nTalen i omvänd ordning:");
for (int i = tal.Length - 1; i >= 0; i--)
{
    Console.WriteLine(tal[i]);
}
