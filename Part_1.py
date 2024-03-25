#PART 1
##I declare that my work contains no examples of misconduct,such as plagaiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name : Yovindu Perera
# IIT ID : 20222155                 #UoW ID : w1985733


progress_count = 0  # Progress Count
trailer_count = 0  # Module Trailer Count
retriever_count = 0  # Module Retriever Count
exclude_count = 0  # Excluded Count
total_count=0
option2 = ''  # This is the option key to continue or quit.
option1 = 0  # This is the first option key to what would you choose either Student Version or Staff Version.
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
            if Defer in valid:
                break
            else:
                print("Out of range")# Check whether Fail is out of range

        except ValueError:  # If we entered a string as a valid mark, this will gives "Integer required" as the output.
            print("Integer required")


def Credits_at_Fail():
    while True:
        try:
            global Fail
            Fail = int(input("Enter your credits at fail: "))  # Get Credits at Fail
            if Fail in valid: # Check whether Defer is out of range
                break
            else:
                print("Out of range")

        except ValueError:  # If we entered a string as a valid mark, this will gives "Integer required" as the output.
            print("Integer required")
def Horizontal():
    print("--------------------Horizontal Histogram--------------------")
    print(" ")
    print('Progress         ', progress_count, '   : ', '*' * progress_count)
    print('Trailer          ', trailer_count, '   : ', '*' * trailer_count)
    print('Retriever        ', retriever_count, '   : ', '*' * retriever_count)
    print('Excluded         ', exclude_count, '   : ', '*' * exclude_count)
    print(" ")

    global total_count
    total_count = progress_count + trailer_count + retriever_count + exclude_count
    print(total_count, " outcomes in total")



while True:
    
    option1 = int(input("Enter number 1 for Student Version or \n      Number 2 for Staff Version:     \n"))

    if option1 == 1 or option1 == 2:
        break
    else:
        print("Enter '1' or '2' ")



if option1 == 1:
    print("-------------------------------Welcome to Student Version-------------------------------")
    print(" ")
    while True:
        
        Credits_at_Pass()  #Calling function credits at pass
        Credits_at_Defer() #Calling function credits at defer
        Credits_at_Fail()  #Calling function credits at fail
        Total = Pass + Defer + Fail
        if Total == 120:
            break
        else:
            print("Total incorrrect")
    
        
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
    print("------------------------Thank you---------------------------")    


if option1 == 2:
    print("-------------------------------Staff Version with Histogram-------------------------------")
    print(" ")
    while option2 != 'q':
        while True:
            Credits_at_Pass()  #Calling function credits at pass
            Credits_at_Defer() #Calling function credits at defer
            Credits_at_Fail()  #Calling function credits at fail

            Total = Pass + Defer + Fail
            if Total == 120:
                break
            else:
                print("Total incorrrect")
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

        while True:
            print(" ")
            option2 = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            option2 = option2.lower()
            print(" ")
            if option2 == 'y' or option2 == 'q':
                break

            else:
                print("Please enter 'y' or 'q'")

    Horizontal() #Calling Function that gives us Horizontal Histogram
