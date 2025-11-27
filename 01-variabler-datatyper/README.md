
# Variabler och Datatyper

>I denna mapp hittar du exempel på de vanligaste datatyperna och hur du deklarerar variabler i C#.

## Exempel på datatyper

| Datatyp   | Exempelvärde      | Beskrivning                        |
|-----------|-------------------|------------------------------------|
| int       | 42                | Heltal                             |
| long      | 1234567890L       | Stort heltal                       |
| short     | -32000            | Litet heltal                       |
| byte      | 255               | Litet positivt heltal              |
| float     | 3.14f             | Flyttal (enkel precision)          |
| double    | 2.718281828       | Flyttal (dubbel precision)         |
| decimal   | 19.99m            | Exakt tal, t.ex. pengar            |
| char      | 'A'               | Enskilt tecken                     |
| string    | "Hej, världen!"   | Textsträng                         |
| bool      | true/false        | Booleskt värde (sant/falskt)       |

### Exempel på deklaration och utskrift

```csharp
int heltal = 42;
double dubbel = 2.718;
string text = "Hej!";
bool flagga = true;
Console.WriteLine(heltal);
Console.WriteLine(dubbel);
Console.WriteLine(text);
Console.WriteLine(flagga);
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
