'''
Title: Precipitate Calculator
Name: Harleen Bajwa
Date: 11/07/18
'''
### Imports ###
import sys

### variables ###

poscharge = 0
negcharge = 0
## should i delete all these def muli - def div
def muli(a, b):
    c = a * b
    return c

def add(a, b):
    c = a + b
    return c

def sub(a, b):
    c = a - b
    return c

def div(a, b):
    c = a / b
    return c


def pos_ion():
    try:
        pvol = float(input("What is the volume of the positive solution. (L)"))
        pcon = float(input("What is the concentration of positive solution. (mol/L)"))
        npos = muli(pvol, pcon)
        print(npos)
        return npos
    except ValueError:
        print("Please enter a number.")
        return pos_ion()
def neg_ion():
    try:
        nvol = float(input("What is the volume of the negative solution. (L)"))
        ncon = float(input("What is the concentration of positive solution. (mol/L)"))
        nneg = muli(nvol, ncon)
        print(nneg)
        return nneg
    except ValueError:
        print("Please enter a number.")
        return neg_ion()

def ion():
   pos = input("Please enter the positive reacting ion. (no charge)")
   pos_ion()
   neg = input("Please enter the negative ion. (no charge)")
   neg_ion()
   return pos, neg

pos, neg = ion()
pos = pos.lower()
print(pos)
neg = neg.lower()
print(neg)
compound = pos + neg
print(compound)
## array 2d
gr1 = [
    ["lif", 1, 1], ["mgf", 1, 2], ["caf", 1, 2], ["srf", 1, 2], ["baf", 1, 2], ["fef", 1, 2], ["hgf", ], ["pbf", 1, 2]]
gr2 = [
    ["cucl", 1, 1] , ["agcl", 1, 1], ["hgcl", 1, 2], ["pbcl", 1, 2], ["tlcl", 1, 1], ["cubr", 1, 1], ["agbr", 1, 1], ["hgbr", 1, 2], ["pbbr", 1, 2], ["tlbr", 1, 1], ["cui", 1, 1] , ["agi", 1, 1], ["hgi", 1, 2], ["pbi", 1, 2], ["tli", 1, 1]
    ]
gr3 = [
    ["caso4",1 , 1], ["srso4",1 , 1], ["baso4", 1, 1], ["agso4", 2, 1], ["hg2so4", 1, 1], ["pbso4", 1, 1], ["raso4", 1, 1]
    ]

match = False 
if neg == "f":
  for i in range (len(gr1)):
    if compound == gr1[i][0]:
      poscharge = gr1[i][1] + poscharge
      negcharge = gr1[i][2] + negcharge
      match = True
  if match == False:
    print("3This solution does not produce a precipitate.")
elif neg =="cl":
  for i in range (len(gr2)):
    if compound == gr2[i][0]:
      poscharge = gr2[i][1] + poscharge 
      negcharge = gr2[i][2] + negcharge
      match = True
  if match == False:
      print("2This solution does not produce a precipitate.")
elif neg == "br":
  for i in range (len(gr2)):
    if compound == gr2[i][0]:
      poscharge = gr2[i][1] + poscharge 
      negcharge = gr2[i][2] + negcharge
      match = True
  if match == False:
      print("4This solution does not produce a precipitate.")
elif neg == "i":
  for i in range (len(gr2)):
    if compound == gr2[i][0]:
      poscharge = gr2[i][1] + poscharge 
      negcharge = gr2[i][2] + negcharge
      match = True
  if match == False:
      print("5This solution does not produce a precipitate.")
elif neg == "so4":
  for i in range (len(gr3)):
    if compound == gr3[i][0]:
      poscharge = gr3[i][1] + poscharge
      negcharge = gr3[i][2] + negcharge
      match = True
  if match == False:
    print("1This solution does not produce a precipitate.")
else:
  print("This solution does not produce a precipitate.")

print(poscharge)
print(negcharge)
## balancing the equation 
if poscharge == negcharge:
  if poscharge == 1:
    print(str(poscharge),str(pos) + " + " + str(negcharge), str(neg)+ " ---> " + str(compound)) 
    neg = negcharge + neg 
    compound = compound + pos
  elif poscharge == 0: ## how do u exit the program 
    pass
#elif not poscharge == negcharge:
