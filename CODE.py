'''
Title: Precipitate Calculator
Name: Harleen Bajwa
Date: 11/07/18
'''
###NOTE: USE PbF2 as the compound
### variables ###

posamount = 0
negamount = 0
suffix1 = ""
suffix2 = ""

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


## array 2d
gr1 = [
    ["LiF", 1, 1], ["MgF", 1, 2], ["CaF", 1, 2], ["SrF", 1, 2], ["BaF", 1, 2], ["FeF", 1, 2], ["Hg2F", 1, 2 ], ["PbF", 1, 2]
]
gr2 = [
    ["CuCl", 1, 1], ["AgCl", 1, 1], ["Hg2Cl", 1, 2], ["PbCl", 1, 2], ["TlCl", 1, 1], ["CuBr", 1, 1], ["AgBr", 1, 1],
    ["Hg2Br", 1, 2], ["PbBr", 1, 2], ["TlBr", 1, 1], ["CuI", 1, 1], ["AgI", 1, 1], ["Hg2I", 1, 2], ["PbI", 1, 2], ["TlI", 1, 1]
]
gr3 = [
    ["CaSO4", 1, 1], ["SrSO4", 1, 1], ["BaSO4", 1, 1], ["AgSO4", 2, 1], ["Hg2SO4", 1, 1], ["PbSO4", 1, 1], ["RaSO4", 1, 1]
]
cation1 = ["Li", "Mg", "Ca", "Sr", "Ba", "Fe", "Hg2", "Pb"]
cation2 = ["Cu", "Ag", "Hg2", "Pb", "Tl"]
cation3 = ["Ca", "Sr", "Ba", "Ag", "Hg2", "Pb", "Ra"]

if pos in cation1 and neg == "F":
    gr = gr1
elif pos in cation2 and neg == "Cl" or neg == "Br" or neg == "I":
    gr = gr2
elif pos in cation3 and neg == "SO4":
    gr = gr3
else:
    print("Element(s) are not recognized.")


try:
    for i in range(len(gr)):
      if compound == gr[i][0]:
        posamount = gr[i][1] + posamount
        negamount = gr[i][2] + negamount

    ## balancing the equation
    if posamount == negamount:
        pass
    elif (posamount % negamount == 0) or (negamount % posamount == 0):
        if posamount > negamount:
            suffix1 = str(int(posamount / negamount))
        else:
            suffix2 = str(int(negamount / posamount))
    else:
        suffix1 = negamount
        suffix2 = posamount
    compound = pos + suffix1 + neg + suffix2
    print(compound)
except NameError:
    print("This solution does not produce a precipitate.")
