def task():
    tasks=[]
    print("--TASK MANAGEMENT APP--")
    task_list=int(input("enter how many number of task do you want to set="))
    for i in range(1,task_list+1):
        task_name=input(f"enter task {i}=")
        tasks.append(task_name)
    print(f"Todays tasks are :\n{tasks}")
    while True:
        choose=int(input(" 1:ADD \n 2:UPDATE \n 3:DELETE \n 4: VIEW ALL \n 5:EXIT \n enter your choice ="))
        if choose==1:
            add=input("add a new task = ")
            if add in tasks:
                print("task already exists ")
            else:
                tasks.append(add)
                print(f"{add} task has been added")
                
        elif choose==2:
            update_val=input("which task you want to update= ")
            if update_val in tasks:
                up=input("enter new task= ")
                ind=tasks.index(update_val)
                tasks[ind]=up
                print(f"{update_val} has been updated")
                
        elif choose==3:
            delete_val=input("enter task to delete= ")
            if delete_val in tasks:
                ind=tasks.index(delete_val)
                del tasks[ind]
                print(f"{delete_val} has been deleted")
                
        elif choose==4:
            print(f"total tasks ={tasks}")
            
        elif choose==5:
            print("closing the program...")
            break
        else:
            print("invalid input")
            
task()