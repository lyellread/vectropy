##vectropy
##Lyell Read

import prettytable
import time

version = "1.1.4"
inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # I know its lazy; Who cares?
Vectors = []
types = ["X -or- i", "Y -or- j", "Z -or- k"]
names = []


print(" + Version: " + version + "; Author: Lyell Read")
# print(
#     "\n + Start this program with Python Turtle?\n    - Note: This will not allow for graphical vector display if off"
# )

# ##Verify here input Y/N
# turtle_Toggle = input("\n + Turn turtle on? (Y/N):")


def title():
    print(
        str("\n") * 70
        + "+----------------------------------------------+\n|vectropy- a Python Vector Program, Vers. "
        + version
        + "|\n|       Date: "
        + time.strftime("%m/%d/%Y")
        + "  Time: "
        + time.strftime("%H:%M:%S")
        + "       |\n+----------------------------------------------+"
    )


def menu():

    # 1:Add Vector 2: print Vectors, 3: delete vectors 4: inverse vectors, 5: Add or subtract vectors, 6:I and J vectors; 7:
    title()
    print(
        "\n + Main Menu:\n"
        + "   + [1] : Add Vector(s) Into Storage\n"
        + "   + [2] : Delete Vector(s) From Storage\n"
        + "   + [3] : Take the Inverse of a Vector\n"
        + "   + [4] : Print Vector(s) in Storage\n"
        + "   + [5] : Display Vector(s) Graphically (uses Turtle if available)\n"
        + "   + [6] : Additional Math Functionality\n"  ## Might change this if cli print is too hard with thetas and len's
        + "   + [7] : Add or Subtract Vector(s)\n"
        + "   + [8] : Display Version and Copyright Infirmation\n"
        + "   + [9] : EXIT this program (clears data)"
    )

    answer = input("\n + Choose An Operation     :")
    while not answer in inputs:  # verify that a valid command has been entered
        answer = input(
            "\n + Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not in the acceptable range.\n\n+Choose An Operation    :"
        )

    # Define a list of available functions in the format [[function_name, parse_value],...]
    functionlist = [
        None,
        [enter, None],
        [remove, None],
        [None, None],
        [display, 1],
        [None, None],
        [None, None],
        [None, None],
        [None, None],
        [_exit, 1],
    ]

    functionlist[int(answer)][0](
        functionlist[int(answer)][1]
    )  # calls the functon at [answer][0] index of the nested function list... then parse it the [answer][1] value, which is often None


### ADD PARAMETER PARSING WITH THE FUNCTION CALL FOR MENU RETURN.


def display(return_Toggle):
    print("\n + All Vectors :\n")
    table = prettytable.PrettyTable(
        ["Name", "X -or- I Comp.", "Y -or- J Comp.", "Z -or- K Comp.", "Comments"]
    )  # PrettyTable module used for nice tables
    for _Vector in Vectors:  # adds a row for every vector in the Vector list
        table.add_row(_Vector)
    print(table)  # Print the table now that it is made

    if (
        return_Toggle == 1
    ):  # sometimes, display() is called by other fxn's with the return_Toggle = 0 so that it prints and returns without requiring action for inline printout
        quit_Toggle = input("\n + Enter to continue:")
        menu()
    else:
        return


def enter(_empty):  # the parsed value is nont anyway so therefore _empty = None
    quantity = input(
        "\n + How many vectors?, 0 to exit:"
    )  # define quantity of vectors to add to the list
    while (
        not type(int(quantity)) == int
    ):  ##Must be fixed: This is by defenition either a TRUE or an ERROR
        quantity = input(
            "\n+ Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not an integer.\n\n+ Choose An Operation    :"
        )
    if int(quantity) == 0:
        menu()  # if the number of vectors is zero, the user does not want to enter more, so we quit to menu
    else:
        for vec in range(0, int(quantity)):  # repeat vector quantity times
            temp = []  # What could be bad with another empty list ;)
            temp_Name = input(
                " + Please choose a name for this vector: "
            )  # add name in [vec][0]
            while [True for x in Vectors if x[0] == temp_Name] == [
                True
            ]:  # Hey sometimes you gotta use a list comprehension where its probably not meant to be
                temp_Name = input(
                    " + Please re-enter the name of the vector or enter 'replace' to override the vector in storage"
                )
            temp.append(temp_Name)
            comments = input(
                " + Enter any comments about this vector: "
            )  # comments have to wait until the end of the vector list [4]
            for comp in range(0, 3):  # enumerate the X, Y, Z component entry
                component = input(
                    " + Input the "
                    + str(types[comp])
                    + " of vector number "
                    + str(vec + 1)
                    + " :"
                )  # Instructions for the user.
                temp.append(
                    float(component)
                )  # Append X,Y,Z in order in indexes [1],[2],[3] respectively
            temp.append(comments)  # Now add the comments in index [4]
            Vectors.append(
                temp
            )  # Bring this simgle vector into the larger Vectors list

    menu()  # return to menu


def remove(_empty):
    vector_Quantity = input(
        "\n + How many vectors to remove?, 0 to exit:"
    )  # Usual start here
    while (
        not type(int(vector_Quantity)) == int
    ):  ## Again needs repairing as this will return ERROR or TRUE
        vector_Quantity = input(
            "\n+ Choose An Operation Again; \n   + The last operation resulted in failure, as the input was not an integer.\n\n+ Choose An Operation    :"
        )
    vector_Quantity = int(vector_Quantity)
    if vector_Quantity == 0:  # return to menu if entered input is zero
        menu()
    else:
        for removal in range(0, vector_Quantity):  # loop number of vectors to remove
            display(
                0
            )  # show vectors in storage, calling display() function with the 0 flag to keep it returning to this function without a break
            remove_Name = input(
                "\n + What is the exact name of the vector you want to delete? :"
            )
            Vector_names = []  # define temporary list for names of all vectors

            Vector_names = [item1[0] for item1 in Vectors]  # List Comprehension!!

            while (
                not remove_Name in Vector_names
            ):  # check for presence of the name in the list
                remove_Name = input(" + Please re-enter :")

            Vectors.remove(
                Vectors[remove_Name.index(remove_Name)]
            )  # remove the specific vector from the main list

    menu()


def _exit(x):
    exit()


menu()
