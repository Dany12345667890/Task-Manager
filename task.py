def add_task(task_id):
    task_name = input("Input new task: ").strip()
    if not task_name:
        print("Task cannot be empty.")
        return None

    print("\nChoose priority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    choice = input("Enter 1, 2 or 3 (default = Medium): ").strip()

    if choice == "1":
        priority = "high"
    elif choice == "3":
        priority = "low"
    else:
        priority = "medium"

    task = {
        "id": task_id,
        "name": task_name,
        "status": "not completed",
        "priority": priority,
    }
    return task


def complete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return False

    try:
        task_id = int(input("Please input the task id to complete: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "completed":
                print("Task is already completed")
            else:
                task["status"] = "completed"
                print("Task is completed")
            return True

    print("Task not found")
    return False


def edit_task(tasks):
    if not tasks:
        print("No tasks available.")
        return False

    try:
        task_id = int(input("Please input the task id to edit: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    for task in tasks:
        if task["id"] == task_id:
            new_name = input("Enter new task: ").strip()
            if new_name:
                task["name"] = new_name
                print("Task has been updated")
            else:
                print("Name cannot be empty.")
            return True

    print("Task not found")
    return False


def delete_task(tasks):
    if not tasks:
        print("No tasks available.")
        return False

    try:
        task_id = int(input("Please input the task id to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task has been removed")
            return True

    print("Task not found")
    return False
