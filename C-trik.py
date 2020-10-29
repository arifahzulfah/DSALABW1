seq=input()
size_seq=len(seq)
ball=1

for i in range(size_seq):
  if seq[i] == 'A':
    if ball == 1:
      ball = ball+1
    elif ball == 2:
      ball = ball-1
  elif seq[i] == 'B':
    if ball == 2:
      ball = ball+1
    elif ball == 3:
      ball = ball-1
  elif seq[i] == 'C':
    if ball == 1:
      ball = ball+2
    elif ball == 3:
      ball = ball-2
print(ball)