##I declare that my work contains no examples of misconduct,such as plagaiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
 #Name : Yovindu Perera
# IIT ID : 20222155                 #UoW ID : w1985733



#-----------------------------------PART 1 - Main Version---------------------------------

progress_count = 0        #Progress Count
trailer_count = 0         #Module Trailer Count
retriever_count = 0       #Module Retriever Count
exclude_count = 0         #Excluded Count
total_count = 0           #Total of above 4 counts
part3list = []            #This list belongs to part 3(List/Tuple/Directory)

option1 = 0               #This is the first option key to what would you choose either Student Version or Staff Version.
option2 = ''              #This is the option key to continue or quit.


valid = [0, 20, 40, 60, 80, 100, 120]

def Credits_at_Pass():
    while True:
        try:
            global Pass
            Pass = int(input("Enter your credits at pass: "))           #Get Credits at Pass
            if Pass in valid: #Check whether Pass is out of range
                break
            else:
                print("Out of range")
                
        except ValueError: #If we entered a string as a valid mark, this will gives "Integer required" as the output.
            print("Integer required")

def Credits_at_Defer():
    while True:
        try:
            global Defer
            Defer = int(input("Enter your credits at defer: "))         #Get Credits at Defer
            if Defer in valid:  
                break
            else:
                print("Out of range")
                
        except ValueError:
            print("Integer required")

def Credits_at_Fail():
    while True:
        try:
            global Fail
            Fail = int(input("Enter your credits at fail: "))           #Get Credits at Fail
            if Fail in valid: 
                break
            else:
                print("Out of range")
                
        except ValueError:
            print("Integer required")

while True:
    
    option1 = int(input("Enter number 1 for Student Version or \n      Number 2 for Staff Version:     \n"))

    if option1 == 1 or option1 == 2:
        break
    else:
        print("Enter '1' or '2' ")

print(" ")
if option1 == 1:
    print("------------------------------Welcome to Student Version------------------------------")
    print(" ")
    Credits_at_Pass()   #Calling credits at pass
    Credits_at_Defer()  #Calling credits at defer 
    Credits_at_Fail()   #Calling credits at fail


    Total = Pass + Defer + Fail
    if Total != 120:
        print("Total Incorrect")
    
    if Pass == 120:
        print("Progress")

    elif Pass == 100:
        print("Progress (module trailer)")

    elif Fail <= 60:
        print("Module retriever")

    elif Fail > 60:
        print("Exclude")

    print("--------------------------------Thank you------------------------------")        
            
            
if option1 == 2:
    print("-------------------------------Staff Version with Histogram-------------------------------")
    print(" ")
    while option2 != 'q':
        while True:
            
            Credits_at_Pass()   #Calling credits at pass
            Credits_at_Defer()  #Calling credits at defer
            Credits_at_Fail()   #Calling credits at fail

            Total = Pass + Defer + Fail
            if Total == 120:
                break
            else:
                print("Total incorrrect")
        if Pass == 120:
            print("Progress")
            progress_count += 1
            part3list.append(["Progress -" , Pass , Defer, Fail ])
        elif Pass == 100:
            print("Progress (module trailer)")
            trailer_count += 1
            part3list.append(["Progress (module trailer) -" , Pass , Defer, Fail ])
        elif Fail <= 60:
            print("Module retriever")
            retriever_count += 1
            part3list.append(["Module retriever -" , Pass , Defer, Fail ])
        elif Fail > 60:
            print("Exclude")
            exclude_count += 1
            part3list.append(["Exclude –" , Pass , Defer, Fail ])
            

            
        print(" ")
        
        while True:
            option2 = input("Would you like enter another data set? \nEnter 'y' for yes or 'q' to quit and view results: ")
            option2 = option2.lower()
            print(" ")
            if option2 == 'y' or option2 == 'q':
                break

            else:
                print("Please enter 'y' or 'q'")

    print("-"*90)
    print(" ")

    def Horizontal():    
        print("--------------------Horizontal Histogram--------------------")
        print(" ")
        print('Progress         ' ,progress_count,  '   : ','*' * progress_count)
        print('Trailer          ' ,trailer_count,  '   : ','*' * trailer_count)
        print('Retriever        ' ,retriever_count,  '   : ','*' * retriever_count)
        print('Excluded         ' ,exclude_count,  '   : ','*' * exclude_count)
        print(" ")

        global total_count
        total_count = progress_count + trailer_count + retriever_count + exclude_count
        print(total_count, " outcomes in total")

    Horizontal() #Calling function that gives us Vertical Histogram

    print(" ")
    print("-"*90)
    print(" ")

    #-----------------------------------PART 2 - Vertical Histogram--------------------------------
    print("-----------------------Vertical Histogram-----------------------")
    print(" ")

    def Vertical():
        pro_count = progress_count
        tra_count = trailer_count
        ret_count = retriever_count
        exc_count = exclude_count

        sum_count = total_count

        print("     progress ",progress_count,"|", "Trailer ",trailer_count,"|", "Retriever ",retriever_count,"|", "Exclude",exclude_count,"|")
        while sum_count != 0:
            if pro_count > 0:
                print("\t *\t", end = '')
                pro_count -= 1
                sum_count -= 1
            else:
                print("\t\t ", end = '')

            if tra_count > 0:
                print("\t* ", end = '')
                tra_count -= 1
                sum_count -= 1
            else:
                print("\t ", end = '')

            if ret_count > 0:
                print("\t      *  ", end = '')
                ret_count -= 1
                sum_count -= 1
            else:
                print("  \t\t   ", end = '')

            if exc_count > 0:
                print("\t    *")
                exc_count -= 1
                sum_count -= 1
            else:
                print("\t ")
        print(" ")
        print(total_count, " outcomes in total")
        

    Vertical() #Calling function that gives us Vertical Histogram

    print(" ")
    print("-"*90)

    #-----------------------------------PART 3 -  List/Tuple/Directory (extension) -----------------------------------
    def elementlist():
        for factor in part3list:
            print(f'{factor[0]} {factor[1]}, {factor[2]}, {factor[3]}')
        print()
    elementlist()   #Calling function that makes a list of progression outcomes 
    

    #-----------------------------------PART 4 - Text File -----------------------------------
    def Textfile():
      with open("Mycw.txt","w")as File_Name: #Saving file as text file
        for factor in part3list:
            print(f'{factor[0]} {factor[1]}, {factor[2]}, {factor[3]}',file = File_Name)
        print()
      with open("Mycw.txt","r") as File_Name: #Reading entire file
          print(File_Name.read())

    Textfile()  #Calling function that save a list of progression outcomes to a text file


print("----------------------------------THE END--------------------------------")
