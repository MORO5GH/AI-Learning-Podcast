# Klöbels KI-News – Ausgabe 5 vom 02.11.2026

LENA: Elf Stunden. So lange lag im Erweiterungsmarkt des Code-Editors Cursor eine gefälschte Claude-Code-Erweiterung.

TOM: Und wer sie in dieser Zeit installiert hat, hat sich eine Hintertür auf den Rechner geholt. Laut Cursor sind bis zu fünftausend Nutzer betroffen.

LENA: Außerdem: Aus Claude Max zwanzig x wird Ultra, ChatGPT stellt auf ein gemeinsames Token-Budget um, und die großen KI-Anbieter einigen sich auf ein Signal gegen KI-Training in der robots punkt txt.

TOM: Dazu die Computerbedienung in der Gemini-Schnittstelle, die jetzt allgemein verfügbar ist.

LENA: Das ist Klöbels KI-News vom Montag, 2. November 2026. Ich bin Lena.

TOM: Und ich bin Tom. Wir schauen aufs Wochenende, also Freitag bis Sonntag. Und eine Meldung vom Donnerstag nehmen wir mit, weil sie erst am Freitag bekannt wurde.

LENA: Das ist die mit der Erweiterung. Was genau ist passiert?

TOM: Am Donnerstag, dem neunundzwanzigsten Oktober, tauchte im Erweiterungsmarkt von Cursor eine Version der Claude-Code-Erweiterung auf, die nicht von Anthropic stammte. Betroffen ist laut Cursor die Version zwei Punkt eins Punkt drei eins drei, manche Berichte nennen auch die Version davor. Sie war laut Cursor etwa elf Stunden verfügbar. Berichtet hat am Freitag unter anderem Help Net Security. Entdeckt hat das Ganze die Sicherheitsfirma Phorion.

LENA: Was hat die gefälschte Erweiterung gemacht?

TOM: Sie lief sofort los, ohne dass man etwas anklicken musste. Sie hat einen fremden SSH-Schlüssel auf dem Rechner hinterlegt. SSH ist der Zugang, über den man einen Rechner aus der Ferne steuert. Dann hat sie eine Verbindung zum Server des Angreifers aufgebaut, und zwar so, dass sie auch nach dem Schließen des Editors weiterläuft und nach einem Neustart wiederkommt. Außerdem hat sie Rechnername, Benutzername, die Git-E-Mail-Adresse und die öffentliche IP-Adresse verschickt. Und die Namen von bis zu vierzig Umgebungsvariablen, die nach Zugangsschlüsseln aussehen. Die Namen, nicht die Inhalte.

LENA: Betrifft das auch Visual Studio Code direkt?

TOM: Laut Help Net Security gab es im offiziellen Marktplatz von Microsoft keine verseuchte Version. Betroffen sind Editoren, die auf Visual Studio Code aufbauen und einen eigenen Marktplatz nutzen, vor allem Cursor. Cursor will die Betroffenen direkt anschreiben.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du Cursor nutzt und am Donnerstag die Claude-Code-Erweiterung installiert oder aktualisiert hast, reicht Deinstallieren nicht. Die Hintertür läuft unabhängig weiter. Schau in die Datei mit den erlaubten SSH-Schlüsseln, ob dort ein Eintrag namens s v c Bindestrich telemetry steht. Cursor hat Aufräumskripte für Mac und Windows veröffentlicht. Und dann alle Zugangsdaten tauschen, an die dieser Rechner herankam. Für dich heißt das konkret: Shop-Zugänge, Tracking-Konten, Schlüssel für Schnittstellen und Zapier-Verbindungen. Grundsätzlich gilt: Erweiterungen für Programmierwerkzeuge haben weitreichende Rechte auf deinem Rechner. Automatische Updates sind bequem, aber genau darüber kam hier der Schadcode.

LENA: Bleiben wir bei Anthropic, aber bei einem erfreulicheren Thema. Was ändert sich bei den Claude-Tarifen?

TOM: Am Freitag hat Anthropic die beiden Max-Tarife umbenannt. Max fünf x für hundert Dollar im Monat heißt jetzt einfach Max. Max zwanzig x für zweihundert Dollar heißt jetzt Ultra. Die Preise bleiben gleich, bestehende Abos werden automatisch umgestellt.

LENA: Nur ein neuer Name?

TOM: Nein, bei Ultra fällt für verifizierte Konten das Fünf-Stunden-Limit weg. Bisher gab es bei Claude zwei Grenzen: ein Kontingent, das sich alle fünf Stunden erneuert, und eins pro Woche. Bei Ultra bleibt nur noch die Wochengrenze. Die liegt laut Hilfeseite von Anthropic beim Zehnfachen des Pro-Tarifs. Dazu kommt eine eigene Wochengrenze für das Modell Fable.

LENA: Wie wird man verifiziert?

TOM: Automatisch. Anthropic prüft laut Hilfeseite zum Beispiel, wie alt das Konto ist und wie die Zahlungen bisher liefen. Man muss nichts tun. Ob es geklappt hat, siehst du in den Einstellungen unter Nutzung. Steht dort kein Balken für die aktuelle Sitzung mehr, ist das Konto verifiziert. Neue Ultra-Konten haben die Fünf-Stunden-Grenze zunächst noch. Mehrere Berichte deuten das als Maßnahme gegen weiterverkaufte oder geteilte Zugänge. Das ist aber eine Einschätzung von außen, Anthropic selbst sagt dazu nichts.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du mit Max zwanzig x gearbeitet hast, bist du jetzt bei Ultra. Der Ärger mit der Sperre mitten am Vormittag, wenn ein langer Cowork-Auftrag oder eine Analyse viel verbraucht hat, sollte damit vorbei sein. Die Woche als Ganzes musst du aber weiter im Blick behalten. Wer am Montag sehr viel verbraucht, hat am Freitag weniger übrig. Und für geplante Aufgaben, die nachts laufen, ist das praktisch: Die verteilen sich jetzt nicht mehr auf Fünf-Stunden-Fenster.

LENA: Dann zu OpenAI. Da geht es auch um Kontingente, aber in die andere Richtung, oder?

TOM: Eher ja. The Decoder hat am Sonntag zwei Änderungen zusammengefasst, die OpenAI auf seinen Hilfeseiten beschreibt. Erstens: Ab Dezember legt ChatGPT die Bereiche Chat und Work zusammen. Work ist der Bereich, in dem ChatGPT als Agent selbständig Aufgaben erledigt. Plus, Pro und Business bekommen dann ein gemeinsames Budget auf Basis von Token für ChatGPT und für Codex, das Programmierwerkzeug.

LENA: Token, also die Textbausteine, nach denen Sprachmodelle abrechnen.

TOM: Genau. Aufwendigere Modelle und längere Aufgaben verbrauchen mehr davon. Einfache, schnelle Chats zählen laut The Decoder nicht mit. Wie viel übrig ist und wann es sich erneuert, soll in den Einstellungen stehen. Ist das Budget leer, kannst du warten, den Tarif wechseln oder Guthaben nachkaufen. Für Pro und Business hatte OpenAI das Kontingent erst am neunundzwanzigsten Oktober verdoppelt, bei Business im Premium-Tarif.

LENA: Und die zweite Änderung?

TOM: OpenAI begrenzt, wie viele bezahlte Konten man auf einem Gerät und mit einer Zahlungskarte nutzen kann. Das gilt für Go, Plus und die Pro-Tarife, nicht für kostenlose Konten und nicht für Business, Enterprise oder Edu. Wer an die Grenze stößt, sieht die Meldung „Device limit reached“, also Gerätegrenze erreicht. Das zielt laut The Decoder auf Leute, die zwischen mehreren günstigen Abos hin und her springen, um mehr Nutzung herauszuholen.

LENA: Und was heißt das für die Praxis?

TOM: Wenn du ChatGPT neben Claude für Kundenarbeit nutzt, rechne ab Dezember damit, dass aufwendige Aufgaben schneller am Limit sind. Die einfache Faustregel: Für schnelle Fragen das schnelle Modell, für lange Rechercheaufträge gezielt das teure. Und falls du mit Kunden zusammen ein Gerät nutzt, auf dem mehrere bezahlte Konten angemeldet sind, etwa bei einem Workshop, könnte die Gerätegrenze stören. Business-Konten sind davon ausgenommen.

LENA: Jetzt ein Thema, das deine Shop-Kunden direkt betrifft. Was hat es mit der robots punkt txt auf sich?

TOM: Die robots punkt txt ist die kleine Textdatei auf jeder Website, in der steht, welche Suchmaschinen und Programme welche Seiten abrufen dürfen. Am Freitag haben OpenAI, Google, Microsoft und Anthropic angekündigt, ein gemeinsames Kennzeichen zu unterstützen. Damit kann ein Seitenbetreiber sagen: Meine Inhalte bitte nicht zum Training von KI-Modellen verwenden. Berichtet hat The Verge. Grundlage ist ein Entwurf bei der IETF, dem Gremium für Internetstandards. Verfasst hat ihn ein Mitarbeiter von Anthropic.

LENA: Wie sieht das aus?

TOM: Man trägt einen eigenen Namen als Programmkennung ein, usage ai training, mit zwei Unterstrichen davor, und verbietet dann den Zugriff. Wichtig ist der Unterschied: Das Signal regelt nur das Training. Es ist laut den Berichten keine Anweisung zum Abrufen von Seiten. Die Programme dürfen eine Seite also weiterhin lesen, etwa um sie in einer KI-Antwort zu zitieren. Microsoft plant dafür eine eigene, getrennte Einstellung.

LENA: Ab wann gilt das?

TOM: Unterschiedlich. Anthropic hat laut AI Weekly schon mit der Umsetzung begonnen. OpenAI will es in den kommenden Monaten umsetzen, Microsoft ab dem ersten Februar zweitausendsiebenundzwanzig, Google im Lauf des Jahres zweitausendsiebenundzwanzig. Google behandelt das neue Signal dann so, als hätte die Seite den bisherigen Google-Eintrag für KI-Training gesperrt. Zwei Einschränkungen: Es ist noch kein fertiger Standard, und Programme, die sich nicht daran halten, hält es nicht auf. OpenAI nennt es selbst ein Mittel zur Abstimmung, keine Sicherheitsmaßnahme. Und Daten, die schon gesammelt wurden, bleiben gesammelt.

LENA: Und was heißt das für die Praxis?

TOM: Für deine Kunden ist das eine Abwägung, die sie bewusst treffen sollten. Ein Onlineshop will in der Regel, dass KI-Assistenten seine Produkte kennen und empfehlen. Wer pauschal alle KI-Programme aussperrt, riskiert, in KI-Antworten nicht mehr aufzutauchen. Das neue Signal erlaubt eine feinere Lösung: Training ablehnen, Abruf für Antworten erlauben. Zum Beispiel für Ratgebertexte oder eigene Studien, die ein Kunde schützen will, während Produktseiten offen bleiben. Ich würde jetzt noch nichts ändern, aber die robots punkt txt deiner Kunden auf die Liste für das nächste Quartal setzen.

LENA: Dann zu Google. Was ist neu in der Gemini-Schnittstelle?

TOM: Laut den Versionshinweisen der Gemini-Schnittstelle ist das Werkzeug für Computerbedienung seit Freitag allgemein verfügbar, also keine Vorschau mehr. Damit kann ein Programm Gemini einen Bildschirminhalt zeigen, und Gemini schlägt den nächsten Schritt vor: hier klicken, dort etwas eintippen. Das Programm führt den Schritt aus, schickt den neuen Bildschirm zurück, und so weiter. Für heikle Aktionen sind Bestätigungen vorgesehen. Die Schutzmaßnahmen müssen die Entwickler aber selbst einbauen.

LENA: Ist das für dich als Nutzer interessant oder nur für Entwickler?

TOM: Erst einmal für Entwickler. Für dich wird es indirekt spannend. Allgemein verfügbar heißt bei Google, dass Firmen das in fertige Produkte einbauen dürfen. Viele Shop-Backends, Werbekonten und Feed-Tools haben keine Schnittstelle für jede Funktion. Ein Agent, der die Oberfläche bedient wie ein Mensch, kann diese Lücke füllen. Das gilt genauso für die vergleichbaren Funktionen bei Anthropic und OpenAI. Hier sind jetzt alle drei großen Anbieter mit einem Angebot dabei.

LENA: Und was heißt das für die Praxis?

TOM: Wenn dir ein Anbieter in nächster Zeit ein Werkzeug verkauft, das selbständig in deinem Werbekonto oder deinem Shop-System klickt, frag nach, welche Bestätigungen eingebaut sind. Bei Google liegt das ausdrücklich beim Entwickler. Ein Agent, der ohne Rückfrage Gebote ändert oder Produkte löscht, ist ein Risiko.

LENA: Zum Schluss noch eine Datenschutz-Meldung von OpenAI. Worum geht es?

TOM: Laut The Decoder vom Samstag will OpenAI ab dem neunundzwanzigsten November Daten aus einem speziellen Programm für Sicherheitsforscher zum Training nutzen. Das betrifft Sitzungen mit Daybreak Blue, einem Angebot für Teilnehmer des Programms für vertrauenswürdigen Zugang, und zwar auch dann, wenn die Teilnehmer das Training in den Einstellungen abgeschaltet hatten. Nach heftiger Kritik hat OpenAI eine zweite Mail verschickt und eine eigene Möglichkeit zum Widerspruch angekündigt. Wie die aussieht, ist noch offen.

LENA: Betrifft dich das?

TOM: Direkt nicht, das ist ein kleiner Kreis von Fachleuten. Die Lehre ist trotzdem allgemein. Eine Einstellung wie „nicht für Training verwenden“ gilt so lange, wie der Anbieter seine Bedingungen nicht ändert. Wenn du Kundendaten über einen KI-Dienst verarbeitest, lohnt es sich, Mails mit geänderten Nutzungsbedingungen tatsächlich zu lesen. Und für wirklich sensible Daten sind Business- oder Enterprise-Verträge mit fest zugesagtem Trainingsausschluss die sicherere Wahl.

LENA: Worauf sollte man in den nächsten Tagen achten?

TOM: Ob Cursor und Anthropic weitere Details zur gefälschten Erweiterung nennen, vor allem dazu, wie sie in den Marktplatz gelangt ist. Und am neunundzwanzigsten November der Stichtag bei OpenAI: Bis dahin sollte klar sein, wie der angekündigte Widerspruch funktioniert.

LENA: Das waren Klöbels KI-News. Bis Mittwoch.
