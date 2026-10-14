from task import add_task, complete_task, edit_task, delete_task
from storage import save_data, load_data


tasks = load_data()
next_id = 1

if tasks:
    next_id = max(task.get("id", 0) for task in tasks) + 1

while True:
    print("       TASK MANAGER     ")
    print("=" * 30)
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Exit")
    print("=" * 30)

    try:
        users_choice = int(input("Input choice: "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    if users_choice == 1:
        task = add_task(next_id)
        if task is not None:
            tasks.append(task)
            save_data(tasks)
            next_id += 1
            print("Task Added")

    elif users_choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            priority_order = {"high": 0, "medium": 1, "low": 2}
            sorted_tasks = sorted(tasks, key=lambda t: priority_order.get(t["priority"], 99))
            print("------ Your Tasks sorted by priority -------")
            for task in sorted_tasks:
                status_icon = "✅" if task["status"] == "completed" else "o"
                print(f"[{task['id']}] {status_icon} {task['name']}  {task['priority'].upper()}")

    elif users_choice == 3:
        if complete_task(tasks):
            save_data(tasks)

    elif users_choice == 4:
        if edit_task(tasks):
            save_data(tasks)

    elif users_choice == 5:
        if delete_task(tasks):
            save_data(tasks)

    elif users_choice == 6:
        save_data(tasks)
        print("Goodbye")
        break
    else:
        print("Wrong input. Please input from 1 to 6.")
    