# u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb: a 100-word villain
# monologue for a fantasy villain who is secretly just very tired. The
# program writes that monologue to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

MONOLOGUE = (
    "Three hundred years I've kept this siege, and the city still hasn't "
    "fallen \u2014 mostly because I keep... postponing the final assault. "
    "The trebuchets are ready. The banners are pressed. My generals wait "
    "below, polishing armor that will never see battle, because every "
    "morning I study the map and think: tomorrow. Tomorrow I'll be rested. "
    "Tomorrow the gates burn. My spies bring reports, and I file them "
    "under... somewhere. The ritual needs an eclipse, a black candle, and "
    "a prince's name spoken backwards \u2014 I have all three, except the "
    "energy. So. Heroes. Come and get me. Bring a blanket."
)

assert 1 <= len(MONOLOGUE) <= 600, f"monologue is {len(MONOLOGUE)} chars, must be 1-600"
assert MONOLOGUE.strip(), "monologue must not be only whitespace"
assert 90 <= len(MONOLOGUE.split()) <= 110, f"monologue is {len(MONOLOGUE.split())} words, want ~100"

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(MONOLOGUE)
