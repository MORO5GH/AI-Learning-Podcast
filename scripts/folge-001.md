# KI-Werkstatt – Folge 1: Was im Modell passiert, wenn du tippst

MIRA: Guten Morgen und willkommen zur ersten Folge der KI-Werkstatt. Ich bin Mira.

JAN: Und ich bin Jan. Die Idee hinter dieser Reihe ist einfach: Jeden Tag eine Viertelstunde, ein Thema, und am Ende eine kleine Übung, die du noch am selben Tag ausprobieren kannst.

MIRA: Wir fangen heute bei der Frage an, die fast alles andere erklärt: Was passiert eigentlich im Modell, wenn du eine Nachricht abschickst? Wer das einmal verstanden hat, schreibt automatisch bessere Prompts.

JAN: Und das Gute ist, man muss dafür kein Informatiker sein. Ein paar Bilder im Kopf reichen.

MIRA: Dann fang mal an. Was ist ein Sprachmodell?

JAN: Im Kern ist es ein Programm, das eine einzige Sache sehr gut kann: Es schaut sich einen Text an und schätzt, welches Stück Text als Nächstes am wahrscheinlichsten kommt. Dann hängt es dieses Stück an und schätzt das nächste. Und so weiter, Stück für Stück, bis die Antwort fertig ist.

MIRA: Das klingt erst mal fast zu simpel. Wie kommen dann Antworten zustande, die richtig durchdacht wirken?

JAN: Weil das Modell beim Training unvorstellbar viel Text gesehen hat. Bücher, Webseiten, Handbücher, Programmcode, Diskussionen. Um in all diesen Texten gut vorherzusagen, was als Nächstes kommt, musste es nebenbei eine Menge lernen: Grammatik, Fakten, wie Argumente aufgebaut sind, wie eine Geschäftsmail klingt, wie man einen Fehler in einer Formel findet.

MIRA: Also eine Art Nebeneffekt.

JAN: Genau. Wenn du gut vorhersagen willst, wie ein Satz in einem Physikbuch weitergeht, hilft es enorm, Physik ein Stück weit verstanden zu haben. Das Modell hat sich diese Muster angeeignet, weil sie beim Vorhersagen helfen.

MIRA: Du hast gerade von Stücken gesprochen. Sind das Wörter?

JAN: Nicht ganz. Man nennt sie Tokens. Ein Token ist oft ein Wortteil. Kurze, häufige Wörter wie „und“ oder „das“ sind meist ein Token. Lange deutsche Wörter wie „Rechnungsweiterleitung“ werden in mehrere Tokens zerlegt. Als Faustregel kannst du dir merken: Ein Token ist im Schnitt etwa drei bis vier Buchstaben.

MIRA: Und warum sollte mich das interessieren?

JAN: Aus zwei Gründen. Erstens wird bei vielen Anbietern nach Tokens abgerechnet und begrenzt. Zweitens erklärt es manche Schwächen. Wenn du ein Modell fragst, wie viele „r“ in einem Wort stecken, liegt es manchmal daneben. Es sieht das Wort eben nicht Buchstabe für Buchstabe, sondern in Brocken.

MIRA: Okay, das ist ein schönes Beispiel. Jetzt kommt der Teil, der mir persönlich am meisten geholfen hat: das Kontextfenster.

JAN: Ja, das ist der wichtigste Begriff der heutigen Folge.

MIRA: Stell dir das Kontextfenster wie einen Schreibtisch vor. Alles, was auf diesem Schreibtisch liegt, kann das Modell beim Antworten sehen. Deine aktuelle Frage, die bisherigen Nachrichten im Chat, hochgeladene Dateien, Anweisungen, die im Hintergrund mitgeschickt werden. Und alles, was nicht auf dem Schreibtisch liegt, existiert für das Modell in diesem Moment schlicht nicht.

JAN: Das ist der Punkt, den viele unterschätzen. Das Modell hat kein laufendes Gedächtnis wie ein Mensch, der sich an gestern erinnert. Bei jeder einzelnen Antwort wird der komplette Inhalt des Schreibtischs neu eingelesen.

MIRA: Moment. Aber Claude kennt doch Dinge aus früheren Gesprächen von mir. Wie passt das zusammen?

JAN: Gute Frage, und die Antwort zeigt, wie das System drumherum gebaut ist. Wenn ein Assistent sich an dich erinnert, dann deshalb, weil vor deiner Nachricht ein paar Notizen über dich mit auf den Schreibtisch gelegt werden. Das Modell selbst merkt sich nichts. Das Programm drumherum speichert Notizen und legt sie bei Bedarf dazu.

MIRA: Das heißt, Gedächtnis ist im Grunde ein cleverer Zettelkasten.

JAN: Ziemlich genau. Und das gilt für fast alle Funktionen, die beeindruckend wirken. Eine Websuche? Das Programm sucht, und die Ergebnisse werden auf den Schreibtisch gelegt. Eine hochgeladene PDF? Ihr Text landet auf dem Schreibtisch. Ein Projekt mit Dokumenten? Die Dokumente liegen auf dem Schreibtisch.

MIRA: Was folgt daraus ganz praktisch?

JAN: Die wichtigste Regel überhaupt: Das Modell weiß nur, was auf dem Schreibtisch liegt. Wenn du schreibst „Mach mir eine Mail an den Kunden wegen der Sache von letzter Woche“, dann fehlen auf dem Schreibtisch drei Dinge: Welcher Kunde, welche Sache, und wie du normalerweise mit diesem Kunden sprichst.

MIRA: Und dann rät es.

JAN: Dann füllt es die Lücken mit dem Wahrscheinlichsten. Das Ergebnis ist eine Mail, die nach Durchschnitt klingt. Nicht falsch, aber auch nicht deine.

MIRA: Ich übersetze das mal in einen Merksatz: Ein guter Prompt ist vor allem ein gut bestückter Schreibtisch.

JAN: Den nehme ich.

MIRA: Jetzt ist der Schreibtisch aber nicht unendlich groß.

JAN: Nein. Moderne Modelle haben sehr große Kontextfenster, da passen ganze Bücher drauf. Aber zwei Dinge passieren, wenn ein Chat sehr lang wird. Erstens wird es irgendwann voll, und ältere Teile werden zusammengefasst oder fallen weg. Zweitens, und das merkt man schon vorher: Die Aufmerksamkeit verteilt sich. Wenn auf dem Schreibtisch hundert Blätter liegen, wird das eine wichtige Blatt leichter übersehen.

MIRA: Das kenne ich. Nach zwei Stunden in einem Chat fängt die KI plötzlich an, Dinge zu vergessen, die wir am Anfang besprochen haben.

JAN: Genau das. Deshalb ist eine der nützlichsten Gewohnheiten überhaupt: Bei einem neuen Thema einen neuen Chat anfangen. Und bei langen Projekten zwischendurch eine Übergabe schreiben lassen, also eine Zusammenfassung des Stands, mit der man frisch weitermacht.

MIRA: Das ist so etwas wie den Schreibtisch aufräumen und nur die wichtigen Blätter wieder hinlegen.

JAN: Schönes Bild.

MIRA: Kommen wir zum zweiten großen Thema: Warum erfindet KI manchmal Dinge? Dieses Halluzinieren.

JAN: Wenn man verstanden hat, wie das Modell funktioniert, ist das fast logisch. Das Modell erzeugt immer das, was am wahrscheinlichsten klingt. Wenn es eine Sache wirklich gut gelernt hat, ist das Wahrscheinlichste auch das Richtige. Wenn es aber eine Lücke gibt, zum Beispiel eine sehr spezielle Zahl, ein seltenes Gesetz oder eine Funktion in einer Software, die es kaum kennt, dann erzeugt es trotzdem etwas, das plausibel klingt.

MIRA: Es hat also keinen eingebauten Alarm, der sagt: Achtung, hier weiß ich es eigentlich nicht.

JAN: Die neueren Modelle sind darin deutlich besser geworden. Sie sagen öfter „Das weiß ich nicht sicher“. Aber verlassen sollte man sich darauf nicht. Besonders gefährlich sind drei Bereiche: konkrete Zahlen, Quellenangaben und alles, was sich in den letzten Monaten verändert hat.

MIRA: Warum gerade das Letzte?

JAN: Weil jedes Modell einen Wissensstand hat, einen Stichtag. Was danach passiert ist, kennt es nicht aus dem Training. Preise, neue Produkte, wer gerade welchen Posten hat. Wenn das Modell dann keine Websuche nutzt, antwortet es mit dem alten Stand und klingt dabei völlig überzeugt.

MIRA: Was macht man dagegen?

JAN: Drei Dinge. Erstens: Für alles Aktuelle die Websuche nutzen oder explizit darum bitten. Zweitens: Quellen verlangen und stichprobenartig anklicken. Drittens, und das ist der unterschätzte Trick: Selbst die Fakten auf den Schreibtisch legen. Wenn du die Preisliste, den Vertrag oder die Tabelle hochlädst und sagst „Antworte nur auf Basis dieses Dokuments“, dann muss das Modell nicht aus dem Gedächtnis raten.

MIRA: Das ist wieder der Schreibtisch.

JAN: Es ist immer der Schreibtisch. Ich glaube, das wird das Leitmotiv dieser Reihe.

MIRA: Jetzt gibt es noch einen Punkt, der für mich lange ein Rätsel war. Warum bekomme ich auf dieselbe Frage manchmal unterschiedliche Antworten?

JAN: Weil das Modell beim Auswählen des nächsten Tokens nicht immer das allerwahrscheinlichste nimmt, sondern ein bisschen würfelt. Unter den passenden Kandidaten wird zufällig gewählt, gewichtet nach Wahrscheinlichkeit. Das macht die Antworten lebendiger und weniger hölzern.

MIRA: Und für mich als Nutzer heißt das?

JAN: Wenn dir eine Antwort nicht gefällt, ist es völlig legitim, sie einfach neu erzeugen zu lassen. Oft kommt beim zweiten oder dritten Versuch etwas Besseres. Und bei kreativen Aufgaben lohnt es sich, direkt nach mehreren Varianten zu fragen. „Gib mir drei unterschiedliche Betreffzeilen“ bringt mehr als eine.

MIRA: Umgekehrt heißt das aber auch: Wenn eine Antwort einmal richtig war, ist das keine Garantie, dass sie es beim nächsten Mal auch ist.

JAN: Richtig. Gerade bei Automatisierungen, die jeden Tag laufen, sollte man deshalb klare Regeln und Beispiele vorgeben, damit der Spielraum klein bleibt.

MIRA: Da sind wir schon fast bei den praktischen Konsequenzen. Lass uns die mal sammeln. Was ändert dieses Wissen konkret an der Art, wie ich prompte?

JAN: Erste Konsequenz: Kontext schlägt Zauberformeln. Es gibt im Netz unzählige Listen mit angeblich magischen Prompt-Formulierungen. Die bringen deutlich weniger als ein paar Sätze echter Hintergrund. Wer ist der Empfänger, was ist das Ziel, was ist schon passiert, was soll auf keinen Fall drinstehen.

MIRA: Zweite Konsequenz?

JAN: Beispiele wirken stärker als Beschreibungen. Wenn du schreibst „Schreib locker, aber professionell“, kann das alles Mögliche heißen. Wenn du eine Mail mitgibst, die du selbst geschrieben hast, und sagst „ungefähr in diesem Ton“, dann hat das Modell ein echtes Muster, an dem es sich orientiert. Das ist im Grunde die Vorhersage-Maschine in Reinform: Sie setzt das Muster fort, das sie vor sich sieht.

MIRA: Das finde ich einen wichtigen Gedanken. Das Modell setzt Muster fort. Wenn ich ihm also einen schlampigen, kurzen Prompt hinlege, bekomme ich tendenziell auch eine schlampigere Antwort?

JAN: In der Tendenz ja. Nicht immer, die Modelle sind darauf trainiert, auch mit knappen Fragen gut umzugehen. Aber ein sorgfältig geschriebener Prompt mit klarer Struktur zieht eine sorgfältigere Antwort nach sich.

MIRA: Dritte Konsequenz?

JAN: Sag, was du willst, nicht nur, was du nicht willst. Wenn du schreibst „Keine Aufzählungen“, ist das okay. Besser ist: „Schreib in zusammenhängenden Absätzen, wie in einer persönlichen Mail.“ Dann hat das Modell ein positives Ziel statt nur ein Verbot.

MIRA: Und vierte?

JAN: Lass dir Rückfragen stellen. Ein sehr nützlicher Satz am Ende eines Prompts ist: „Wenn dir Informationen fehlen, frag mich, bevor du anfängst.“ Damit drehst du das Rate-Problem um. Statt Lücken mit Durchschnitt zu füllen, sagt dir das Modell, was auf dem Schreibtisch fehlt.

MIRA: Den benutze ich tatsächlich seit einiger Zeit und merke, wie viel besser die Ergebnisse werden. Gerade bei Texten für Kunden.

JAN: Und fünftens: Arbeite in Runden. Der erste Entwurf ist ein Entwurf. Die eigentliche Qualität entsteht im zweiten und dritten Schritt, wenn du sagst: „Der zweite Absatz ist zu lang, und der Ton ist mir zu förmlich.“ Das Modell hat dann den ersten Entwurf und deine Kritik auf dem Schreibtisch und kann gezielt nachbessern.

MIRA: Ich fasse die fünf kurz zusammen, damit man sie beim Spazierengehen behält. Eins: Kontext schlägt Zauberformeln. Zwei: Beispiele schlagen Beschreibungen. Drei: Sag, was du willst. Vier: Lass dir Rückfragen stellen. Fünf: Arbeite in Runden.

JAN: Und alles fünf folgt aus dem einen Bild: Das Modell sieht nur den Schreibtisch und setzt fort, was darauf liegt.

MIRA: Ich möchte noch mal auf den Schreibtisch zurückkommen. Du hast vorhin gesagt, dass da auch Dinge liegen, die ich gar nicht sehe. Was genau ist das?

JAN: Das ist ein Punkt, über den kaum jemand nachdenkt. Wenn du in einer App wie Claude oder ChatGPT eine Frage stellst, ist deine Nachricht nie das Erste auf dem Schreibtisch. Davor liegt ein ganzer Stapel Anweisungen vom Anbieter. Wie sich der Assistent verhalten soll, welche Werkzeuge er hat, wie er formatieren soll, was er ablehnen soll. Das nennt man den Systemprompt.

MIRA: Und der kann ziemlich lang sein, oder?

JAN: Teilweise sehr lang, viele Seiten. Und dann kommen noch Dinge dazu, die du selbst festgelegt hast. In den Einstellungen deine persönlichen Vorlieben, in einem Projekt die Projektanweisungen und die hochgeladenen Dokumente, dazu die Notizen aus dem Gedächtnis. Erst danach kommt deine eigentliche Frage.

MIRA: Das heißt, wenn ich in meinen Einstellungen hinterlege „Antworte immer auf Deutsch und frag nach, bevor du etwas tust“, dann liegt das bei jeder Nachricht mit auf dem Tisch.

JAN: Genau. Und das ist einer der stärksten Hebel, die du als Nutzer hast. Alles, was du dem Assistenten sonst in jedem Chat neu sagen müsstest, gehört in diese dauerhaften Anweisungen. Dein Beruf, deine Kunden, wie du Texte magst, welche Sprache, welcher Ton.

MIRA: Aber Vorsicht, oder? Wenn da zu viel drinsteht, wird der Schreibtisch auch voll.

JAN: Richtig. Dauerhafte Anweisungen sollten kurz und allgemeingültig sein. Was nur für ein Thema gilt, gehört in ein Projekt. Für deine Kundenarbeit zum Beispiel ein Projekt pro Kunde, mit Ansprechpartnern, Hintergrund und den wichtigsten Dokumenten. Dann liegt in diesem Projekt genau das auf dem Tisch, was für diesen Kunden zählt, und nicht der ganze Rest.

MIRA: Das finde ich einen guten Gedanken. Projekte sind im Grunde vorbereitete Schreibtische.

JAN: So kann man es sagen. Und wir machen dazu später noch eine eigene Folge, weil man mit gut eingerichteten Projekten sehr viel Zeit spart.

MIRA: Ein anderes Thema, das mich interessiert: Viele Assistenten haben inzwischen so einen Denkmodus. Man sieht dann, dass die KI erst eine Weile nachdenkt, bevor sie antwortet. Was passiert da?

JAN: Erinnere dich an das Grundprinzip: Das Modell schreibt Token für Token. Es kann also nicht im Stillen nachdenken und dann eine fertige Antwort ausspucken. Denken passiert beim Schreiben. Der Denkmodus nutzt genau das. Das Modell schreibt zuerst eine Art Notizzettel: Was ist eigentlich gefragt, welche Wege gibt es, wo könnte ein Fehler stecken. Und erst danach schreibt es die Antwort.

MIRA: Und dieser Notizzettel liegt dann auch auf dem Schreibtisch.

JAN: Ja, und deshalb wird die Antwort besser. Das Modell kann auf seine eigenen Zwischenschritte zurückgreifen. Bei Rechenaufgaben, bei Analysen, bei kniffligen Entscheidungen macht das einen großen Unterschied.

MIRA: Sollte ich den dann immer anschalten?

JAN: Nicht unbedingt. Für eine kurze Umformulierung oder eine einfache Frage ist er überflüssig und macht die Antwort nur langsamer. Für alles, wo man selbst auch erst nachdenken müsste, lohnt er sich. Eine Faustregel: Würdest du für die Aufgabe einen Zettel und einen Stift nehmen, dann gib der KI auch einen.

MIRA: Und wenn ein Tool keinen Denkmodus hat?

JAN: Dann kannst du ihn ein Stück weit selbst herstellen. Schreib in den Prompt: „Überleg zuerst Schritt für Schritt, welche Punkte wichtig sind, und schreib erst dann die Antwort.“ Das ist ein alter Trick, der bei schwierigen Aufgaben immer noch hilft.

MIRA: Mir fällt dazu ein Beispiel aus dem Arbeitsalltag ein. Angenommen, ich lade eine Tabelle mit Monatszahlen hoch und frage: Warum ist der Umsatz im September eingebrochen? Was mache ich da am besten?

JAN: Drei Dinge. Erstens die Daten selbst mitgeben, nicht beschreiben. Zweitens den Kontext dazu: Was war im September los, gab es eine Aktion, eine Umstellung, ein technisches Problem? Das weiß das Modell nicht. Drittens um Denkschritte bitten: „Prüf zuerst, welche Kanäle betroffen sind, dann, ob es an der Zahl der Besucher oder an der Kaufquote liegt, und dann erst die Ursache.“

MIRA: Dann gibst du dem Modell quasi den Analyseweg vor.

JAN: Genau. Und das ist auch eine Absicherung gegen Halluzinationen. Wenn die KI ihre Zwischenergebnisse zeigt, siehst du sofort, an welcher Stelle sie falsch abbiegt.

MIRA: Bevor wir zur Übung kommen, noch eine Frage, die bestimmt viele haben: Sind die verschiedenen Modelle, also Claude, ChatGPT, Gemini, im Grunde alle gleich gebaut?

JAN: Vom Grundprinzip her ja. Alle sind Vorhersage-Maschinen mit einem Kontextfenster. Die Unterschiede liegen im Training, also worauf sie besonders gut getrimmt wurden, im Charakter, also wie sie schreiben und wie vorsichtig sie sind, und vor allem in dem, was drumherum gebaut ist. Welche Werkzeuge kann das Modell benutzen? Kann es im Web suchen, Dateien erstellen, mit deinem Kalender oder Postfach arbeiten, Aufgaben nach Zeitplan ausführen?

MIRA: Also eher das Werkzeug drumherum als das Gehirn selbst.

JAN: Bei den Spitzenmodellen sind die Unterschiede im reinen Denken inzwischen oft kleiner als die Unterschiede in der Ausstattung. Darüber machen wir eigene Folgen, weil das genau die Frage ist, welches Werkzeug für welche Aufgabe am besten passt.

MIRA: Da freue ich mich schon drauf. Und jetzt die Übung für heute.

JAN: Die Übung heißt „Schreibtisch-Check“. Nimm dir heute eine Aufgabe, die du sowieso mit KI erledigen wolltest. Eine Mail, eine Zusammenfassung, eine Recherche. Bevor du den Prompt abschickst, stell dir eine Frage: Wenn ein kluger neuer Kollege nur diesen Text bekommen würde und sonst gar nichts, könnte er die Aufgabe gut erledigen?

MIRA: Und wenn nicht?

JAN: Dann ergänze genau das, was dem Kollegen fehlen würde. Wer ist der Empfänger, was ist das Ziel, wie soll es klingen, gibt es ein Beispiel. Und schreib ans Ende: „Wenn dir etwas fehlt, frag nach, bevor du anfängst.“

MIRA: Und als Bonus: Schick denselben Auftrag einmal in der kurzen, ursprünglichen Version und einmal in der ergänzten Version ab, jeweils in einem neuen Chat. Vergleich die beiden Ergebnisse. Dieser Unterschied macht das Prinzip greifbarer als jede Erklärung.

JAN: Das dauert fünf Minuten und bringt mehr als eine Stunde Prompt-Listen lesen.

MIRA: In der nächsten Folge geht es um den Aufbau eines richtig guten Prompts. Welche Bausteine es gibt, in welcher Reihenfolge sie Sinn ergeben, und warum ein bisschen Struktur, zum Beispiel mit klaren Abschnitten, so viel bewirkt.

JAN: Danke fürs Zuhören und viel Spaß beim Schreibtisch-Check.

MIRA: Bis morgen in der KI-Werkstatt.
