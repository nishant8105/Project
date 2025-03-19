def main():
  tasks=[]
  
  while True:
    print("\n=====TO-DO LIST=====")
    print("1.add task")
    print("2.show task")
    print("3.Mark as done task")
    print("4.exit")
    
    choice=int(input("Enter the choice:"))
    
    if choice==1:
      n_task=int(input("enter no. of task"))
      
      for i in range(n_task):
        task= input("Enter task:")
        tasks.append({'task':task,'done':False})
        print("Task added.")
      
    elif choice==2:
      print("\n")
      for idx,task in enumerate(tasks):
        status="done" if task['done'] else "not done"
        print(f"{idx+1}.{task['task']}-{status}")
        
    elif choice==3:
      task_in=int(input("Enter task no. to mark as done:"))
      task_index=task_in-1
      if 0<=task_index<len(tasks):
        tasks[task_index]["done"]=True
        print(f"Task is done as mark {task_index+1}")
        
      else:
        print("invalid task no.")
        
    
    elif choice==4:
      print("Exiting To-Do list")
      break
    
    else:
      print("Invalid choice!!.Enter valid choice")
  print(tasks)
if __name__=="__main__":
  main()
