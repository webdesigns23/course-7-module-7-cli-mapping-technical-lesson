# lib/models.py

# TODO: Define a Task class
class Task:
    def __init__(self, title):
        # TODO: Store the title
        # TODO: Initialize completed state to False
        self.title = title
        self.completed = False

    def complete(self):
        # TODO: Set completed to True
        # TODO: Print confirmation message
        self.completed = True
        print(f"✅ Task '{self.title}' marked as complete.")


# TODO: Define a User class
class User:
    def __init__(self, name):
        # TODO: Store the user's name
        # TODO: Initialize an empty task list
        self.name = name
        self.tasks = []

    def add_task(self, task):
        # TODO: Append task to the user's task list
        # TODO: Print confirmation message
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}'s task list.")

    def get_task_by_title(self, title):
        # TODO: Return the task matching the title if it exists
        # TODO: Return None if not found
        for task in self.tasks:
            if task.title == title:
                return task
            else:
                return None
