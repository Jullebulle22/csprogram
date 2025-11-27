internal class Program
{
    private static void Main(string[] args)
    {
        string password = "hemligt";
        
        int antalFörsök = 0;
        
        string gissning;
        
        do
        {
            Console.Write("Gissa lösenordet: ");
            gissning = Console.ReadLine() ?? "";
            
            antalFörsök++;
            
            if (gissning != password)
            {
                Console.WriteLine("Fel lösenord! Försök igen.");
            }
        } while (gissning != password);
        
        Console.WriteLine($"Grattis! Du gissade rätt efter {antalFörsök} försök.");
    }
}