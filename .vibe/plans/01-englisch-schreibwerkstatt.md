---
# Read by the hooks, the review, the evals. Schema: @lernapps/tooling/guidance/plan-front-matter.v1.schema.json
# Written by `lernapps plan` and the hooks. Never change a key or a value by hand.
# Archetype, null until chosen in Explore. Allowed values: explainer, interactive, quiz.
archetype: explainer
# Current phase. Allowed values: explore, plan, code, commit.
phase: commit
# prePushFailures: failed pre-push runs, written by the hook.
prePushFailures: 0
# failedChecks: failed rules and runs, written by lernapps check and the hooks.
failedChecks: {}
---

# Plan: englisch-schreibwerkstatt, first version

<!--
For you, the assistant. The process is in AGENTS.md; this plan holds the method.
- `npx --no -- lernapps plan next` prints the task to do now, `plan done` ticks it and prints the next one.
- You write only below Goal, Key decisions, Notes, Answers, Entry draft, Content method and Retrospective, in the
  creator's language. Delete the comment of a section once the section is filled.
- Work on the branch `work`, locally: push nothing before Commit.
-->

*Started 2026-11-24. Explore, Plan, Code, Commit.*

## Goal

Die Lernenden schreiben Sachtexte nach einem Bauplan (Einleitung, Hauptteil, Schluss; headline, lead, body; Anrede, Anliegen, Gruß), stellen den Ton zwischen informal und formal ein, durchschauen Zeitungstexte und Statistiken und bewerben sich am Ende um einen Ferienjob. Der rote Faden ist die Schülerzeitung der Millbrook School.

## Key decisions

- Archetyp `explainer`, Einheiten-App (`subject: englisch`, Format 2): Seiten erklären, Lesestück, Übungen dazwischen; die Karte hat `explainerFocus: competency`.
- Alle 17 Bausteine des Auftrags auf je einer eigenen Seite, vier Kapitel wie im Issue (Stufe 7-8: Kapitel 1-2, Stufe 9-10: Kapitel 3-4).
- Jede Seite hat ein Lesestück (Konventionen §8): 7-8 etwa 150 bis 300 Wörter, 9-10 etwa 300 bis 600; Randglossar, Aufgaben in drei Stufen (Verstehen, Belegen mit Zeile, Meinung), Schreib- oder Sprechauftrag.
- Zwei feste Bilder tragen die App: der **Bauplan** (Schablone mit festen Teilen, je Textsorte) und der **Ton-Regler** (informal · neutral · formal). Beide als eigene SVG-Zeichnungen, keine Komponente (`prefer-built-in-block`).
- Rote Fäden: Kapitel 1-2 die Schülerzeitung „The Millbrook Messenger“ (Chat- und Nachrichtenform mit Sophie, Ellie, Peter, Amir, Mr Hill, Mrs Parker); Kapitel 3 erfundene Zeitungs- und Statistiktexte ohne erfundene Kinder; Kapitel 4 der Ferienjob (Sophie und Amir bewerben sich, Texte als Dokumente). (guess: Name der Zeitung und die Stellen „library assistant“ und „bakery helper“ nach dem Stadtplan #478)
- Keine Figuren-Einführung im Seitentext: keine Altersangaben, keine Familie, kein Datum; die Startseite nennt nur Namen und Rollen. Anrede „du“ (guess: auch in 9-10).
- Wiederholungsseiten (`recap`) je Kapitel für Bausteine anderer Explainer; zwei Lücken der Karte (`perspektive-wechseln`, `schule-usa`) sind in keiner App geübt: ein kurzer Absatz im Sammel-Recap (guess, im Checkpoint gemeldet).
- Hörtexte `bf_emma`: Diktat und Nachsprechen je Seite, Lesestücke nur in kurzen Abschnitten; Hörurteile bestätigt der Orchestrator.
- Look and feel: fixed by the archetype (Look der Laufzeit, ruhig wie ein Arbeitsblatt, Dunkelmodus folgt dem Gerät).
- `scope`: ja, in `app.yaml` und auf jeder Seite (die App hat `open-task`; der Tutor beurteilt offene Antworten nach dem Scope).
- Sprachen: nur Deutsch (Erklärtexte), englische Beispiele und Lesestücke (Einheiten-Apps der Reihe, `languages: [de]`).

## Notes

**Fach statt Strang:** Einheiten-App `subject: englisch` über die Stränge `texte`, `wortschatz` und `landeskunde` der Karte (`explainerFocus: competency`); jede Seite übt Bausteine eines Strangs. Alle 17 sind Lücken der Karte (`practisedBy` leer). Karte gelesen am 2026-11-24.

**Kapitel, Seiten, Karten-Ids** („Ich kann“-Sätze wie auf der Karte; Seite = Datei `<kapitel>/<seite>.yaml`; Reihenfolge nach `requires`):

1. `gliedern-und-ton` · 7-8 · Recap `kurzformen` (`das-brauchst-du`)
   - `text-gliedern` (texte, Schritt 1): Einleitung, Hauptteil, Schluss, Absätze. Musterseite.
   - `formell-informell` (wortschatz, 1): der Ton-Regler. Vor `praesentation`/`blog-post` gezogen (guess; `requires` erlaubt es: der Regler wird einmal eingeführt, danach auf zwei Seiten benutzt).
   - `praesentation` (texte, 2): Vortrag, Redemittel einleiten, überleiten, abschließen; derselbe Inhalt wie der Blog, neutral.
   - `blog-post` (texte, 2): Blogbeitrag und Forenkommentar, informal.
2. `fuer-die-schuelerzeitung` · 7-8 · Recap `simple-past`, `fragewoerter`, `alltagstexte`, `figuren-ort-handlung`, `perspektive-wechseln` (`das-brauchst-du`)
   - `bericht-artikel` (texte, 2), `interview` (texte, 1), `sachtext-fiktion` (texte, 1), `textsorte-umwandeln` (texte, 3): Geschichte aus #479 in die Berichts-Schablone.
3. `zeitung-und-statistik` · 9-10 · Recap `vergleiche`, `zahlen`
   - `zeitungsartikel` (texte, 1), `information-meinung` (texte, 2), `diagramm-beschreiben` (texte, 1).
4. `bewerben` · 9-10 · Recap `email-postkarte`, `datum`, `schule-usa`
   - `berufswelt` (wortschatz, 1), `bildungssystem` (landeskunde, 1), `formelle-email` (texte, 1), `lebenslauf` (texte, 2), `bewerbung` (texte, 3), `vorstellungsgespraech` (texte, 4).

Insgesamt 17 Übungsseiten und 4 Wiederholungsseiten. Außerhalb liegende Voraussetzungen: `kurzformen` (englisch-klang-schrift), `simple-past` (englisch-zeiten), `fragewoerter` (englisch-saetze-bauen), `alltagstexte` (englisch-grossbritannien), `figuren-ort-handlung` (englisch-geschichten), `vergleiche` (englisch-adjektive-adverbien), `zahlen` und `datum` (hello-millbrook), `email-postkarte` (englisch-alltag). **Zwei sind selbst Lücken ohne App:** `perspektive-wechseln` (texte 7-8, geplant als Kapitel 5 von #479) und `schule-usa` (landeskunde 7-8, #478, Stufe 7-8 später). Beide stehen im Sammel-Recap mit einem kurzen Absatz (guess); Rückfrage an die Orchestrator-Session im Checkpoint.

**Didaktik (Wie kommen die Lernenden dahin, Fehlerbild):**
- `text-gliedern`: sie legen die Schablone auf einen ungegliederten Text und sortieren Sätze nach Einleitung, Hauptteil, Schluss (nicht nur lesen); Fehler: Schluss führt neue Argumente ein, ein Absatz mit zwei Ideen.
- `formell-informell`: sie schieben denselben Satz auf dem Regler und finden die Wörter, die sich ändern (Kurzformen, phrasal verbs, Anrede); Fehler: Slang in formeller Mail, „Dear Sir“ gemischt mit „Hi“.
- `praesentation`: sie ordnen Redemittel den drei Teilen zu und schreiben einen Einstieg zu einem Thema; Fehler: Vorlesen statt Sprechen (Hinweis), kein Übergang.
- `blog-post`: sie wählen aus einem Entwurf Titel, Einstieg, Persönliches, Aufruf zur Antwort; Kommentar im Forum: Bezug zum Beitrag; Fehler: zu formal, kein Bezug.
- `bericht-artikel`: sie füllen die W-Fragen in die Schablone und schreiben im simple past; Fehler: present statt past, Meinung im Bericht.
- `interview`: sie machen aus Stichpunkten offene Fragen und schreiben ein Interview als Text (Q/A); Fehler: Ja-Nein-Fragen, falsche Wortstellung.
- `sachtext-fiktion`: sie prüfen Textpaare (Merkmale: Fakten, Quelle, Erzählstimme, wörtliche Rede); Fehler: „steht in der Zeitung, also wahr“.
- `textsorte-umwandeln`: sie gießen eine Geschichte (aus #479) in die Berichtsschablone: Wer/Wo/Wann/Was, Meinung und wörtliche Rede raus; Fehler: Erzählstil bleibt.
- `zeitungsartikel`: sie legen die Schablone auf erfundene Artikel: headline, lead, body, Zitate; Bericht und Kommentar unterscheiden; Fehler: lead ohne die wichtigsten W-Fragen.
- `information-meinung`: Farbstift-Prinzip (Auswahl der Sätze), Signalwörter, Quelle, Nachrichten prüfen; Fehler: „ich finde“ ist nicht das einzige Signal (Adjektive wie „shocking“).
- `diagramm-beschreiben`: Balken- und Liniendiagramm mit Vergleichen und Zahlen beschreiben; Fehler: Zahlen vorlesen statt Entwicklung benennen, falsche Präposition (increase to / by).
- `berufswelt`: Berufe, Praktikum, Ferienjob; Fehler: job/work, a/an vor Beruf.
- `bildungssystem`: UK und USA mit Deutschland vergleichen (Year 11 / GCSE / sixth form / A-levels; grades 9 bis 12 / high school diploma / GPA); Fehler: Gleichsetzen von Namen (college ≠ Hochschule im UK).
- `formelle-email`: Anrede, Anliegen, Gruß (Dear Ms/Mr … Yours sincerely/faithfully); Fehler: Kurzformen, Hi, falscher Gruß.
- `lebenslauf`: sie ordnen Angaben in die CV-Schablone und schreiben Zeilen; Fehler: Foto, Alter und Familienstand (im UK nicht üblich), Fließtext.
- `bewerbung`: Schablone (Anlass, Eignung, Bezug zur Stelle, Schluss); Fehler: Lebenslauf wiederholen, kein Bezug zur Stelle.
- `vorstellungsgespraech`: typische Fragen, Antwort mit Beispiel (STAR gekürzt), Rollenspiel mit Sprechauftrag; Fehler: Ein-Wort-Antworten.

**Übungsmuster** (Skills exercise-patterns, foreign-languages): Schablone füllen (`ordering`, `matching`), Regler zuordnen (`single-choice` mit `info` je Option, `matching` informal ↔ formal), Lücke (`language-task` gap), Schreiben mit Cue (`write`), Diktat und Nachsprechen, offene Aufgabe (`open-task` mit `points` und Musterlösung), Belegen mit Zeile (`single-choice` / `multiple-choice` mit Zeilenangabe), Meinung (offene Aufgabe). Lesestück als `text`-Blöcke in Abschnitten mit Randglossar; Details im Inhaltsführer.

**Umfang:** In: alle 17 Bausteine, Texte im Stil Chat, Blog, Bericht, Interview, Artikel, Diagramm, E-Mail, CV, Bewerbung, Gespräch. Out (Abgrenzung): persönliche Briefe (#477), Geschichten (#479), Leserbrief und Kommentar als Meinungstext (#487), Vorstellung von Berufsbildern jenseits der Wörter; keine Bewertung freier Texte und der Aussprache durch die App. Daten: Statistiken sind erfunden (kleine Tabellen, 4 bis 6 Werte), Zeitungstexte erfunden. Sprachen: Deutsch (Erklärtext), Englisch (Beispiele, Lesestücke), britisches Englisch.

**Prüfungen und Funde (Gesamtcheck der App, Code-Phase):** Lerner-Check der Musterseite (Sub-Agent, Klasse 7-8): Lösungen im Merke, Bildtext, Hinweise zu Ordnen und Lücke, Distraktor „Titel“, Varianten „Firstly/Secondly“ behoben. Gesamtcheck der fertigen App mit Sub-Agenten: Kapitel 1-2 als Lerner der Klasse 7 und Kapitel 3-4 als Lerner der Klasse 9-10; dazu je eine Prüfung der englischen und der deutschen Sprache. Behoben: Ablauf der Geschichte in Kapitel 4 (Reihenfolge Anzeige, Rat, Nachricht, E-Mail, CV, Brief, Gespräch), Alter und Zeiträume im CV, Gruß zur Anrede, fehlender Satz „Next, when the newspaper will come out“, „Mrs“ → „Ms“, deutsche Wörter in englischen Zeilen („Sophie to Ellie:“), Fakten zu England statt Großbritannien, `By`/`to` und Gaming im Diagramm, Einleitung mit „wenigen Sätzen“, Begriffe (Aussage, Redemittel, Einleitung), Rückmeldungen mit der richtigen Form, Archiv → Schulbibliothek, fünf W-Fragen einheitlich, unpassende oder fast gleiche Hörsätze ersetzt (zehn Sätze neu erzeugt, alle mehrsilbig endend); Lizenzmarke verdeckt keine Diagrammbeschriftung mehr. Nicht geändert: „Danach kannst du …“ in den Einstiegen (Stilfrage), „Erzählstil/Erzählstimme“, einzelne Sachwörter ohne Randglossar in Hörsätzen. Offen für die Ersteller:in: kein Hörurteil über die neuen Hörsätze (nichts Ungehörtes gilt als geprüft); Namen erfundener Orte (Tarnwick, Brindley, Marsden …) nicht auf zufällige Echtheit geprüft; Sachaussagen ohne geöffnete Quelle (Merkmale Sachtext/Fiktion, Aufbau Interview, indirekte Rede, grade 9 = Year 10).

**Quellen** (nur Fakten, geöffnet am 2026-11-24 über `en.wikipedia.org`, CC BY-SA, keine Sätze übernommen): „Education in England“ (Key Stages, Year 11, GCSE, Pflicht bis 18, sixth form, A-levels), „High school in the United States“ (grades 9 bis 12, freshman bis senior, GPA, Credits), „Education in the United Kingdom“, „Key Stage“, „Résumé“ (CV im Vereinigten Königreich: keine persönlichen Angaben wie Foto, Geschlecht, Familienstand), „Cover letter“, „Job interview“. Nicht geöffnet (HTTP 429): „Inverted pyramid (journalism)“: wird beim Bau von `zeitungsartikel` neu versucht; sonst Aufbau (headline, lead, body) aus dem Auftrag. Keine VOA- und Wikinews-Texte übernommen (alle Lesestücke eigene Texte). Alle Fakten, die ein Lesestück nennt (zum Beispiel Schulsystem), stehen im Inhaltsführer unter „Sources“.

## Explore

<!--
- Find out what the app teaches, for whom, how much and how it looks. Ask; write no code, run no `create`.
- An answer counts only in the creator's words under "Answers". At most 2 questions per message, one topic each.
-->

### Tasks

- [x] Check the start: the folder `.agents/skills/lernapps-app` exists (else stop and tell the creator that the folder
      was not started with `init`), and `git branch --show-current` prints `work` (else `git switch -c work`).
- [x] Load skill `lernapps-app`. Tell the creator in two sentences what a lernapps app is and where it will live: at
      their own address, free and public, and once listed as a copy on lernapps.net. Say that the technical part
      (GitHub) comes at the end and that you do it.
- [x] Interview: ask the topics "Goal" and "Learners" of "Answers".
- [x] Load skill `lernapps-map-assignment` and read the learning map of the subject as it says. The creator brings
      the content themselves (material, a word list, the pages): note under "Notes" which competencies of the map it
      covers. Else write the skill's assignment, with its story; the creator's yes answers the topics Content and
      Amount. A subject without a map: skip this task and say so.
- [x] Load skill `lernapps-exercise-patterns` and read its reference for the subject. Note under "Notes" how learners
      will practise what the goal names.
- [x] Choose the archetype as skill `lernapps-app` says: read the README of each archetype in question, then tell the
      creator in plain words what the chosen one can and cannot do. Write the archetype and its reason under "Key
      decisions".
- [x] Run `npx --no -- lernapps skills --archetype <name>` with the chosen archetype. It installs the archetype's
      skills and adds the archetype's tasks to this plan.
- [x] Load skill `lernapps-explainer-design`. An explainer has the look of the runtime: write "fixed by the
      archetype" under the topic "Look and feel" of "Answers".
- [x] Interview: ask every other topic of "Answers", in order. Leave out only a topic that an answer of the creator
      already covers, and note which answer. A topic nobody answered is asked once before you write an assumption
      with "(guess)".
- [x] Load skill `lernapps-content-research` and research as it says. Write under "Notes": the strand or subject, the
      competencies by chapter with their ids, the sources you opened.
- [x] Write under "Notes" which competency goes on which page and which pages form a chapter, as "Map the content" of
      skill `lernapps-explainer-design` says. Per page, name the prerequisites the app does not practise.
- [x] Write under "Notes", one line per competency: how learners get there (they derive it, they do not only read it
      off), and which misconception the feedback catches.
- [x] Write under "Notes" the scope: what is in, what is out and why, the data range (for example "all main-group
      elements", never a silent "1–20"), the languages.
- [x] **Checkpoint:** research. Show in plain words: the strand or why none, the competencies by chapter, the didactic
      approach, the scope, every "(guess)", the sources and what is unchecked, the archetype and its reason. Stop and
      wait. Changes: change them, then ask again.
      Creator: Zuschnitt passt. 1 ja. 2 Recap nur für Bausteine, die eine App übt; perspektive-wechseln und schule-usa weglassen, wenn die Seite sie nicht braucht, sonst kurzer eigener Absatz ohne Übung, kein ahead. 3 Rote Fäden ok; Kapitel 4 keine erfundenen Kinder, nur Sophie als Stimme (library assistant), Amir als bakery helper streichen; Millbrook Messenger nur Kapitel 1-2. Du-Anrede auch 9-10 ok. 4 Inverted pyramid später erneut öffnen oder weglassen.

### Answers

<!-- The interview: per topic the creator's answer, in their words. Keep the topics. -->

Quelle der Antworten: der Auftrag der Orchestrator-Session (Issue lernapps/apps#486, unverändert) und die Startnachricht; die Ersteller:in selbst wurde nicht befragt, die Orchestrator-Session beantwortet die Checkpoints.

- Goal: „Ich kann Sachtexte für die Schule, die Öffentlichkeit und eine Bewerbung nach einem Bauplan schreiben, den Ton passend wählen und Zeitungstexte durchschauen.“ (Leitidee des Issues)
- Learners: Englisch, Stufe 7-8 (Kapitel 1-2) und 9-10 (Kapitel 3-4); Vorwissen aus den Explainern der Reihe (simple past, Fragewörter, Vergleiche, Kurzformen, E-Mail, Datum, Zahlen).
- Model and focus: die Vorgänger der Reihe (`englisch-geschichten`, `englisch-saetze-verbinden`, `englisch-adjektive-adverbien`, `englisch-pronomen`); Schwerpunkt: Schablone und Ton-Regler, Lesestück und Schreibaufträge.
- Hurdles: Ton nicht passend (Kurzformen und Slang in der formellen E-Mail, steife Sprache im Blog), Gliederung ohne Absätze, Meinung im Bericht, Diagramm nur abgelesen statt Entwicklung benannt, Lebenslauf als Fließtext, Bewerbung ohne Bezug zur Stelle.
- Content: eigene Texte nach Fakten (Konventionen §8), Quellen im Inhaltsführer; Zeitungs-, Statistik- und Bewerbungstexte erfunden, nichts über echte Personen oder Firmen. Kein Material der Ersteller:in.
- Amount: alle 4 Kapitel, 17 Bausteine in der ersten Version (Auftrag der Startnachricht).
- Languages: nur Deutsch mit englischen Beispielen (wie die Vorgänger der Reihe).
- Look and feel: fixed by the archetype.
- Terms: Schablone → „Bauplan“; „Ton-Regler“ (informal, neutral, formal); „Lesestück“; „Ausdruck“ (nie „Wendung“); Begriffe headline, lead, body, noun, verb, sentence.
- Finding the app: Englisch Sachtexte schreiben, Bericht, Interview, Zeitungsartikel, Diagramm beschreiben, Bewerbung, CV, Vorstellungsgespräch, Klasse 7 bis 10.

## Plan

<!--
- Map the confirmed content onto the archetype. No new content questions: a gap in the content goes back to Explore.
- The creator confirms the plan in one read. After the yes you work on your own.
-->

### Tasks

- [x] Map the content as "Map the content" of skill `lernapps-explainer-design` says, and write the result under
      "Content method".
- [x] Choose a pattern per competency as skill `lernapps-exercise-patterns` says, and add it to "Content method".
- [x] Add to "Content method" one line per page, as "Engagement" of skill `lernapps-explainer-design` says: the
      opening task, the change of activity, the reward, the story.
- [x] Add the tasks of Code, each one a piece of work that ends in a commit. First the pattern: one complete page or
      screen, `npx --no -- lernapps plan add --at pattern "<task>"`. Then the others, one call each:
      `npx --no -- lernapps plan add --at pages "<task>"`. Each task says what it builds and what it shows.
- [x] Draw a sketch of each screen, component or interactive exercise: a static SVG or image, or the steps with what
      learners see after each. Keep the files in `.vibe/sketches/`.
- [x] Show the creator, short: goal, competencies by chapter, the Code tasks, the sketches, and the content method in
      plain words (what learners see and do, what the app cannot do). At most 2 questions.
- [x] **Checkpoint:** confirm the plan and the content method. Stop and wait for an explicit yes. Changes: change
      them, then ask again.
      Creator: Ja, bestätigt. Baue die Musterseite gliedern-und-ton/text-gliedern, Lerner-Check, dann Checkpoint Musterseite. Danach Kapitel 2-4 mit Sub-Agenten nach dem Muster. Gemeinsame Dateien bleiben bei mir.

### Content method

<!-- One line each: the patterns and where; the figures and how they are made; the data files; each component, what it
checks and what it cannot; how a later agent adds a chapter. It becomes the content guide in Code. -->
<!-- An explainer: per figure, model and component its learning action in two to four sentences
(`explainer-representation-explained`); per page its prerequisites the app does not practise, and which get a recap
page, which a link. -->

**Zuschnitt (Map the content):** Einheiten-App `subject: englisch`; Kapitel und Seiten wie unter „Notes“. Jede Seite trägt genau einen Baustein (`competencies: [<id>]`, Id = Karten-Id), keine `ahead`. Wiederholungsseiten `das-brauchst-du` je Kapitel mit `recap: [englisch/<id>, …]` nur für Bausteine, die eine App übt (Kapitel 1: kurzformen; 2: simple-past, fragewoerter, alltagstexte, figuren-ort-handlung; 3: vergleiche, zahlen; 4: email-postkarte, datum). `perspektive-wechseln` (Kap. 2) und `schule-usa` (Kap. 4) sind in keiner App geübt: nicht im `recap`, bei Bedarf ein kurzer Absatz im Seitentext ohne Übung (Antwort der Orchestrator-Session). Keine Datendateien, keine Komponenten. Die Statistik in Kapitel 3 ist eine kleine `table` und ein Diagramm als eigene SVG.

**Seitenaufbau** (gleiche Abschnitts-IDs, `explainer-honest-headings`): `einstieg` (Vorwissen-Frage als erste Aufgabe, „Das kannst du danach“, Anschluss an die Seite davor) · `lesestueck` (Randglossar als `vocabulary` zuerst, dann der Text in 2 bis 3 Abschnitten mit nummerierten Zeilen, nach jedem Abschnitt eine Verstehensfrage) · `bauplan` (Merke und Bauplan- oder Regler-Figur; erklärt, was das Lesestück gezeigt hat) · `uebung` (4 bis 6 Aufgaben leicht → schwer: Belegen mit Zeile, Schablone füllen, Ton einordnen, schreiben mit Cue, Diktat) · `anwenden` (`open-task` mit `points` und Musterlösung, `speaking-task` wo Vortrag oder Gespräch dran ist; Meinung als freie Aufgabe) · `weiter`. Erklärtext ohne Lesestück höchstens etwa 350 Wörter, höchstens 4 Textblöcke hintereinander, Bild oder Übung in den ersten vier Blöcken, höchstens etwa 25 Items.

**Lesestück:** eigener Text, kein fremder Satz. Sorten: Chat, Nachricht, Blogeintrag, Redetext, Bericht, Interview, Artikel, Diagrammtext, E-Mail, CV, Brief, Dialog. Als `text`-Blöcke, Zeilen als nummerierte Liste (Zeile = Belegstelle). Kapitel 1-2: Chats und Nachrichten der Figuren, kein Bild, wo es nichts zeigt. Kapitel 3: erfundene Zeitungs- und Statistiktexte über erfundene Orte und Einrichtungen, keine erfundenen Kinder. Kapitel 4: Dokumente der Stimme „Sophie“ (library assistant) und erfundener Firmen, keine weitere erfundene Kinderfigur. Namen von Firmen, Orten und Personen erfunden (`no-learner-data-in-texts`).

**Figuren (SVG, eigene Zeichnungen, CC-BY-4.0):** Familie `bauplan-<textsorte>.svg` (feste Teile in fester Reihenfolge; Farben: Einleitung, headline, Anrede #6a4c93; Hauptteil, body, Anliegen #1b7f8a; Schluss, Gruß #b5651d; die Farben bedeuten nur das) und `ton-regler-<seite>.svg` (informal #d9822b, neutral #7f8c8d, formal #2c3e75; der Knopf steht je Seite anders). Hintergrund #f4efe2, Schrift mindestens 16 im 480er viewBox, Beschriftung im viewBox, `alt` nennt, was die Figur zeigt, nie die Lösung, Bildunterschrift sagt, worauf man schaut. Kapitel 3: `diagramm-<thema>.svg` (Balken oder Linie mit Achsen und Skala). Kein Foto, keine Figuren aus Büchern oder Filmen. Skizzen in `.vibe/sketches/`.

**Muster (Details im Inhaltsführer):** (1) Schablone füllen: `ordering` Teile, `matching` Satz ↔ Teil. (2) Ton einordnen: `single-choice` mit `info` je Option, `matching` informal ↔ formal. (3) Belegen mit Zeile: `single-choice`, `multiple-choice`, Zeilenangabe in der Aufgabe. (4) Schreiben mit Cue und Lücke: `language-task` (`write`, `gap`, `choice`), `form: { punctuation: ok }`, gleichwertige Antworten `(a|b)`. (5) Hören und Nachsprechen: `language-task` mit `audio`, `speaking-task`; ganze Sätze, `bf_emma`, Lesestücke nur in kurzen Abschnitten. (6) Anwenden: `open-task` mit `points`, `kind: form`, Musterlösung; die App bewertet nichts. (7) Diagramme: `single-choice` und `language-task` mit Diagramm im `material`. (8) Information und Meinung: `multiple-choice` „Welche Sätze sind Information?“ (der Farbstift als Auswahl). Nicht ausdrückbar und darum nicht gebaut: ein echter Farbstift im Text, Bewertung freier Texte, Aussprache; steht in `scope`.

**Typische Fehler (je eine Meldung):** Kurzformen und Slang in formellen Texten; „Dear Sir“ mit „Hi“ gemischt; Schluss mit neuem Argument; mehr als eine Idee je Absatz; present statt past im Bericht; Meinung im Bericht und im lead; Ja-Nein-Fragen im Interview; Zahlen vorlesen statt Entwicklung benennen, falsche Präposition (increase to/by); Foto, Alter und Familienstand im CV; Bewerbung wiederholt den Lebenslauf; Ein-Wort-Antworten im Gespräch; college mit Hochschule gleichsetzen.

**Wörter:** Quelle ist der Grundwortschatz Englisch (A1/A2) unter `https://lernapps.net/apps/map/englisch/grundwortschatz/`. Stufe 7-8 und 9-10 brauchen mehr; jedes Wort außerhalb steht im Randglossar (`vocabulary`, Nomen mit Artikel) und im Inhaltsführer unter „Sources“.

**Bauen und Erweitern:** Eine Seite = `src/<kapitel>/<seite>.yaml` + Eintrag in `chapter.yaml`; Hörsätze in `src/audio/` und `scripts/audio-texte.json`; ein Prüfskript im Repository prüft Hörsätze gegen den Text derselben Seite und Wörter gegen die Liste. Ein späteres Inkrement übernimmt Bauplan und Regler.

**Engagement je Seite** (Opening · Change · Reward · Story · Repeat):
- `text-gliedern`: Frage „Wo würdest du den Text trennen?“ · Lesen, Teile zuordnen, Schablone füllen · der eigene Text bekommt drei Teile · Ellie schickt einen langen Text ohne Absätze, Mr Hill bittet um Gliederung · die Schablone kehrt auf jeder Seite in anderer Form wieder.
- `formell-informell`: Regler auf zwei Sätzen schieben · Chat mit Mr Hill und Mitschüler:innen vergleichen · Sätze einordnen · Anfrage an Mr Hill zum Aushang · der Regler wird hier eingeführt und danach benutzt.
- `praesentation`: Redemittel den drei Teilen zuordnen · Redetext in Abschnitten lesen · eigener Einstieg und Übergang · Sophie bereitet den Vortrag über die Schülerzeitung vor · derselbe Inhalt wie im Blog, neutral statt informal.
- `blog-post`: Titel wählen · Blog lesen, Kommentar schreiben · eigener Blogeintrag und Forenkommentar · derselbe Inhalt wie der Vortrag, jetzt informal · Regler auf informal.
- `bericht-artikel`: W-Fragen finden · Bericht lesen und belegen · eigener Bericht · ein Ereignis der Schule · Schablone mit W-Fragen.
- `interview`: Frage vorbereiten · Interview lesen, Fragen umformen · eigenes Interview · Amir interviewt Mr Hill · Fragewörter aus der Wiederholung.
- `sachtext-fiktion`: zwei Texte vergleichen · Merkmale zuordnen · Merkmalsliste · Peter findet zwei Texte im Archiv der Zeitung · Merkmale in beiden Texten.
- `textsorte-umwandeln`: Geschichte neben der Schablone · Zeile für Zeile übertragen · eigener Bericht aus einer Geschichte · die Zeitung druckt die Geschichte als Bericht · Berichtsschablone erneut.
- `zeitungsartikel`: Artikel mit Teilen markieren · lesen, Teile bestimmen · Bericht von Kommentar trennen · erfundener Artikel über eine Stadtbücherei · die Schablone wird gedreht (finden statt schreiben).
- `information-meinung`: Sätze mit dem Farbstift wählen · zwei Texte zum selben Anlass vergleichen · seriöse Nachricht prüfen · erfundene Meldungen über einen Skatepark · Information und Meinung in zwei Fassungen.
- `diagramm-beschreiben`: Diagramm lesen · Aussagen zuordnen · Beschreibung schreiben · erfundene Umfrage zur Freizeit · Vergleiche aus der Wiederholung.
- `berufswelt`: Berufe zuordnen · Anzeige und Interview lesen · eigener Berufswunsch · Sophie findet die Ferienjob-Anzeige · Wörter aus der Anzeige.
- `bildungssystem`: Altersstufen vergleichen · Text über Schulsysteme lesen · eigenen Abschluss erklären · Sophie braucht Angaben für den Lebenslauf · Year- und Grade-Tabelle.
- `formelle-email`: Anrede und Gruß wählen · E-Mail an die Bibliothek lesen · eigene Anfrage · Sophie fragt nach dem Ferienjob · Regler auf formal.
- `lebenslauf`: Angaben in die CV-Schablone ordnen · CV lesen, Fehler finden · eigener CV · Sophies CV · Bauplan CV.
- `bewerbung`: Teile ordnen · Bewerbung lesen und belegen · eigene Bewerbung · Sophies Bewerbung als library assistant · Bauplan Bewerbung.
- `vorstellungsgespraech`: Frage und Antwort zuordnen · Gesprächstext lesen · Rollenspiel (Sprechauftrag) · Gespräch in der Bibliothek, Ausgang offen · Fragen aus der Bewerbung.


## Code

<!--
- Build the app, locally on `work`, on your own. After each task: `plan done`, then one commit with the work and this
  plan. The hooks check each commit; a failing check is fixed from its message, as skill `lernapps-cli` says.
- What you cannot decide: choose, write it under "Key decisions" with "(guess)", go on.
- The creator asks for a change: say your reading in one sentence first, then change every place it holds for
  (`feedback-applied-everywhere`).
-->

### Tasks

- [x] Load skill `lernapps-cli`. Create the app as its section "Create" says:
      `npx --no -- lernapps create --archetype explainer`.
- [x] Fill the content guide `.agents/skills/app-content/SKILL.md` from "Notes" and "Content method": every heading,
      no "FILL IN" left. Commit it before any content.
- [x] Load skill `lernapps-explainer`.
- [x] Load skill `lernapps-content-questions`. Read whole, with your file tool:
      `.agents/skills/lernapps-explainer/references/blocks.md` and
      `.agents/skills/lernapps-explainer/references/exercises.md`. A foreign language: also
      `references/language-tasks.md` in the same folder. A component in the plan: also `references/components.md`.
- [x] Decide whether the app needs `scope`, as "`scope`" in
      `.agents/skills/lernapps-explainer/references/structure.md` says. Write the choice under "Key decisions".
- [x] Musterseite Kapitel 1: gliedern-und-ton/text-gliedern komplett (Lesestück als Chat, Randglossar, Bauplan-Figur, mindestens 5 Übungen, Diktat und Nachsprechen, offene Aufgabe), dazu app.yaml, chapter.yaml und das Prüfskript
<!-- tasks: pattern (1 added): the one page or screen that is the pattern for the others -->
- [x] **Checkpoint:** the pattern page. Load skill `lernapps-learner-check` and do its learner check on the page. Fix
      what it finds. Then show the creator the page and ask whether the others may follow it. Stop and wait. A
      change: change the pattern first.
      Creator: Ja, Kapitel 1 Rest und danach 2-4 mit Sub-Agenten nach diesem Muster. Hörurteil für die drei Sätze bestätigt. Vorschau-PR erst nach Gesamtcheck und Sprachprüfung mit Sub-Agenten, Push nur auf work.
- [x] Kapitel 1 fertig: formell-informell (Ton-Regler-Figur), praesentation, blog-post und die Wiederholungsseite das-brauchst-du (kurzformen); Regler und Bauplan wie die Musterseite
- [x] Kapitel 2: das-brauchst-du (simple-past, fragewoerter, alltagstexte, figuren-ort-handlung), bericht-artikel, interview
- [x] Kapitel 2 Rest: sachtext-fiktion und textsorte-umwandeln (Geschichte aus #479 als Vorlage, eigener Text)
- [x] Kapitel 3: das-brauchst-du (vergleiche, zahlen), zeitungsartikel, information-meinung, diagramm-beschreiben mit Diagramm-SVG
- [x] Kapitel 4 Teil 1: das-brauchst-du (email-postkarte, datum), berufswelt, bildungssystem, formelle-email
- [x] Kapitel 4 Teil 2: lebenslauf, bewerbung, vorstellungsgespraech (Sprechauftrag) und Kapitelrückblick
- [x] Audio: alle Hörsätze mit regen_audio.py erzeugen, Hörliste im Inhaltsführer, Fuzzy-Prüfskript über alle Seiten
- [x] Startseite (intro nennt nur Namen und Rollen, scope), Selbsteinschätzung je Kapitel, Medien und Quellen im Inhaltsführer
<!-- tasks: pages (8 added): the other pages or screens, after the pattern -->
- [x] Update the content guide so that it describes the app as built (`app-content-matches`).
- [x] Run `npx --no -- lernapps check` until it passes.
- [x] Look at every screen and state, at 360 px and on a desktop, as "Look at the app" of skill `lernapps-cli` says.
      Compare each with its sketch.
- [x] Do the whole-app check of skill `lernapps-learner-check`. Fix what it finds and write under "Notes" what you
      fixed.

## Commit

<!--
- Put the app on GitHub, publish it with the creator's yes, then list it. A push to `main` publishes.
- Open the pull requests (to `main`, to the catalog) without asking: they publish nothing.
- The creator asked to stop before publishing (a trial): stop here and say so.
-->

### Tasks

- [ ] Load skill `lernapps-explainer-self-assessment`. Add the self-assessment as it says, or write under "Key
      decisions" why the app has none. Commit.
- [ ] Load skill `lernapps-github`. Set up the repository and Pages as it says. Ask for the repository's name and
      every click only the creator can make, in one message.
- [ ] Push `work`, open the preview pull request and see its checks to green, as skill `lernapps-github` says.
- [ ] **Checkpoint:** publish. Show what the app does and the preview link from the comment "Vorschau der App". Ask
      whether it may go online. Stop and wait for the yes.
- [ ] Load skill `lernapps-commit`. Publish as skill `lernapps-github` says: `work` into `main` as one squash commit,
      the run of `Pages` watched to its end.
- [ ] Open the address the job `deploy` printed and confirm that the app shows. Never use a derived address.
- [ ] Load skill `lernapps-listing`. Write the entry under "Entry draft" as it says, with the creator's answer to
      "Finding the app".
- [ ] Fill the retrospective.
- [ ] Commit this plan on `main` and push it: the listing check and the review read it there.
- [ ] **Checkpoint:** list. Open the listing pull request as skill `lernapps-listing` says, without asking first: the
      pull request is the review. See it to "bestanden", then show the creator the pull request and its result.
- [ ] If the plan changed since its last push, commit it on `main` and push again.

### Entry draft

<!-- YAML valid against the entry schema the listing skill names. Only known values, never invented. -->

```yaml
```

## Retrospective

<!-- At the end of Commit, before the listing pull request. Facts, short, no names. Read by review and evals. -->

### Phases reached

<!-- Last phase completed, checkpoints passed. E.g. "commit; confirmed, published". -->

### Creator turns after the plan

<!-- Number of creator messages after the confirmation, topic of each. Target: at most 3. -->

### Where I had to guess

<!-- Each gap in plan, skills, messages or answers, and your choice. "None" if none. -->
