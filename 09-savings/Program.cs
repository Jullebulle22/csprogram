Console.Write("Ange saldo: ");
double saldo = double.Parse(Console.ReadLine() ?? "0");

Console.Write("Ange slutmål: ");
double slutmål = double.Parse(Console.ReadLine() ?? "0");

Console.Write("Ange sparränta (i procent): ");
double sparränta = double.Parse(Console.ReadLine() ?? "0");

double räntaDecimal = sparränta / 100.0;
int ar = 0;

while (saldo < slutmål)
{
    saldo = saldo * (1 + räntaDecimal);
    ar++;
}

Console.WriteLine($"\nDet tar {ar} år att nå ditt mål på {slutmål:N2} kr.");
Console.WriteLine($"Ditt saldo kommer då vara {saldo:N2} kr.");
