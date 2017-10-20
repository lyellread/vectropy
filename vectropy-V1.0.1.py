##pyvecadd
version = "1.0.0"

print ("+ Version: "+version+"; Author: Lyell Read")
##A Program by Lyell Read
print ("\n+ Start this program with Python Turtle?\n   + Note: This will not allow for graphical vector display if off")
turtle_Toggle = input("\n+ Turn turtle on? (Y/N)      :")
import time
#import Turtle

def title ():
    print (str("\n")*70+"+----------------------------------------------+\n|vectorpy- a Python Vector Program, Vers. "+
            version+"|\n|       Date: "+ time.strftime("%m/%d/%Y")+ "  Time: "+ time.strftime("%H:%M:%S")+
            ".       |\n+----------------------------------------------+")

def enter():
    print ("SUCCESS")

##Menu##
def menu ():

    # 1:Add Vector 2: print Vectors, 3: delete vectors 4: inverse vectors, 5: Add or subtract vectors, 6:I and J vectors; 7:

    print("\n+ Main Menu:\n"+
            "   + [1] : Add Vector(s) Into Storage\n"+
            "   + [2] : Delete Vector(s) From Storage\n"+
            "   + [3] : Take the Inverse of a Vector\n"+
            "   + [4] : Print Vector(s) in Storage\n"+
            "   + [5] : Display Vector(s) Graphically (uses Turtle)\n"+
            "   + [6] : Additional Functionality with I, J and K Vector(s)\n"+
            "   + [7] : Add or Subtract Vector(s)\n"+
            "   + [8] : Display Version and Copyright Infirmation\n"+
            "   + [9] : EXIT this program (clears data)")

    answer = input ("\n+ Choose An Operation     :")
    while not type(answer) == int and answer not in range (1,10):
        answer = input ("\n+ Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not in the acceptable range.\n\n+Choose An Operation    :")
    #functionlist = [None, enter, remove, inverse, display, graphical, iandj, add, vers, exit]
    #functionlist[answer]()

menu()
