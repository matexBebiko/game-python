import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "♤": 2,
    "𓆜": 1,
    "❤": 3,
    "𓃱": 8,
}

def get_spin_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_machine(columns):
    for row in range(len(columns[0])):  # Ensure the loop runs for the rows (not columns)
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def check_win(columns, lines, bet, values):
    win = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            win += values[symbol] * bet
            win_lines.append(line + 1)
    return win, win_lines

def deposit():
    while True:
        kaska = input("Za ile chcesz zagrać?: $")
        if kaska.isdigit():
            kaska = int(kaska)
            if kaska > 0:
                break
            else:
                print("Nie mozna za tyle zagrać")
        else:
            print("Podaj liczbe")
    return kaska

def liczba_wierszy():
    while True:
        lines = input("Podaj liczbę lini na które chcesz postawić (1-" + str(MAX_LINES) + "):")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Podaj prawidłową liczbą linii")
        else:
            print("Podaj liczbę")
    return lines

def get_bet():
    while True:
        bet = input("Podaj ile chcesz postawić $ ? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Twoj bet musi mieć wartośc miedzy {MIN_BET}, a {MAX_BET}")
        else:
            print("Podaj liczbe")
    return bet

def game(balance):
    lines = liczba_wierszy()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if balance < total_bet:
            print("Masz za mało pieniędzy")
        else:
            break
    print(f"Postawiłeś ${bet} na {lines} linie, twój całkowity zakład wynosi {total_bet}")
    slots = get_spin_machine(ROWS, COLS, symbol_count)
    print_machine(slots)
    win, win_lines = check_win(slots, lines, bet, symbol_count)
    print(f"Twoja wygrana to: ${win}")
    print(f"Wygrałeś na {win_lines} linii")
    return win - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Bieżacy stan konta: ${balance}")
        spin = input("Klinij enter aby zagrać (q aby skończyć): ")
        if spin == "q":
            break
        balance += game(balance)
    print(f"Skonczyłeś na dziś twoja wygrana to ${balance}")

main()
