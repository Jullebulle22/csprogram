// See https://aka.ms/new-console-template for more information

// List<string> namnLista = new List<string>
// {
// 	"Anna",
// 	"Erik",
// 	"Sara",
// 	"Johan",
// 	"Maria",
// 	"Oskar",
// 	"Elin",
// 	"Lars",
// 	"Emma",
// 	"David"
// };

// Console.WriteLine("Hello, what's your name?");
// string namn = Console.ReadLine();
// Console.WriteLine($"Välkommen, {namn}!");

// namnLista.Add(namn);

// Console.WriteLine(namnLista.Count);

// for (int i = 0; i < namnLista.Count; i++)
// {
//     Console.WriteLine($"Namn {i}: {namnLista[i]}");
// }





int mittkonto = 100000;
Console.WriteLine($"Ditt saldo är: {mittkonto} kr");

mittkonto -= 15000;
Console.WriteLine($"Ditt saldo är: {mittkonto} kr");

mittkonto -= 700;
Console.WriteLine($"Ditt saldo är: {mittkonto} kr");

mittkonto += 5590;
Console.WriteLine($"Ditt saldo är: {mittkonto} kr");


double nyttkonto = mittkonto;
for (int i = 0; i < 10; i++)
{
    Console.WriteLine($"År {i + 1}");
    Console.WriteLine($"Ditt saldo är: {nyttkonto} kr");
    nyttkonto *= 1.10;
}

