
def eqbox():
  n = int(input())
  A = []
  B = []
  X = []
  Y = []
  for i in range(0,n):
    a,b,x,y = input().split()
    if(int(a) >= 1 and int(b) >= 1):
      A.append(int(a))
      B.append(int(b))
    if(int(x) <= 50000 and int(y) <= 50000):
      X.append(int(x))
      Y.append(int(y))
  for i in range(0,n):
    if(A[i]*B[i] > X[i]*Y[i]):
      print("Escape is possible.")
    else:
      print("Box cannot be dropped.")

eqbox()

