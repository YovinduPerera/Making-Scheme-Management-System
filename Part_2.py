#PART 2
##I declare that my work contains no examples of misconduct,such as plagaiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
 #Name : Yovindu Perera
# IIT ID : 20222155                 #UoW ID : w1985733




progress_count = 0  # Progress Count
trailer_count = 0  # Module Trailer Count
retriever_count = 0  # Module Retriever Count
exclude_count = 0  # Excluded Count
total_count=0 # Total of above 4 counts
option2 = ''  # This is the option key to continue or quit.

valid = [0, 20, 40, 60, 80, 100, 120]


def Credits_at_Pass():
    while True:
        try:
            global Pass
            Pass = int(input("Enter your credits at pass: "))  # Get Credits at Pass
            if Pass in valid:  # Check whether Pass is out of range
                break
            else:
                print("Out of range")

        except ValueError:  # If we entered a string as a valid mark, this will gives "Integer required" as the output.
            print("Integer required")


def Credits_at_Defer():
    while True:
        try:
            global Defer
            Defer = int(input("Enter your credits at defer: "))  # Get Credits at Defer
            if Defer in valid:  # Check whether Defer is out of range
                break
            else:
                print("Out of range")

        except ValueError: # If we entered a string as a valid mark, this will gives "Integer required" as the output.
            print("Integer required")


def Credits_at_Fail():
    while True:
        try:
            global Fail
            Fail = int(input("Enter your credits at fail: "))  # Get Credits at Fail
            if Fail in valid:   # Check whether Fail is out of range
                break
            else:
                print("Out of range")

        except ValueError: # If we entered a string as a valid mark, this will gives "Integer required" as the output.
            print("Integer required")


while option2 != 'q':
    while True:
        Credits_at_Pass()  # Calling function credits at pass
        Credits_at_Defer()  # Calling function credits at defer
        Credits_at_Fail()  # Calling function credits at fail


        Total = Pass + Defer + Fail
        if Total == 120:
            break
        else:
            print("Total incorrrect")
    total_count = progress_count + trailer_count + retriever_count + exclude_count
    if Pass == 120:
        print("Progress")
        progress_count += 1

    elif Pass == 100:
        print("Progress (module trailer)")
        trailer_count += 1

    elif Fail <= 60:
        print("Module retriever")
        retriever_count += 1

    elif Fail > 60:
        print("Exclude")
        exclude_count += 1


    total_count = progress_count + trailer_count + retriever_count + exclude_count

    print(" ")
    
    while True:
        option2 = input("Would you like enter another data set? \nEnter 'y' for yes or 'q' to quit and view results: ")
        option2 = option2.lower()
        print(" ")
        if option2 == 'y' or option2 == 'q':
            break

        else:
            print("Please enter 'y' or 'q'")

    print("-" * 90)
    print(" ")


def Vertical():
    pro_count = progress_count
    tra_count = trailer_count
    ret_count = retriever_count
    exc_count = exclude_count

    sum_count = total_count
    print("----------------------------Vertical Histogram---------------------------------")
    print("    |" "progress ", progress_count, "|", "Trailer ", trailer_count, "|", "Retriever ", retriever_count, "|","Exclude", exclude_count, "|")

    while sum_count != 0:
        if pro_count > 0:
            print("\t *\t", end='')
            pro_count -= 1
            
        else:
            print("\t\t ", end='')

        if tra_count > 0:
            print("\t* ", end='')
            tra_count -= 1
            
        else:
            print("\t ", end='')

        if ret_count > 0:
            print("\t      *  ", end='')
            ret_count -= 1
            
        else:
            print("  \t\t   ", end='')

        if exc_count > 0:
            print("\t    *")
            exc_count -= 1
            
        else:
            print("\t ")
            print(" ")
            
        sum_count -= 1
    print(total_count, " outcomes in total")


Vertical()  # Calling function that gives us Vertical Histogram

print(" ")
print("-" * 90)
