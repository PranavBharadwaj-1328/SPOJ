
def multiply():
  n = int(input())
  n1 = []
  n2 = []
  for i in range(0,n):
    x,y = input().split()
    n1.append(int(x))
    n2.append(int(y))
  for i in range(0,n):
    print(n1[i]*n2[i])

multiply()
