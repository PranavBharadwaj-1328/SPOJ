
def addrev():
  n = int(input())
  n1 = []
  n2 = []
  for i in range(0,n):
    x,y = input().split()
    n1.append(rev(int(x)))
    n2.append(rev(int(y)))
  for i in range(0,n):
    print(rev(n1[i]+n2[i]))

def rev(n):
  rev1=0
  while(n>0):
    dig=n%10
    rev1=rev1*10+dig
    n=n//10
  return rev1

addrev()
