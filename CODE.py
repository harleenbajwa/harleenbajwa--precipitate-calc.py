'''
Title: Precipitate Calculator
Name: Harleen Bajwa
Date: 11/07/18
'''
### variables ###
posamount = 0
negamount = 0
suffix1 = ""
suffix2 = ""
molarmass = 0

### Subroutines ###
def pos_ion():
    try:
        pvol = float(input("What is the volume of the positive solution. (L)"))
        pcon = float(input("What is the concentration of positive solution. (mol/L)"))
        #positive Volume * positive concentration = postives mole(s)
        npos = pvol * pcon
        return npos
    except ValueError:
        print("Please enter a number.")
        return pos_ion()

def neg_ion():
    try:
        nvol = float(input("What is the volume of the negative solution. (L)"))
        ncon = float(input("What is the concentration of negative solution. (mol/L)"))
        # negative mole(s) = negative volume * negative concentration
        nneg = nvol * ncon
        return nneg
    except ValueError:
        print("Please enter a number.")
        return neg_ion()
def ion():
  pos = input("Please enter the positive reacting ion. (no charge)")
  npos = pos_ion()
  neg = input("Please enter the negative ion. (no charge)")
  nneg = neg_ion()
  return pos, npos, neg, nneg
## Making them variables on the outside of def ion()
pos, npos, neg, nneg = ion()
compound = pos + neg


## array 2d
gr1 = [
    ["LiF", 1, 1, 25.94], ["MgF", 1, 2, 62.31], ["CaF", 1, 2, 60.08], ["SrF", 1, 2, 125.62], ["BaF", 1, 2, 175.33], ["FeF", 1, 2, 92.94], ["Hg2F", 1, 2, 238.59], ["PbF", 1, 2, 238.59]
]
gr2 = [
    ["CuCl", 1, 1, 99], ["AgCl", 1, 1, 143.32], ["Hg2Cl", 1, 2, 472.08], ["PbCl", 1, 2, 278.1], ["TlCl", 1, 1, 239.83], ["CuBr", 1, 1, 143.45], ["AgBr", 1, 1, 187.77],
    ["Hg2Br", 1, 2, 481.08], ["PbBr", 1, 2, 367], ["TlBr", 1, 1, 284.28], ["CuI", 1, 1, 190.45], ["AgI", 1, 1, 234.77], ["Hg2I", 1, 2, 654.98], ["PbI", 1, 2, 461], ["TlI", 1, 1, 331.28]
]
gr3 = [
    ["CaSO4", 1, 1, 136.15], ["SrSO4", 1, 1, 183.69], ["BaSO4", 1, 1, 233.4], ["AgSO4", 2, 1, 331.81], ["Hg2SO4", 1, 1, 497.25], ["PbSO4", 1, 1, 303.27], ["RaSO4", 1, 1, 322.07]
]
cation1 = ["Li", "Mg", "Ca", "Sr", "Ba", "Fe", "Hg2", "Pb"]
cation2 = (("Cu", "Ag", "Hg2", "Pb", "Tl"))
cation3 = ["Ca", "Sr", "Ba", "Ag", "Hg2", "Pb", "Ra"]

## Checking if it's the right ion
if pos in cation1 and neg == "F":
    gr = gr1
elif pos in cation2 and neg == "Cl" or neg == "Br" or neg == "I":
    gr = gr2
elif pos in cation3 and neg == "SO4":
    gr = gr3
else:
    print("Element(s) are not recognized.")

## Adding a number for positive amount, negative amount, and atomic molar mass of the compound
try:
    for i in range(len(gr)):
      if compound == gr[i][0]:
        posamount = gr[i][1] + posamount
        negamount = gr[i][2] + negamount
        molarmass = gr[i][3] + molarmass


    ## balancing the equation
    if posamount == negamount:
        pass
    elif (posamount % negamount == 0) or (negamount % posamount == 0): ## Checking if the amount of positve/negative has a remainder
        if posamount > negamount:
            suffix1 = str(int(posamount / negamount)) ## Reducing the value of each amount eg. 4/2 = 2 = suffix1
        else:
            suffix2 = str(int(negamount / posamount)) # Reducing the value of each amount eg. 4/2 = 2 = suffix2
    else:
        suffix1 = negamount
        suffix2 = posamount
    compound = pos + suffix1 + neg + suffix2 ## replacing the value of the negative and positive ion in the compund
except NameError:
    print("This solution does not produce a precipitate.")

### Calculating the limiting reagant ###
nneg1 = ((npos*negamount)/posamount)
if npos < nneg1:
  print("The limiting reagant is "+ str(neg) + ".")
  ## compound moles
  ncompound= nneg*(1/negamount)
elif npos > nneg1:
  print("The limiting reagant is " + str(pos) + ".")
  ## compound moles
  ncompound= npos*(1/posamount)

## Calculating the product mass
massp = ncompound*molarmass

## Rounding it to 2 decimal places
if massp == int(massp):
  pass
else:
  massp = round(massp, 2)

print("The mass of " + str(compound) + " is " + str(massp) +" grams.")
