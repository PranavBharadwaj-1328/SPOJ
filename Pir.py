from math import *

def tetra():
  n = int(input())
  n1 = []
  n2 = []
  n3 = []
  n4 = []
  n5 = []
  n6 = []
  for i in range(n):
    x1,x2,x3,x4,x5,x6=input().split()
    n1.append(int(x1))
    n2.append(int(x2))
    n3.append(int(x3))
    n4.append(int(x4))
    n5.append(int(x5))
    n6.append(int(x6))
  for i in range(n):
    print(findVolume(n6[i],n3[i],n5[i],n1[i],n4[i],n2[i],12))

def findVolume(u, v, w, U, V, W, b) :
  uPow = u**2
  vPow = v**2 
  wPow = w**2
  UPow = U**2
  VPow = V**2
  WPow = W**2
  a = (4 * (uPow * vPow * wPow) - uPow * pow((vPow + wPow - UPow), 2) - vPow * pow((wPow + uPow - VPow), 2) - wPow * pow((uPow + vPow - WPow), 2) + (vPow + wPow - UPow) * (wPow + uPow - VPow) * (uPow + vPow - WPow))
  vol = sqrt(a)
  vol /= b
  return (round(vol,4))

tetra()
