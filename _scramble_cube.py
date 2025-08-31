#!/usr/bin/env python3
# Generate cube scramble sequence.

import argparse
import random

# Prioritizing R, F, U and D faces by giving them bigger weights.
FACES = (
    ["R", "R'"] * 8
    + ["F", "F'"] * 8
    + ["U", "U'"] * 8
    + ["D", "D'"] * 4
    + ["L", "L'"]
    + ["B", "B'"]
)


def filter_faces(*faces_to_filter: list[str]) -> list[str]:
    """Return `faces` with all occurences of `faces_to_filter` removed."""
    faces = FACES.copy()
    for face in faces_to_filter:
        while True:
            try:
                faces.remove(face)
            except ValueError:
                break
    return faces


def opposite_of(face: str) -> str:
    """Translate FACE to FACE', and FACE' to FACE."""
    if face.endswith("'"):
        return face[0]
    return face + "'"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("len", type=int)
    args = parser.parse_args()

    if args.len < 1:
        raise ValueError("len must be greater than 0")

    scramble = [random.choice(FACES)]

    for _ in range(args.len - 1):
        previous = scramble[-1]
        if previous.startswith("2"):
            # If previous == 2FACE, don't insert FACE or FACE'
            previous_without_2 = previous[-1]
            filtered_faces = filter_faces(
                previous_without_2, opposite_of(previous_without_2)
            )
            new = random.choice(filtered_faces)
            scramble.append(new)
        else:
            # If previous == FACE, don't insert FACE'
            filtered_faces = filter_faces(opposite_of(previous))
            new = random.choice(filtered_faces)
            if new == previous:
                # 2FACE is the same as 2FACE'
                new = new[0]
                scramble[-1] = "2" + new
            else:
                scramble.append(new)

    print(" ".join(scramble))


if __name__ == "__main__":
    main()
