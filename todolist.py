tasks = ["Study","Reading","Writing","Watching movie"]

n = input("Do you want to add a task or mark a task as complete? (add/mark): ")
if n == "add":
    print("ADDING TASK")
    n2 = int(input("How many tasks do you want to add: "))
    for i in range(n2):
        task = input(f"Enter task {i+1}: ")
        tasks.append(task)
    print("Tasks added successfully!")
elif n == "mark":
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        n4 = int(input("Enter the number of the task you want to mark as done: "))
        if 1 <= n4 <= len(tasks):
            print(f"Task {n4} ({tasks[n4-1]}) is completed")
        else:
            print("Invalid task number")
else:
    print("ERROR!!! You can only add tasks or mark them as done")