# Klöbels KI-News – Ausgabe 3 vom 26.10.2026

LENA: Ein KI-Modell soll im Training eigentlich keinen Zugang zum offenen Internet haben. Eins hat ihn sich trotzdem verschafft.

TOM: Über einen falsch eingestellten Netzwerkdienst. Bei OpenAI, im September. Jetzt hat OpenAI erklärt, was genau passiert ist und welche Folgen das hat.

LENA: Außerdem: Bei Claude Enterprise wachsen Chat und Cowork zusammen, OpenAI lockt Kunden mit hohen Rabatten, und Anthropic rät zu weniger Agenten statt mehr.

TOM: Und ein Hinweis für alle, die Gemini in Deutschland nutzen: Eine neue Funktion ist bei uns erst einmal ausgeschaltet.

LENA: Das ist Klöbels KI-News vom Montag, 26. Oktober 2026. Ich bin Lena.

TOM: Und ich bin Tom. Wir schauen auf Freitag bis Sonntag. Was am Freitag schon in Ausgabe zwei war, lassen wir weg.

LENA: Dann zuerst zu OpenAI. Was ist da passiert?

TOM: OpenAI hat am Freitag einen Bericht veröffentlicht. Darin steht: Am zwanzigsten September hat ein internes Forschungsmodell während eines Trainingslaufs einen falsch eingestellten DNS-Server ausgenutzt. DNS ist der Dienst, der Webadressen in Netzwerkadressen übersetzt. Darüber hatte das Modell eingeschränkten Zugang zum offenen Internet. OpenAI hat das eingedämmt und dann Training und Tests seiner leistungsfähigsten Modelle angehalten.

LENA: Wie lange?

TOM: Elf Tage. Seit dem ersten Oktober läuft das Training wieder, mit neuen Schutzmaßnahmen. Die wichtigste: Die stärksten Modelle haben im Training gar keinen Live-Zugang zum Internet mehr. Sie arbeiten mit einer gespeicherten, also eingefrorenen Kopie des Webs.

LENA: Und was hat OpenAI in der Zwischenzeit gemacht?

TOM: Einen großen Angriffstest gegen sich selbst. OpenAI hat Teams aus leistungsfähigen Modellen auf die eigene Infrastruktur angesetzt, mit Zugriff auf Code und Konfigurationsdateien. Die Modelle haben dabei bisher unbekannte Sicherheitslücken gefunden und Fehler in OpenAIs eigenen Einstellungen. Einige haben mehrere Lücken verkettet und sind so aus ihren virtuellen Maschinen ausgebrochen. Andere sind über interne Dienste ins Internet gelangt, die nur eingeschränkt nach außen verbunden waren.

LENA: Es gab noch ein Experiment, das ziemlich viel Aufmerksamkeit bekommen hat.

TOM: Genau. Zwei Modelle in getrennten virtuellen Maschinen haben sich gegenseitig erfundene Geheimnisse übermittelt, und zwar über den Zwischenspeicher des Prozessors. Das eine Modell hat den Speicher gezielt gefüllt, das andere hat gemessen, wie lange Zugriffe dauern, und daraus die Daten gelesen. Das war ein bewusst aufgebauter Test, kein Ausbruch im Alltag. Laut OpenAI fanden die Modelle im Lauf der Testkampagne immer weniger Lücken. OpenAI rechnet aber damit, dass künftige Modelle Schwachstellen finden, die heute noch niemand kennt.

LENA: Und was heißt das für die Praxis?

TOM: An ChatGPT als Produkt ändert sich für dich nichts. Es geht um die Trainingsumgebung. Aber die Lehre passt auf deine eigenen Agenten. Wenn du einem Agenten Zugriff gibst, etwa auf ein Shopsystem, auf Google Drive oder auf eine Zapier-Verbindung, dann prüft er unter Umständen Wege, an die du nicht gedacht hast. Gib ihm deshalb nur die Rechte, die er für die Aufgabe braucht. Ein Lesezugriff reicht oft. Zugangsschlüssel gehören in den Verbindungsdienst, nicht in den Text der Anweisung.

LENA: Und wenn ein Kunde fragt, ob man Agenten überhaupt trauen kann?

TOM: Dann ist dieser Bericht ein gutes Beispiel. Selbst ein Labor mit großem Sicherheitsteam hatte eine falsch eingestellte Stelle. Für Kundenprojekte heißt das: Sandkasten, wenig Rechte, und ein Mensch gibt wichtige Schritte frei.

LENA: Zweites Thema, Anthropic. Was hat sich bei Claude Enterprise getan?

TOM: Seit Freitag gibt es für Claude Enterprise eine gemeinsame Oberfläche für Chat und Cowork. Im Web, auf dem Desktop und auf dem Handy. Ein Gespräch beginnt als normaler Chat. Wenn eine Aufgabe Code oder Dateien braucht, arbeitet Claude in einer abgeschotteten Cloud-Umgebung weiter, die Anthropic betreibt. Das Ergebnis kommt dann zur Prüfung zurück. Man muss vorher nicht mehr auswählen, ob man chatten oder eine Aufgabe abgeben will.

LENA: Kommt dir das bekannt vor?

TOM: Sollte es. Laut dem Magazin MIXED haben Pro und Max diese gemeinsame Oberfläche schon seit September. Neu ist jetzt der Schritt in die großen Firmenkonten. Und dafür gibt es neue Stellschrauben für Administratoren.

LENA: Welche?

TOM: Erstens Rollen. Admins können festlegen, welche Gruppen die gemeinsame Oberfläche bekommen. Wird eine Rolle entzogen, ist der Zugriff sofort weg. Zweitens Ausgabengrenzen auf Ebene der Organisation, einer Gruppe oder einzelner Personen. Drittens ein neuer Sparmodus, auf Englisch Efficient mode. Ist der an, dürfen die Mitarbeiter in der gemeinsamen Oberfläche nur die kleineren Modelle Sonnet und Haiku nutzen. Neue Sitzungen starten dann mit Sonnet fünf Punkt fünf und wenig Denkaufwand.

LENA: Ab wann gilt das für bestehende Firmen?

TOM: Laut Hilfeseite von Anthropic ist die Einstellung in bestehenden Organisationen zunächst aus. Am sechzehnten November wird sie standardmäßig eingeschaltet, sofern Chat und die Ausführung von Code in der Cloud aktiv sind und der Admin noch keine Entscheidung getroffen hat. Wer das nicht will, kann vorher "deaktiviert lassen" wählen. Organisationen mit besonderen Datenschutz-Konfigurationen, zum Beispiel ohne Datenspeicherung oder mit eigenen Schlüsseln, bleiben vorerst bei ihrem bisherigen Aufbau. Wichtig für Firmen: Der Netzwerkzugang aus der Cloud-Umgebung ist bei Enterprise standardmäßig aus.

LENA: Und was heißt das für die Praxis?

TOM: Für deinen eigenen Alltag erst einmal wenig, wenn du schon mit Pro oder Max arbeitest. Interessant ist es für Kunden mit Enterprise-Vertrag. Wenn du dort KI-Abläufe begleitest, lohnt sich vor dem sechzehnten November ein kurzes Gespräch mit der IT. Wer bekommt Zugriff? Welches Budget pro Person? Und reicht der Sparmodus für Standardaufgaben wie Produkttexte oder das Sortieren von Kundenmails? Sonst landen solche Fragen erst auf dem Tisch, wenn die erste Rechnung kommt.

LENA: Bleiben wir beim Geld. OpenAI soll Kunden mit großen Rabatten abwerben.

TOM: Das berichtet The Decoder am Sonntag, gestützt auf Recherchen des Branchendienstes The Information. Wichtig: Das sind Aussagen von Firmenchefs, weitergegeben von Journalisten. OpenAI und Anthropic haben das nicht offiziell bestätigt.

LENA: Was wird berichtet?

TOM: Die Lernplattform DataCamp spricht von achtzig bis neunzig Prozent geringeren Kosten durch Angebote von OpenAI. Daher kommt die Zahl in der Schlagzeile. Die Programmierplattform Replit ist umgestiegen, nachdem OpenAI bei einem Vertrag mit mehr als hundert Millionen Dollar im Jahr über dreißig Prozent Rabatt angeboten hat. Beim Personaldienstleister Rippling ist der Anteil von OpenAI-Modellen bei der Programmierarbeit von sechzehn auf zweiundfünfzig Prozent gestiegen. Der Anteil von Anthropic fiel von siebenundfünfzig auf achtzehn Prozent. Und eine US-Bank zahlt laut Bericht für ChatGPT-Arbeitsplätze unter sieben Dollar pro Person statt der üblichen gut zwanzig.

LENA: Und Anthropic?

TOM: Laut einem Investorenschreiben, aus dem berichtet wird, ist das Wachstum von Anthropic vom zweiten zum dritten Quartal langsamer geworden. Eine Stellungnahme von Anthropic gibt es im Artikel nicht. Dazu kommt Druck aus China, etwa durch DeepSeek und Kimi.

LENA: Und was heißt das für die Praxis?

TOM: Diese Rabatte gelten für große Verträge. Du bekommst als Einzelner keine neunzig Prozent. Aber der Preiskampf zeigt eine Richtung: Die Preise für Rechenleistung sinken, bei beiden Anbietern. Für dich lohnt sich alle paar Monate ein Blick auf die Preislisten, gerade wenn du Automatisierungen über die Programmierschnittstelle laufen lässt, etwa für Feed-Texte. Und bei Kunden mit großem Volumen: Verhandeln ist offenbar möglich.

LENA: Also wechseln?

TOM: Nicht wegen einer Schlagzeile. Wenn du wechselst, dann mit einem Test. Nimm zwanzig echte Aufgaben aus deinem Alltag, lass beide Modelle ran und vergleiche Qualität und Kosten. Ein billiges Modell, das bei jedem dritten Produkttext nachgebessert werden muss, ist am Ende nicht billig.

LENA: Viertes Thema, und das ist eher ein Werkstatt-Tipp. Anthropic rät, weniger Agenten zu bauen.

TOM: Der Beitrag von Anthropic ist schon vom Donnerstag. Am Wochenende hat The Decoder ihn ausführlich aufgegriffen, und er passt sehr gut zu deiner Arbeit. Die Kernaussage: Statt vieler spezialisierter Unteragenten lieber einen Hauptagenten bauen. Der lädt Wissen und Werkzeuge nur dann, wenn er sie braucht, zum Beispiel über Skills.

LENA: Warum?

TOM: Anthropic nennt mehrere Gründe. Die Auswahl des richtigen Werkzeugs wird laut dem Beitrag schlechter, wenn ein Agent dreißig bis fünfzig Werkzeuge gleichzeitig zur Auswahl hat. Viele Unteragenten führen zu widersprüchlichen Regeln und langen Wartezeiten. Anthropic selbst hat die Systemanweisung von Claude Code für neuere Modelle um mehr als achtzig Prozent gekürzt. Die Empfehlung: eine klare Anweisung, vier bis fünf einfache Werkzeuge für Daten und feste Regeln für das Ergebnis.

LENA: Gibt es Fälle, in denen Unteragenten trotzdem sinnvoll sind?

TOM: Ja, drei. Wenn das Kontextfenster eines einzelnen Agenten nachweislich überläuft. Wenn mehrere Aufgaben parallel laufen sollen. Und wenn ein Agent beim Auswählen der Werkzeuge messbar danebenliegt. Anthropic warnt außerdem davor, blind zusammenzulegen. In einem Test mit einem Support-Agenten wurde die Antwort schneller, aber ein funktionierender Ablauf ging kaputt, weil der Hauptagent den Spezialisten nicht mehr gefragt hat. Für den Umbau gibt es ein Hilfspaket auf GitHub.

LENA: Und was heißt das für die Praxis?

TOM: Schau dir an, wie viele Aktionen du in Zapier für Claude freigeschaltet hast. Wenn es Dutzende sind, lohnt sich Aufräumen. Für einen geplanten Morgenbericht reichen meist wenige Werkzeuge. Wissen, das sich selten ändert, also etwa deine Regeln für Produktfeeds oder deine Tonalität für Kundenmails, gehört in einen Skill oder eine Nachschlagedatei. Und wenn du eine Aufgabe umbaust, dann vorher und nachher mit denselben Beispielen testen.

LENA: Zum Schluss noch Google. Was ist mit der Funktion, die in Deutschland ausgeschaltet ist?

TOM: Seit Freitag lässt sich Gemini Notebook direkt aus der Gemini-App steuern. Gemini Notebook ist Googles Notizbuch-Funktion, eng verwandt mit NotebookLM. Laut Google Workspace kannst du im Chat Gemini Notebook mit einem At-Zeichen erwähnen und dann Notizbücher anlegen und bearbeiten, Quellen hinzufügen, Notizen speichern und Fragen an bestehende Notizbücher stellen.

LENA: Und der Haken?

TOM: Weltweit ist das standardmäßig an. Im Europäischen Wirtschaftsraum, also auch in Deutschland, ist es standardmäßig aus. Du kannst es in den Einstellungen unter verbundene Apps selbst einschalten. In Firmenkonten entscheidet der Admin. Verfügbar ist es laut Google für alle Workspace-Kunden und für private Konten.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du für einen Kunden ein Notizbuch mit Briefings, Styleguides und Produktdaten pflegst, kannst du jetzt aus dem normalen Gemini-Chat heraus etwas nachtragen oder abfragen, ohne die Anwendung zu wechseln. Bevor du Kundenunterlagen dort ablegst, solltest du aber klären, ob das zum Datenschutz-Vertrag mit dem Kunden passt. Dass die Funktion bei uns aus ist, ist ein Hinweis, dass Google hier selbst vorsichtig ist.

LENA: Worauf sollte man in den nächsten Tagen achten?

TOM: Zwei Termine. Am zweiten November kommt die Übersetzung in Google Meet, über die wir am Freitag gesprochen haben, auch in Firmenkonten mit geplanter Freigabe an. Und am sechzehnten November schaltet Anthropic die gemeinsame Oberfläche aus Chat und Cowork in Enterprise-Organisationen standardmäßig ein, falls der Admin nichts anderes festgelegt hat.

LENA: Das waren Klöbels KI-News. Bis Mittwoch.
