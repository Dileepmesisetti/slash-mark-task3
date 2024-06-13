tasks = []

def add_task(task):
    tasks.append({"task":task,"Completed":False})
    print("Added task: '{task}'")
    
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        for i,task in enumerate(tasks):
            status = "*"
            print(f"{i}. [{status}] {task['task']}")
            
def remove_task(task_number):
    if 0 <= task_number < len(tasks):
        removed_tasks = tasks.pop(task_number)
        print(f"Removed tasks: '{removed_tasks['task']}'")
    else:
        print("Invalid task number")
def main():
    while True:
        print("**** TO - DO LIST ****")
        print("1.Add Task")
        print("2.Remove task")
        print("3.Show task")
        print("4.Exit")
        
        choice = input("Enter your choice:")
        
        if choice == '1':
            print()
            task_number = int(input("How many tasks you want to add:"))
            
            for i in range(task_number):
                task = input("Enter the task:")
                tasks.append({"task":task,"done":False})
                print("Task added...!")
                
        elif choice == '2':
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except:
                print("Please enter a vaild number")
                
                
        elif choice == '3':
            show_tasks()
        
                
        elif choice == '4':
            print("Exiting the TO-DO list.")
            break
        else:
            print("Invalid choice , please try again.")
            
if __name__ == "__main__":
    main()