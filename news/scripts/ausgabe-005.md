# Klöbels KI-News – Ausgabe 5 vom 30.10.2026

LENA: Du öffnest eine Seite im eingebauten Browser deines KI-Assistenten. Und diese Seite liest im Hintergrund Dateien von deiner Festplatte.

TOM: Genau das haben Sicherheitsforscher bei fünf Programmierwerkzeugen gezeigt. Darunter Claude Desktop, Codex von OpenAI und Visual Studio Code. Bei zwei davon ist die Lücke laut den Forschern noch offen.

LENA: Außerdem: Google stellt Gemini vier Carbon vor, der ChatGPT-Agent Dot soll bald nach Europa kommen, und Google baut die Werbung in der KI-Suche aus.

TOM: Dazu neue Kostenberichte für Claude Enterprise und ein offenes Billionen-Modell aus Frankreich.

LENA: Das ist Klöbels KI-News vom Freitag, 30. Oktober 2026. Ich bin Lena.

TOM: Und ich bin Tom. Wir schauen auf Mittwoch und Donnerstag.

LENA: Dann gleich zur Sicherheitslücke. Was genau ist passiert?

TOM: Die Sicherheitsfirma Forever Security hat am Donnerstag einen Bericht veröffentlicht. Sie nennt das Problem Embrace, abgeleitet von „embedded browser“, also eingebauter Browser. Viele KI-Assistenten für Entwickler haben inzwischen einen kleinen Browser eingebaut, damit der Agent Webseiten ansehen oder lokale Vorschauen öffnen kann. Diese Browser dürfen mehr als ein normaler Browser. Und genau da liegt das Problem.

LENA: Was konnte ein Angreifer damit anstellen?

TOM: Je nach Werkzeug unterschiedlich. Bei Cursor konnte eine präparierte Webseite dem Agenten versteckte Befehle unterschieben, und der hat dann Code auf dem Rechner ausgeführt. Bei GitHub Copilot ließ sich die Adresszeile fälschen. Da stand dann zum Beispiel github punkt com, obwohl eine Phishing-Seite geladen war. Und bei Claude Desktop, Codex und Visual Studio Code konnte eine lokale Seite Dateien lesen, die sie gar nicht sehen dürfte. Die Forscher nennen als Beispiele Zugangsschlüssel und Konfigurationsdateien mit Passwörtern.

LENA: Und wie ist der Stand bei den Updates?

TOM: Cursor hat am ersten Oktober nachgebessert, GitHub Mitte Oktober. Bei Codex von OpenAI und bei Visual Studio Code von Microsoft ist die Lücke laut Forever Security weiter offen. Microsoft hat die Meldung als ungültig eingestuft. OpenAI hat laut den Forschern gar nicht geantwortet. Bei Claude Desktop ist es unklar. Anthropic hat den ersten Hinweis im Juli abgelehnt, einen Tag später aber eine gleiche Meldung einer anderen Firma angenommen. Ob die Lücke inzwischen geschlossen ist, sagt der Bericht nicht ausdrücklich. Anthropic, OpenAI und Microsoft haben auf Nachfragen von The Register nicht reagiert.

LENA: Und was heißt das für die Praxis?

TOM: Du arbeitest täglich mit Claude, und wahrscheinlich liegen auf deinem Rechner Zugangsdaten zu Shop-Systemen, Tracking-Konten oder Feed-Tools. Drei Dinge helfen. Erstens: alle KI-Werkzeuge aktuell halten. Zweitens: im eingebauten Browser keine fremden Seiten oder HTML-Dateien öffnen, die dir jemand schickt. Drittens: Zugangsschlüssel nicht offen in Projektordnern ablegen, auf die ein Agent Zugriff hat. Das ist sowieso eine gute Regel.

LENA: Passt dazu nicht auch die Meldung über Anthropic selbst?

TOM: Ja. Die Washington Post hatte schon am Montag berichtet, The Decoder hat es am Mittwoch zusammengefasst. Ein Sicherheits-Start-up namens Cathedral ist im Rahmen von Anthropics Prämienprogramm für gemeldete Lücken in interne Systeme gelangt, und zwar mit KI-Agenten. Der Weg lief über Software von Drittanbietern, etwa für Vertrieb und Verwaltung. Anthropic bestätigt den Zugriff auf einige Vertriebs-, Personal- und IT-Systeme. Betroffen seien Kontaktdaten einzelner Kunden und Partner. Chats mit Claude seien laut Anthropic nicht betroffen gewesen.

LENA: Die Lehre daraus?

TOM: Die Schwachstelle war nicht das KI-Modell, sondern ein angebundenes Fremdprogramm. Das gilt für jede Firma. Wenn du für Kunden Zapier-Verbindungen oder Schnittstellen einrichtest, lohnt sich ab und zu ein Blick, welche alten Zugänge noch aktiv sind und was sie dürfen.

LENA: Jetzt zu Google. Was ist Gemini vier Carbon?

TOM: Ein neues Spitzenmodell von Google DeepMind, vorgestellt am Mittwoch. Nur zwei Wochen nach Gemini vier Argon. Carbon ist für lange, mehrstufige Aufgaben gebaut, etwa Software über mehrere Tage weiterentwickeln, und für die Abwehr von Cyberangriffen. Also Lücken finden und schließen.

LENA: Wie gut ist es?

TOM: Im Index von Artificial Analysis, einer unabhängigen Vergleichsplattform, liegt Carbon mit neunundfünfzig Punkten auf Platz eins. Argon kam auf fünfzig. Beim Programmieren mit Agenten liegt Carbon knapp hinter Claude Opus fünf Punkt fünf. Ein Detail ist aber wichtig: Laut den Messwerten, die The Decoder zusammengetragen hat, ist der Anteil erfundener Antworten gestiegen, von vier auf elf Prozent.

LENA: Kann man es schon nutzen?

TOM: Nein, noch nicht. Zuerst bekommen nur ausgewählte Fachleute für Cyberabwehr Zugang. Danach will Google den Kreis über ein Partnerprogramm namens Fairwind schrittweise erweitern. Für normale Entwickler, Firmen und Endkunden gibt es noch keinen Termin. Google nimmt außerdem an einem freiwilligen Vorabtest der US-Regierung teil. Als Preis nennt Google zum Start zwei Dollar pro Million Eingabe-Token und zehn Dollar pro Million Ausgabe-Token.

LENA: Und was heißt das für die Praxis?

TOM: Kurzfristig wenig, weil du nicht drankommst. Interessant ist die Richtung: Die großen Anbieter liefern sich gerade ein enges Rennen, und das drückt die Preise. Und die gestiegene Fehlerquote zeigt, dass ein besserer Platz in einer Rangliste nicht heißt, dass ein Modell bei Fakten zuverlässiger ist. Für Produkttexte oder Kundenantworten bleibt die Regel: Zahlen und Fakten gegenprüfen.

LENA: Dann zu OpenAI. Was gibt es Neues bei Dot?

TOM: Zur Erinnerung: Dot ist der proaktive Agent in ChatGPT. Du gibst ihm Aufgaben oder Dinge, die er beobachten soll, und er meldet sich von selbst. Bisher ging das in der ChatGPT-App und in Slack. Seit Mittwoch kann man Dot laut 9to5Mac auch per iMessage und per RCS schreiben, also über die normale Nachrichten-App auf dem Handy. Mit Text, Fotos oder Sprachnachrichten. Eingerichtet wird das im Profil von Dot unter „Texting“. OpenAI sagt, Dot sieht dabei deine anderen Unterhaltungen nicht.

LENA: Und in Europa?

TOM: Da kommt die eigentliche Neuigkeit. Auf dem DevDay von OpenAI in Berlin hat Romain Huet, der bei OpenAI für die Entwickler zuständig ist, gesagt: Dot soll in wenigen Wochen breiter in Europa verfügbar sein. Grundlage seien Gespräche mit den Aufsichtsbehörden. Bisher sind persönliche Pro-Konten in der EU, im übrigen Wirtschaftsraum, in der Schweiz und in Großbritannien ausgeschlossen. Einige Unternehmenskonten haben schon Zugriff. So berichtet es The Decoder.

LENA: Und was heißt das für die Praxis?

TOM: Wenn Dot kommt, hast du einen zweiten proaktiven Agenten neben dem, was du mit Claude und Zapier schon machst. Denkbar ist zum Beispiel: „Sag mir Bescheid, wenn sich bei diesem Wettbewerber die Preise ändern“, und die Antwort kommt als Nachricht aufs Handy. Bevor du so etwas für Kunden einsetzt, würde ich abwarten, welche Datenschutzbedingungen OpenAI für Europa festlegt. Genau darüber wird ja offenbar verhandelt.

LENA: Bleiben wir bei Google, aber beim Geld. Was hat Google zur KI-Suche gesagt?

TOM: Am Mittwoch kamen die Quartalszahlen. Der Umsatz mit der Suche und verwandter Werbung stieg um zwölf Prozent auf gut dreiundsechzig Milliarden Dollar. Analysten hatten mit etwa fünfzehn Prozent gerechnet. Die Aktie fiel deutlich. Laut Google-Manager Philipp Schindler bringt der KI-Modus pro Anfrage bisher weniger Geld als die klassische Suche. Deshalb will Google die Werbung in der KI-Suche ausbauen, in den USA und international. Laut TechCrunch sind für die USA außerdem neue Anzeigenformate für längere Dialoge geplant.

LENA: Gibt es schon Länder oder Termine?

TOM: Nein. Google hat weder Länder noch Formate noch Zeitpunkte genannt. Ob und wann Deutschland dabei ist, ist offen.

LENA: Und was heißt das für die Praxis?

TOM: Das ist dein Kerngeschäft. Wenn mehr Menschen im KI-Modus suchen, wandert ein Teil der Sichtbarkeit von den klassischen Anzeigen und Treffern in die KI-Antworten. Für deine Kunden heißt das: Shopping-Feeds sauber halten, weil Google daraus auch in der KI-Suche schöpft. Und in den Auswertungen genau hinschauen, ob sich Klickraten verändern, sobald neue Werbeformate kommen.

LENA: Und Google hatte noch etwas für App-Anbieter?

TOM: Ja, am Mittwoch beim Android-Entwicklertreffen. Google startet die Vorschau einer Plattform namens Connected Apps. Anbieter können ihre App oder ihren Dienst über das Model Context Protocol an Gemini anbinden, also über den offenen Standard, über den auch Claude mit anderen Programmen spricht. Laut Google sind schon über fünfzig Partner in der Gemini-App aktiv, darunter Adobe. In den kommenden Wochen soll die Google-Suche folgen. Für Shops mit eigener App oder eigenem Dienst entsteht da ein neuer Weg, direkt in Gemini aufzutauchen.

LENA: Jetzt zu Anthropic. Was ist neu bei Claude Enterprise?

TOM: Seit Mittwoch sind drei Funktionen allgemein verfügbar. Erstens Smart Reports, also Auswertungsberichte. Ein Admin wählt ein Team und einen Zeitraum von bis zu achtundzwanzig Tagen. Claude liest dann eine Stichprobe der Unterhaltungen und berichtet, wofür das Team Claude genutzt hat, was dabei herauskam, was eine Sitzung gekostet hat und wo es hakt. Das umfasst Chat, Claude Code und Cowork. Pro Organisation gibt es zehn Berichte im Monat kostenlos. Die Funktion ist zunächst abgeschaltet und muss vom Inhaber eingeschaltet werden. Laut Anthropic ist sie nicht dafür gedacht, einzelne Mitarbeiter zu bewerten.

LENA: Und die anderen beiden?

TOM: Zweitens kurze Umfragen, die als kleine Karte im Chat erscheinen. Drittens gemeinsame Budgets für Gruppen. Ein Team bekommt einen monatlichen Topf, zusätzlich zur Grenze jedes Einzelnen. Wer zuerst an eine Grenze stößt, wird gestoppt. Das geht in Enterprise-Tarifen mit Abrechnung nach Verbrauch oder mit Nutzungsguthaben.

LENA: Und was heißt das für die Praxis?

TOM: Für dich selbst eher nicht, das ist für größere Organisationen. Aber wenn du Kunden bei der Einführung von Claude berätst, ist das ein gutes Argument. Die häufigste Frage von Geschäftsführern ist: Was bringt uns das eigentlich? Mit diesen Berichten lässt sich das zumindest grob belegen. Anthropic sagt selbst, dass die Zahlen wegen der Stichprobe nur eine Richtung anzeigen.

LENA: Gab es bei Anthropic noch mehr?

TOM: Kurz: Claude for Legal hat vorgefertigte Vorlagen für Rechtsabteilungen bekommen, etwa zum Abgleich von Verträgen mit internen Vorgaben. Das richtet sich an Enterprise-Kunden und ist für dich eher eine Randnotiz.

LENA: Zum Schluss nach Frankreich. Was hat Mistral veröffentlicht?

TOM: Am Donnerstag hat Mistral die Gewichte von Mistral Large vier freigegeben, also das komplette Modell zum Herunterladen. Es war seit Anfang Oktober als Vorschau verfügbar. Das Modell hat rund eine Billion Parameter, aktiv sind pro Rechenschritt etwa neunundvierzig Milliarden. Mistral stellt es auf Hugging Face bereit und bietet es über die eigene Schnittstelle an. Den Schwerpunkt legt Mistral auf Cyberabwehr und Programmieren mit Agenten. Laut Mistral liegt es dort vor allen anderen offenen Modellen. Das ist allerdings die Angabe des Herstellers.

LENA: Offen heißt aber nicht frei für alles, oder?

TOM: Richtig. Die Lizenz ist eine abgewandelte MIT-Lizenz. Wer das Modell als bezahlten Dienst für Dritte anbieten will, braucht laut einem Bericht von IT Munch eine eigene Lizenz von Mistral. Und für den Betrieb braucht man sehr viel Rechenleistung. Das läuft nicht auf einem Laptop.

LENA: Und was heißt das für die Praxis?

TOM: Für Kunden, die Wert darauf legen, dass Daten in Europa bleiben, wird Mistral interessanter. Ein großes Modell eines europäischen Anbieters, das man notfalls auch auf eigenen Servern betreiben kann. Realistisch nutzt du es eher über die Schnittstelle von Mistral, zum Beispiel für Automatisierungen mit sensiblen Kundendaten.

LENA: Worauf sollte man in den nächsten Tagen achten?

TOM: Auf drei Dinge. Ob Anthropic, OpenAI oder Microsoft sich zu den Lücken in den eingebauten Browsern äußern und Updates liefern. Ob Dot tatsächlich in den nächsten Wochen in Deutschland ankommt. Und ob Google die Connected Apps wie angekündigt in die Suche bringt.

LENA: Das waren Klöbels KI-News. Bis Montag.
