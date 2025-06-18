import sys
from typing import Iterable, List
from gocard import GoCard, RegularGoCard, PensionerGoCard, Person


def create_card(card_type: str, balance: float) -> GoCard:
    card_type = card_type.lower()
    if card_type == "regular":
        return RegularGoCard(balance)
    elif card_type == "pensioner":
        return PensionerGoCard(balance)
    else:
        return GoCard(balance)


def process_lines(lines: Iterable[str]):
    people: List[Person] = []
    current: Person | None = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        tokens = line.split()
        cmd = tokens[0].lower()
        if cmd == "person":
            if len(tokens) < 4:
                print("Invalid person line. Expected: person <name> <type> <balance>")
                continue
            name = tokens[1]
            card_type = tokens[2]
            try:
                balance = float(tokens[3])
            except ValueError:
                print(f"Bad balance for person {name}")
                continue
            current = Person(name, create_card(card_type, balance))
            people.append(current)
        elif cmd == "r" and current:
            try:
                amount = float(tokens[1])
                current.card.ride(amount)
            except (IndexError, ValueError) as e:
                print(e)
        elif cmd == "t" and current:
            try:
                amount = float(tokens[1])
                current.card.top_up(amount)
            except (IndexError, ValueError) as e:
                print(e)
        elif cmd == "b" and current:
            print(f"{current.name} balance: ${current.card.get_balance():.2f}")
        elif cmd == "q" and current:
            print(f"Statement for {current.name}:")
            print(current.card.statement())
            current = None
        else:
            print(f"Ignoring invalid input: {line}")

    # print statements for any open account not closed by q
    if current:
        print(f"Statement for {current.name}:")
        print(current.card.statement())


def lines_from_input() -> Iterable[str]:
    try:
        while True:
            yield input()
    except EOFError:
        return


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
        process_lines(lines)
    else:
        print("Enter commands (type q to finish a customer):")
        process_lines(lines_from_input())


if __name__ == "__main__":
    main()
