X, Y, N = map(int,input().split())
for i in range(N):
    j = i+1
    if j%X == 0 and j%Y == 0:
      print("FizzBuzz")
    elif j%X == 0:
      print("Fizz")
    elif j%Y == 0:
      print("Buzz")
    else:
      print(j)