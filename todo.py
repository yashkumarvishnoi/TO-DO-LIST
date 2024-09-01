tasks=[]

def addTasks(task):
    tasks.append({"task":task,"status":False})
    print(f"Task {task} added successfully")

def markTasks(index):
    if index >= 0 and  index< len(tasks):
        if tasks[index]["status"] == True:
            print("Task has already been completed")
        else:
            tasks[index]["status"]=True
            tsk=tasks[index]["task"]
            print(f"Your Task of {tsk} has been marked successfully")
    else:
        print("The Task you want to access does not exist")

def deleteTasks(index):
    if index >= 0 and  index< len(tasks):
        deltask=tasks.pop(index)
        tsk=deltask["task"]
        print(f"{tsk} has been deleted")
    else:
        print("The task you want to Delete does not exist")
        
def showTasks():
    print("\n\n")
    for i,task in enumerate(tasks):
        t=task["task"]
        st=task["status"]
        
        print(f"{i}. {t} -{st}")

def main():
    while True:
        try:
            print("\n\n---To-Do List Application---")
            print("1: Add a Task to the list")
            print("2: Mark a Task as Complete")
            print("3: Delete a Task from the list")
            print("4: Show the To-Do List")
            print("5: Exit")
            choice=int(input("Please provide your choice:---"))

            match choice:
                case 1:
                    task=input("Enter the task you want to add:--")
                    addTasks(task)
                case 2:
                    index=int(input("Enter the index of task you want to mark as complete:--"))  
                    markTasks(index)
                case 3:
                    index=int(input("Enter the index of task you want to delete:--"))  
                    deleteTasks(index)
                case 4:
                    showTasks()
                case 5:
                    break
        except ValueError:
            print("Invalid input. Please enter an integer index not String/float.")
        

main()
