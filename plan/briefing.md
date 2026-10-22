# Briefing: KI-Werkstatt – Skript schreiben

## Die Sendung
"KI-Werkstatt" (im Feed: Klöbels KI Podcast) ist ein persönlicher, deutschsprachiger Lern-Podcast für einen Hörer: Andre, technisch versierter Berater im E-Commerce/Digital-Marketing (Feed-Management, Tracking, Analysen, Kundenkommunikation). Er nutzt KI schon viel (Claude, Automatisierungen über Zapier, geplante Aufgaben), will aber systematisch besser werden. Er hört beim Spazierengehen, also: kein Bildschirm, nur Ohr.

Zwei Sprecher im Dialog:
- MIRA: führt durch die Folge, stellt die Fragen, die ein Hörer stellen würde, fasst zusammen, bringt Praxisbeispiele aus dem Arbeitsalltag.
- JAN: erklärt, hat das Fachwissen, aber spricht locker und ohne Fachchinesisch.
Beide duzen sich und den Hörer. Sie reden wie zwei Kollegen in der Kaffeeküche, nicht wie ein Lehrbuch.

## Format (zwingend)
- Datei beginnt mit `# KI-Werkstatt – Folge N: <Titel>`, danach Leerzeile.
- Danach NUR Dialogzeilen, jede beginnt mit `MIRA: ` oder `JAN: `, zwischen den Zeilen eine Leerzeile. Keine Regieanweisungen, keine Zwischenüberschriften, kein Markdown, keine Aufzählungszeichen, keine Klammern mit Hinweisen.
- Länge: 3.400 bis 3.700 Wörter (prüfe mit `wc -w`). Das ergibt ca. 18 Minuten Audio.
- Einzelne Redebeiträge höchstens ca. 120 Wörter, meist kürzer. Echtes Hin und Her, Nachfragen, kurze Reaktionen ("Okay, das ist ein gutes Beispiel.").
- Ablauf: kurze Begrüßung (Mira stellt das Thema vor, ein Satz Rückbezug auf die letzte Folge) → Hauptteil in 4–6 Abschnitten mit konkreten Beispielen → kurze mündliche Zusammenfassung der Kernpunkte (als Merksätze, die man beim Gehen behält) → "Übung für heute" (konkret, in 5–15 Minuten machbar, am selben Tag) → Ausblick auf die nächste Folge → Verabschiedung "Bis morgen in der KI-Werkstatt."

## Für das Ohr schreiben
- Kurze Sätze. Keine Tabellen, keine Listen mit mehr als drei Punkten am Stück, keine Zahlenkolonnen.
- Prompt-Beispiele werden vorgelesen: so formulieren, dass sie gesprochen funktionieren ("Ich schreibe dann zum Beispiel: Du bist ... "). Keine Sonderzeichen, keine spitzen Klammern im gesprochenen Text; wenn XML-Tags erklärt werden, umschreiben ("ein Abschnitt, der mit dem Wort Kontext in spitzen Klammern beginnt und endet").
- Keine Abkürzungen, die man schlecht vorlesen kann. "KI" ist ok. Zahlen ausschreiben, wenn sie gesprochen besser klingen.
- Beispiele aus Andres Welt, aber OHNE echte Kundennamen oder Firmennamen von Kunden: Kundenmail, Analyse eines Umsatzrückgangs, Produktdaten-Feed prüfen, Präsentation fürs Quartalsmeeting, Mail an eine Agentur, Tracking-Einrichtung bei einem Onlineshop usw. Gern auch ein privates Beispiel (Reiseplanung, Hobby).
- Tools neutral und korrekt benennen (Claude, ChatGPT, Gemini). Keine erfundenen Produktfunktionen, keine konkreten Menüpfade, keine Preise, keine Versionsnummern. Wenn unsicher: allgemein bleiben.

## Sprache (zwingend, Anti-KI-Stil)
Verboten: "In der heutigen Welt/Zeit", "Hand aufs Herz", Game-Changer, revolutioniert, bahnbrechend, Paradigmenwechsel, "auf das nächste Level", "spielt eine entscheidende/zentrale Rolle", "es ist wichtig zu beachten", ganzheitlich, nahtlos, akribisch, "tauchen wir ein", "lass uns/lassen Sie uns", "begeben wir uns auf eine Reise", "Insgesamt lässt sich sagen", "Zusammenfassend", "Eines ist klar", "nicht nur ..., sondern auch ...", "Es ist nicht X. Es ist Y.", eintauchen, navigieren (übertragen), entfesseln, facettenreich, vielschichtig, tiefgreifend, befähigen. Keine Ketten aus drei Adjektiven. Konkrete Aussagen statt Floskeln: lieber ein Beispiel als eine Behauptung, dass etwas wichtig ist.

## Anschluss an frühere Folgen
- Lies vor dem Schreiben plan/lehrplan.md (welches Thema dran ist, was schon behandelt wurde) und plan/feedback.md (Andres Wünsche, haben Vorrang).
- Lies das Skript der direkt vorherigen Folge (scripts/folge-NNN.md) und halte dich an deren Ausblick. Frühere Inhalte nur kurz aufgreifen, nicht wiederholen.
- Wiederkehrendes Bild aus Folge 1: der "Schreibtisch" (Kontextfenster: die KI sieht nur, was auf dem Schreibtisch liegt). Darf auftauchen, aber sparsam.
- Ausblick am Ende: das nächste offene Thema aus dem Lehrplan.
- Themen mit dem Hinweis "vorher recherchieren": vor dem Schreiben per Websuche den aktuellen Stand prüfen. Nur belegte Fakten verwenden, keine Preise oder Versionsnummern, die du nicht gerade nachgeprüft hast.
