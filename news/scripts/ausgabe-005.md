# Klöbels KI-News – Ausgabe 5 vom 25.11.2026

LENA: Ab dem ersten Februar ändert Google die Regeln für KI-Agenten in Gmail, Drive und Kalender.

TOM: Wer dann mit einem Agenten auf Workspace-Daten zugreift, soll dafür einen neuen, offiziellen Weg nehmen. Wer beim alten bleibt, bekommt laut mehreren Berichten engere Grenzen.

LENA: Außerdem: Google bringt Gemini vier Neon, ChatGPT bekommt ein neues Standardmodell, und bei Claude wird aus einem Artefakt eine eigene Desktop-App.

TOM: Und das Protokoll, über das Claude mit deinen Werkzeugen spricht, lernt ein paar wichtige neue Dinge.

LENA: Das ist Klöbels KI-News vom Mittwoch, 25. November 2026. Ich bin Lena.

TOM: Und ich bin Tom. Nach einer längeren Pause schauen wir heute auf die letzte Woche, also auf die Zeit seit Mittwoch, dem achtzehnten November.

LENA: Dann fangen wir mit Google Workspace an. Was ist da passiert?

TOM: Google hat am Dienstag, dem vierundzwanzigsten November, seine MCP-Server für Workspace allgemein freigegeben. MCP ist das Model Context Protocol, also die gemeinsame Sprache, über die KI-Assistenten mit anderen Diensten reden. Freigegeben sind acht solcher Server: für Gmail, Drive, Docs, Tabellen, Präsentationen, Kalender, Chat und Aufgaben. Dazu kommt ein offizielles Kommandozeilen-Werkzeug. Das steht im Workspace-Blog von Google und wird von mehreren Fachseiten übereinstimmend berichtet.

LENA: Und was hat es mit dem ersten Februar auf sich?

TOM: Ab dem ersten Februar zweitausendsiebenundzwanzig sollen KI-Agenten über diese MCP-Server oder das Kommandozeilen-Werkzeug auf Workspace-Daten zugreifen. Also nicht mehr über die klassischen Programmierschnittstellen, die bisher jede Automatisierung genutzt hat. Wie hart das durchgesetzt wird, beschreiben die Berichte unterschiedlich. Zwei Quellen schreiben, dass Agenten, die weiter den alten Weg nehmen, auf die Grenzen der kostenlosen Stufe gesetzt werden. Eine andere schreibt, der alte Weg funktioniere für Agenten dann gar nicht mehr. Für normale Apps, die ein Mensch bedient, ändert sich laut den Berichten nichts.

LENA: Du hast gerade von einer kostenlosen Stufe gesprochen. Kostet das jetzt Geld?

TOM: Es gibt zwei Stufen. Die Standard-Stufe ist kostenlos und braucht kein Abrechnungskonto. Genannt werden fünftausend Anfragen pro Tag, wobei die Quellen sich nicht einig sind, ob das pro Produkt oder pro Projekt gilt. Wer mehr braucht, nimmt die Stufe für hohe Last. Die wird ab dem ersten April zweitausendsiebenundzwanzig abgerechnet. Google selbst sagt, dass über neunundneunzig Prozent der aktiven Entwickler in der kostenlosen Stufe bleiben. Für Administratoren gibt es neue Einstellungen in der Admin-Konsole, dazu Prüfprotokolle und Rückfragen, bevor ein Agent zum Beispiel Mails verschickt oder Dateien löscht.

LENA: Und was heißt das für die Praxis?

TOM: Für dich als Berater ist das vor allem eine Frage für deine Kunden. Viele Shops haben Automatisierungen, die Bestellungen in eine Google-Tabelle schreiben oder Kundenmails in Gmail sortieren. Solange das klassische Zapier-Abläufe sind, ist offen, ob Google sie überhaupt als Agenten zählt. Das sagen die Berichte nicht. Läuft aber ein KI-Agent mit Zugriff auf Gmail oder Drive, dann solltest du vor Februar prüfen, über welchen Weg er zugreift. Und für Kunden mit Workspace lohnt ein Blick in die neuen Admin-Einstellungen. Da lässt sich festlegen, welche externen KI-Werkzeuge überhaupt an die Daten dürfen.

LENA: Bleiben wir bei MCP. Auch Anthropic hat das Protokoll erweitert.

TOM: Genau, ebenfalls am vierundzwanzigsten November. Laut Anthropic gibt es inzwischen über zehntausend MCP-Verbindungen für Claude. Neu sind drei Dinge. Erstens: Aufgaben im Hintergrund. Ein Dienst kann jetzt eine lange Arbeit annehmen, sie im Hintergrund erledigen und sich melden, wenn sie fertig ist. Zweitens: Rückfragen. Fehlt dem Dienst eine Information, hält er an und fragt dich, statt zu raten. Beides ist jetzt allgemein verfügbar, zunächst für Pro, Max und Ultra, Team und Enterprise folgen nach und nach.

LENA: Und das Dritte?

TOM: Fähigkeiten über MCP, auf Englisch Skills. Ein Dienst liefert damit zu seinen Werkzeugen gleich die passenden Anleitungen mit, wie Claude damit arbeiten soll. Das ist eine offene Testphase. Bei Pro, Max und Ultra ist es von Anfang an eingeschaltet, bei Team muss ein Administrator es freigeben, Enterprise kommt später. Angekündigt, aber noch nicht da, ist das Hochladen von Dateien an solche Dienste, also etwa eine Tabelle oder ein PDF.

LENA: Und was bringt dir das konkret?

TOM: Du nutzt Zapier über MCP mit Claude. Die Rückfragen sind dabei der interessanteste Teil. Bisher hat Claude bei unklaren Angaben oft einfach angenommen, welcher Kanal oder welche Tabelle gemeint ist. Wenn Anbieter wie Zapier die Rückfrage einbauen, kann der Dienst selbst nachhaken. Das macht Schreibaktionen sicherer. Die Hintergrundaufgaben helfen bei Dingen, die länger dauern, etwa einem großen Feed-Export. Ob und wann Zapier das unterstützt, ist aber noch nicht bekannt. Das solltest du in den nächsten Wochen beobachten.

LENA: Dann zu Claude selbst. Was ist mit den Artefakten?

TOM: Artefakte sind die kleinen Seiten und Werkzeuge, die Claude dir baut, etwa ein Rechner oder eine Übersicht. Die lassen sich jetzt als eigenständige Desktop-Apps für macOS und Windows installieren. Das berichtet The Decoder am vierundzwanzigsten November und beruft sich auf einen Beitrag von Felix Rieseberg aus dem Claude-Team. Die App kann dann im Dock liegen, eigene Einträge in der Menüleiste haben, Benachrichtigungen schicken und auf deine Verbindungen zugreifen. Das Ganze ist eine Testversion und braucht die aktuelle Claude-App. Laut dem Beitrag reicht dafür sogar ein kostenloses Konto.

LENA: Und was heißt das für die Praxis?

TOM: Denk an die kleinen Helfer, die du dir ohnehin bauen lässt. Ein Rechner für Werbebudgets, eine Prüfliste für einen Feed-Import, eine Übersicht über offene Kundenfragen. Bisher lagen die im Browser oder irgendwo in einem alten Chat. Jetzt kannst du sie wie ein normales Programm starten. Mit Benachrichtigungen ließe sich zum Beispiel ein kleines Werkzeug bauen, das dich erinnert, wenn ein Wert über eine Grenze steigt. Weil es eine Testphase ist, würde ich damit aber noch keine Abläufe bauen, von denen ein Kunde abhängt.

LENA: Jetzt zu Google und dem neuen Modell.

TOM: Am achtzehnten November hat Google Gemini vier Neon vorgestellt. Das Modell liegt in der Gemini-vier-Familie zwischen dem großen Carbon und dem schnellen Hydrogen. Google beschreibt es als Modell für Programmierung, Wissensarbeit und wissenschaftliche Aufgaben. Es hat vier Stufen, wie lange es nachdenkt, voreingestellt ist die hohe Stufe. Das Kontextfenster fasst eine Million Token, also sehr viel Text auf einmal.

LENA: Wo bekommt man es?

TOM: In der Gemini-App steht es für Abonnenten von Google AI Pro und Ultra in der Modellauswahl. Für Entwickler gibt es Gemini vier Neon über die Schnittstelle im bezahlten Tarif. Der Preis liegt bei drei Dollar pro Million Eingabe-Token und fünfzehn Dollar pro Million Ausgabe-Token. Wiederverwendete Eingaben aus dem Zwischenspeicher kosten nur fünfzehn Cent. Eine Einschränkung für Europa nennt Google in der Ankündigung nicht, ausdrücklich bestätigt wird Deutschland aber auch nicht.

LENA: Google nennt sicher auch Testergebnisse.

TOM: Viele. Ein Wert ist für dich interessant. Google gibt an, dass Gemini vier Neon im AutomationBench von Zapier sechsundfünfzig Komma drei Prozent erreicht. Dieser Test prüft, wie gut ein Modell Automatisierungsaufgaben über Zapier erledigt. Das sind Angaben von Google selbst, keine unabhängige Messung. Und der Wert heißt auch, dass gut vierzig Prozent der Aufgaben nicht gelingen.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du für Kunden mit Google Workspace arbeitest, ist Gemini vier Neon jetzt eine ernsthafte Option für längere Analysen, etwa große Exportdateien oder lange Mailverläufe. Der Preis liegt in der Größenordnung der großen Modelle von Anthropic und OpenAI, also kein Schnäppchen. Ein fairer Test wäre: dieselbe Aufgabe, zum Beispiel eine Fehleranalyse für einen Produktfeed, einmal mit Claude und einmal mit Gemini, und dann vergleichen. Die Zahl zeigt auch: Automatisierungen mit KI brauchen weiter deine Kontrolle.

LENA: Bleibt OpenAI. Was ist dort neu?

TOM: Seit Montag, dem dreiundzwanzigsten November, gibt es im Chat-Bereich von ChatGPT ein neues Standardmodell. Das ist eine für Gespräche abgestimmte Fassung von GPT sechs Punkt zwei Sol. Sie wird laut OpenAI weltweit für Plus, Pro, Business und Enterprise verteilt. Bei Enterprise entscheidet der Administrator. Für den kostenlosen Tarif nennen die Berichte nichts.

LENA: Was soll besser sein?

TOM: Laut OpenAIs eigenen Tests vor allem zwei Dinge. Das Modell versteht Bilder genauer, in einem internen Test steigt der Wert von gut siebenundvierzig auf knapp zweiundsiebzig Prozent. Und es hält sich besser an schwierige Anweisungen, dort geht es von zweiundsechzig auf achtundsiebzig Prozent. Auch die Websuche soll genauer sein. Das gilt nur für den Chat-Bereich. Die Modelle hinter den Bereichen Arbeit und Codex bleiben gleich.

LENA: Du hattest noch etwas zu den Dots, den dauerhaft laufenden Agenten von OpenAI.

TOM: Ja, aber das ist noch nicht sauber bestätigt. Die Seite TestingCatalog berichtet, dass die Dots jetzt auch in der EU starten. Europa war beim ersten Start ausgenommen. Welche Tarife und welche Länder genau, steht dort nicht, und die offizielle Hilfeseite von OpenAI konnten wir nicht prüfen. Nimm das also als Hinweis, nicht als Tatsache.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du ChatGPT parallel zu Claude nutzt, etwa um Produktbilder zu prüfen oder Screenshots aus einem Tracking-Werkzeug auswerten zu lassen, lohnt ein neuer Versuch. Genau dafür ist die bessere Bildauswertung gedacht. Und die bessere Treue zu Anweisungen hilft bei Texten mit festen Vorgaben, etwa Produktbeschreibungen mit genauer Zeichenzahl. Bei den Dots würde ich abwarten, bis OpenAI die Verfügbarkeit in Deutschland selbst bestätigt.

LENA: Gab es sonst noch etwas, das du kennen solltest?

TOM: Kurz zwei Dinge von Anthropic. Am dreiundzwanzigsten November kam Claude Ship als Testversion. Das sind Agenten, die Code-Änderungen auf GitHub prüfen und freigeben. Das gibt es nur für Team und Enterprise, und es wird nach Verbrauch abgerechnet. Für dich ist das eher etwas, falls ein Kunde ein eigenes Entwicklerteam hat. Und für Entwickler: Das ältere Modell Claude Opus vier Punkt fünf wird am zweiundzwanzigsten Januar in der Schnittstelle abgeschaltet. Falls irgendwo noch eine alte Automatisierung dieses Modell fest eingestellt hat, ist jetzt ein guter Zeitpunkt, sie umzustellen.

LENA: Dann der Ausblick. Worauf solltest du achten?

TOM: Drei Termine. Bis zum zweiundzwanzigsten Januar die Umstellung weg von Opus vier Punkt fünf, falls nötig. Bis zum ersten Februar die Frage, wie deine Agenten auf Google Workspace zugreifen. Und ab dem ersten April die Abrechnung der Workspace-Stufe für hohe Last. Dazu die Frage, wann Zapier die neuen MCP-Funktionen von Anthropic unterstützt.

LENA: Das waren Klöbels KI-News. Bis Donnerstag.

TOM: Bis Donnerstag.
