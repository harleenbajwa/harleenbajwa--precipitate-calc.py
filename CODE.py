'''
Title: Precipitate Calculator
Name: Harleen Bajwa
Date: 11/07/18
'''

### variables ###

poscharge = 0
negcharge = 0
prefix1 = ""
prefix2 = ""

def pos_ion():
    try:
        pvol = float(input("What is the volume of the positive solution. (L)"))
        pcon = float(input("What is the concentration of positive solution. (mol/L)"))
        return pvol * pcon
    except ValueError:
        print("Please enter a number.")
        return pos_ion()

def neg_ion():
    try:
        nvol = float(input("What is the volume of the negative solution. (L)"))
        ncon = float(input("What is the concentration of positive solution. (mol/L)"))
        return nvol * ncon
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
compound = pos + neg
print(compound)

## array 2d
gr1 = [
    ["LiF", 1, 1], ["MgF", 1, 2], ["CaF", 1, 2], ["SrF", 1, 2], ["BaF", 1, 2], ["FeF", 1, 2], ["HgF", ], ["PbF", 1, 2]
]
gr2 = [
    ["CuCl", 1, 1], ["AgCl", 1, 1], ["HgCl", 1, 2], ["PbCl", 1, 2], ["TlCl", 1, 1], ["CuBr", 1, 1], ["AgBr", 1, 1],
    ["HgBr", 1, 2], ["PbBr", 1, 2], ["TlBr", 1, 1], ["CuI", 1, 1], ["AgI", 1, 1], ["HgI", 1, 2], ["PbI", 1, 2], ["TlI", 1, 1]
]
gr3 = [
    ["CaSO4", 1, 1], ["SrSO4", 1, 1], ["BaSO4", 1, 1], ["AgSO4", 2, 1], ["Hg2SO4", 1, 1], ["PbSO4", 1, 1], ["RaSO4", 1, 1]
]
cation1 = ["Li", "Mg", "Ca", "Sr", "Ba", "Fe", "Hg2", "Pb"]
cation2 = ["Cu", "Ag", "Hg2", "Pb", "Tl"]
cation3 = ["Ca", "Sr", "Ba", "Ag", "Hg2", "Pb", "Ra"]

if pos in cation1:
  if neg == "F":
    gr = gr1
elif pos in cation2:
  if neg == "Cl" or neg == "Br" or neg == "I":
    gr = gr2
elif pos in cation3:
  if neg == "SO4":
    gr = gr3


for i in range(len(gr)):
    if compound == gr[i][0]:
        poscharge = gr[i][1] + poscharge
        negcharge = gr[i][2] + negcharge
