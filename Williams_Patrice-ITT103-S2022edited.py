

# Function definition for Class 1
def commission_1(amount=0.0):
    sales_amount = (float(amount))
    if sales_amount <= 1000:
        return round(sales_amount * 0.06 , 2)
     
    elif sales_amount > 1000 and sales_amount < 2000:
        return round(sales_amount * 0.07 , 2)
        
    elif sales_amount >= 2000:
        return round( sales_amount * 0.10 , 2)

     
# Function definition for Class 2
def commission_2(amount = 0.0):
    sales_amount = (float(amount))
    if sales_amount < 1000:
        return round(sales_amount * 0.04 , 2)
        
    elif sales_amount >= 1000:
        return round(sales_amount * 0.06 , 2)


# Function definition for Class 3
def commission_3(amount = 0.0):
    sales_amount = (float(amount))
    return round(sales_amount * 0.045 , 2)

    
# Function definition to check if Sales Number is Valid    
def validateID(x):
    if len(x) == 0:
        print("Error! Field cannot be empty")
        main()
        
    elif len(x) != 5:
        print("Invalid Input! Sales number must be 5 characters long. Try Again")
        main()
        
    initials = x[0:2]
    if not initials.isalpha():
        print("Invalid Input! Sales number must start with 2 letters(First and Last initial). Try Again")
        main()

    user_num = x[-3:]
    if not user_num.isdigit():
        print("Invalid Input! Sales number must end with 3 numbers. Try Again")
        main()
    else:
        return x
    

# Function definition to check if Sales Amount input is decimal
def check(y):    
    try:
        float(y)
        return True
    except ValueError:
        return False
            

# Function definition to check if Sales Amount input is Valid    
def validateAmt(y):
    x = str(y)
    if check(y) == True:
        return y
    else:
        print("Invalid Input! Please enter a decimal value")
        get_Amt()
    if len(x) == 0:
         print("Error! Field cannot be empty")
         get_Amt()
         
# Function definition to check if Sales Amount input is Valid   
def validateClass(option):
    status = False
    if option == "1" or option == "2" or option == "3":
        status = True
        return status
    else:
         print(f"The Class '{option}' is not an option.")
         
   

# Function definition to Prompt for Salesperson Number    
def get_ID():
    print("\nPlease enter your sales number: ")
    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        time.sleep(6)
        sys.exit()
    else:
        agent_num = str(input())
        return validateID(agent_num) # Call ID Validation Function


# Function definition to Prompt for Sales Amount                 
def get_Amt():
    print("\nPlease enter sales amount: ")
    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        time.sleep(6)
        sys.exit()
    else:
        amt = str(input())
        return validateAmt(amt) # Call Sales Validation Function


# Function definition to Prompt for Sales Class
def get_Class():
    print("\nPlease enter: \n \t '1' for Class 1 \n \t '2' for Class 2 \n \t '3' for Class 3 \n \t 'Esc' to exit")
    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        time.sleep(6)
        sys.exit()
    else:
        opt = str(input())
        return opt 


    
# Function definition to display results
def displayDetails(ID="",Amt=0.0, Comm=0.0):
    print("\t\t Details")
    print("\t ________________________________")
    print("\n\t Sales Number: \t\t" ,ID)
    print("\n\t Total Sales: \t\t$" , Amt)
    print("\n\t Commission Earned:\t$" ,Comm)
    print("\t ________________________________")


 
# Function definition to run calculation   
  
def main():
    ID = get_ID() #Call Function
    sales = get_Amt() #Call function and assign return value
    
    while True: #Loops Until validation function returns true
        Class = get_Class() #Call function and assign return value
        
        classDict={ 
                    '1': commission_1(sales), #Call Class1 Function
                    '2': commission_2(sales), #Call Class2 Function
                    '3': commission_3(sales), #Call Class3 Function
                  }
            
        if validateClass(Class) == True:
            displayDetails(ID.upper(),sales, classDict.get(Class, f""))
            break
                  
               


    
import keyboard
import sys
import time

print ("\nWelcome to JamEx Commission Calculator!   ")


while True:    #Loop until user presses 'Esc'
    
    print("\nPress Esc to exit at any time. ")

    main()
    
    if keyboard.read_key() == "esc":
        print("You pressed 'Esc'. Exiting Console...")
        break
        time.sleep(6)
        sys.exit()
    
    
            



















