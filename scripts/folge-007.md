# Klöbels KI-Podcast – Folge 7: Mit Dateien arbeiten

MIRA: Guten Morgen und willkommen zur siebten Folge von Klöbels KI-Podcast. Ich bin Mira.

JAN: Und ich bin Jan. Hallo.

MIRA: Letztes Mal ging es ums Gedächtnis, also darum, was die KI sich über dich merkt. Heute wird es handfester. Wir reden über Dateien. PDFs, Tabellen, Screenshots, Fotos. Alles, was du nicht abtippst, sondern einfach hochlädst.

JAN: Und am Ende der letzten Folge hatten wir gesagt: Leg dir eine Datei zurecht, mit der du sowieso arbeiten musst. Wenn du das gemacht hast, perfekt. Wenn nicht, denk beim Zuhören einfach an den letzten Export, den du dir angeschaut hast.

MIRA: Bei mir wäre das ein Produktdaten-Feed. Ein paar tausend Zeilen, Titel, Preise, Verfügbarkeit, Kategorien. Den hab ich letzte Woche einfach in den Chat gezogen und gefragt, ob was auffällt.

JAN: Und, ist was aufgefallen?

MIRA: Ja, die KI hat mir drei Probleme genannt. Zwei davon stimmten. Das dritte war Quatsch. Und genau da will ich heute ansetzen. Warum stimmt das eine und das andere nicht?

JAN: Die Antwort fängt damit an, dass "Datei hochladen" je nach Dateityp etwas völlig anderes bedeutet. Für dich sieht es immer gleich aus. Du ziehst etwas in das Fenster, fertig. Aber im Hintergrund passiert bei einer Tabelle etwas anderes als bei einem PDF oder bei einem Foto.

MIRA: Dann gehen wir das der Reihe nach durch. Was passiert mit einem PDF?

JAN: Bei einem normalen PDF, also einem, das am Computer erstellt wurde, steckt der Text als Text drin. Den kann die KI direkt lesen. Das landet sozusagen als Abschrift auf dem Schreibtisch, den kennst du aus der ersten Folge. Viele Assistenten schauen sich inzwischen zusätzlich die Seiten als Bild an. Dann sehen sie auch Diagramme, Tabellen und das Layout.

MIRA: Und wenn das PDF ein eingescannter Brief ist?

JAN: Dann gibt es keinen Textanteil. Dann ist jede Seite nur ein Foto von Papier. Die KI muss den Text aus dem Bild erkennen. Das klappt bei sauberen Scans meistens gut. Bei schiefen Seiten, Handschrift oder blassen Kopien wird es fehleranfälliger. Und das Tückische ist: Die KI sagt dir nicht immer, dass sie an einer Stelle geraten hat.

MIRA: Woran merke ich das?

JAN: Ein einfacher Trick. Lass dir eine Stelle wörtlich zitieren, die du selbst im Original prüfen kannst. Zum Beispiel: Zitiere mir den ersten Satz auf Seite drei. Wenn der stimmt, hat das Lesen funktioniert. Wenn da etwas ganz anderes steht, weißt du Bescheid, bevor du dich auf die Auswertung verlässt.

MIRA: Okay, das ist schnell gemacht. Wie sieht es mit langen PDFs aus? Ich bekomme manchmal Agenturberichte mit sechzig, siebzig Seiten.

JAN: Da gibt es zwei Grenzen. Erstens hat jeder Assistent eine Obergrenze für Dateigröße und Seitenzahl. Die ist je nach Anbieter und Tarif unterschiedlich, deshalb nenne ich keine Zahl. Zweitens, und das ist wichtiger: Selbst wenn alles reinpasst, ist der Schreibtisch dann sehr voll. Die KI hat alles vor sich, aber sie gewichtet nicht alles gleich gut.

MIRA: Das heißt, bei einem langen Bericht lieber gezielt fragen?

JAN: Genau. Statt: Fass mir das zusammen, lieber: Such mir alle Stellen, an denen es um die Kosten pro Bestellung geht, und nenn mir jeweils die Seitenzahl. Mit der Seitenzahl kannst du nachschauen. Und die KI muss sich auf eine Sache konzentrieren statt auf siebzig Seiten gleichzeitig.

MIRA: Das gefällt mir, weil ich dann auch direkt eine Spur ins Original habe.

JAN: Und noch ein Tipp für Berichte: Wenn du nur fünf Seiten brauchst, schick nur die fünf Seiten. Das ist keine Faulheit, das ist Schreibtisch aufräumen.

MIRA: Kommen wir zu meinem Feed. Tabellen. Was passiert da?

JAN: Da wird es spannend. Es gibt im Grunde zwei Wege, wie eine KI mit einer Tabelle umgeht. Weg eins: Sie liest die Tabelle als Text. Zeile für Zeile, wie einen langen Brief. Weg zwei: Sie schreibt im Hintergrund ein kleines Programm, meistens in Python, lässt das über die Tabelle laufen und bekommt echte Rechenergebnisse zurück.

MIRA: Und welcher Weg ist besser?

JAN: Zum Rechnen ganz klar der zweite. Ein Sprachmodell rechnet nicht wie ein Taschenrechner. Es sagt das wahrscheinlichste nächste Wort voraus. Das kennst du aus Folge eins. Wenn es also eine Summe über dreitausend Zeilen "im Kopf" bildet, kommt etwas Plausibles raus. Aber plausibel ist nicht richtig.

MIRA: Und das Programm rechnet dann wirklich?

JAN: Das Programm rechnet wirklich, ja. Das ist dann keine Schätzung mehr, sondern eine Berechnung. Claude, ChatGPT und Gemini können das alle, in unterschiedlicher Form und je nach Einstellung. Oft siehst du es daran, dass irgendwo Code angezeigt wird oder ein Hinweis, dass gerade analysiert wird.

MIRA: Jetzt verstehe ich mein falsches drittes Problem. Die KI hatte behauptet, bei rund zweihundert Produkten fehle der Preis. Ich hab nachgeschaut, das waren in Wirklichkeit zwölf.

JAN: Da würde ich wetten, dass sie nicht gezählt, sondern geschätzt hat. Oder sie hat nur einen Teil der Datei angeschaut und hochgerechnet. Das passiert, wenn die Datei groß ist und keine echte Analyse läuft.

MIRA: Wie verhindere ich das?

JAN: Indem du es verlangst. Ich schreibe dann zum Beispiel: Bitte werte die Datei mit Code aus, nicht durch Lesen. Nenn mir die genaue Anzahl der Zeilen, in denen das Preisfeld leer ist, und zeig mir fünf Beispiele mit ihrer Artikelnummer.

MIRA: Die fünf Beispiele sind der Trick, oder?

JAN: Das ist der Trick. Mit den Artikelnummern kannst du in deinem Original nachschauen. Wenn die fünf stimmen, ist die Zählung sehr wahrscheinlich auch richtig. Wenn die fünf Artikel einen Preis haben, ist irgendwas schiefgelaufen.

MIRA: Gibt es typische Stolperfallen bei Tabellen?

JAN: Ein paar Klassiker. Der größte, gerade bei deutschen Exporten: das Komma. Wir schreiben neunzehn Komma neunundneunzig. Viele Programme erwarten einen Punkt. Wenn die KI das falsch einliest, wird aus neunzehn Euro neunundneunzig plötzlich eintausendneunhundertneunundneunzig. Oder der Wert wird gar nicht als Zahl erkannt.

MIRA: Das ist bei Feeds ein echtes Thema. Da hab ich schon Exporte gesehen, in denen beides gemischt war.

JAN: Dann sag es gleich am Anfang dazu. Zum Beispiel: Die Datei ist mit Semikolon getrennt, Dezimaltrennzeichen ist das Komma, Datumsformat ist Tag Punkt Monat Punkt Jahr. Das sind zehn Sekunden Arbeit.

MIRA: Und weitere Klassiker?

JAN: Mehrere Blätter in einer Excel-Datei. Die KI schaut sich vielleicht nur das erste an, und deine Daten stehen auf dem dritten. Dann zusammengeführte Zellen, Zwischensummen mitten in der Tabelle, Überschriften über zwei Zeilen. Alles, was für Menschen hübsch aussieht, ist für eine Auswertung schwierig.

MIRA: Also lieber eine nackte Tabelle hochladen?

JAN: Wenn du die Wahl hast, ja. Ein schlichter Export, eine Kopfzeile, darunter nur Daten. Bei einer aufbereiteten Excel-Datei sag dazu, welches Blatt und welcher Bereich gemeint ist.

MIRA: Ich hab mir angewöhnt, bei Tabellen immer erst eine Frage vorneweg zu stellen. Bevor ich irgendwas auswerten lasse, frage ich: Beschreib mir, was du in der Datei siehst. Wie viele Zeilen, welche Spalten, welcher Datentyp in jeder Spalte.

JAN: Das ist der beste Einzeltipp der Folge, finde ich. Nenn ich mal den Strukturcheck. Du siehst sofort, ob die KI die Datei so verstanden hat wie du. Wenn sie sagt, die Preisspalte enthält Text, weißt du, dass das Komma-Problem zugeschlagen hat. Wenn sie dreitausend Zeilen nennt und du weißt, es sind fünftausend, fehlt etwas.

MIRA: Und erst dann die eigentliche Frage.

JAN: Erst dann. Und dann am besten mit Bedeutung. Die KI weiß ja nicht, was deine Spalten heißen. Eine Spalte, die "Status" heißt, kann alles Mögliche sein. Sag dazu: Status zwei bedeutet, das Produkt ist ausverkauft. Dann kann sie damit arbeiten.

MIRA: Das ist eigentlich dasselbe wie bei einem guten Prompt, oder? Kontext mitgeben.

JAN: Genau dasselbe. Die Datei ersetzt nicht den Kontext. Sie ist nur das Material. Was du damit willst, wofür das Ergebnis ist, wie die Spalten zu lesen sind, das musst du immer noch sagen.

MIRA: Ein Beispiel aus dem Alltag, das ich spannend finde: der Umsatzrückgang. Kunde ruft an, Umsatz im letzten Monat deutlich runter, warum. Ich hab einen Export aus der Webanalyse, nach Kanälen und Tagen.

JAN: Gutes Beispiel. Da würde ich in drei Schritten vorgehen. Schritt eins: Strukturcheck, wie eben. Schritt zwei: Die KI soll rein beschreibend arbeiten. Welche Kanäle haben sich wie verändert, im Vergleich zum Vormonat, in absoluten Zahlen und in Prozent. Ohne Interpretation.

MIRA: Warum ohne?

JAN: Weil die KI sonst sehr schnell eine schöne Geschichte erzählt. "Der Rückgang liegt vermutlich an der Saison." Klingt gut, aber vielleicht steht in den Daten etwas ganz anderes. Erst die Zahlen, dann die Deutung. Und Schritt drei ist dann die Deutung, mit der Bitte, jede Vermutung als Vermutung zu kennzeichnen und zu sagen, welche Daten man bräuchte, um sie zu prüfen.

MIRA: Das gefällt mir. Weil ich dem Kunden am Ende ja nicht sagen will: Die KI meint, es liegt am Wetter.

JAN: Nein. Und oft ist die beste Antwort in Schritt drei: Mit diesen Daten lässt sich das nicht klären, schau dir zusätzlich noch das und das an. Das ist eine hilfreiche Antwort, auch wenn sie unbefriedigend klingt.

MIRA: Wechseln wir zu Bildern und Screenshots. Das nutze ich ehrlich gesagt am häufigsten. Ein Screenshot aus einem Werbekonto, und dann die Frage: Was siehst du da?

JAN: Da passiert wieder etwas anderes. Bei einem Bild gibt es keinen Text, den man auslesen kann. Die KI schaut sich das Bild an, ähnlich wie bei dem eingescannten PDF. Sie erkennt Text, Zahlen, Diagramme, Farben, Anordnungen. Das funktioniert inzwischen erstaunlich gut.

MIRA: Aber?

JAN: Aber es gibt drei typische Schwächen. Erstens: kleine Schrift. Wenn du einen ganzen Bildschirm mit einer Tabelle in winziger Schrift fotografierst, werden Zahlen verwechselt. Eine Acht wird zur Drei, ein Komma verschwindet. Zweitens: Diagramme ohne Beschriftung. Die KI kann sagen, dass eine Linie steigt. Aber wenn sie den genauen Wert an einem Tag ablesen soll, schätzt sie anhand der Achse.

MIRA: Und drittens?

JAN: Drittens: Was nicht auf dem Bild ist, existiert nicht. Wenn dein Screenshot oben die Datumsauswahl abschneidet, weiß die KI nicht, welcher Zeitraum das ist. Sie wird vielleicht trotzdem einen annehmen.

MIRA: Das ist mir tatsächlich schon passiert. Ich hatte einen Ausschnitt mit Kampagnenzahlen, und die KI hat von "diesem Monat" geredet. Es waren aber die letzten sieben Tage.

JAN: Typisch. Deshalb: Schneide den Screenshot so zu, dass das Wichtige groß drauf ist. Und alles, was nicht drauf ist, schreibst du dazu. Zeitraum, Währung, welcher Kanal, was dich interessiert.

MIRA: Gibt es Fälle, in denen ein Screenshot besser ist als ein Export?

JAN: Ja. Wenn es um das Aussehen geht. Eine Produktseite, ein Newsletter-Entwurf, ein Formular, eine Fehlermeldung. Da willst du ja gerade, dass die KI sieht, was ein Mensch sieht. Ich schicke zum Beispiel einen Screenshot einer Produktseite und frage: Was würde dich als Käufer hier stutzig machen?

MIRA: Und bei Fehlermeldungen ist das auch praktisch. Bei einer Tracking-Einrichtung im Onlineshop bekomme ich oft eine kryptische Meldung in irgendeiner Konsole.

JAN: Da geht beides. Screenshot ist bequem. Aber wenn du den Text der Fehlermeldung kopieren kannst, ist Text besser. Dann gibt es keine Lesefehler. Faustregel: Text, wenn es um Inhalt geht. Bild, wenn es um Aussehen geht. Und Export, wenn gerechnet werden soll.

MIRA: Die merke ich mir. Text für Inhalt, Bild für Aussehen, Export zum Rechnen.

JAN: Und ein privates Beispiel, weil ich das neulich gemacht habe: Ich hatte die Bedienungsanleitung für eine Kamera als PDF, zweihundert Seiten, und ein Foto von dem Display mit einer Meldung, die ich nicht verstanden habe. Beides hochgeladen und gefragt: Was bedeutet diese Meldung laut Anleitung, und auf welcher Seite steht das?

MIRA: Und es hat geklappt?

JAN: Hat geklappt. Mit Seitenzahl. Ich hab nachgeschaut, stimmte. Das ist eine Kombination, die ich sehr mag. Ein Bild vom Problem und das Dokument mit der Lösung. Die KI verbindet die beiden.

MIRA: Jetzt muss ich eine Frage stellen, die bei Kundendateien natürlich sofort kommt. Darf ich die überhaupt hochladen?

JAN: Wichtige Frage, und wir machen dazu eine eigene Folge über Datenschutz und Kundendaten. Deshalb heute nur die Kurzfassung. Bevor du eine Datei hochlädst, frag dich: Stehen da personenbezogene Daten drin? Kundennamen, Mailadressen, Bestellungen mit Adressen?

MIRA: Bei einem Produkt-Feed eher nicht.

JAN: Bei einem Feed meistens nicht, da geht es um Produkte. Bei einem Bestellexport sehr wohl. Und dann gilt: Nimm die Spalten raus, die du für die Frage nicht brauchst. Wenn du wissen willst, welche Produkte sich wie verkauft haben, brauchst du keine Namen und Adressen. Das ist sowieso gute Praxis, weil der Schreibtisch dann auch aufgeräumter ist.

MIRA: Zwei Fliegen mit einer Klappe.

JAN: Genau. Und wie die Regeln bei deinem Assistenten und deinem Tarif aussehen, also was gespeichert wird und ob damit trainiert wird, das schauen wir uns in der Datenschutz-Folge genauer an.

MIRA: Noch ein Punkt, über den ich gestolpert bin: Wie lange ist eine Datei eigentlich "da"? Wenn ich am nächsten Tag im selben Chat weiterfrage, weiß die KI noch, was drinstand?

JAN: Innerhalb desselben Chats liegt die Datei normalerweise weiter auf dem Schreibtisch. Aber bei sehr langen Chats kann es passieren, dass ältere Teile in den Hintergrund rücken oder gekürzt werden. In einem neuen Chat ist die Datei weg, außer du hast sie in einem Projekt abgelegt.

MIRA: Das war ja Thema in Folge fünf. Dateien, die du immer wieder brauchst, gehören ins Projekt.

JAN: Richtig. Die Markenrichtlinien eines Kunden, eine Vorlage für Berichte, die Spaltenbeschreibung eures Standard-Exports. Das legst du einmal ins Projekt. Die wechselnden Daten, also den Export von dieser Woche, lädst du im Chat hoch.

MIRA: Und wenn ich eine Datei ändere, zum Beispiel einen neuen Export ziehe?

JAN: Dann ist es eine neue Datei. Die KI sieht nicht automatisch die neue Version. Lade sie neu hoch und sag dazu: Das ist die aktualisierte Fassung, bitte ignoriere die alte. Sonst vermischt sie im schlimmsten Fall beide.

MIRA: Okay. Und jetzt die Gegenrichtung. Kann ich mir von der KI auch Dateien zurückgeben lassen?

JAN: Ja, und das wird oft vergessen. Viele Assistenten können dir eine bereinigte Tabelle zum Herunterladen erzeugen. Zum Beispiel: Nimm meinen Feed, korrigiere die Dezimaltrennzeichen, markiere alle Zeilen ohne Preis in einer neuen Spalte und gib mir die Datei zurück.

MIRA: Und das muss ich dann genauso prüfen wie eine Auswertung.

JAN: Natürlich. Der Strukturcheck funktioniert auch rückwärts. Öffne die neue Datei, vergleiche die Zeilenzahl mit dem Original, schau dir ein paar Stichproben an. Wenn aus fünftausend Zeilen plötzlich viertausendneunhundert geworden sind, will ich wissen, wo die hundert hin sind.

MIRA: Gut. Ich fasse mal zusammen, was ich mir für unterwegs merke.

JAN: Gern.

MIRA: Erstens: Datei ist nicht gleich Datei. Ein PDF wird gelesen, ein Bild wird angeschaut, eine Tabelle sollte berechnet werden. Zweitens: Bei Tabellen erst den Strukturcheck. Beschreib mir, was du siehst, dann die eigentliche Frage. Drittens: Zum Rechnen ausdrücklich Code verlangen und dir Beispiele mit Artikelnummer geben lassen, die du im Original nachprüfen kannst.

JAN: Und viertens?

MIRA: Viertens: Was nicht in der Datei steht, schreibst du dazu. Zeitraum, Trennzeichen, was die Spalten bedeuten. Und fünftens: Text für Inhalt, Bild für Aussehen, Export zum Rechnen.

JAN: Da würde ich nichts weglassen. Vielleicht noch einen Satz zum Mitnehmen: Die KI ist bei Dateien ein schneller Leser, aber kein Buchhalter. Wenn eine Zahl wichtig ist, prüfst du sie an einer Stelle selbst.

MIRA: Kommen wir zur Übung für heute.

JAN: Die Übung dauert etwa zehn Minuten. Nimm eine echte Tabelle aus deinem Alltag, einen Feed, einen Export aus der Webanalyse oder aus einem Werbekonto. Wenn Kundendaten mit Namen oder Adressen drin sind, lösch diese Spalten vorher.

MIRA: Und dann?

JAN: Schritt eins: Lade sie hoch und frag nur nach der Struktur. Wie viele Zeilen, welche Spalten, welcher Datentyp. Vergleiche die Zeilenzahl mit dem, was du im Original siehst.

MIRA: Schritt zwei?

JAN: Schritt zwei: Stell eine Zählfrage, deren Antwort du selbst schnell prüfen kannst. Zum Beispiel, wie viele Zeilen in einer bestimmten Spalte leer sind. Einmal ohne weiteren Hinweis. Dann im selben Chat noch einmal mit dem Satz: Bitte mit Code auswerten und fünf Beispiele mit Kennung nennen.

MIRA: Und dann vergleichen, ob beide Antworten gleich sind.

JAN: Genau. Und eine davon im Original prüfen. Schritt drei, wenn du noch Zeit hast: Mach einen Screenshot von derselben Ansicht und stell dieselbe Frage zum Bild. Dann hörst du ziemlich deutlich, wo der Unterschied zwischen Anschauen und Rechnen liegt.

MIRA: Das klingt machbar. Und wer möchte, schreibt sich danach die Spaltenbeschreibung seines Standard-Exports einmal sauber auf und legt sie ins passende Projekt.

JAN: Gute Ergänzung. Das spart dir bei jedem künftigen Export die Erklärung.

MIRA: Damit kommen wir zum Ausblick. In der nächsten Folge geht es um Recherche mit KI. Also Websuche, Quellen prüfen und ausführliche Recherche-Aufträge, bei denen die KI länger selbstständig sucht.

JAN: Und da passt die heutige Folge gut davor. Denn auch bei Webseiten gilt: Die KI liest schnell, aber du willst wissen, woher eine Aussage kommt.

MIRA: Danke fürs Zuhören und viel Spaß mit deiner Tabelle.

JAN: Bis Donnerstag beim Klöbels KI-Podcast.
