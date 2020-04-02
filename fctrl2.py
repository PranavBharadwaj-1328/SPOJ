
def factorial():
  t = int(input())
  n = []
  for i in range(0,t):
    a = int(input())
    n.append(a)
#  out = []
  #print("Output:")
  for i in range(0,t):
    print (fact(n[i]))
 #   out.append(fact(n[i]))


def fact(n):
  if (n == 0):
    return 1
  else:
    a = 1
    while(n != 1):
      a = a*n
      n = n - 1
    return a

factorial()
