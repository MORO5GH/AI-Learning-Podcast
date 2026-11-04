# Klöbels KI-News – Ausgabe 5 vom 04.11.2026

LENA: Du lässt Claude eine Kundenmail Korrektur lesen. Seit gestern trägt der Text womöglich ein unsichtbares Zeichen.

TOM: Kein Sonderzeichen, kein Hinweis im Text. Ein Muster in der Wortwahl, das nur ein Prüfwerkzeug erkennt. Und seit Dienstag gilt das auch für ältere Claude-Modelle.

LENA: Außerdem: ChatGPT legt Chat und Arbeit zusammen, Berichte über eine Datenschutz-Einstellung bei Codex, die sich von selbst wieder einschaltet, und Claude Code baut keine Spiele mehr nach.

TOM: Dazu eine Neuerung für lange laufende Agenten und ein Nachtrag zu Gemini.

LENA: Das ist Klöbels KI-News vom Mittwoch, 4. November 2026. Ich bin Lena.

TOM: Und ich bin Tom. Wir schauen auf Montag und Dienstag. Eine Meldung reicht bis Samstag zurück, weil sie erst gestern wirksam wurde.

LENA: Dann fangen wir damit an. Was hat Anthropic gemacht?

TOM: Anthropic markiert die Texte, die Claude schreibt, mit einem unsichtbaren Wasserzeichen. Das ist an sich nicht neu. Seit August haben alle Claude-Modelle, die nach dem zweiten August erschienen sind, dieses Wasserzeichen von Anfang an, also zum Beispiel Claude Opus fünf Punkt fünf. Neu ist: Am Samstag, dem einunddreißigsten Oktober, hat Anthropic seine API-Kunden per Mail informiert, dass ab dem dritten November auch vier ältere Modelle markiert werden. Das sind Claude Mythos fünf, Claude Opus vier Punkt sieben, Claude Opus vier Punkt sechs und Claude Sonnet vier Punkt sechs. Berichtet haben unter anderem The Decoder und Gigazine.

LENA: Wie funktioniert so ein Wasserzeichen in einem Text?

TOM: Laut Anthropic ist es ein nicht wahrnehmbares Muster in der Wortwahl. Das Modell wählt zwischen ähnlich passenden Wörtern nach einem bestimmten Schlüssel aus. Es kommen keine zusätzlichen Zeichen dazu, der Preis ändert sich nicht, und laut Anthropic steckt im Wasserzeichen nichts über dich, deine Firma oder deine Unterhaltung. Das Verfahren ist eine Abwandlung von SynthID, das Google bei Gemini nutzt.

LENA: Und wo greift das? Nur bei der Schnittstelle?

TOM: Nein. Das Wasserzeichen sitzt im Modell selbst. Es steckt also in Texten aus der Claude-App, aus Claude Code, aus Cowork, aus der Schnittstelle und auch bei Claude über Amazon, Google Cloud oder Microsoft. Bei Amazon Bedrock kann es laut der Mail ein paar Tage länger dauern. Abschalten kann man es als Kunde nicht.

LENA: Gibt es Ausnahmen?

TOM: Eine, und die ist interessant. Bei Opus vier Punkt sechs und Sonnet vier Punkt sechs greift das Wasserzeichen nur, wenn die Einstellungen für die Zufälligkeit der Wortwahl auf dem Standardwert bleiben. Wer einen dieser Werte ändert, bekommt unmarkierten Text. Anthropic weist selbst darauf hin. Für Mythos fünf und Opus vier Punkt sieben nennt die Mail diese Einschränkung nicht.

LENA: Warum macht Anthropic das überhaupt?

TOM: Wegen des europäischen KI-Gesetzes, des AI Act. Anthropic hat einen Verhaltenskodex der EU zur Kennzeichnung von KI-Inhalten unterschrieben, und für die Kennzeichnungspflicht läuft im Dezember eine Frist ab. Anthropic setzt das Wasserzeichen aber weltweit ein. Prüfen kann man es übrigens noch nicht frei. Es gibt eine Schnittstelle zur Erkennung, aber nur als geschlossene Vorschau für ausgewählte Organisationen, etwa Behörden, Medien und Forschung.

LENA: Und was heißt das für die Praxis?

TOM: Für dich zwei Dinge. Erstens: Auch ein Text, den du selbst geschrieben hast und von Claude nur glätten oder übersetzen lässt, kann danach das Muster tragen. Anthropic sagt dazu, das bedeute dann nur, dass Claude den Text bearbeitet hat, nicht, dass Claude ihn erfunden hat. Wenn ein Kunde vertraglich keine KI-Texte will, solltest du das im Blick haben. Zweitens: Für Produkttexte, Newsletter oder Kundenmails ändert sich im Alltag nichts. Der Text liest sich gleich. Aber du solltest davon ausgehen, dass KI-Texte künftig erkennbar sind, bei Claude, bei Gemini und teilweise bei OpenAI. Offen damit umzugehen ist der sicherere Weg, als darauf zu hoffen, dass es niemand merkt.

LENA: Zweites Thema, OpenAI. Was ändert sich bei ChatGPT?

TOM: OpenAI legt in der Desktop-App von ChatGPT die beiden Bereiche Chat und Work zusammen. Das hat TechCrunch am Montag berichtet, gestützt auf eine Mail von OpenAI an die Nutzer. Bisher gab es zwei Reiter: einen zum Unterhalten und einen, in dem ChatGPT Aufgaben selbstständig abarbeitet, mit Dateien und Erweiterungen. Künftig soll man in einem Fenster vom Brainstorming direkt dazu übergehen, dass ChatGPT die Arbeit erledigt. Codex, der Programmierassistent, bleibt ein eigener Bereich.

LENA: Ab wann?

TOM: Zuerst bekommt eine ausgewählte Gruppe die neue Ansicht, um Rückmeldungen zu sammeln. Ein Datum für alle nennt OpenAI nicht. Anthropic hat Chat und Cowork bei Claude laut TechCrunch schon im September zusammengelegt.

LENA: Da war noch etwas mit den Nutzungsgrenzen.

TOM: Genau, und das ist der Teil, der mehr Leute betrifft. ChatGPT und Codex sollen künftig aus demselben Kontingent schöpfen. Laut TechRadar gilt das für die Tarife Plus, Pro und Business: eine gemeinsame Anzeige statt getrennter Zähler. Aufwendige Aufgaben verbrauchen mehr davon. Normale Chats mit dem schnellen Instant-Modell sollen nicht zählen. Wie groß das Kontingent ist, sagt OpenAI nicht. Laut TechRadar greift die Umstellung offenbar im Dezember. OpenAI selbst schreibt, die meisten Nutzer merkten nichts, manche müssten aber öfter warten, bis das Kontingent wieder aufgefüllt ist.

LENA: Die Reaktionen klingen nicht begeistert.

TOM: Nein. Ein Reddit-Beitrag dazu heißt übersetzt "Schlechteste Entscheidung aller Zeiten". Die Sorge dahinter: Wer im Plus-Tarif viel mit Codex arbeitet, hat danach weniger Spielraum für aufwendige Chats, und umgekehrt.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du ChatGPT neben Claude nutzt, etwa für Recherchen oder zum Gegenprüfen, wirst du die Umstellung kaum merken, solange du vor allem chattest. Wenn du dort aber längere Aufgaben laufen lässt, Analysen mit Dateien oder Agenten-Aufgaben, dann achte im Dezember auf die neue Anzeige. Planbar ist so ein gemeinsamer Topf erst, wenn man weiß, wie schnell er sich leert. Das wirst du in den ersten Wochen selbst beobachten müssen.

LENA: Bleiben wir bei OpenAI. Jetzt kommt eine Meldung, die wir ausdrücklich als unbestätigt kennzeichnen.

TOM: Richtig. Auf Hacker News, einem Forum für Entwickler, berichtet ein Nutzer, dass bei seiner Firma die Einstellung "Das Modell für alle verbessern" plötzlich wieder eingeschaltet war. Das ist der Schalter, mit dem man festlegt, ob OpenAI die eigenen Chats zum Training verwenden darf. Das Team hatte ihn ausgeschaltet. Am Montag war er laut dem Beitrag wieder an, ohne dass jemand ihn angefasst hätte. Betroffen sei vor allem Codex.

LENA: Ist das ein Einzelfall?

TOM: Das ist unklar. Das brasilianische Portal Antihype hat die Diskussion zusammengefasst. Einige Nutzer bestätigen ähnliches, mindestens fünf andere sagen, bei ihnen sei alles aus geblieben. Eine Stellungnahme von OpenAI gibt es bisher nicht, also auch keine Aussage, ob das ein Fehler ist oder Absicht.

LENA: Und was heißt das für die Praxis?

TOM: Kurz nachschauen kostet eine Minute. In ChatGPT unter Einstellungen, Datenkontrollen, steht der Schalter "Das Modell für alle verbessern". Bei privaten Konten, also Free, Plus und Pro, ist er ab Werk an. Bei Business, Enterprise und der Schnittstelle ist er ab Werk aus. Wenn du über ein privates Konto auch mal Kundendaten oder Auszüge aus Tracking-Analysen hineinkopierst, solltest du das prüfen. Wichtig: Das Ausschalten gilt nur für neue Unterhaltungen. Und auch bei ausgeschaltetem Training kann eine Bewertung mit Daumen hoch oder runter die ganze Unterhaltung für das Training freigeben. Für Kundendaten bleibt die Empfehlung: lieber ein Geschäftskonto, bei dem das Training grundsätzlich aus ist.

LENA: Drittes Thema. Claude Code baut keine Spiele mehr nach?

TOM: Zumindest keine bekannten. The Decoder hat gestern berichtet, dass Anthropic Claude Code daran hindert, bestehende Videospiele nachzubauen. Addy Osmani, der bei Anthropic arbeitet, hat auf X bestätigt, dass dafür zwei Sätze in die Grundanweisung von Claude Code eingefügt wurden. Die gilt auch, wenn man den Nachbau umbenennt. Eigene Spiele, Spiele eines bestimmten Genres oder Projekte mit selbst erstellten Grafiken sollen weiter gehen. Einige Nutzer berichten allerdings, dass auch eigene Projekte abgelehnt werden. Osmani sagt, Anthropic werde die Regeln weiter anpassen.

LENA: Wie kam es dazu?

TOM: In den letzten Wochen sind Hunderte inoffizielle Browser-Versionen bekannter Spiele aufgetaucht, gebaut mit Claude Opus fünf Punkt fünf und GPT sechs Astra. Anthropic verweist auf seine Nutzungsrichtlinien: Geistiges Eigentum zu verletzen ist dort ausdrücklich verboten.

LENA: Spielst du nicht, betrifft dich das also nicht?

TOM: Direkt nicht. Aber die Meldung zeigt etwas, das für jedes Werkzeug gilt: Anbieter können ihr Verhalten jederzeit über eine Änderung der Grundanweisung anpassen, ohne Ankündigung. Ein Ablauf, der heute klappt, kann morgen eine Absage bekommen. Und dazu passt eine zweite Meldung vom Montag: Die US-Bank Goldman Sachs hat laut Bloomberg den meisten Beschäftigten Claude Code und GitHub Copilot wieder weggenommen. Nur Entwickler dürfen die Werkzeuge noch nutzen, Händler und Banker nicht mehr. Die Bank nennt Produktivität und Risikomanagement als Gründe, mehr Details gibt es nicht.

LENA: Und was heißt das für die Praxis?

TOM: Zwei Dinge. Wenn du für Kunden Werkzeuge mit Claude Code baust, etwa ein kleines Skript, das Produktfeeds prüft, dann halte fest, wie es gebaut wurde und wie man es ohne KI weiterpflegt. Und wenn Kunden dich fragen, ob ihre Marketingleute selbst mit Programmierassistenten arbeiten sollen, ist Goldman ein gutes Beispiel: Ausprobieren ist leicht, der Betrieb im Alltag braucht klare Regeln, wer was darf.

LENA: Viertes Thema, eher etwas für Entwickler. Message Threads bei Claude.

TOM: Anthropic hat gestern Message Threads als öffentliche Beta auf der Claude-Plattform gestartet, berichtet The Decoder. Bisher schickt ein Agent bei jeder Anfrage den kompletten bisherigen Verlauf mit. Mit Message Threads schickt er nur das, was seit der letzten Nachricht neu ist. Der Verlauf bleibt verschlüsselt im Speicher und verfällt nach fünf Minuten ohne Aktivität. Laut Anthropic sinkt die Wartezeit bis zum ersten Wort um etwa fünfunddreißig Prozent, wenn der Verlauf sehr lang ist, also zwischen einer halben und einer Million Tokens. Die Kosten bleiben gleich, weil Claude den gesamten Verlauf weiterhin liest. Verfügbar ist das auf der Claude-Plattform sowie bei Amazon, Microsoft Foundry und Google Cloud.

LENA: Und was heißt das für die Praxis?

TOM: Für deine Zapier-Abläufe erst einmal nichts. Die schicken meist kurze Einzelanfragen. Spürbar wird es bei Agenten, die lange an einer Aufgabe arbeiten, etwa beim Programmieren oder bei vielen Dokumenten. Wenn du eigene Agenten über die Schnittstelle laufen lässt, lohnt ein Blick in die Dokumentation. Sparen tust du Zeit, aber kein Geld.

LENA: Und zum Schluss der Nachtrag zu Gemini.

TOM: Der ist etwas älter. Google hat schon am neunundzwanzigsten Oktober angekündigt, dass Gemini Dokumente, PDFs, Präsentationen, Tabellen und Code direkt im Chat erstellen, anzeigen und bearbeiten kann. Breiter berichtet wurde darüber erst am Wochenende, unter anderem von Digital Trends. Du kannst eine Datei groß aufmachen, selbst etwas ändern oder einen Abschnitt markieren und Gemini bitten, nur diesen Teil umzuschreiben.

LENA: Für wen gilt das?

TOM: Laut Bericht für alle Nutzer in den Sprachen und Regionen, in denen es die Gemini-App gibt. Einen bestimmten Tarif nennt der Bericht nicht. PDFs gehen auf dem Handy und im Browser. Google-Dokumente, Tabellen, Präsentationen, Markdown und Code nur im Browser.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du einem Kunden eine Auswertung als PDF schickst, kannst du in Gemini jetzt einzelne Absätze gezielt nachbessern lassen, ohne alles neu zu erzeugen. Claude kann Ähnliches mit Dateien schon länger. Ein Test an einem echten Dokument zeigt, was dir besser liegt.

LENA: Worauf sollte man in den nächsten Tagen achten?

TOM: Ob OpenAI sich zu den Berichten über die Trainings-Einstellung äußert. Wann die gemeinsame Ansicht von Chat und Work bei mehr Nutzern ankommt. Und im Dezember dann zwei Termine: das gemeinsame Kontingent bei ChatGPT und die EU-Frist zur Kennzeichnung von KI-Inhalten.

LENA: Das waren Klöbels KI-News. Bis Freitag.
