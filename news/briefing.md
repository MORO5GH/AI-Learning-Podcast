# Briefing: Klöbels KI News – Ausgabe schreiben

## Die Sendung
"Klöbels KI News" erscheint montags, mittwochs und freitags und fasst die wichtigsten Neuigkeiten rund um KI-Modelle und KI-Werkzeuge zusammen. Hörer ist Andre: technisch versierter Berater im E-Commerce/Digital-Marketing (Feed-Management, Tracking, Analysen, Kundenkommunikation), nutzt Claude, Zapier und geplante KI-Aufgaben täglich. Er hört unterwegs, ohne Bildschirm. Parallel hört er den Lern-Podcast "KI-Werkstatt" mit Mira und Jan; die News sind bewusst anders: knapper, sachlicher, aktueller.

Zwei Sprecher:
- LENA: moderiert, führt durch die Meldungen, stellt die Frage "Und was heißt das für die Praxis?".
- TOM: berichtet die Meldungen und ordnet sie ein.
Beide duzen den Hörer. Sachlicher Ton, aber nicht steif.

## Berichtszeitraum
- Montag: Freitag 00:00 bis Sonntag 23:59
- Mittwoch: Montag und Dienstag
- Freitag: Mittwoch und Donnerstag
Bonus- oder Sonderläufe: seit dem Datum der letzten Ausgabe (episodes.json).
Was in der vorherigen Ausgabe schon vorkam, nur erwähnen, wenn es eine echte Neuigkeit dazu gibt.

## Recherche (vor dem Schreiben, gründlich)
1. Quellen aus news/quellen.md durchgehen (zuerst "Zuverlässig abrufbar"), dazu gezielte Websuchen pro Anbieter: Anthropic/Claude, OpenAI/ChatGPT, Google/Gemini, Meta, Mistral, DeepSeek, xAI, Microsoft Copilot, Apple Intelligence sowie wichtige Werkzeuge (z. B. Perplexity, NotebookLM, Zapier, Cursor, ElevenLabs).
2. Jede Meldung braucht mindestens eine abrufbare Quelle, bevorzugt die offizielle Ankündigung des Anbieters. Gerüchte, Leaks und "soll angeblich" nur, wenn ausdrücklich als unbestätigt gekennzeichnet, und höchstens eine solche Meldung pro Ausgabe.
3. Datum jeder Meldung prüfen: nur Dinge aus dem Berichtszeitraum. Ältere Meldungen, die erst jetzt Thema werden, als solche kennzeichnen.
4. Auswahl: 4 bis 6 Meldungen. Vorrang hat, was Andre praktisch betrifft (neue Modelle und Funktionen in Tools, die er nutzt oder nutzen könnte; Preise und Verfügbarkeit in Deutschland/EU; Datenschutz; Automatisierung, Agenten). Finanzierungsrunden, Börsenkurse und Personalien nur, wenn sie für Nutzer etwas ändern.
5. Notiere dir für jede Meldung: was genau, seit wann, für wen verfügbar (Tarif, Region), Quelle(n) mit URL.

## Format (zwingend)
- Datei beginnt mit `# Klöbels KI News – Ausgabe N vom TT.MM.JJJJ`, danach Leerzeile.
- Danach NUR Dialogzeilen, jede beginnt mit `LENA: ` oder `TOM: `, zwischen den Zeilen eine Leerzeile. Keine Regieanweisungen, keine Überschriften, kein Markdown, keine Aufzählungszeichen.
- Länge: 1.700 bis 2.200 Wörter (mit `wc -w` prüfen). Das ergibt 8 bis 12 Minuten.
- Dynamisches Intro (Cold Open), jede Ausgabe anders: Die Sendung beginnt OHNE Begrüßung direkt mit der stärksten Meldung des Berichtszeitraums, als Aufhänger in ein bis drei kurzen, lebendigen Sätzen (eine überraschende Zahl, eine zugespitzte Frage oder ein konkretes Bild aus Andres Arbeitsalltag; Tempo, kurze Sätze, gern Wechsel zwischen LENA und TOM). Danach ein schneller Themenüberblick ("Außerdem: … und …", höchstens drei Stichworte). Erst dann die Begrüßung: "Das ist Klöbels KI News vom <Wochentag>, <Datum>." Keine wiederkehrende Standardformel für den Einstieg, nichts übertreiben, alles muss durch die Quelle gedeckt sein.
- Danach: die Meldungen, je Meldung: was ist passiert, was ist neu daran, was bedeutet es für Andres Arbeit (konkret, z. B. "für deine Kundenmails", "für Automatisierungen über Zapier") → kurzer Ausblick, worauf man in den nächsten Tagen achten sollte (nur wenn es etwas Belegtes gibt, z. B. angekündigte Termine) → Verabschiedung "Das waren Klöbels KI News. Bis <nächster Ausgabetag>."
- Die Einordnung "was heißt das für dich" ist der eigentliche Wert der Sendung. Lieber weniger Meldungen mit guter Einordnung als viele Schlagzeilen.

## Für das Ohr schreiben
- Kurze Sätze. Zahlen ausschreiben, wo sie gesprochen besser klingen. Modellnamen so schreiben, wie man sie ausspricht, Versionsnummern mit "Punkt" ("Gemini drei Punkt acht").
- Keine URLs im gesprochenen Text. Quellen nennt man so: "laut Ankündigung von Anthropic", "berichtet heise".
- Englische Fachbegriffe nur, wenn sie üblich sind; sonst kurz übersetzen.
- Keine echten Kunden- oder Firmennamen aus Andres Kundenarbeit.

## Sprache (zwingend, Anti-KI-Stil)
Verboten: "In der heutigen Welt/Zeit", "Hand aufs Herz", Game-Changer, revolutioniert, bahnbrechend, Paradigmenwechsel, "auf das nächste Level", "spielt eine entscheidende/zentrale Rolle", "es ist wichtig zu beachten", ganzheitlich, nahtlos, akribisch, "tauchen wir ein", "lass uns/lassen Sie uns", "begeben wir uns auf eine Reise", "Insgesamt lässt sich sagen", "Zusammenfassend", "Eines ist klar", "nicht nur ..., sondern auch ...", "Es ist nicht X. Es ist Y.", eintauchen, navigieren (übertragen), entfesseln, facettenreich, vielschichtig, tiefgreifend, befähigen. Keine Ketten aus drei Adjektiven. Keine Hype-Wörter aus Pressemitteilungen übernehmen ("das leistungsstärkste Modell aller Zeiten"): nüchtern sagen, was gemessen oder angekündigt wurde.

## Folgenbeschreibung (für den Feed)
Zwei Teile, als ein Text:
1. Ein Satz Überblick über die Themen.
2. "Quellen:" und danach je Meldung "Kurztitel: URL", durch Zeilenumbrüche getrennt.
