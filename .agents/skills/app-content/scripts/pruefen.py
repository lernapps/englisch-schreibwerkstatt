#!/usr/bin/env python3
"""Prüft alle Seiten: (1) Hörsätze wörtlich oder fast wörtlich im Text derselben Seite, (2) englische Wörter außerhalb
des Grundwortschatzes A1/A2 (Liste: Feld `vocabulary` der Karte, Datei per Argument oder aus dem Netz).

Aufruf: python3 .agents/skills/app-content/scripts/pruefen.py [karte.json]
Die Wortprüfung ist eine Hilfe: sie meldet auch deutsche Wörter in englischen Feldern; ein Mensch entscheidet.
"""
import difflib, glob, json, re, sys, urllib.request
import yaml

KARTE = "https://lernapps.net/apps/map/englisch.json"
NAMEN = {"sophie", "ellie", "peter", "amir", "hill", "parker", "millbrook", "mr", "mrs", "max", "england", "saturday",
         "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "january", "i'm", "it's", "don't", "doesn't",
         "didn't", "isn't", "aren't", "wasn't", "can't", "he's", "she's", "that's", "what's", "let's"}
UNREG = {"went": "go", "took": "take", "fell": "fall", "had": "have", "got": "get", "said": "say", "found": "find",
         "saw": "see", "was": "be", "were": "be", "is": "be", "are": "be", "am": "be", "been": "be", "ran": "run", "came": "come", "gave": "give", "made": "make",
         "did": "do", "ate": "eat", "sat": "sit", "told": "tell", "thought": "think", "knew": "know", "wrote": "write",
         "read": "read", "met": "meet", "felt": "feel", "left": "leave", "brought": "bring", "bought": "buy",
         "heard": "hear", "kept": "keep", "lost": "lose", "won": "win", "stood": "stand", "sang": "sing",
         "swam": "swim", "drew": "draw", "flew": "fly", "grew": "grow", "began": "begin", "woke": "wake",
         "children": "child", "men": "man", "women": "woman", "people": "person", "mice": "mouse", "feet": "foot"}


def karte():
    src = sys.argv[1] if len(sys.argv) > 1 else None
    if src:
        return json.load(open(src))
    return json.load(urllib.request.urlopen(KARTE))


def grundformen(w):
    w = w.lower()
    if w.endswith("'s"):
        w = w[:-2]
    yield w
    if w in UNREG:
        yield UNREG[w]
    for suf, ers in (("ies", "y"), ("ied", "y"), ("ing", ""), ("ing", "e"), ("ed", ""), ("ed", "e"), ("es", ""), ("s", ""), ("d", ""), ("er", ""), ("est", ""), ("ly", ""), ("ier", "y"), ("iest", "y")):
        if w.endswith(suf) and len(w) > len(suf) + 1:
            k = w[: -len(suf)] + ers
            yield k
            if len(k) > 2 and k[-1] == k[-2]:
                yield k[:-1]


def seiten():
    for pfad in sorted(glob.glob("src/*/*.yaml")):
        if pfad.endswith("chapter.yaml"):
            continue
        yield pfad, yaml.safe_load(open(pfad))


def blocks(b):
    for x in b or []:
        yield x
        if isinstance(x, dict) and "blocks" in x:
            yield from blocks(x["blocks"])


def saetze(text):
    text = re.sub(r"[„“‚‘\"]", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", text) if s.strip()]


def norm(s):
    return re.sub(r"[^a-z' ]", "", s.lower().replace("’", "'")).split()


def alle_texte(seite, ohne_audio=True):
    """Alle Texte der Seite, in denen ein Hörsatz nicht stehen darf."""
    out = []
    for b in blocks(seite.get("blocks")):
        if not isinstance(b, dict):
            continue
        t = b.get("type")
        if t == "speaking-task":
            continue
        if t == "language-task" and any("audio" in i for i in b.get("items", [])):
            continue
        for k in ("text", "task", "caption", "alt", "explanation", "title"):
            if isinstance(b.get(k), str):
                out.append(b[k])
        for o in b.get("options", []):
            out.append(o.get("text", ""))
        for p in b.get("pairs", []):
            out += [p["left"], p["right"]]
        out += [str(i) for i in b.get("items", []) if isinstance(i, str)]
        for i in b.get("items", []):
            if isinstance(i, dict):
                out += [str(i.get(k, "")) for k in ("source", "target", "cue")]
        for p in b.get("points", []):
            out.append(p.get("text", ""))
        out.append(b.get("solution", "") or "")
        for r in b.get("rows", []):
            out += [str(c) for c in r]
    texte = []
    for t in out:
        t = re.sub(r"\(([^()|]*)\|([^()]*)\)", lambda m: m.group(1), t)  # erste Variante
        texte += saetze(t)
    return texte


def hoersaetze(seite):
    for b in blocks(seite.get("blocks")):
        if not isinstance(b, dict):
            continue
        if b.get("type") == "speaking-task":
            for i in b["items"]:
                yield b["id"], i.get("text", "")
        if b.get("type") == "language-task":
            for i in b.get("items", []):
                if "audio" in i:
                    yield b["id"], i.get("target", i.get("source", ""))


def pruefe_hoeren():
    fehler = 0
    for pfad, s in seiten():
        texte = alle_texte(s)
        for ex, satz in hoersaetze(s):
            n = " ".join(norm(satz))
            for t in texte:
                tn = " ".join(norm(t))
                if not tn or len(norm(satz)) < 3:
                    continue
                if n in tn or tn in n and len(norm(t)) >= 4 or difflib.SequenceMatcher(None, n, tn).ratio() >= 0.8:
                    print(f"HÖREN {pfad} {ex}: „{satz}“ ähnelt „{t}“")
                    fehler += 1
                    break
    return fehler


def pruefe_woerter(m, extra):
    erlaubt = {w["word"].lower() for w in m["vocabulary"]["words"]} | NAMEN | extra
    fehler = 0
    for pfad, s in seiten():
        felder = []
        for b in blocks(s.get("blocks")):
            if not isinstance(b, dict):
                continue
            t = b.get("type")
            if t == "table":
                felder += [str(r[0]) for r in b["rows"]]
            for i in b.get("items", []):
                if isinstance(i, dict):
                    felder += [str(i.get(k, "")) for k in ("target", "cue", "text")]
                elif isinstance(i, str) and t == "ordering":
                    felder.append(i)
            for o in b.get("options", []):
                felder.append(o["text"])
            if t == "text":
                felder += re.findall(r"„([^“]*)“", b["text"])
        unbekannt = set()
        for f in felder:
            f = re.sub(r"[\[\]()|]", " ", f)
            for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", f):
                w = w.replace("’", "'")
                if not any(g in erlaubt for g in grundformen(w)) and w.lower() not in erlaubt:
                    unbekannt.add(w.lower())
        if unbekannt:
            print(f"WORT  {pfad}: {', '.join(sorted(unbekannt))}")
            fehler += 1
    return fehler


if __name__ == "__main__":
    m = karte()
    extra = set()
    try:
        extra = set(json.load(open(".agents/skills/app-content/scripts/woerter-erklaert.json")))
    except OSError:
        pass
    a = pruefe_hoeren()
    b = pruefe_woerter(m, extra)
    print("fertig:", "Hörsätze", a, "Seiten mit unbekannten Wörtern", b)
