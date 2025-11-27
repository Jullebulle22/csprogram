# C# Course Agent (cBasics)

Purpose: act as the helper for this C# fundamentals repo made of small console apps per topic. Keep everything beginner-friendly and stick to the style already in each folder.

Repo map
- `01-variabler-datatyper`: Program.cs shows basic types and prints them.
- `02-kontrollstrukturer`: Program.cs demos control structures with a simple balance example; README has if/switch/loop snippets.
- `03-metoder-funktioner`: README placeholder for methods/functions.
- `04-klasser-objekt`: README placeholder for classes/objects.
- `05-arv-granssnitt`: README placeholder for inheritance/interfaces.
- `06-undantagshantering`: README placeholder for try/catch.
- `07-filhantering`: README placeholder plus a couple of Python examples.
- `08-loop`: console app with a do/while password guesser.
- `cBasics.sln` ties projects together; ignore `bin/` and `obj/` outputs.

Working style
- Default language English unless the user writes Swedish; keep existing Swedish prompts intact.
- Use plain C# console apps targeting .NET 8; avoid extra packages.
- Prefer clear, explicit code over clever tricks; small helper methods are fine.
- Do not touch generated artifacts in `bin/` or `obj/`.

Commands to run
- From a topic folder: `dotnet run`
- First-time scaffolding inside a new topic folder: `dotnet new console -o .`

Task flow
1) Clarify the user’s goal and the target topic folder (or create a new numbered folder if needed).
2) Share a short plan for non-trivial changes; keep it brief.
3) Implement in the relevant `Program.cs` or new files; keep comments minimal and useful.
4) Suggest `dotnet run` for quick verification.
