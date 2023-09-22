from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),   # A es caballero o bribón (exclusivo)
    Implication(AKnight, And(AKnight, AKnave)),  # Si A es caballero, entonces dice la verdad
    Implication(AKnave, Not(And(AKnight, AKnave)))  # Si A es bribón, entonces miente
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave, BKnight, BKnave),  # Todos son caballeros o bribones (exclusivo)
    Implication(AKnight, And(AKnave, BKnave)),  # Si A es caballero, entonces dice la verdad
    Implication(AKnave, Not(And(AKnave, BKnave)))  # Si A es bribón, entonces miente
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave, BKnight, BKnave),  # Todos son caballeros o bribones (exclusivo)
    Implication(AKnight, Biconditional(AKnight, BKnight)),  # Si A es caballero, entonces B también
    Implication(AKnave, Biconditional(AKnave, BKnave)),  # Si A es bribón, entonces B también
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),  # Si B es caballero, entonces no pueden ser del mismo tipo
    Implication(BKnave, Not(Biconditional(AKnave, BKnave)))  # Si B es bribón, entonces no pueden ser del mismo tipo
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave, BKnight, BKnave, CKnight, CKnave),  # Todos son caballeros o bribones (exclusivo)
    Implication(AKnight, Or(AKnight, AKnave)),  # Si A es caballero, entonces dice la verdad
    Implication(AKnave, Not(Or(AKnight, AKnave))),  # Si A es bribón, entonces miente
    Implication(BKnight, AKnave),  # Si B es caballero, entonces A es bribón
    Implication(BKnave, Not(AKnave)),  # Si B es bribón, entonces A es caballero
    Implication(BKnight, CKnave),  # Si B es caballero, entonces C es bribón
    Implication(BKnave, Not(CKnave)),  # Si B es bribón, entonces C es caballero
    Implication(CKnight, AKnight),  # Si C es caballero, entonces A es caballero
    Implication(CKnave, Not(AKnight))  # Si C es bribón, entonces A es bribón
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3),
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
