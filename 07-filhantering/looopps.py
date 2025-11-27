"""Python-exempel: for-loopar med index och enumerate

Det här är en ren Python-fil (inga code-fences). Filen visar:
- utskrift av första element
- iteration över lista
- iteration med index via range(len(...))
- iteration med index+värde via enumerate
"""

namn_produkt = ["tv", "hörlurar", "radionna"]

# Skriv ut första elementet
print(namn_produkt[0])

# Enkel for-loop som skriver ut varje namn
for namn in namn_produkt:
    print(namn)

# Korrekt Python-for-loop med index som ersätter C-stil-syntaxen
# Använd range för att iterera över index, eller enumerate för index+värde
print("\nExempel: index med range(len(...)):")
for i in range(len(namn_produkt)):
    print(f"index={i}, namn={namn_produkt[i]}, i*2={i*2}")

print("\nExempel: index med enumerate:")
for idx, namn in enumerate(namn_produkt):
    print(f"index={idx}, namn={namn}")

# Kommentar: exempel på while-loop (avkommentera under test om du vill köra)
# x = 0
# while True:
#     x += 1
#     print(f"hej {x}")
#     if x == 10:
#         break