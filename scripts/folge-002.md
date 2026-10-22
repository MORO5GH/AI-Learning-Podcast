# KI-Werkstatt – Folge 2: Der Aufbau eines richtig guten Prompts

MIRA: Guten Morgen und willkommen zurück in der KI-Werkstatt. Ich bin Mira.

JAN: Und ich bin Jan.

MIRA: Gestern ging es darum, was im Modell passiert, wenn du tippst. Das Bild, das hängen geblieben ist: Das Modell sieht nur, was auf dem Schreibtisch liegt. Heute klären wir die Frage, die direkt daraus folgt. Was genau gehört auf diesen Schreibtisch, und in welcher Ordnung?

JAN: Also der Aufbau eines richtig guten Prompts. Welche Bausteine es gibt, in welcher Reihenfolge sie Sinn ergeben, wie man einen längeren Prompt gliedert und welche Fehler man sich sparen kann.

MIRA: Und damit es nicht theoretisch bleibt, nehmen wir ein Beispiel mit durch die ganze Folge. Einen Prompt, wie ihn wahrscheinlich jeder schon mal geschrieben hat.

JAN: Nämlich?

MIRA: „Schreib eine Mail an den Kunden wegen der Verzögerung.“

JAN: Der Klassiker. Ein Satz, zehn Wörter, und man hofft das Beste.

MIRA: Was kommt dabei raus, wenn ich das so abschicke?

JAN: Eine Mail, die in jedes Unternehmen der Welt passen würde. „Sehr geehrte Damen und Herren, leider müssen wir Ihnen mitteilen, dass sich das Projekt verzögert. Wir bitten um Ihr Verständnis.“ Dazu ein paar Platzhalter in eckigen Klammern, wo der Name hin soll. Grammatisch sauber, inhaltlich leer.

MIRA: Und schuld ist nicht das Modell.

JAN: Nein. Auf dem Schreibtisch lag fast nichts. Also hat das Modell die Lücken mit dem Durchschnitt aller Verzögerungsmails gefüllt, die es je gesehen hat.

MIRA: Dann bauen wir den Prompt jetzt Stück für Stück aus. Womit fangen wir an?

JAN: Mit dem ersten Baustein, der Aufgabe und dem Ziel. Und da steckt schon eine Feinheit drin. Die Aufgabe ist „Schreib eine Mail“. Das Ziel ist die Frage, was die Mail beim Empfänger bewirken soll.

MIRA: Das ist ein Unterschied?

JAN: Ein großer. Eine Verzögerungsmail kann ganz verschiedene Ziele haben. Vielleicht willst du nur sachlich informieren. Vielleicht willst du den Kunden beruhigen, weil er schon nervös ist. Vielleicht brauchst du von ihm eine Entscheidung, zum Beispiel ob er lieber auf alles wartet oder einen Teil vorab bekommt. Je nach Ziel sieht die Mail komplett anders aus.

MIRA: Also schreibe ich dazu: „Ziel der Mail ist, dass der Kunde versteht, warum es länger dauert, und dass er mir bis Freitag sagt, ob wir mit einem Teil schon starten sollen.“

JAN: Genau so. Jetzt weiß das Modell, worauf die Mail hinauslaufen muss. Am Ende steht eine klare Frage an den Kunden, und alles davor bereitet diese Frage vor.

MIRA: Zweiter Baustein?

JAN: Kontext und Hintergrund. Also alles, was du weißt und das Modell nicht. Worum geht es in dem Projekt? Warum gibt es die Verzögerung? Wie lange? Gab es vorher schon Ärger?

MIRA: Bei mir wäre das zum Beispiel so: Wir richten für einen Onlineshop ein neues Tracking ein. Die Verzögerung kommt daher, dass die Entwickler des Shops die nötigen Zugänge erst zwei Wochen später freigeschaltet haben als vereinbart. Und der Kunde hat schon einmal nachgefragt, wann es losgeht.

JAN: Und jeder dieser Sätze ändert die Mail. Dass die Verzögerung nicht bei dir liegt, sondern bei den Entwicklern des Shops, ist heikel. Du willst das sagen, aber ohne mit dem Finger auf jemanden zu zeigen, der vielleicht beim Kunden selbst sitzt. Dass der Kunde schon nachgefragt hat, heißt: Er wartet auf diese Mail, und sie sollte nicht ausweichend klingen.

MIRA: Das alles kann sich das Modell nicht denken.

JAN: Unmöglich. Der kluge neue Kollege von gestern wüsste das auch nicht.

MIRA: Dritter Baustein: der Empfänger.

JAN: Für wen ist der Text? Das klingt banal, aber es entscheidet über Ton, Länge und Fachwortschatz. Eine Mail an den Geschäftsführer eines Shops klingt anders als eine an den Marketingleiter, der jeden Tag mit Tracking zu tun hat.

MIRA: Ich würde also schreiben: „Die Mail geht an die Leiterin des Onlinemarketings. Wir duzen uns, arbeiten seit gut einem Jahr zusammen, sie ist technisch fit, aber kein Entwickler.“

JAN: Perfekt. Mit dem letzten Halbsatz weiß das Modell, dass es Begriffe wie Zugang oder Freigabe benutzen darf, aber keine Details über Server und Schnittstellen erklären muss.

MIRA: Jetzt kommt ein Baustein, über den man im Netz ständig liest. Die Rolle. „Du bist ein erfahrener Kundenberater“ und so weiter.

JAN: Ja, und da muss ich ein bisschen Wasser in den Wein gießen.

MIRA: Bringt das nichts?

JAN: Es bringt etwas, aber weniger, als viele glauben. Eine Rolle gibt dem Modell eine Richtung. Wenn du schreibst „Du bist ein erfahrener Berater für Webanalyse“, dann greift es eher auf Fachwissen aus diesem Bereich zurück und schreibt etwas souveräner. Das ist der Effekt.

MIRA: Und wo ist das Problem?

JAN: Dass viele Leute die Rolle als Ersatz für Kontext benutzen. Sie schreiben „Du bist ein Weltklasse-Texter mit zwanzig Jahren Erfahrung“ und sonst nichts. Aber auch der beste Texter der Welt kann keine gute Mail schreiben, wenn er nicht weiß, an wen, warum und was passiert ist. Die Rolle sagt, wer schreibt. Der Kontext sagt, worüber. Ohne den Kontext ist die Rolle ein Kostüm ohne Text.

MIRA: Die Rolle ist also eher die Prise Salz als die Hauptzutat.

JAN: So kann man es sagen.

MIRA: Wann lohnt sich eine Rolle dann richtig?

JAN: Wenn sie eine Perspektive vorgibt, die du sonst nicht bekommst. Zum Beispiel: „Lies diesen Entwurf aus Sicht eines skeptischen Einkäufers, der jeden Euro zweimal umdreht, und sag mir, wo er hängen bleibt.“ Das ist eine Rolle mit klarem Auftrag. Die verändert das Ergebnis wirklich.

MIRA: Okay, das ist ein gutes Beispiel. Weiter mit den Vorgaben und Grenzen.

JAN: Das sind die Leitplanken. Was muss rein, was darf auf keinen Fall rein? Bei unserer Mail könnte das sein: Keine Schuldzuweisung an die Entwickler. Kein neues festes Datum versprechen, solange der Zugang nicht getestet ist. Dafür ein realistisches Zeitfenster nennen.

JAN: Jede Leitplanke, die du vorher nennst, spart dir eine Runde Nachbessern. Modelle sind hilfsbereit, und hilfsbereit heißt bei einer Verzögerungsmail oft: ein konkretes neues Datum nennen. Wenn du das nicht willst, musst du es sagen.

MIRA: Nächster Baustein: Beispiele. Das hatten wir gestern schon als Merksatz.

JAN: Beispiele schlagen Beschreibungen, ja. Heute nur die praktische Seite. Bei unserer Mail wäre das beste Beispiel eine echte Mail, die du dieser Kundin schon mal geschrieben hast. Dann sieht das Modell, wie du sie ansprichst, wie lang deine Mails sind, ob du mit „Viele Grüße“ oder „Beste Grüße“ aufhörst.

MIRA: Kopiert das Modell dann nicht einfach die alte Mail?

JAN: Nicht, wenn du dazuschreibst: „Hier eine frühere Mail von mir an sie. Nimm sie als Vorbild für Ton und Länge, nicht für den Inhalt.“ Mehr dazu morgen.

MIRA: Dann zum vorletzten Baustein: Format und Länge.

JAN: Wie soll das Ergebnis aussehen? Eine Mail mit Betreffzeile? Drei kurze Absätze? Höchstens hundertfünfzig Wörter? Fließtext oder Stichpunkte? Wenn du nichts sagst, entscheidet das Modell, und viele Modelle neigen zu längeren Texten mit Aufzählungen und fett gedruckten Zwischenzeilen.

MIRA: Das kenne ich. Ich will eine kurze Mail und bekomme eine halbe Präsentation.

JAN: Deshalb gehört eine Längenangabe in fast jeden Prompt, der einen Text erzeugen soll. Und ruhig konkret. „Kurz“ heißt für jeden etwas anderes. „Maximal fünf Sätze“ ist eindeutig.

MIRA: Und der letzte Baustein?

JAN: Der wird am häufigsten vergessen, obwohl er am meisten bringt. Das Erfolgskriterium. Also die Frage: Woran merkst du, dass das Ergebnis gut ist?

MIRA: Wie formuliert man so etwas?

JAN: Stell dir vor, du liest die fertige Mail. Was müsste passieren, damit du zufrieden bist? Bei unserem Beispiel vielleicht: „Die Mail ist gut, wenn die Kundin nach dem Lesen nicht das Gefühl hat, dass wir uns rausreden, und wenn sie die Frage am Ende mit einem Satz beantworten kann.“

MIRA: Das ist ja fast schon eine Prüfanleitung.

JAN: Genau das ist es. Und das Schöne: Du kannst das Modell bitten, seinen Entwurf gegen dieses Kriterium zu prüfen, bevor es ihn dir zeigt. Dann fängt es selbst Dinge ab, die du sonst hinterher korrigieren würdest.

MIRA: Ich zähle mal durch, was wir jetzt haben. Aufgabe und Ziel, Kontext, Empfänger, Rolle, Vorgaben und Grenzen, Beispiele, Format und Länge, Erfolgskriterium. Acht Bausteine. Das ist eine Menge für eine kurze Mail.

JAN: Du brauchst nicht immer alle acht. Oft reichen drei oder vier, und jeder ist nur ein Satz. Die Bausteine sind eine Checkliste im Kopf.

MIRA: Kommen wir zur Reihenfolge. Ist es egal, wo was steht?

JAN: Ja, vor allem bei längeren Prompts. Die Faustregel lautet: Material zuerst, Auftrag am Ende.

MIRA: Was heißt Material?

JAN: Alles, was das Modell lesen soll, um die Aufgabe zu erledigen. Ein langes Dokument, ein Mailverlauf, ein Vertrag, eine Tabelle mit Zahlen, ein Protokoll. Das kommt nach oben. Danach kommen Kontext und Vorgaben, und ganz am Ende steht, was genau das Modell damit tun soll, und die konkrete Frage.

MIRA: Warum so herum? Intuitiv würde ich erst sagen, was ich will, und dann das Material dranhängen.

JAN: Das machen die meisten. Aber denk an den Schreibtisch. Wenn das Modell zuerst die Aufgabe liest und dann zwanzig Seiten Material, dann ist die Aufgabe am Ende ziemlich weit weg. Wenn die Frage dagegen ganz unten steht, also direkt vor der Stelle, an der das Modell anfängt zu schreiben, ist sie frisch.

MIRA: Ein Beispiel?

JAN: Nimm einen Produktdaten-Feed, den du prüfen willst. Du kopierst ein paar hundert Zeilen hinein. Dann schreibst du darunter: „Das ist ein Auszug aus dem Feed eines Onlineshops für Gartenmöbel. Er wird an Preisvergleichsportale ausgespielt. Prüf, bei welchen Produkten Pflichtfelder fehlen oder die Preise nicht plausibel sind, und gib mir eine Liste der zehn auffälligsten Fälle mit kurzer Begründung.“

MIRA: Also erst der Stapel Papier, dann der Zettel obendrauf, auf dem steht, was ich damit will.

JAN: Genau. Bei einem kurzen Prompt ohne Material ist die Reihenfolge übrigens fast egal. Das wird erst wichtig, wenn viel auf dem Schreibtisch liegt.

MIRA: Jetzt hattest du im Vorgespräch noch einen Punkt, der mir sehr gefallen hat. Begründungen mitgeben.

JAN: Ja, das ist einer meiner Lieblingstricks. Statt nur eine Regel aufzustellen, sagst du, warum es die Regel gibt.

MIRA: Gib mal ein Beispiel.

JAN: Angenommen, du schreibst einen Text, der später vorgelesen wird. Du könntest schreiben: „Keine Aufzählungen.“ Oder du schreibst: „Der Text wird vorgelesen, deshalb keine Aufzählungen.“ Im zweiten Fall versteht das Modell den Grund und leitet daraus weitere Dinge selbst ab. Es vermeidet dann auch Tabellen, Klammern, lange Zahlenkolonnen und Abkürzungen, die man schlecht aussprechen kann. Obwohl du davon nichts gesagt hast.

MIRA: Weil es weiß, worauf es ankommt.

JAN: Genau. Eine Regel deckt einen Fall ab. Eine Begründung deckt alle verwandten Fälle mit ab.

MIRA: Bei unserer Mail wäre das dann zum Beispiel: „Kein festes neues Datum, weil wir den Zugang noch nicht testen konnten und ich nicht ein zweites Mal verschieben will.“

JAN: Und mit dieser Begründung wird das Modell auch vorsichtig formulieren, wenn es um andere Zusagen geht. Es versteht: Hier geht es darum, keine Versprechen zu machen, die man vielleicht nicht halten kann.

MIRA: Ich merke mir: Eine Regel mit Weil ist mehr wert als drei Regeln ohne.

JAN: Den Satz nehme ich.

MIRA: Nächster großer Punkt: Struktur. Wenn mein Prompt jetzt aus acht Bausteinen plus einer alten Mail plus vielleicht noch einem Mailverlauf besteht, wird das ein ziemlich langer Text.

JAN: Und genau dann wird Struktur wichtig. Das Grundprinzip ist einfach: Trenn die Anweisungen vom Material. Das Modell soll klar erkennen können, was es tun soll und was es nur lesen soll.

MIRA: Was passiert, wenn ich das nicht trenne?

JAN: Dann kann es zu Verwechslungen kommen. Stell dir vor, du kopierst einen Mailverlauf hinein, und in einer der Mails schreibt jemand: „Bitte fasse dich kurz.“ Ist das jetzt eine Anweisung an das Modell oder Teil des Materials? Für dich ist das klar. Für das Modell nicht immer.

MIRA: Und wie trenne ich das sauber?

JAN: Die einfachste Variante sind Überschriften im Prompt. Du schreibst zum Beispiel ein Wort wie Hintergrund, gefolgt von einem Doppelpunkt, und darunter den Hintergrund. Dann das Wort Beispielmail und darunter die alte Mail. Dann Aufgabe und darunter, was zu tun ist. Das reicht für viele Fälle schon.

MIRA: Und die Profivariante?

JAN: Das sind sogenannte Tags, die man aus der Programmierung kennt. Du setzt vor einen Abschnitt das Wort Kontext in spitzen Klammern, und am Ende des Abschnitts noch einmal das Wort Kontext in spitzen Klammern, mit einem Schrägstrich davor. Alles dazwischen gehört zu diesem Abschnitt. Genauso machst du einen Abschnitt, der mit dem Wort Mailverlauf in spitzen Klammern beginnt und endet, und einen für die Beispielmail.

MIRA: Das klingt beim Zuhören erst mal technisch.

JAN: Ist es aber nicht. Es sind beschriftete Umschläge. Auf dem einen steht Kontext, auf dem anderen Mailverlauf. Claude kommt mit solchen Abschnitten sehr gut zurecht, die anderen großen Modelle auch.

MIRA: Welchen Vorteil hat das gegenüber einfachen Überschriften?

JAN: Drei Vorteile. Erstens ist das Ende eines Abschnitts eindeutig, auch wenn im Material selbst Überschriften oder Leerzeilen vorkommen. Zweitens kannst du dich in der Aufgabe auf die Abschnitte beziehen. Du schreibst dann: „Nimm die Mail im Abschnitt Beispielmail als Vorbild für den Ton.“ Drittens kannst du dir das Ergebnis auch in Abschnitten zurückgeben lassen.

MIRA: Wie meinst du das?

JAN: Du schreibst zum Beispiel: „Schreib zuerst deine Überlegungen in einen Abschnitt namens Analyse, und danach die fertige Mail in einen Abschnitt namens Mail.“ Dann kannst du die Mail direkt herauskopieren, ohne die Überlegungen mitzunehmen. Bei Automatisierungen ist das Gold wert, weil das nächste Programm in der Kette genau weiß, wo das Ergebnis steht.

MIRA: Also für Zapier-Abläufe, wo die Antwort automatisch weiterverarbeitet wird.

JAN: Genau. Mit klaren Abschnitten bleibt die Form stabil, und der nächste Schritt bricht nicht.

MIRA: Muss ich jetzt jeden Prompt so aufbauen?

JAN: Nein. Für fünf Sätze ohne Material braucht man das nicht. Die Faustregel: Sobald du etwas hineinkopierst, das du nicht selbst für das Modell geschrieben hast, lohnt sich eine Trennung. Also bei Dokumenten, Mailverläufen, Tabellen, Protokollen.

MIRA: Jetzt haben wir alle Teile beisammen. Bauen wir unseren Einzeiler mal komplett zusammen. Und ich lese ihn vor, so wie ich ihn tippen würde.

JAN: Gern.

MIRA: Ganz oben ein Abschnitt Beispielmail, mit einer echten Mail, die ich der Kundin vor ein paar Wochen geschrieben habe. Dann ein Abschnitt Hintergrund. Darin steht: „Wir richten für einen Onlineshop ein neues Tracking ein. Der Start war für Anfang des Monats geplant. Die Entwickler des Shops haben die nötigen Zugänge erst zwei Wochen später freigeschaltet. Wir konnten deshalb noch nicht testen. Die Kundin hat letzte Woche schon nachgefragt, wann es losgeht.“

JAN: Gut. Weiter.

MIRA: Dann ein Abschnitt Empfängerin: „Die Mail geht an die Leiterin Onlinemarketing. Wir duzen uns und arbeiten seit gut einem Jahr zusammen. Sie ist technisch fit, aber keine Entwicklerin.“

JAN: Und jetzt der Auftrag.

MIRA: Ein Abschnitt Aufgabe: „Schreib mir eine Mail an sie, in der ich die Verzögerung erkläre. Ziel ist, dass sie den Grund versteht und mir bis Freitag sagt, ob wir mit einem Teil der Einrichtung schon starten sollen. Nenn kein festes neues Datum, weil wir den Zugang noch nicht testen konnten und ich nicht ein zweites Mal verschieben will. Nenn stattdessen ein Zeitfenster von ein bis zwei Wochen. Schieb die Schuld nicht auf die Entwickler, weil die eng mit ihr zusammenarbeiten. Sag sachlich, dass die Zugänge später kamen als geplant.“

JAN: Und Format und Erfolgskriterium?

MIRA: „Nimm die Beispielmail als Vorbild für Ton und Länge. Höchstens hundertfünfzig Wörter, mit Betreffzeile, Fließtext ohne Aufzählungen. Die Mail ist gut, wenn sie nicht nach Ausrede klingt und wenn die Kundin die Frage am Ende mit einem Satz beantworten kann. Prüf deinen Entwurf vor der Ausgabe gegen diese beiden Punkte. Wenn dir etwas fehlt, frag mich vorher.“

JAN: Das ist ein richtig guter Prompt.

MIRA: Und das Tippen hat vielleicht drei Minuten gedauert.

JAN: Vergleich das mit dem Einzeiler. Abschicken, lesen, nachbessern: „Nein, wir duzen uns.“ Nächste Runde: „Kein festes Datum.“ Nächste Runde: „Kürzer.“ Am Ende zehn Minuten, und ganz zufrieden bist du trotzdem nicht.

MIRA: Und die Rolle haben wir gar nicht verwendet.

JAN: Richtig. Hier braucht es keine. Das Modell weiß aus dem Kontext genug darüber, wer schreibt. Daran sieht man gut, dass die Bausteine eine Auswahl sind und kein Pflichtprogramm.

MIRA: Kommen wir zu den typischen Fehlern. Was siehst du am häufigsten?

JAN: Erster Fehler: zu viele Anweisungen auf einmal. Manche Leute haben irgendwann eine Vorlage, die über Monate gewachsen ist. Dreißig Regeln, und jedes Mal, wenn etwas schiefging, kam eine neue dazu.

MIRA: Das klingt nach mir.

JAN: Das klingt nach fast allen. Das Problem: Je mehr Regeln, desto weniger Aufmerksamkeit bekommt jede einzelne. Das Modell versucht, alles gleichzeitig zu erfüllen, und dann gehen einzelne Punkte unter. Oft genau die, die dir am wichtigsten waren.

MIRA: Was hilft?

JAN: Ab und zu ausmisten. Frag bei jeder Regel: Passiert das ohne sie überhaupt noch? Und die wichtigsten zwei oder drei Punkte mit Begründung versehen.

MIRA: Zweiter Fehler?

JAN: Widersprüchliche Vorgaben. Das passiert öfter, als man denkt. Oben steht „Fass dich kurz“, weiter unten „Erklär alle Hintergründe ausführlich“. Oder „Schreib locker“ und gleichzeitig „Benutz die Sie-Form und bleib formell“.

MIRA: Und was macht das Modell dann?

JAN: Es versucht einen Kompromiss, und der ist meist schlechter als beide Varianten. Bei langen Prompts hilft es, das Modell selbst zu fragen: „Gibt es in diesen Anweisungen Widersprüche?“ Das funktioniert erstaunlich gut.

MIRA: Dritter Fehler. Den kenne ich aus vielen Vorlagen im Netz. Alles in Großbuchstaben. „Du MUSST unbedingt“, „NIEMALS“, drei Ausrufezeichen.

JAN: Das stammt aus der Anfangszeit. Heutige Modelle lesen aufmerksam. Wenn du da laut wirst, nehmen sie es zu ernst.

MIRA: Zu ernst? Wie sieht das aus?

JAN: Ein Beispiel. Du schreibst in Großbuchstaben: „Erwähne NIEMALS den Preis.“ Dann vermeidet das Modell das Thema so krampfhaft, dass die Mail seltsam wird. Es redet um alles herum, was auch nur entfernt mit Kosten zu tun hat, auch wenn die Kundin genau danach gefragt hat. Ruhig formuliert, mit Begründung, funktioniert besser: „Nenn in dieser Mail keinen Preis, weil das Angebot noch mit der Geschäftsführung abgestimmt wird.“

MIRA: Und der vierte Fehler?

JAN: Nur Verbote. Das hatten wir gestern als Merksatz: Sag, was du willst. Wenn ein Prompt nur aus „kein“, „nicht“ und „niemals“ besteht, weiß das Modell, wo es nicht hin soll. Aber nicht, wo es hin soll.

MIRA: Wie ein Navi, das nur sagt, wo man nicht abbiegen darf.

JAN: Schönes Bild. Und es gibt noch einen Nebeneffekt. Wenn du schreibst „Benutz nicht das Wort spannend“, dann steht das Wort spannend auf dem Schreibtisch. Manchmal taucht es dann erst recht auf. Besser ist es, das Gewünschte zu beschreiben oder ein Beispiel zu geben, in dem die Sprache schon so ist, wie du sie haben willst.

MIRA: Jetzt haben wir eine halbe Folge lang erklärt, wie man lange Prompts baut. Ich möchte zum Schluss noch eine Gegenfrage stellen. Muss jede Anfrage so aussehen?

JAN: Auf keinen Fall. Das wäre die falsche Lehre aus dieser Folge. Viele Fragen sind mit einem Satz perfekt gestellt.

MIRA: Zum Beispiel?

JAN: Alles, wo es eine klare Antwort gibt und kein persönlicher Kontext nötig ist. „Was ist der Unterschied zwischen einer Weiterleitung mit dem Code dreihunderteins und einer mit dreihundertzwei?“ Da brauchst du keinen Empfänger, kein Erfolgskriterium, keine Beispielmail. Oder „Formulier diesen Satz freundlicher“, und dann der Satz.

MIRA: Wo ist dann die Grenze?

JAN: Eine gute Faustregel: Je mehr das Ergebnis von Dingen abhängt, die nur du weißt, desto mehr musst du aufschreiben. Eine Faktenfrage hängt nicht von dir ab. Eine Kundenmail hängt fast komplett von dir ab. Dazwischen gibt es alles.

MIRA: Und wenn ich unsicher bin?

JAN: Dann fang kurz an. Wirkt das Ergebnis generisch, fehlt etwas auf dem Schreibtisch. Dann gehst du die Bausteine durch und ergänzt.

MIRA: Das nimmt Druck raus.

JAN: Ja. Für die Aufgaben, die du jede Woche machst und bei denen viel auf dem Spiel steht, lohnt sich ein gut gebauter Prompt. Und den baust du einmal und verwendest ihn immer wieder. Das ist genau das Thema von morgen.

MIRA: Dann kommen wir zu den Merksätzen für heute. Ich versuche, sie so kurz zu machen, dass man sie beim Gehen behält.

JAN: Leg los.

MIRA: Erstens: Ziel vor Aufgabe. Sag dazu, was der Text beim Empfänger bewirken soll.

JAN: Zweitens: Kontext vor Rolle. Zwei Sätze Hintergrund bringen mehr als ein Satz „Du bist Experte“.

MIRA: Drittens: Material oben, Frage unten. Lange Dokumente zuerst, der Auftrag ganz am Ende.

JAN: Viertens: Eine Regel mit Weil schlägt drei Regeln ohne.

MIRA: Und fünftens: Ruhig und positiv formulieren. Keine Großbuchstaben, keine reinen Verbotslisten, lieber sagen, was du willst.

JAN: Und darüber steht die Entwarnung: Nicht jede Frage braucht ein Briefing.

MIRA: Jetzt die Übung für heute.

JAN: Such dir einen Prompt, den du oft benutzt. Eine Mail an einen Kunden, eine Zusammenfassung eines Termins, eine Auswertung von Zahlen, egal. Am besten etwas, bei dem du mit den Ergebnissen bisher nur halb zufrieden warst.

MIRA: Und dann?

JAN: Dann bau ihn nach den Bausteinen um. Geh sie im Kopf durch. Ist das Ziel klar? Steht der Hintergrund drin? Weiß das Modell, für wen der Text ist? Gibt es Grenzen, die du sonst immer hinterher korrigierst? Hast du ein Beispiel? Hast du Format und Länge genannt? Und weißt du, woran du ein gutes Ergebnis erkennst?

MIRA: Das sind die Bausteine als Fragen.

JAN: Genau. Und dann achte auf zwei Dinge aus der heutigen Folge. Gib mindestens einer Regel eine Begründung mit. Und wenn du Material hineinkopierst, setz es nach oben und trenn es mit einem beschrifteten Abschnitt von deinem Auftrag.

MIRA: Und dann der Vergleich wie gestern?

JAN: Genau. Schick die alte und die neue Version jeweils in einem neuen Chat ab und leg die Ergebnisse nebeneinander. Achte vor allem darauf, wie viele Runden Nachbessern du beim neuen Prompt noch brauchst. Das ist der eigentliche Gewinn.

MIRA: Und heb den umgebauten Prompt auf. Den brauchen wir morgen.

JAN: Richtig. Das dauert insgesamt zehn bis fünfzehn Minuten.

MIRA: Morgen geht es nämlich um Beispiele, Vorlagen und die eigene Prompt-Bibliothek. Wie man gute Beispiele auswählt, warum manchmal mehrere besser sind als eines, wie man aus einem gelungenen Prompt eine Vorlage macht, und wie man seine Vorlagen so ablegt, dass man sie auch wiederfindet.

JAN: Und dein umgebauter Prompt von heute wird dann der erste Eintrag in dieser Bibliothek.

MIRA: Danke fürs Zuhören und viel Spaß beim Umbauen.

JAN: Bis morgen in der KI-Werkstatt.
