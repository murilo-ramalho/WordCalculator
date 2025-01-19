import os

def card_to_number(card):
    values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'j': 9, 'q': 10, 'k': 11, 'a': 12}
    suits = {
        'c': 3, 'h': 2, 's': 1, 'd': 0,
        'p': 3, 'd': 2, 'e': 1, 'o': 0,
        }  # ♦clubs (♣), hearts (♥), Spades (♠) and diamonds (♦)
    value = card[:-1].lower()
    suit = card[-1].lower()

    if value not in values or suit not in suits:
        raise ValueError("invalid Card")
    
    return values[value] + suits[suit] * 13

def calculate(cards):
    return (card_to_number(cards[0]) +
            card_to_number(cards[1]) * 52 +
            card_to_number(cards[2]) * 52**2 +
            card_to_number(cards[3]) * 52**3) % 2048

def main():
    cards = []

    for i in range(4):
        print(f"\nCard {i+1}")
        card = input(f"insert card: ")
        cards.append(card)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()