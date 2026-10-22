# KI-Werkstatt – Folge 3: Beispiele, Vorlagen und die eigene Prompt-Bibliothek

MIRA: Guten Morgen und willkommen zur dritten Folge der KI-Werkstatt. Ich bin Mira.

JAN: Und ich bin Jan. Hallo!

MIRA: Gestern haben wir einen guten Prompt Baustein für Baustein zusammengesetzt. Heute geht es um drei Dinge, die dir viel Tipparbeit sparen: Beispiele, Vorlagen und eine eigene Prompt-Bibliothek.

JAN: Also um die Frage: Wie schreibe ich einen guten Prompt einmal und nutze ihn dann immer wieder?

MIRA: Genau. Und wir fangen mit den Beispielen an. Die waren gestern einer der Bausteine, aber wir sind nur kurz darüber gegangen.

JAN: Zu Recht, denn die verdienen eine eigene Folge. Wenn ich nur einen einzigen Baustein behalten dürfte, wären es wahrscheinlich die Beispiele.

MIRA: Warum eigentlich? Eine Beschreibung kann doch genauso gut sagen, was ich will.

JAN: Erinnere dich an Folge eins. Das Modell ist eine Vorhersage-Maschine. Es schaut auf den Schreibtisch und setzt fort, was es dort sieht. Eine Beschreibung wie „Schreib kurz und freundlich“ muss das Modell erst übersetzen. Was heißt kurz? Drei Sätze? Zehn? Was heißt freundlich? Mit Ausrufezeichen oder ohne? Ein Beispiel muss es nicht übersetzen. Da steht das Muster einfach vor ihm.

MIRA: Das Modell muss also weniger raten.

JAN: Viel weniger. Ein Beispiel transportiert Dutzende Entscheidungen auf einmal. Länge, Satzbau, Anrede, ob es Absätze gibt, wie der Schluss klingt. Das alles in Worten zu beschreiben, würde eine halbe Seite dauern, und selbst dann würde man die Hälfte vergessen.

MIRA: Ich habe das neulich selbst erlebt. Ich wollte Produkttexte für einen Onlineshop umschreiben lassen und habe lang und breit erklärt, wie die klingen sollen. Das Ergebnis war okay, aber irgendwie daneben. Dann habe ich zwei Texte mitgegeben, die mir gefallen haben, und plötzlich passte es.

JAN: Typisch. Und es macht einen Unterschied, ob du ein Beispiel mitgibst oder mehrere.

MIRA: Was ist der Unterschied?

JAN: Bei einem einzigen Beispiel weiß das Modell nicht, was daran wichtig ist und was Zufall. Nimm eine Mail, die mit „Hallo Herr Becker“ anfängt, drei Absätze hat und zufällig einen Termin am Donnerstag erwähnt. Welcher Teil davon ist das Muster? Die Anrede? Die drei Absätze? Der Donnerstag?

MIRA: Der Donnerstag sicher nicht.

JAN: Für dich ist das klar. Für das Modell nicht unbedingt. Bei einem einzigen Beispiel neigt es dazu, zu viel zu übernehmen. Dann haben plötzlich alle Entwürfe genau drei Absätze, und manchmal schleicht sich sogar ein Donnerstag ein, wo keiner hingehört.

MIRA: Und bei mehreren Beispielen?

JAN: Da kann das Modell vergleichen. Was in allen Beispielen gleich ist, ist offenbar gewollt. Was sich unterscheidet, ist offenbar frei. Mit drei Beispielen zeigst du dem Modell ziemlich gut, wo die Grenzen des Musters liegen.

MIRA: Drei ist also eine gute Zahl?

JAN: Für die meisten Alltagsaufgaben ja. Zwei bis fünf ist ein guter Bereich. Mehr bringt selten viel und macht den Schreibtisch nur voller.

MIRA: Damit sind wir schon bei der nächsten Frage: Wie wähle ich gute Beispiele aus?

JAN: Die wichtigste Regel: Die Beispiele sollten sich deutlich voneinander unterscheiden. Und zwar in allem, was nicht zum Muster gehört.

MIRA: Mach das mal konkret.

JAN: Nehmen wir Kundenmails nach einem Termin. Wenn du drei Mails mitgibst, die alle an denselben Kunden gehen, alle über dasselbe Thema und alle ungefähr gleich lang sind, dann lernt das Modell genau diese Oberfläche. Besser sind drei Mails an unterschiedliche Kunden, eine kurze, eine längere, eine mit guter Nachricht, eine mit einer Verzögerung. Was dann noch gleich bleibt, ist dein eigentlicher Stil. Und genau den soll das Modell übernehmen.

MIRA: Das Modell soll also das Prinzip kopieren und nicht die Oberfläche.

JAN: Schön gesagt. Und wenn du nur ein Beispiel hast, hilft ein einfacher Satz dazu. Ich schreibe dann etwa: Hier ist ein Beispiel für den Ton, den ich mir wünsche. Übernimm den Ton und die Länge, aber nicht den Inhalt und nicht die Struktur.

MIRA: Man sagt dem Modell also dazu, was an dem Beispiel wichtig ist.

JAN: Genau. Diesen halben Satz lassen viele weg.

MIRA: Wie sieht es mit Gegenbeispielen aus? Also: So bitte nicht.

JAN: Die können nützlich sein, aber sparsam. Wenn du dem Modell einen schlechten Text zeigst, liegt dieser schlechte Text ja auch auf dem Schreibtisch. Und das Modell setzt fort, was es sieht. Manchmal schleichen sich dann genau die Formulierungen ein, die man vermeiden wollte.

MIRA: Das ist fast schon paradox.

JAN: Deshalb meine Faustregel: Positive Beispiele zuerst und in der Mehrzahl. Ein Gegenbeispiel nur, wenn es einen ganz bestimmten Fehler gibt, der immer wieder passiert. Und dann kurz und klar beschriftet. Etwa: Das hier ist ein Beispiel, wie es nicht klingen soll, weil es zu förmlich ist und zu viele Floskeln enthält.

MIRA: Und die Begründung gleich mit dazu, wie in Folge zwei.

JAN: Genau. Mit der Begründung kann das Modell verallgemeinern. Ohne Begründung vermeidet es vielleicht nur genau diese eine Formulierung und greift zur nächsten Floskel.

MIRA: Noch eine praktische Frage: Wohin kommen die Beispiele im Prompt?

JAN: Gestern haben wir gesagt: Material zuerst, Auftrag am Ende. Beispiele sind Material. Ich packe sie in einen eigenen, klar markierten Abschnitt. Zum Beispiel einen Abschnitt, der mit dem Wort Beispiele in spitzen Klammern beginnt und endet. Und jedes einzelne Beispiel bekommt eine Nummer. Dann kann das Modell sie sauber vom Rest trennen und verwechselt sie nicht mit dem eigentlichen Auftrag.

MIRA: Okay. Jetzt kommt der Teil, auf den ich mich am meisten gefreut habe: eigene Texte als Stilvorlage.

JAN: Das ist auch einer meiner Lieblingstricks.

MIRA: Ich kenne das Problem gut. Ich lasse mir eine Mail entwerfen, und sie ist inhaltlich in Ordnung, aber sie klingt einfach nicht nach mir. Zu glatt, zu viele Höflichkeitsformeln. Ich schreibe dann die Hälfte wieder um.

JAN: Und der einfachste Weg dagegen ist, drei deiner eigenen Mails mitzugeben. Mails, die du an ähnliche Empfänger geschrieben hast und mit denen du zufrieden warst. Dazu schreibst du etwa: Hier sind drei Mails, die ich selbst geschrieben habe. Schreib den neuen Entwurf so, dass er klingt, als hätte ich ihn geschrieben. Achte auf Anrede, Satzlänge und wie ich Mails beende.

MIRA: Das klingt fast zu einfach.

JAN: Ist es auch. Und der Unterschied ist trotzdem riesig. Die Entwürfe übernehmen deine Grußformel, deine typische Länge, ob du eher direkt zum Punkt kommst oder erst eine Zeile Smalltalk machst.

MIRA: Und wenn ich an verschiedene Leute unterschiedlich schreibe? An einen langjährigen Kunden schreibe ich anders als an eine Agentur, mit der ich zum ersten Mal zu tun habe.

JAN: Dann nimm Beispiele aus genau dieser Beziehung. Am besten den bisherigen Mailverlauf mit dieser Person. Der zeigt Anrede, Ton und Länge, die sich zwischen euch eingespielt haben. Das ist fast immer besser als allgemeine Stilbeispiele.

MIRA: Das mache ich tatsächlich schon so. Aber jedes Mal drei Mails heraussuchen und hineinkopieren, das ist auf Dauer mühsam.

JAN: Und dafür gibt es den nächsten Schritt: den Stil-Steckbrief.

MIRA: Was ist das?

JAN: Du gibst der KI einmal eine größere Auswahl deiner eigenen Texte. Sagen wir zehn Mails, ein paar Slack-Nachrichten, vielleicht einen Absatz aus einem Bericht. Und dann bittest du sie, daraus eine Beschreibung deines Schreibstils abzuleiten.

MIRA: Wie formuliere ich das?

JAN: Ich würde etwa schreiben: Hier sind zehn Texte, die ich selbst geschrieben habe. Beschreib meinen Schreibstil so genau, dass jemand anderes Texte in meinem Stil schreiben könnte. Achte auf Satzlänge, Anrede, Grußformeln, typische Wendungen, was ich vermeide und wie direkt ich formuliere. Gib mir zu jedem Punkt ein kurzes Beispiel aus meinen Texten.

MIRA: Und was kommt da heraus?

JAN: Meistens eine halbe bis eine Seite. Da steht dann zum Beispiel: Kurze Sätze, selten mehr als zwanzig Wörter. Kommt im ersten Satz zur Sache. Duzt Kollegen, siezt neue Kunden. Benutzt kaum Ausrufezeichen. Beendet Mails oft mit einer konkreten nächsten Aktion.

MIRA: Das ist ja fast unheimlich, wenn man sich selbst so beschrieben liest.

JAN: Der eigentliche Nutzen ist, dass du diesen Steckbrief speichern kannst. Ab dann legst du einfach den Steckbrief auf den Schreibtisch, statt jedes Mal Beispiele herauszusuchen.

MIRA: Ersetzt der Steckbrief die Beispiele komplett?

JAN: Nicht ganz. Die beste Kombination ist der Steckbrief plus ein oder zwei echte Beispiele. Der Steckbrief sagt, worauf es ankommt, und die Beispiele zeigen es. Das ist dann wieder die Regel: Beispiele schlagen Beschreibungen. Aber Beschreibung plus Beispiel schlägt beides allein.

MIRA: Und den Steckbrief würde ich auch prüfen, bevor ich ihn speichere, oder?

JAN: Unbedingt. Lies ihn durch und streich, was nicht stimmt. Manchmal leitet die KI aus drei Mails eine Regel ab, die nur Zufall war. Und ergänz, was dir wichtig ist. Wenn du zum Beispiel bestimmte Wörter nicht ausstehen kannst, gehört das da rein.

MIRA: Gut. Wechseln wir zu den Vorlagen. Was meinen wir damit genau?

JAN: Eine Vorlage ist ein fertiger Prompt für eine Aufgabe, die immer wiederkommt. Der größte Teil bleibt jedes Mal gleich, und nur ein paar Stellen setzt du neu ein. Diese Stellen nennt man Platzhalter.

MIRA: So wie ein Serienbrief.

JAN: Genau so. Und jeder hat solche wiederkehrenden Aufgaben. Bei dir zum Beispiel der Wochenbericht, die Kundenmail nach einem Termin oder die Analyse der Monatszahlen.

MIRA: Und die Prüfung eines Produktdaten-Feeds, das kommt bei mir auch ständig vor.

JAN: Perfektes Beispiel. Nehmen wir das mal auseinander. Wie würde eine Vorlage für die Feed-Prüfung aussehen?

MIRA: Fang du an.

JAN: Ganz oben steht der feste Teil, der sich nie ändert. Die Rolle, etwa: Du prüfst Produktdaten-Feeds für Onlineshops, bevor sie an Preisvergleiche und Werbeplattformen gehen. Dann das Ziel: Finde Fehler, die dazu führen, dass Produkte abgelehnt werden oder falsch angezeigt werden.

MIRA: Das ist der Teil, den ich sonst jedes Mal neu tippe.

JAN: Und meistens jedes Mal ein bisschen anders und ein bisschen schlechter. Dann kommen die festen Vorgaben. Welche Felder Pflicht sind. Dass Preise ein bestimmtes Format haben müssen. Dass ein Titel mehr enthält als die Artikelnummer. Dass Bildlinks funktionieren sollen. Das sind deine Prüfregeln, die du über die Zeit gesammelt hast.

MIRA: Und dann das Format.

JAN: Ja, auch fest. Etwa: Gib mir zuerst eine kurze Einschätzung in zwei Sätzen, ob der Feed grundsätzlich in Ordnung ist. Dann die Fehler, sortiert nach Schwere, mit Beispielzeilen und der Zahl der betroffenen Produkte. Am Ende drei konkrete Empfehlungen für den Kunden.

MIRA: Und was ist variabel?

JAN: Wenig. Der Feed selbst, also die Datei. Der Shop, um den es geht, und wofür der Feed gedacht ist. Und ein Feld für Besonderheiten, etwa: Der Kunde hat gerade sein Sortiment umgestellt, achte besonders auf neue Kategorien.

MIRA: Wie markiere ich diese Platzhalter in der Vorlage?

JAN: Hauptsache, du erkennst sie auf einen Blick. Viele schreiben das Wort in Großbuchstaben, zum Beispiel SHOPNAME oder BESONDERHEITEN, oder setzen es in eckige Klammern. Manche benutzen auch die Abschnitte mit spitzen Klammern aus Folge zwei. Dann gibt es einen Abschnitt Feed, einen Abschnitt Shop und einen Abschnitt Besonderheiten, und du füllst einfach die Lücken aus.

MIRA: Und wenn ich vergesse, einen Platzhalter auszufüllen?

JAN: Dafür gibt es einen kleinen Trick. Schreib in die Vorlage: Wenn ein Platzhalter noch nicht ausgefüllt ist, frag mich danach, bevor du anfängst. Dann merkt die KI das und fragt nach, statt einfach etwas zu erfinden.

MIRA: Lass mich ein zweites Beispiel durchspielen, damit man das Prinzip hört. Die Kundenmail nach einem Termin.

JAN: Gern.

MIRA: Fest wäre: Ich bin Berater im E-Commerce und schreibe nach Terminen eine Zusammenfassung an den Kunden. Die Mail fasst zusammen, was besprochen wurde, nennt die Vereinbarungen mit Verantwortlichen und Terminen und endet mit dem nächsten Schritt. Dazu mein Stil-Steckbrief. Und die Regel: Erfinde keine Vereinbarungen, die nicht in meinen Notizen stehen.

JAN: Sehr gut, besonders die letzte Regel.

MIRA: Variabel wären meine Notizen aus dem Termin, der Name des Ansprechpartners, ob wir uns duzen oder siezen, und vielleicht der bisherige Mailverlauf.

JAN: Genau so. Und merkst du was? Der feste Teil ist eigentlich das, was wir gestern als Bausteine besprochen haben. Ziel, Rolle, Vorgaben, Format, Erfolgskriterium. Den baust du einmal sorgfältig, und danach kostet dich jede einzelne Mail nur noch das Einsetzen der Notizen.

MIRA: Und für die Analyse der Monatszahlen wäre es dasselbe Prinzip?

JAN: Dasselbe. Fest ist der Analyseweg aus Folge eins und das Format für den Bericht. Variabel sind die Zahlen des Monats und das, was in dem Monat los war, also Aktionen, Umstellungen, technische Probleme.

MIRA: Okay, jetzt habe ich Beispiele, einen Stil-Steckbrief und mehrere Vorlagen. Wo lege ich die alle ab?

JAN: Das ist die Prompt-Bibliothek. Und die Antwort ist: Fang einfach an. Ein einzelnes Dokument reicht für den Anfang völlig. Ein Textdokument oder eine Seite in deiner Notiz-App, mit einer Überschrift pro Vorlage.

MIRA: Kein spezielles Tool?

JAN: Für den Anfang nicht. Wichtig ist, dass du es schnell findest und schnell kopieren kannst. Wenn die Bibliothek erst nach drei Klicks erreichbar ist, wirst du sie nicht nutzen.

MIRA: Und die KI-Tools selbst? Da gibt es doch inzwischen Möglichkeiten, Dinge dauerhaft zu speichern.

JAN: Ja. In Claude und ChatGPT kannst du zum Beispiel Projekte mit eigenen Anweisungen anlegen. Eine Vorlage, die du nur für einen bestimmten Kunden brauchst, kann gut in den Anweisungen dieses Projekts liegen. Dann ist sie automatisch auf dem Schreibtisch, sobald du in dem Projekt arbeitest.

MIRA: Die vorbereiteten Schreibtische aus Folge eins.

JAN: Genau. Und einige Tools bieten außerdem gespeicherte Vorlagen oder sogenannte Skills an. Das sind im Grunde Anleitungen, die das Tool bei passenden Aufgaben selbst heranzieht. Wie das im Einzelnen heißt und wo man es findet, unterscheidet sich von Tool zu Tool und ändert sich auch öfter. Das Prinzip ist aber immer gleich: ein guter Prompt, einmal geschrieben, an einem festen Ort gespeichert.

MIRA: Würdest du trotzdem zusätzlich das einfache Dokument behalten?

JAN: Ja, als Hauptquelle. Dann bist du an kein Tool gebunden und hast alles an einem Ort.

MIRA: Wie benenne ich die Vorlagen am besten?

JAN: Nach der Aufgabe, nicht nach dem Tool und nicht nach dem Datum. Also „Kundenmail nach Termin“, „Feed-Prüfung“, „Monatsanalyse“, „Wochenbericht“. Dazu ein, zwei Sätze darunter: wofür die Vorlage da ist und welche Platzhalter du ausfüllen musst. Und ein Datum, wann du sie zuletzt geändert hast.

MIRA: Das Datum, damit ich weiß, wie aktuell sie ist?

JAN: Genau. Und es hilft beim Pflegen. Eine Vorlage ist nie fertig. Jedes Mal, wenn du ein Ergebnis nachbessern musst, ist das ein Hinweis, dass in der Vorlage etwas fehlt.

MIRA: Kannst du das an einem Beispiel zeigen?

JAN: Sagen wir, du nutzt die Vorlage für die Kundenmail und merkst dreimal hintereinander, dass du den Betreff selbst umschreibst, weil er zu allgemein ist. Dann gehört in die Vorlage eine Regel: Der Betreff nennt das Datum des Termins und das wichtigste Ergebnis. Einmal ergänzt, und das Problem ist für immer weg.

MIRA: Also nicht im Chat nachbessern und vergessen, sondern die Verbesserung in die Vorlage zurückschreiben.

JAN: Genau das ist der Kern. Sonst korrigierst du dieselben Fehler immer wieder.

MIRA: Und dann gibt es noch eine Gewohnheit, die du mir mal empfohlen hast.

JAN: Ja, die wichtigste von allen: Nach jedem richtig guten Ergebnis den Prompt sichern.

MIRA: Warum ist das so wichtig?

JAN: Weil die besten Prompts selten am Schreibtisch geplant werden. Sie entstehen im Gespräch. Du fängst mit einer kurzen Frage an, gibst Kontext nach, korrigierst zweimal, und am Ende kommt etwas heraus, das richtig gut ist. Und dann schließt du den Chat, und das ganze Wissen, wie du dahin gekommen bist, ist weg.

MIRA: Das kenne ich. Drei Wochen später habe ich dieselbe Aufgabe und weiß nicht mehr, wie ich es beim letzten Mal geschafft habe.

JAN: Deshalb: Wenn ein Ergebnis richtig gut ist, nimm dir zwei Minuten. Und das Schöne ist, du musst den Prompt nicht einmal selbst zusammenbauen. Schreib einfach am Ende des Chats: Fass alles, was ich dir in diesem Gespräch an Anweisungen und Korrekturen gegeben habe, zu einem einzigen Prompt zusammen, mit dem ich beim nächsten Mal direkt dieses Ergebnis bekomme. Markiere die Stellen, die sich jedes Mal ändern, als Platzhalter.

MIRA: Oh, das ist gut. Dann wird aus dem Chat direkt eine Vorlage.

JAN: Genau. Den Prompt kopierst du in deine Bibliothek, gibst ihm einen Namen, fertig. Und beim nächsten Mal testest du ihn in einem neuen Chat. Wenn das Ergebnis wieder passt, hast du eine funktionierende Vorlage.

MIRA: Damit sind wir schon beim letzten großen Thema: die KI selbst Prompts schreiben oder verbessern lassen.

JAN: Ja, und das ist ein Werkzeug, das viele unterschätzen.

MIRA: Wie gehe ich da vor?

JAN: Der einfachste Weg: Du beschreibst deine Aufgabe in ein paar Sätzen und bittest die KI, daraus einen Prompt zu schreiben. Der entscheidende Zusatz ist: Frag mich vorher, was fehlt. Ich schreibe dann etwa: Ich will jede Woche einen kurzen Bericht über die Kennzahlen meiner Kunden für meinen Vorgesetzten schreiben. Schreib mir einen Prompt dafür, den ich als Vorlage benutzen kann. Bevor du ihn schreibst, stell mir die Fragen, die du brauchst, um ihn wirklich gut zu machen.

MIRA: Und dann kommen Fragen?

JAN: Meistens fünf bis zehn. Wer liest den Bericht? Wie viel Zeit hat er dafür? Welche Kennzahlen sind wichtig? Soll der Bericht Empfehlungen enthalten oder nur Fakten? Was ist in früheren Berichten schiefgelaufen?

MIRA: Das sind genau die Fragen, die ich mir selbst nicht gestellt hätte.

JAN: Und genau deshalb funktioniert es. Die KI kennt viele gute Prompts und weiß, welche Bausteine meistens fehlen. Sie arbeitet dir quasi die Liste aus Folge zwei ab, nur zugeschnitten auf deine Aufgabe.

MIRA: Und das Verbessern? Wenn ich schon einen Prompt habe, der so mittel funktioniert?

JAN: Dann gibst du den Prompt mit und dazu ein Ergebnis, das dir nicht gefallen hat. Und schreibst, was dich stört. Etwa: Hier ist mein Prompt, und hier ist ein Ergebnis davon. Das Ergebnis ist zu lang, und es fehlen konkrete Empfehlungen. Verbessere den Prompt so, dass diese Probleme nicht mehr auftreten, und erklär mir kurz, was du geändert hast.

MIRA: Die Erklärung, damit ich etwas dabei lerne.

JAN: Und damit du prüfen kannst, ob die Änderung Sinn ergibt. Was mich zu den Grenzen bringt.

MIRA: Die wollte ich gerade ansprechen. Wo hört das auf zu funktionieren?

JAN: Erste Grenze: Die KI kennt deine Situation nicht. Sie kann einen Prompt schreiben, der auf dem Papier gut aussieht, aber er enthält nur das, was du ihr gesagt hast, plus allgemeine Annahmen. Dein Wissen über den Kunden, über frühere Probleme, über das, was dein Vorgesetzter wirklich lesen will, muss trotzdem von dir kommen.

MIRA: Deshalb die Rückfragen.

JAN: Genau. Zweite Grenze: Von der KI geschriebene Prompts werden gern zu lang und zu feierlich. Da stehen dann Sätze wie „Du bist ein erfahrener Experte mit zwanzig Jahren Berufserfahrung“ und eine Liste mit fünfzehn Regeln, von denen sich die Hälfte überschneidet.

MIRA: Und was mache ich dann?

JAN: Kürzen. Streich alles, was keinen Unterschied macht. Ein guter Test: Würde das Ergebnis schlechter werden, wenn dieser Satz fehlt? Wenn nicht, raus damit.

MIRA: Und die dritte Grenze?

JAN: Ein Prompt ist erst gut, wenn er getestet ist. Die KI kann dir sagen, dass ihr Prompt toll ist, aber das weiß sie nicht. Du musst ihn ausprobieren, am besten mit zwei, drei echten Fällen, auch mit einem schwierigen. Erst dann gehört er in die Bibliothek.

MIRA: Mir fällt noch ein privates Beispiel ein. Ich plane gerade eine Reise und lasse mir dafür immer wieder Vorschläge machen.

JAN: Klassischer Fall für eine kleine Vorlage. Alles, was du mehr als zweimal machst, verdient eine. Fest wäre: wer mitfährt, worauf ihr Wert legt, was euch nicht interessiert, euer ungefähres Budget. Variabel: das Ziel, die Reisezeit, die konkrete Frage. Dann musst du der KI nicht jedes Mal neu erklären, dass ihr mit Kind unterwegs seid und keine Lust auf Clubhotels habt.

MIRA: Das stimmt, das schreibe ich tatsächlich jedes Mal neu.

JAN: Siehst du. Und da merkst du auch, wo die Grenze zu den dauerhaften Anweisungen liegt. Was immer gilt, egal bei welcher Aufgabe, gehört in deine allgemeinen Einstellungen. Was für eine bestimmte Art von Aufgabe gilt, gehört in eine Vorlage oder ein Projekt.

MIRA: Okay. Ich fasse die wichtigsten Punkte zusammen, damit man sie beim Gehen behält.

JAN: Gern.

MIRA: Erstens: Ein Beispiel zeigt mehr als jede Beschreibung, und drei unterschiedliche Beispiele zeigen das Prinzip statt der Oberfläche.

JAN: Zweitens: Gegenbeispiele sparsam und immer mit Begründung.

MIRA: Drittens: Lass dir aus deinen eigenen Texten einen Stil-Steckbrief schreiben und nutz ihn immer wieder.

JAN: Viertens: Was du öfter als zweimal machst, bekommt eine Vorlage. Fester Teil oben, Platzhalter für das, was sich ändert.

MIRA: Und fünftens: Nach jedem richtig guten Ergebnis den Prompt sichern.

JAN: Und als Zugabe: Die KI darf dir beim Schreiben von Prompts helfen. Aber die Rückfragen beantworten und das Testen, das bleibt deine Aufgabe.

MIRA: Kommen wir zur Übung für heute.

JAN: Die Übung heißt „Die erste Vorlage“. Überleg dir, welche Aufgabe du am häufigsten mit KI erledigst. Bei den meisten ist das irgendeine Art von Mail oder eine Zusammenfassung.

MIRA: Bei mir wäre es die Mail nach einem Kundentermin.

JAN: Perfekt. Dann öffnest du einen neuen Chat und schreibst: Ich möchte eine Vorlage für diese Aufgabe bauen. Dann beschreibst du die Aufgabe in drei, vier Sätzen und hängst an: Stell mir zuerst die Fragen, die du brauchst, und schreib dann einen Prompt mit Platzhaltern für die Teile, die sich jedes Mal ändern.

MIRA: Und dann beantworte ich die Fragen.

JAN: Genau. Dann kürzt du den Prompt, bis nur noch übrig ist, was wirklich etwas bewirkt. Dann testest du ihn einmal mit einem echten Fall von heute oder gestern, in einem frischen Chat. Und wenn das Ergebnis passt, kopierst du ihn in ein neues Dokument mit dem Namen Prompt-Bibliothek.

MIRA: Das ist dann der erste Eintrag.

JAN: Genau. Das Ganze dauert zehn bis fünfzehn Minuten. Und spätestens beim dritten Einsatz hast du die Zeit wieder raus.

MIRA: Und wer noch fünf Minuten übrig hat: Gib der KI fünf deiner eigenen Mails und lass dir den ersten Stil-Steckbrief schreiben. Der kommt als zweiter Eintrag in die Bibliothek.

JAN: Gute Ergänzung.

MIRA: In der nächsten Folge geht es um das, was nach dem ersten Entwurf passiert. Nachbessern statt neu anfangen. Wie du einer KI sagst, was genau an einem Ergebnis nicht stimmt, damit die zweite Runde wirklich besser wird.

JAN: Und warum „Mach das besser“ fast nie funktioniert, ein konkreter Satz Kritik aber fast immer.

MIRA: Danke fürs Zuhören und viel Erfolg mit deiner ersten Vorlage.

JAN: Bis morgen in der KI-Werkstatt.
