import math

history=[]
def choices():
    print("welcome to simple calculator")
    print("Entre your choice from below")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. remainder/modulas")
    print("6. Square Root")
    print("7. exponentiation")
    print("8.view history")
    print("9.clear history")
    print("10. EXIT")
    
def get_choice():
    while True:
      choice=input("Enter your choice:")
      if choice in ['1','2','3','4','5','6','7','8','9','10']:
        return choice
      else:
        print("'INVALID' choice Enter again number in between 1-10")       

def add(x,y):
    return x+y
    
   
def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
    
def div(x,y):
    if y!=0:
        return x/y
    else:
        return"ERROR, division by zero"

def mod(x,y):
    return x%y

def view_history():
  if history:
    print("\n:---Calculation of history---")
    for idx,record in enumerate(history,1):
      print(f"{idx,record}")
    print("\n")
  else:
    print("No history avialable\n\n")
    
def clear_history():
  history.clear()
  print("History is cleared\n\n")
  
def sqrt(x):
    if x<0:
        return "ERROR, square root of negative number is not real"
    else:
        return math.sqrt(x)

        
def expo(x,y):
    return x**y
    
    
while True:
    choices()
    choice= get_choice()
    
    if choice=='1':
      num1=float(input("Enter first number"))
      num2=float(input("Enter second number"))
      result=add(num1,num2)
      history.append(f"{num1}+{num2}={result}")
      print(f"The addition is:{add(num1,num2)}\n\n")
        
    elif choice=='2':
      num1=float(input("Entre first number"))
      num2=float(input("Enter second number"))
      result=sub(num1,num2)
      history.append(f"{num1}-{num2}={result}")
      print(f"The subtration is:{sub(num1,num2)}\n\n")
        
    elif choice=='3':
      num1=float(input("Enter first number"))
      num2=float(input("Enter secomd number"))
      result=mul(num1,num2)
      history.append(f"{num1}*{num2}={result}")
      print(f"The multiplication is:{mul(num1,num2)}\n\n")
        
    elif choice=='4':
      num1=float(input("Enter first number"))
      num2=float(input("Enter second number"))
      result=div(num1,num2)
      history.append(f"{num1}/{num2}={result}")
      print(f"The division is:{div(num1,num2)}\n\n")
        
    elif choice=='5':
      num1=float(input("Enter first number"))
      num2=float(input("Enter second number"))
      result=mod(num1,num2)
      history.append(f"{num1}%{num2}={result}")
      print(f"The modulas is {mod(num1,num2)}\n\n")
        
    elif choice=='6':
      num1=float(input("Enter first number"))
      result=sqrt(num1)
      history.append(f"sqrt{num1}={result}")
      print(f"The square root is : {sqrt(num1)} \n\n")
        
    elif choice=='7':
      num1=float(input("Enter first number"))
      num2=float(input("Enter second number"))
      result=expo(num1,num2)
      history.append(f"{num1}**{num2}={result}")
      print(f"The exponentiation is: {expo(num1,num2)}\n\n")
        
    elif choice=='8':
      view_history()
      
    elif choice=='9':
      clear_history()
      
    elif choice=='10':
      print("THANK YOU")
      break
print("THANKS")
