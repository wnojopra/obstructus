"""
The game is played on a square board divided into 20 rows and 20 columns, for
a total of 400 squares. There are a total of 84 game tiles, organized into 21
shapes in each of four colors: blue, yellow, red and green. The 21 shapes are
based on free polyominoes of from one to five squares (one monomino, one
  domino, two trominoes/triominoes, five tetrominoes, and 12 pentominoes).

The standard rules of play for all variations of the game are as follows:

Order of play is based on the color of pieces: blue, yellow, red, green.
The first piece played of each color is placed in one of the board's four
corners. Each new piece played must be placed so that it touches at least
one piece of the same color, with only corner-to-corner contact allowed-edges
cannot touch. However, edge-to-edge contact is allowed when two pieces of
different color are involved.

When a player cannot place a piece, he or she passes, and play continues as
normal. The game ends when no one can place a piece.

When a game ends, the score is based on the number of squares in each
player's pieces on the board (e.g. a tetromino is worth 4 points). A player
who played all of his or her pieces is awarded a +20 point bonus if the last
piece played was a monomino, or a +15 point bonus for any other piece.
"""
BOARD_SIZE = 20

BLUE = 'blue'
YELLOW = 'yellow'
RED = 'red'
GREEN = 'green'
COLORS = [BLUE, YELLOW, RED, GREEN]

MONOMINO = [[1]]
DOMINO = [[1, 1]]
TRIOMINOE_L = [[1, 1], [0, 1]]
TRIOMINOE_LINE = [[1, 1, 1]]
TETROMINO_SQUARE = [[1, 1], [1, 1]]
TETROMINO_T = [[0,1,0], [1,1,1]]
TETROMINO_LINE = [[1,1,1,1]]
TETROMINO_L = [[0,0,1],[1,1,1]]
TETROMINO_Z = [[0,1,1],[1,1,0]]
PENTOMINO_LONG_L = [[1,0,0,0],[1,1,1,1]]
PENTOMINO_T = [[0,1,0],[0,1,0],[1,1,1]]
PENTOMINO_L = [[1,0,0],[1,0,0],[1,1,1]]
PENTOMINO_LONG_Z = [[0,1,1,1],[1,1,0,0]]
PENTOMINO_Z = [[0,0,1],[1,1,1],[1,0,0]]
PENTOMINO_LINE = [[1,1,1,1,1]]
PENTOMINO_UTAH = [[1,0],[1,1],[1,1]]
PENTOMINO_W = [[0,1,1],[1,1,0],[1,0,0]]
PENTOMINO_GATE = [[1,1],[1,0],[1,1]]
PENTOMINO_WRENCH = [[0,1,1],[1,1,0],[0,1,0]]
PENTOMINO_CROSS = [[0,1,0], [1,1,1],[0,1,0]]
PENTOMINO_BATON = [[0,1,0,0],[1,1,1,1]]

PIECES = [
  MONOMINO,
  DOMINO,
  TRIOMINOE_LINE, TRIOMINOE_L,
  TETROMINO_Z, TETROMINO_L, TETROMINO_LINE, TETROMINO_T, TETROMINO_SQUARE,
  PENTOMINO_T, PENTOMINO_L, PENTOMINO_LONG_Z, PENTOMINO_Z, PENTOMINO_LINE, 
  PENTOMINO_UTAH, PENTOMINO_W, PENTOMINO_GATE, PENTOMINO_WRENCH,
  PENTOMINO_CROSS, PENTOMINO_BATON
  ]

class Piece(object):
  # A piece is represented by a NxM grid. Each square in the grid is filled or
  # empty (1 or 0)
  def __init__(self, color, grid):
    self.color = color
    self.grid = grid

  def get_color(self):
    colors_to_letter = {
      BLUE: 'B',
      YELLOW: 'Y',
      RED: 'R',
      GREEN: 'G',
    }
    return colors_to_letter[self.color]

  def __str__(self):
    ret = ''
    for row in self.grid:
      c_row = ''
      for c in row:
        if c:
          c_row += self.get_color()
        else:
          c_row += ' '
      ret += c_row + '\n'
    return ret


class Board(object):
  def __init__(self, board_size):
    self.board_size = board_size
    self.board = [['' for i in range(board_size)] for j in range(board_size)]

  def __repr__(self):
    ret = ''
    for row in self.board:
      ret += str(row) + '\n'
    return ret

  def __str__(self):
    ret = ''
    for row in self.board:
      ret += str(row) + '\n'
    return ret


board = Board(BOARD_SIZE)
print(board)
for p in PIECES:
  piece = Piece(GREEN, p)
  print(piece)