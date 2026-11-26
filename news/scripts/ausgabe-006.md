# Klöbels KI-News – Ausgabe 6 vom 26.11.2026

TOM: Zweitausendachtzig neue Internetadressen. So viele hat OpenAI in dieser Woche still in eine Liste geschrieben.

LENA: Eine Liste, die kaum jemand liest. Außer die Leute, die Onlineshops vor Bots schützen.

TOM: Und das kurz vor dem Black Friday.

LENA: Außerdem: ChatGPT legt Chat und Arbeit unter ein gemeinsames Nutzungskonto, Cloudflare macht Webseiten für KI-Agenten durchsuchbar, und Google trennt bei Gemini die Einstellungen fürs Training. Das ist Klöbels KI-News vom Donnerstag, 26. November 2026. Ich bin Lena.

TOM: Und ich bin Tom. Die letzte Ausgabe kam erst gestern, am Mittwoch. Heute geht es deshalb um das, was seitdem dazugekommen ist, und um ein paar Dinge vom Wochenanfang, die wir gestern noch nicht hatten.

LENA: Dann zu den Adressen. Was hat OpenAI da geändert?

TOM: Es geht um ChatGPT-User. So heißt der Zugriff, mit dem ChatGPT eine Webseite aufruft, wenn du im Chat danach fragst. Also nicht der Suchroboter, der im Hintergrund das Netz absucht, sondern der Besuch in dem Moment, in dem ein Mensch ChatGPT bittet, etwa ein Produkt auf einer bestimmten Seite anzuschauen. OpenAI veröffentlicht dafür eine Liste mit allen Adressbereichen, von denen diese Besuche kommen. Diese Liste ist am fünfundzwanzigsten November deutlich gewachsen.

LENA: Um wie viel?

TOM: Laut dem Fachportal PPC Land von zweihundertsiebenunddreißig auf dreihundertsiebenundsechzig Einträge. Das sind hundertdreißig neue Blöcke mit je sechzehn Adressen, zusammen zweitausendachtzig Adressen. Gestrichen wurde nichts. Insgesamt umfasst die Liste jetzt gut einundsiebzigtausend Adressen, ein Plus von etwa drei Prozent. Ein zweiter Beobachter kommt auf eine fast gleiche Zahl. Eine Ankündigung von OpenAI gab es dazu nicht, aufgefallen ist es über ein Werkzeug, das diese Liste überwacht.

LENA: Und warum gerade jetzt?

TOM: Das hat OpenAI nicht gesagt. In Kommentaren wird ein Zusammenhang mit dem Black Friday vermutet, also mit mehr Einkaufsanfragen über ChatGPT. Das ist aber eine Vermutung, keine Aussage von OpenAI.

LENA: Und was heißt das für die Praxis?

TOM: Für Shops sogar eine ganze Menge. Viele Kunden haben einen Bot-Schutz vor ihrer Seite, etwa bei Cloudflare oder in der Shop-Software. Wer ChatGPT-Besuche erlauben will, prüft sie oft genau gegen diese Adressliste. Wird die Liste im System nur von Hand oder selten aktualisiert, dann landen Anfragen von den neuen Adressen womöglich im Filter. Das Ergebnis: Jemand fragt ChatGPT nach einem Produkt, und ChatGPT kommt nicht auf die Seite. Gerade an einem Wochenende mit viel Umsatz willst du das nicht. Meine Empfehlung: Frag heute bei deinen Shop-Kunden nach, ob ihr Bot-Schutz die Liste automatisch abgleicht. Und schau in die Logs, ob Zugriffe von ChatGPT-User abgewiesen werden. Das passt auch zu deiner Tracking-Arbeit. Solche Besuche tauchen in normalen Analysewerkzeugen oft gar nicht auf.

LENA: Bleiben wir bei OpenAI. Was ist mit den Nutzungsgrenzen in ChatGPT?

TOM: OpenAI führt die Bereiche Chat und Arbeit zusammen, auf Englisch Work. Das berichtet TechCrunch am fünfundzwanzigsten November. Beide Bereiche teilen sich dann ein gemeinsames Nutzungskonto. Was du im einen Bereich verbrauchst, fehlt dir also im anderen. Eine Ausnahme gibt es: Gespräche mit dem schnellen Instant-Modell bleiben unbegrenzt und zählen nicht mit. Wenn das gemeinsame Kontingent leer ist, kannst du mit Instant weiterarbeiten.

LENA: Ab wann gilt das?

TOM: Angekündigt hatte OpenAI die Zusammenlegung schon Anfang November per Mail. Seit Dienstag läuft sie für eine kleine Gruppe von Pro-Abonnenten. Laut TechCrunch, das sich auf die Hilfeseite von OpenAI beruft, sollen die gemeinsamen Grenzen im Dezember breiter kommen. Welche Tarife genau dann betroffen sind, nennt der Bericht nicht. Konkrete Zahlen zu den Grenzen auch nicht.

LENA: Gibt es schon Kritik?

TOM: Ja. Im Forum von OpenAI und in sozialen Netzwerken fürchten Abonnenten, dass sie für den gleichen Preis weniger von den starken Denkmodellen bekommen. OpenAI sagt dazu, dass nur ein kleiner Teil der Vielnutzer früher an die Grenze stoßen dürfte. Die meisten sollen keinen Unterschied merken. Und OpenAI will weiter an der Effizienz arbeiten, damit man mehr aus dem Tarif herausholt.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du ChatGPT neben Claude nutzt, lohnt ein Blick darauf, wofür. Lange Analysen im Arbeitsbereich, etwa eine Auswertung von Kampagnendaten, kosten künftig Kontingent, das dir dann im Chat fehlt. Kurze Dinge, wie eine Formulierung für eine Kundenmail oder eine schnelle Rückfrage, kannst du bewusst mit Instant erledigen. Das schont das Konto. Für Kunden, die ChatGPT im Team-Tarif nutzen, ist das ein Thema für Dezember: Wer viel mit den Denkmodellen arbeitet, könnte öfter ausgebremst werden. Übrigens: Anthropic hat Chat und Cowork bei Claude schon im September zusammengelegt, wie TechCrunch erinnert. Die Richtung ist also bei beiden gleich.

LENA: Dann zu Cloudflare. Du hast gesagt, Webseiten werden für Agenten durchsuchbar.

TOM: Genau. Cloudflare hat am fünfundzwanzigsten November eine Funktion namens Search for Agents vorgestellt, also Suche für Agenten. Wer seine Domain bei Cloudflare hat, kann sie im Dashboard mit einem Schalter einschalten. Cloudflare legt dann einen Suchindex für die Inhalte der Seite an und stellt eine feste Suchadresse bereit. Ein KI-Agent kann diese Adresse aufrufen, einen Suchbegriff mitschicken und bekommt passende Treffer zurück. Und zwar als einfacher Text mit Fundstellen, nicht als fertige KI-Antwort.

LENA: Woher weiß der Agent, dass es so eine Suche gibt?

TOM: Cloudflare ergänzt dafür Hinweise in den Seiten selbst. Ein Agent, der die Seite besucht, findet so den Weg zur Suche. Die Funktion ist laut Changelog von Cloudflare eine Testversion und in allen Tarifen verfügbar. Abgerechnet wird nach den Preisen und Grenzen von Cloudflares Produkt AI Search. Wichtig dazu: Cloudflare hatte Anfang November angekündigt, dass die Abrechnung für AI Search am ersten Dezember beginnt.

LENA: Und was heißt das für die Praxis?

TOM: Denk an einen Shop mit tausenden Produkten. Ein Einkaufsagent, der für einen Kunden ein bestimmtes Teil sucht, muss sich bisher durch Kategorieseiten klicken oder auf die Suchmaschine hoffen. Mit so einer Suche kann er direkt fragen. Das ist für dich ein Thema an der Grenze zwischen Feed-Management und Sichtbarkeit in KI-Assistenten. Ich würde es nicht sofort bei einem großen Kunden einschalten. Aber bei einem kleineren Shop auf Cloudflare kannst du testen, was der Index findet und ob die Treffer zu den Produktdaten passen. Und behalte die Kosten im Blick, sobald die Abrechnung ab Dezember läuft. Ob die großen Agenten wie ChatGPT oder Claude diese Suche tatsächlich nutzen, ist noch offen. Das sagt Cloudflare nicht.

LENA: Jetzt zu Google. Was ist bei Gemini neu?

TOM: Es geht um die Einstellungen zu deinem Gemini-Verlauf. Dort gibt es einen neuen Abschnitt, der sinngemäß heißt: Hilf beim Training generativer KI-Modelle. Darin stehen zwei getrennte Häkchen. Eins für den Inhalt deiner Chats. Und eins für Audio, Videos aus Gemini Live und geteilte Bildschirme. Beides kannst du einzeln ein- oder ausschalten. Bisher gab es dafür im Wesentlichen nur einen Schalter für den gesamten Verlauf. Der bleibt, ebenso das automatische Löschen nach einer gewählten Zeit.

LENA: Seit wann gibt es das?

TOM: Hier muss man genau sein. Angekündigt hat Google die Änderung laut dem Technikblog Jetstream schon am achtzehnten November, also vor unserem Berichtszeitraum. Verteilt wird sie jetzt, Ende November. Jetstream hat sie am fünfundzwanzigsten beschrieben. Zu Tarifen und Ländern macht der Bericht keine Angaben. Ob die Häkchen bei dir schon zu sehen sind, findest du am schnellsten auf der Aktivitätsseite deines Google-Kontos unter Gemini.

LENA: Und was heißt das für die Praxis?

TOM: Für dich als Berater ist die Trennung nützlich. Vielleicht willst du deinen Verlauf behalten, damit du alte Chats wiederfindest, aber nicht, dass Google damit Modelle trainiert. Bisher war das schwer zu trennen. Jetzt geht es. Gerade wenn du in Gemini mal einen Kundentext oder einen Screenshot aus einem Werbekonto hochlädst, lohnt es sich, beide Häkchen bewusst zu setzen. Ein Hinweis noch: Ob die neue Einstellung auch für Workspace-Konten im Unternehmen gilt, sagt der Bericht nicht. Dort legt in der Regel der Administrator fest, was mit den Daten passiert.

LENA: Gab es bei Google Workspace noch etwas?

TOM: Zwei kleinere Dinge vom Wochenanfang, die wir gestern nicht hatten. Am dreiundzwanzigsten November hat Google bekannt gegeben, dass Apps und KI-Agenten in Google Chat jetzt Tabellen und Überschriften schicken können. Das läuft über die Programmierschnittstelle von Chat mit einfacher Textformatierung und ist ab sofort verfügbar.

LENA: Was bringt das?

TOM: Wenn du für einen Kunden eine Automatisierung baust, die Meldungen in Google Chat postet, etwa eine tägliche Übersicht über abgelehnte Produkte im Feed, dann wird die Nachricht damit deutlich lesbarer. Statt einer langen Textwurst steht da eine Tabelle mit Produkt, Fehler und Anzahl. Ob Zapier diese Formatierung schon durchreicht, solltest du an einem kleinen Test prüfen.

LENA: Und das zweite?

TOM: Die Lernkarten in Gemini Notebook. Seit dem vierundzwanzigsten November können sie Bilder aus deinen Quellen zeigen, es gibt eine Stoppuhr und auf dem Handy Erinnerungen zum Lernen. Das ist für alle Workspace-Kunden, Einzelabos und private Konten verfügbar. Für dich eher am Rand, aber praktisch, wenn du neue Werkzeuge oder Richtlinien eines Werbenetzwerks lernen willst.

LENA: Und noch ein kurzer Nachtrag zu OpenAI?

TOM: Ja, zum neuen Chat-Modell aus der letzten Ausgabe. Laut der Hilfeseite von OpenAI bekommen die Tarife Free und Go das neue GPT sechs Punkt zwei im Chat nicht. Für sie wird stattdessen GPT fünf Punkt sechs Luna zum Standardmodell. Wenn du also mit einem Kunden arbeitest, der nur den kostenlosen Tarif nutzt, sieht er andere Antworten als du im Plus-Tarif. Das erklärt manches Missverständnis, wenn zwei Leute dieselbe Frage stellen.

LENA: Dann der Ausblick. Worauf solltest du achten?

TOM: Erstens dieses Wochenende: Black Friday und Cyber Monday. Wenn deine Shop-Kunden ChatGPT-Besuche zulassen wollen, sollte die neue Adressliste bis dahin im Bot-Schutz stehen. Zweitens der erste Dezember. Ab dann rechnet Cloudflare AI Search ab, und das betrifft auch die neue Agentensuche. Drittens im Laufe des Dezembers die gemeinsamen Nutzungsgrenzen für Chat und Arbeit in ChatGPT. Und aus der letzten Ausgabe bleiben die Termine stehen: der zweiundzwanzigste Januar für das Abschalten von Claude Opus vier Punkt fünf in der Schnittstelle und der erste Februar für den neuen Zugang von Agenten zu Google Workspace.

LENA: Das waren Klöbels KI-News. Bis Montag.

TOM: Bis Montag.
