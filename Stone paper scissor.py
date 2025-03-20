import random
user_score=0
comp_score=0
while True:
  my_list=["stone","paper","scissor","quit"]
  my_list1=["stone","paper","scissor"]
  comp = random.choice(my_list1)
  user = str(input("Enter stone, paper,scissor (or 'quit' to exit)\n")).lower()
  if user not in my_list:
    print ("give proper input")
    continue
  if user=="quit":
      print("Exiting the game")
      break
  
  def check(comp,user):
    if comp==user:
      return 0
    
    elif(comp=="paper" and user=="stone"):
      return ("computer")
    elif(comp=="stone"and user=="scissor"):
      return ("computer")
    elif(comp=="scissor" and user=="paper"):
      return ("computer")
    elif(user=="paper" and comp=="stone"):
      return ("user")
    elif(user=="stone"and comp=="scissor"):
      return ("user")
    elif(user=="scissor" and comp=="paper"):
      return ("user")
    
  result=check(comp,user)
  
  print(f"You:{user}")
  print(f"comp:{comp}")
  
  if result=="computer":
    print("you lose")
    comp_score+=1
  elif result=="user":
    print ("you win")
    user_score+=1
  else:
    print("its draw")
  
  print(f"Current score-->YOU:{user_score}|COMP:{comp_score}")