## 1. Description
"""
Class name: ...
Functionality: ...
"""
# -------------------------------------------- #

## 2. Libraries
# -------------------------------------------- #

## 3. Functions

# Place the pieces on the board
def place_the_pieces(allpieces):
    for piece, positions in allpieces.items():
        for pos in positions:
            col = ord(pos[0]) - ord('a')
            row = 8 - int(pos[1])
            board[row][col] = piece


def print_chessboard():

    place_the_pieces (pieces)

    # Print the chessboard
    print("  +---+---+---+---+---+---+---+---+")
    for i in range(8):
        print(f"{8-i} | {' | '.join(board[i])} |")
        print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h  ")


# -------------------------------------------- #

## 4. Static Variables

# Define the pieces with their initial positions

# Create an empty 8x8 chessboard
board = [[" " for _ in range(8)] for _ in range(8)]

pieces = {
    "R": ["a1", "h1"],
    "N": ["b1", "g1"],
    "B": ["c1", "f1"],
    "Q": ["d1"],
    "K": ["e1"],
    "P": ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
    "r": ["a8", "h8"],
    "n": ["b8", "g8"],
    "b": ["c8", "f8"],
    "q": ["d8"],
    "k": ["e8"],
    "p": ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]
    }


# -------------------------------------------- #

## 5. User Entries
# -------------------------------------------- #

## 6. Main Class Action

print_chessboard()

# -------------------------------------------- #

## 7. Draft, Tests, TODO List, References
class MyString(str):
    def masihDoubled(self, number):
        return f"{self}{number}Masih"

# Usage
my_str = MyString("shoombool")
print(my_str.masihDoubled(4))
# -------------------------------------------- #