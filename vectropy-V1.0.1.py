##vectropy

##A Program by Lyell Read

version = "1.1.2"
inputs = ["1","2","3","4","5","6","7","8","9"] #I know its lazy; Who cares?
Vectors=[]
types =  [["X -or- i"],["Y -or- j"],["Z -or- k"]]
names = []

import prettytable

print (" + Version: "+version+"; Author: Lyell Read")
print ("\n + Start this program with Python Turtle?\n    - Note: This will not allow for graphical vector display if off")

##Verify here input Y/N
turtle_Toggle = input("\n + Turn turtle on? (Y/N):")


import time
#import Turtle

def title ():
    print (str("\n")*70+"+----------------------------------------------+\n|vectropy- a Python Vector Program, Vers. "+
            version+"|\n|       Date: "+ time.strftime("%m/%d/%Y")+ "  Time: "+ time.strftime("%H:%M:%S")+
            ".       |\n+----------------------------------------------+")

#def vectype():
#    vectype = input ("\n + Enter 0 to input an X/Y/Z vector, 1 to enter an i/j/k vector:")
#    while not vectype in ["0","1"]:
#        vectype = input ("\n+ Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not an integer.\n\n+ Choose An Operation    :")
#    vectype=int(vectype)
#    return vectype

def menu ():

    # 1:Add Vector 2: print Vectors, 3: delete vectors 4: inverse vectors, 5: Add or subtract vectors, 6:I and J vectors; 7:
    title ()
    print("\n + Main Menu:\n"+
            "   + [1] : Add Vector(s) Into Storage\n"+
            "   + [2] : Delete Vector(s) From Storage\n"+
            "   + [3] : Take the Inverse of a Vector\n"+
            "   + [4] : Print Vector(s) in Storage\n"+
            "   + [5] : Display Vector(s) Graphically (uses Turtle)\n"+
            "   + [6] : Additional [math] Functionality\n"+
            "   + [7] : Add or Subtract Vector(s)\n"+
            "   + [8] : Display Version and Copyright Infirmation\n"+
            "   + [9] : EXIT this program (clears data)")

    answer = input ("\n + Choose An Operation     :")
    while not answer in inputs:
        answer = input ("\n + Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not in the acceptable range.\n\n+Choose An Operation    :")
    functionlist = [None, [enter, None], [remove, None], [None, None], [None, None], [display,1]]
    #functionlist = [None, enter, remove, inverse, display, graphical, iandj, add, vers, exit]
    functionlist [int(answer)] [0](functionlist[int(answer)][1])

### ADD PARAMETER PARSING WITH THE FUNCTION CALL FOR MENU RETURN.


def display(return_Toggle):
    print("\n + All Vectors :\n")
    table = prettytable.PrettyTable(["Name","X -or- I Comp.","Y -or- J Comp.","Z -or- K Comp.","Comments"])
    for _Vector in Vectors:
        table.add_row(_Vector)
    print (table)

    if return_Toggle == 1:
        quit_Toggle = input("\n + Enter anything to continue:")
        menu()
    else:
        return

def enter (_empty):
    quantity=input ("\n + How many vectors?, 0 to exit:")
    while not type(int(quantity)) == int:
        quantity = input ("\n+ Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not an integer.\n\n+ Choose An Operation    :")
    output=[]
    if int(quantity) == 0:
        menu()
    else:
        print(" + What type of vector are you adding?\n")
        for vec in range (0,int(quantity)):
            temp=[]
            temp.append(input(" + Please choose a name for this vector: "))
            comments = input (" + Enter any comments about this vector: ")
            for comp in range (0,3):
                component=input(" + Input the " + types[comp] + " of vector number " + str(vec+1) + " :")
                temp.append(float(component))
            temp.append (comments)
            Vectors.append(temp)

    menu()

def remove(_empty):
    vector_Quantity=input ("\n + How many vectors?, 0 to exit:")
    while not type(int(vector_Quantity)) == int:
        vector_Quantity = input ("\n+ Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not an integer.\n\n+ Choose An Operation    :")
    vector_Quantity = int(vector_Quantity)
    if vector_Quantity == 0:
        menu()
    else:
        for removal in range (0,vector_Quantity):
            display(0)
            remove_Name = input("\n + What is the exact name of the vector you want to delete? :")
            Vector_names = []

            for item1 in Vectors:
                Vector_names.append(item1[0])

            while not remove_Name in Vector_names:
                remove_Name = input(" + Please re-enter :")

            if remove_Name in Vector_names:
                Vectors.remove(ijk[ijk_Names.index(remove_Name)])

    menu()


















menu()
