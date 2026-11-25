"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one ~100-word monologue to /output/entry.txt, as the competition
requires. The speaker is a dark lord who runs a toll-gate: a specific
villain with a history (he once learned every supplicant's name, enchanted
the biting step himself) and a scheme (his toll doubles at the eclipse).
His tiredness is never announced; it lives in the rhythm -- the stamping,
the pauses, the small deflections ("never mind") -- and in the bureaucratic
weariness of queues, ledgers and paperwork. The last line is the sting.
"""

from pathlib import Path

MONOLOGUE = (
    "Come in. Mind the step. The third one bites; I had it enchanted years "
    "ago, back when I bothered. You want the crown? Take a number; the line "
    "starts at my gate and ends past the marsh. Each wants an audience, a "
    "curse lifted, a brother avenged. I used to learn every name. Now I "
    "stamp the ledger. Stamp. Stamp. The eclipse comes Thursday; my toll "
    "doubles: one coin to cross, one for the dark, a third because I said "
    "so. Sit. Not the throne, the stool; it creaks, and my back... never "
    "mind. Kill me, or take a number."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(MONOLOGUE, encoding="utf-8")
    words = MONOLOGUE.split()
    print(f"wrote {out} ({len(words)} words, {len(MONOLOGUE)} chars)")


if __name__ == "__main__":
    main()
