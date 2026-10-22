# Klöbels KI News – Ausgabe 1 vom 22.10.2026

TOM: Zwei Sicherheitslücken in PHP. Bewertet mit neun Punkt zwei von zehn. Betroffen ist praktisch jeder Webserver, der PHP ausliefert.

LENA: Also auch Onlineshops mit WordPress, Magento oder Shopware.

TOM: Genau. Und gefunden wurden die Lücken mit Hilfe von KI-Modellen, von OpenAI und von Google.

LENA: Außerdem heute: Anthropic startet Claude Duet, einen Agenten, der sich von selbst meldet. Walmart öffnet seinen Shop für KI-Einkaufsagenten. Und Google Cloud bietet jetzt die Modelle von OpenAI, Anthropic und Google unter einem Dach an.

LENA: Das ist Klöbels KI News vom Donnerstag, 22. Oktober 2026. Die allererste Ausgabe. Ich bin Lena.

TOM: Und ich bin Tom. Wir schauen auf die Meldungen seit Montag, also auf diese Woche bis heute.

LENA: Dann zurück zur PHP-Lücke. Was genau ist da passiert?

TOM: Am Mittwochnachmittag, dem 21. Oktober, haben die PHP-Entwickler zwei kritische Lücken veröffentlicht und gleichzeitig die Updates bereitgestellt. Die Lücken laufen unter dem Namen PHP2Shell. Vereinfacht gesagt: Ein Angreifer kann über eine präparierte Anfrage eigenen Code auf dem Server ausführen, ohne sich anzumelden. Laut Borns IT-Blog stecken die Fehler seit PHP fünf im Code. Die PHP-Entwickler gehen davon aus, dass alle gängigen Arten betroffen sind, wie PHP Webseiten ausliefert.

LENA: Und wo kommt die KI ins Spiel?

TOM: Laut OpenAI hat die Sicherheitsfirma Calif eine der Lücken mit dem Modell GPT fünf Punkt sechs Sol gefunden. Das lief über eine Initiative, die OpenAI "Patch the Planet" nennt. Unabhängig davon hat die Sicherheitsfirma Wiz beide Lücken entdeckt und gemeldet. Wiz hat dabei unter anderem Googles Gemini vier Argon eingesetzt. Laut The Decoder wurde die Behebung dann rund zwei Monate lang im Hintergrund vorbereitet, mit den PHP-Entwicklern, Cloudflare und US-Behörden.

LENA: Gibt es schon Angriffe?

TOM: Da gehen die Angaben auseinander. OpenAI schreibt, nach eigenem Wissen hätten die KI-Modelle die Lücken vor den Angreifern gefunden. Borns IT-Blog berichtet aber, dass Cloudflare bereits Angriffsversuche beobachtet hat. Und es gibt einen öffentlichen Beispiel-Angriff für eine bestimmte Serverkonfiguration. Das BSI rät, die Updates sofort einzuspielen.

LENA: Und was heißt das für die Praxis?

TOM: Für dich ist das heute die wichtigste Meldung. Du betreust Kunden im E-Commerce, und sehr viele Shops laufen auf PHP. Die abgesicherten Versionen sind PHP acht Punkt fünf Punkt zwölf, acht Punkt vier Punkt siebenundzwanzig, acht Punkt drei Punkt sechsunddreißig und acht Punkt zwei Punkt fünfunddreißig. Alles, was älter ist als PHP acht Punkt zwei, bekommt vom PHP-Projekt keine Updates mehr.

LENA: Die meisten Kunden haben ja einen Hoster.

TOM: Richtig. Dann ist der konkrete Schritt eine kurze Nachricht an den Hoster oder die Agentur: Ist das PHP-Update eingespielt, und läuft die neue Version auch wirklich? Diese zweite Frage ist wichtig. OpenAI empfiehlt ausdrücklich zu prüfen, ob die aktualisierte Software tatsächlich aktiv ist. Wer alte Shops auf PHP sieben oder acht Punkt eins betreibt, hat ein größeres Problem. Laut Borns IT-Blog bleiben dann nur Notlösungen aus der PHP-Sicherheitsmeldung oder im Zweifel, die Seite vorübergehend vom Netz zu nehmen.

LENA: Und die KI-Seite der Geschichte?

TOM: OpenAI warnt selbst: Dieselben Fähigkeiten, die solche Lücken finden, helfen auch Angreifern. Das Unternehmen rechnet in den nächsten Monaten mit weiteren Funden dieser Größenordnung. Für dich heißt das: Kürzere Abstände zwischen "Lücke bekannt" und "Update nötig". Ein fester Ablauf mit deinen Kunden, wer bei solchen Meldungen was prüft, spart dir beim nächsten Mal Zeit.

LENA: Zweite Meldung. Anthropic hat am Mittwoch Claude Duet vorgestellt. Was ist das?

TOM: Claude Duet ist eine eigene App, getrennt von der normalen Claude-App. Anthropic beschreibt es als proaktiven Agenten. Du schreibst Claude dort Nachrichten wie einem Menschen, per Text oder Sprache. Und Duet meldet sich auch von selbst, wenn etwas deine Aufmerksamkeit braucht.

LENA: Wie funktioniert das technisch?

TOM: Duet läuft auf einem eigenen Rechner in der Cloud, mit eigenem Browser. Deine Geräte können also aus sein, während Duet weiterarbeitet. Es nutzt dieselben Erinnerungen, Fähigkeiten und verbundenen Dienste wie dein normales Claude-Konto. Laut 9to5Mac arbeitet im Hintergrund Claude Opus fünf Punkt fünf. Es gibt ein tägliches Morgen-Briefing über E-Mail und Kalender. Tagsüber schaut Duet alle paar Stunden in die verbundenen Konten und meldet sich nur, wenn etwas ansteht.

LENA: Und wenn es etwas tun soll, zum Beispiel eine Mail verschicken?

TOM: Dann fragt es vorher. Vor dem Senden einer Nachricht, einer Zahlung, einer Unterschrift oder einem Löschvorgang zeigt Duet die geplante Aktion und wartet auf deine Freigabe. Manche Dinge lehnt es laut Anthropic sogar mit Freigabe ab, etwa Wertpapierhandel oder Überweisungen zwischen Konten. Zahlungen laufen über virtuelle Karten von Stripe, damit die echte Kartennummer nicht beim Händler landet.

LENA: Wer kann das nutzen?

TOM: Hier kommt der Haken für dich. Duet ist eine Forschungsvorschau. Sie startet nur in den USA, für Pro- und Max-Abos, über eine Warteliste. Team- und Enterprise-Tarife sind noch nicht dabei. Zu Deutschland oder der EU gibt es bisher keine Angabe. Es kostet nichts extra, zählt aber gegen die normalen Nutzungsgrenzen deines Abos. Auch die Hintergrundprüfungen verbrauchen Kontingent.

LENA: Und was heißt das für die Praxis?

TOM: Kurzfristig kannst du Duet in Deutschland nicht ausprobieren. Interessant ist die Richtung. Anthropic nennt als verbundene Dienste unter anderem Gmail, Slack, Stripe, Canva und Shopify. Ein Beispiel aus der Ankündigung: Duet sucht offene Rechnungen in Stripe und entwirft Zahlungserinnerungen. Das ist sehr nah an dem, was du heute schon mit geplanten Aufgaben in Claude oder mit Zapier baust.

LENA: Also abwarten?

TOM: Abwarten und vergleichen. Geplante Aufgaben in Claude gibt es bereits, und laut AInauten seit Anfang Oktober auch im Pro-Tarif. Die laufen ebenfalls in der Cloud und greifen auf verbundene Dienste zu. Der Unterschied bei Duet: Es entscheidet selbst, wann es sich meldet, und es kann einen Browser bedienen. Wenn Duet nach Europa kommt, wäre die Frage für dich: Welche Kundendaten dürfen dort überhaupt hin? Dazu gleich mehr.

LENA: Dritte Meldung, direkt aus deinem Fachgebiet. Walmart lässt KI-Einkaufsagenten in seinen Shop.

TOM: Walmart-Chef John Furner hat am 21. Oktober zwei Dinge vorgestellt. Erstens ein Agent Gateway. Das ist ein MCP-Server, also eine standardisierte Schnittstelle, über die KI-Assistenten mit einem Dienst sprechen. Zugelassene KI-Agenten können darüber das Sortiment durchsuchen und im Auftrag von Kunden einkaufen. Zweitens sogenannte Agent Profiles.

LENA: Was steckt in diesen Profilen?

TOM: Laut dem Bericht von TechCrunch, den AI Weekly zusammenfasst, bekommt jeder Agent einen eigenen Kontobereich mit Ausgabenlimit. Jeder Kauf muss einzeln freigegeben werden. Die Agenten sehen weder Zahlungsdaten noch die Kaufhistorie. Agenten, die sich nicht an die Regeln halten, werden gesperrt. Das gilt auch für Sam's Club, und man braucht kein Walmart-Plus-Abo.

LENA: Und Amazon?

TOM: Amazon blockiert laut demselben Bericht Einkaufsagenten von Drittanbietern. Die zwei größten Händler in den USA gehen also gerade in entgegengesetzte Richtungen.

LENA: Und was heißt das für die Praxis?

TOM: Für deine Arbeit mit Produktfeeds ist das ein deutliches Signal. Bisher optimierst du Feeds für Google Shopping, für Preisvergleiche, für Marktplätze. Jetzt kommt eine weitere Gruppe von Lesern dazu: KI-Agenten, die im Auftrag von Menschen Produkte suchen und vergleichen. Die brauchen vollständige, maschinenlesbare Daten. Verfügbarkeit, Varianten, Preise, Lieferzeiten. Wenn da Lücken sind, fällt ein Produkt aus der Auswahl, bevor ein Mensch es je sieht.

LENA: Das betrifft aber erst mal den US-Markt.

TOM: Ja, Walmart ist ein US-Thema. Aber die Technik dahinter, also MCP-Server für Shops, ist nicht an ein Land gebunden. Und es passt zu dem, was wir bei Claude Duet gerade gehört haben: Shopify als verbundener Dienst, Einkäufe mit Freigabe. Wenn du mit Kunden über das nächste Jahr sprichst, ist die Frage "Wie lesen KI-Agenten unseren Shop?" eine gute Frage für die Planung.

LENA: Vierte Meldung. Google Cloud hat am Mittwoch angekündigt, dass dort jetzt auch Modelle von OpenAI laufen.

TOM: Genau. Laut OpenAI kommen die großen OpenAI-Modelle und die Programmier-Werkzeuge von Codex in den Model Garden von Google Cloud. Das ist der Katalog, aus dem Firmen dort Modelle auswählen. Laut The Decoder sind es GPT sechs Astra für anspruchsvolle Aufgaben, GPT sechs Punkt eins Sol als günstigere Variante und GPT sechs Luna für den schnellen Alltag. Claude von Anthropic gibt es dort schon länger. Damit ist Google Cloud laut The Decoder der erste große Cloud-Anbieter mit Gemini, Claude und GPT auf einer Plattform.

LENA: Ab wann?

TOM: Erst einmal als private Vorschau für ausgewählte Firmenkunden, mit Anmeldeformular. Die allgemeine Verfügbarkeit soll laut OpenAI in den kommenden Wochen folgen. Später sollen die Modelle auch in Gemini für Unternehmen und in Googles Entwicklungsumgebung Antigravity auftauchen, ohne Datum. Abgerechnet wird über die normale Google-Cloud-Rechnung. Angaben zu Rechenzentren in der EU macht keine der beiden Quellen.

LENA: Und was heißt das für die Praxis?

TOM: Für dich als Einzelnutzer ändert sich wenig. Spannend wird es bei Kunden, die schon Google Cloud nutzen, etwa für BigQuery und ihre Analysen. Die können künftig Modelle verschiedener Anbieter mit einem Vertrag und einer Rechnung testen. Das senkt die Hürde, für eine Aufgabe mal GPT, mal Claude, mal Gemini zu nehmen. Ein Hinweis: Microsoft bleibt laut OpenAI der wichtigste Cloud-Partner. Wer bei Microsoft ist, muss also nicht wechseln.

LENA: Fünfte Meldung, ein Block zum Datenschutz. Da gab es diese Woche gleich mehrere Dinge.

TOM: Zuerst Meta. Laut t3n konnte man geteilte Gespräche aus Metas KI-App Muse über eine einfache Suchanfrage finden. Die Sicherheitsfirma Claroc hat rund sechstausendachthundert solcher geteilten Links gefunden. Darunter eine Notiz zu einem Vorstellungsgespräch und der komplette Urlaubskalender einer Firma. Meta hat die Teilen-Funktion vorübergehend abgeschaltet und prüft sie.

LENA: Und OpenAI?

TOM: Bei ChatGPT gibt es seit Dienstag gesperrte Chats. Laut den ChatGPT-Versionshinweisen kannst du einzelne Chats aus dem Verlauf, den angehefteten Chats und der Suche ausblenden. Geöffnet werden sie mit einer vierstelligen PIN oder mit der Entsperrung deines Geräts. Das kommt schrittweise für Free, Go, Plus und Pro, im Browser, auf dem Handy und in der neuen Desktop-App.

LENA: Schützt das vor solchen Fällen wie bei Meta?

TOM: Nein, das ist eher ein Sichtschutz, etwa wenn jemand auf deinen Bildschirm schaut. Wo deine Daten verarbeitet werden, ändert es nicht. Dazu hatte der deutsche Newsletter AInauten heute eine brauchbare Einordnung. Die Kurzfassung: In private Tarife wie ChatGPT Plus oder Claude Pro gehört nichts Sensibles, und das Training mit deinen Daten solltest du dort abschalten. Business-Tarife mit Auftragsverarbeitungsvertrag, etwa ChatGPT Business oder Claude Team, reichen laut AInauten für normale Kundendaten, die Verarbeitung läuft aber in den USA. Wer EU-Verarbeitung braucht, schaut auf europäische Anbieter wie Langdock oder Mistral.

LENA: Und was heißt das für die Praxis?

TOM: Erstens: Teilen-Links aus KI-Apps sind öffentlich gemeint, auch wenn sie sich privat anfühlen. Wenn du Kunden ein Ergebnis zeigen willst, lieber als Datei verschicken. Zweitens: Für Kundenmails und Analysen mit echten Kundendaten lohnt ein kurzer Blick, in welchem Tarif du gerade arbeitest. AInauten weist auf eine kostenlose Browser-Erweiterung des DFKI hin, also des Deutschen Forschungszentrums für Künstliche Intelligenz. Sie ersetzt Namen und Kontonummern vor dem Absenden durch Platzhalter und setzt sie in der Antwort wieder ein. Die Erweiterung ist noch in der Testphase.

LENA: Zum Schluss noch eine Kurzmeldung von Microsoft.

TOM: Laut t3n entfernt Microsoft die sogenannten Copilot-Aktionen aus dem Rechtsklick-Menü von Windows elf. Das waren Kurzbefehle, mit denen Copilot ausgewählte Dateien vergleichen oder eine Zusammenfassung in OneDrive speichern konnte. Der Rückbau beginnt frühestens im November und soll bis etwa Dezember abgeschlossen sein. Microsoft reagiert damit auf Kritik, dass Copilot zu präsent in Windows ist.

LENA: Und für die Praxis?

TOM: Wenn du diese Kurzbefehle nutzt, plane schon mal den Weg über die Copilot-App oder OneDrive direkt ein. Wer sie nie gesehen hat, bekommt sie auch nicht mehr.

LENA: Worauf sollte man in den nächsten Tagen achten?

TOM: Zwei Dinge. Erstens PHP: Hoster und Shop-Anbieter melden gerade nach und nach, ob sie die Updates eingespielt haben. Da lohnt ein Blick in die Mails und Statusseiten. Zweitens Mistral. Das französische Unternehmen hat schon Anfang Oktober sein großes Modell Mistral Large vier vorgestellt. Laut Ankündigung sollen die Modellgewichte bis Ende Oktober frei veröffentlicht werden. Dann könnte man das Modell auch auf eigenen Servern in Europa betreiben.

LENA: Das waren Klöbels KI News. Bis Freitag.
