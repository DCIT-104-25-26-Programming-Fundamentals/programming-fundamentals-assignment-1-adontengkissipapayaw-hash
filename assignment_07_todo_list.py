# =============================================================================
# To-Do List Application — Console Edition
# Topic: Lists, Functions, and User Interaction
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# A simple, friendly to-do list program where you can:
#   - Add tasks to your list
#   - View all your tasks
#   - Delete tasks when they're done
#   - Keep using it until you're ready to quit
#
# All tasks are stored in a list and persist during your session.
#
# =============================================================================
# YOUR CODE BELOW — implement the required functions
# =============================================================================


# Global task list
tasks = []


def add_task():
    """Add a new task to the to-do list."""
    task = input("\nWhat task would you like to add? ").strip()
    if not task:
        print("Error: Task cannot be empty.")
        return
    tasks.append(task)
    print(f"✓ Task added: \"{task}\"")


def view_tasks():
    """Display all tasks currently in the list."""
    print("\n" + "─" * 50)
    if not tasks:
        print("Your to-do list is empty. Time to relax! 😊")
    else:
        print("Your Tasks:")
        print("─" * 50)
        for i, task in enumerate(tasks, start=1):
            print(f"  {i}. {task}")
    print("─" * 50)


def delete_task():
    """Delete a task from the list."""
    if not tasks:
        print("\nError: Your to-do list is empty. Nothing to delete!")
        return
    
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if task_num < 1 or task_num > len(tasks):
            print(f"Error: Please enter a number between 1 and {len(tasks)}.")
            return
        
        removed_task = tasks.pop(task_num - 1)
        print(f"✓ Task \"{removed_task}\" has been removed.")
    except ValueError:
        print("Error: Please enter a valid number.")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 50)
    print("          TO-DO LIST MENU")
    print("=" * 50)
    print("  1. Add task")
    print("  2. View tasks")
    print("  3. Delete task")
    print("  4. Quit")
    print("=" * 50)


def main():
    """Main menu loop."""
    print("\nWelcome to your Personal To-Do List! 📝")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("\nGoodbye! Keep being productive! 👋")
            break
        else:
            print("\nError: Please enter a valid choice (1, 2, 3, or 4).")


if __name__ == "__main__":
    main()

