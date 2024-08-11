def main():
    tasks=[]
    print("---- TO DO LIST ---- ",end="\n")

    total_tasks=int(input("Enter the number of tasks: "))
    for i in range (1, total_tasks+1):
        todays_task=input(f"Enter the task {i}= ")
        tasks.append(todays_task)

    print(f"Today's Tasks are \n {tasks}")

    while True:
        operations=int(input("Enter: \n1-To add a task \n2-To update a task \n3-To delete a task \n4- To check the final tasks \n5-stop \exit \nEnter here: "))
       
        if operations==1:
            add_operation=input("Enter the task you want to add: ")
            tasks.append(add_operation)
            print(f"{add_operation} has been added succesfully \n{tasks}")
        
        elif operations==2:
            update_opp=input("Enter the task you want to update: ")
            
            if update_opp in tasks:
                up_date=input("Enter the new task you want to update: ")
                in_dex=tasks.index(update_opp)
                tasks[in_dex]=up_date
                print(f"{up_date} has been updated succesfully \n{tasks}")
            
            else:
                print("No such task exists")
        
        elif operations==3:
            delete_opp=input("Enter the task you want to delete: ")
            
            if delete_opp in tasks:
                in_dex=tasks.index(delete_opp)
                del tasks[in_dex]
                print(f"{delete_opp} task succesfully deleted \n{tasks}")
            
            else:
                print("No such task exists")
        
        elif operations==4:
            print(f"Today's tasks \n{tasks}")

        elif operations==5:
            print(f"----- HAVE A GREAT DAY ----- \nToday's Total Task: \n{tasks}")
            break
        
        else:
            print("Invalid Input")

main()
        