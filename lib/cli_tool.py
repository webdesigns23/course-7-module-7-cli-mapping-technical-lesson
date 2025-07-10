# # lib/cli_tool.py

# import argparse
# from models import Task, User

# # Global dictionary to simulate in-memory storage
# users = {}

# def add_task(args):
#     user = users.get(args.user)
#     if not user:
#         user = User(args.user)
#         users[args.user] = user
#     task = Task(args.title)
#     user.add_task(task)

# def complete_task(args):
#     user = users.get(args.user)
#     if not user:
#         print("❌ User not found.")
#         return
#     task = user.get_task_by_title(args.title)
#     if task:
#         task.complete()
#     else:
#         print("❌ Task not found.")

# def main():
#     parser = argparse.ArgumentParser(description="Task Manager CLI")
#     subparsers = parser.add_subparsers()

#     add_parser = subparsers.add_parser("add-task", help="Add a task to a user")
#     add_parser.add_argument("user")
#     add_parser.add_argument("title")
#     add_parser.set_defaults(func=add_task)

#     complete_parser = subparsers.add_parser("complete-task", help="Complete a task for a user")
#     complete_parser.add_argument("user")
#     complete_parser.add_argument("title")
#     complete_parser.set_defaults(func=complete_task)

#     args = parser.parse_args()
#     if hasattr(args, "func"):
#         args.func(args)
#     else:
#         parser.print_help()

# if __name__ == "__main__":
#     main()


# lib/cli_tool.py

import argparse
# TODO: Import Task and User classes from models module
from models import Task, User

# TODO: Initialize an empty dictionary to store users
users = {}

# TODO: Define function to handle adding a task
def add_task(args):
    # This function should:
    # - Get or create a User based on args.user
    # - Create a Task using args.title
    # - Add the task to the user's task list
    user = users.get(args.user) or User(args.user)
    users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

# TODO: Define function to handle completing a task
def complete_task(args):
    # This function should:
    # - Look up the user in the dictionary
    # - Find the task by title
    # - Mark the task as complete
    user = users.get(args.user)
    if user:
        for task in user.tasks:
            if task.title == args.title:
                task.complete()
                return
        print("❌ Task not found.")
    else:
        print("❌ User not found.")

# TODO: define main()
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI Tool")
    subparsers = parser.add_subparsers()
    
    # Add Task
    # Subparser for add-task
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Complete Task
    # Subparser for complete-task
    complete_parser = subparsers.add_parser("complete-task", help="Mark a user's task as complete")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
