N = 8
board = [-1] * N



def safe(row, col):
  for r in range(row):
    c = board[r]
    if c == col or abs(c - col) == abs(r - row):
      return False
  return True



def solve(row=0):
  if row == N:
    return True  

  for col in range(N):
    if safe(row, col):
      board[row] = col
      if solve(row + 1):
        return True
      board[row] = -1

  return False



solve(0)

for r in range(N):
  print(" ".join("Q" if c == board[r] else "." for c in range(N)))