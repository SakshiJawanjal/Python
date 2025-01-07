import os

class ToDoListApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks to display.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self):
        task = input("Enter the new task: ").strip()
        if task:
            self.tasks.append(task)
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    def update_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter the task number to update: "))
                if 1 <= task_num <= len(self.tasks):
                    updated_task = input("Enter the updated task: ").strip()
                    if updated_task:
                        self.tasks[task_num - 1] = updated_task
                        print("Task updated successfully.")
                    else:
                        print("Updated task cannot be empty.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(self.tasks):
                    deleted_task = self.tasks.pop(task_num - 1)
                    print(f"Task '{deleted_task}' deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.view_tasks()
                elif choice == 2:
                    self.add_task()
                elif choice == 3:
                    self.update_task()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    print("Exiting the application. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
