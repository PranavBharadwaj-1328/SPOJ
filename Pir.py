from math import *

def tetra():
  n = int(input())
  name_1 = []
  name_2 = []
  name_3 = []
  name_4 = []
  name_5 = []
  name_6 = []
  for i in range(n):
    x1,x2,x3,x4,x5,x6=input().split()
    name_1.append(int(x1))
    name_2.append(int(x2))
    name_3.append(int(x3))
    name_4.append(int(x4))
    name_5.append(int(x5))
    name_6.append(int(x6))
  for i in range(n):
    print(findVolume(name_6[i],name_3[i],name_5[i],name_1[i],name_4[i],name_2[i],12))

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
