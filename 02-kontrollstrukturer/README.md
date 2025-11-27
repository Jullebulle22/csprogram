# Kontrollstrukturer

Här hittar du exempel på if-satser, switch, loopar m.m. i C#.

## Exempel på kontrollstrukturer

### If-sats
```csharp
int tal = 10;
if (tal > 5)
{
   Console.WriteLine("Talet är större än 5");
}
else
{
   Console.WriteLine("Talet är 5 eller mindre");
}
```

### Switch-sats
```csharp
string färg = "röd";
switch (färg)
{
   case "röd":
      Console.WriteLine("Färgen är röd");
      break;
   case "blå":
      Console.WriteLine("Färgen är blå");
      break;
   default:
      Console.WriteLine("Okänd färg");
      break;
}
```

### For-loop
```csharp
for (int i = 0; i < 5; i++)
{
   Console.WriteLine($"Varv: {i}");
}
```

### While-loop
```csharp
int count = 0;
while (count < 3)
{
   Console.WriteLine($"Count: {count}");
   count++;
}
```

### Foreach-loop
```csharp
string[] namn = { "Anna", "Erik", "Sara" };
foreach (string n in namn)
{
   Console.WriteLine(n);
}
```

## Kompilera och kör

1. Navigera till denna mapp i terminalen.
2. Kör:
   ```
   dotnet new console -o .
   ```
   (Kör endast första gången för att skapa projektet.)
3. Lägg till/ändra kod i `Program.cs`.
4. Kompilera och kör med:
   ```
   dotnet run
   ```
