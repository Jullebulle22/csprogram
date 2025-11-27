# C# Grunder – Översikt

Detta projekt är uppdelat i mappar för varje grundläggande område i C#. Gå in i respektive mapp för att hitta exempel och instruktioner.

## Områden

1. **01-variabler-datatyper** – Variabler och datatyper
2. **02-kontrollstrukturer** – If, switch, loopar
3. **03-metoder-funktioner** – Metoder och funktioner
4. **04-klasser-objekt** – Klasser och objekt
5. **05-arv-granssnitt** – Arv och gränssnitt
6. **06-undantagshantering** – Undantagshantering
7. **07-filhantering** – Filhantering

## Kompilera och köra kod

Gå in i önskad mapp och följ instruktionerna i respektive README.md. Alla exempel körs med .NET CLI:

```sh
dotnet run
```

> Skapa projektet första gången med:
> ```sh
> dotnet new console -o .
> ```

Lycka till med C#!

## Projektstruktur

```text
cBasics/
│
├── 01-variabler-datatyper/
│   ├── 01-variabler-datatyper.csproj
│   ├── Program.cs
│   └── README.md
│
├── 02-kontrollstrukturer/
│   ├── 02-kontrollstrukturer.csproj
│   ├── Program.cs
│   └── README.md
│
├── 03-metoder-funktioner/
│   └── README.md
│
├── 04-klasser-objekt/
│   └── README.md
│
├── 05-arv-granssnitt/
│   └── README.md
│
├── 06-undantagshantering/
│   └── README.md
│
├── 07-filhantering/
│   └── README.md
│
├── .github/
│   └── copilot-instructions.md
│
├── cBasics.sln
└── README.md
```