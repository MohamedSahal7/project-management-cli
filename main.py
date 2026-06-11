import argparse
import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")

def load_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_json(filename, data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_user(args):
    users = load_json(USERS_FILE)
    user = {
        "name": args.name,
        "email": args.email
    }
    users.append(user)
    save_json(USERS_FILE, users)
    print("User created successfully.")

def list_users(args):
    users = load_json(USERS_FILE)
    if not users:
        print("No users found.")
        return
    for user in users:
        print(f"Name: {user['name']} | Email: {user['email']}")

def add_project(args):
    users = load_json(USERS_FILE)
    if not any(user["name"] == args.user for user in users):
        print("User not found.")
        return
    projects = load_json(PROJECTS_FILE)
    project = {
        "title": args.title,
        "description": args.description,
        "due_date": args.due_date,
        "owner": args.user,
        "tasks": []
    }
    projects.append(project)
    save_json(PROJECTS_FILE, projects)
    print("Project created successfully.")

def list_projects(args):
    projects = load_json(PROJECTS_FILE)
    if not projects:
        print("No projects found.")
        return
    for project in projects:
        print(
            f"\nTitle: {project['title']}"
        )
        print(f"Owner: {project['owner']}")
        print(f"Description: {project['description']}")
        print(f"Due Date: {project['due_date']}")

def add_task(args):
    projects = load_json(PROJECTS_FILE)
    for project in projects:
        if project["title"] == args.project:
            task = {
                "title": args.title,
                "status": "Pending",
                "assigned_to": args.assigned_to
            }
            project["tasks"].append(task)
            save_json(PROJECTS_FILE, projects)
            print("Task added successfully.")
            return
    print("Project not found.")

def list_tasks(args):
    projects = load_json(PROJECTS_FILE)
    for project in projects:
        if project["title"] == args.project:
            if not project["tasks"]:
                print("No tasks found.")
                return
            for task in project["tasks"]:
                print(
                    f"Task: {task['title']} | "
                    f"Status: {task['status']} | "
                    f"Assigned To: {task['assigned_to']}"
                )
            return
    print("Project not found.")

def complete_task(args):
    projects = load_json(PROJECTS_FILE)
    for project in projects:
        if project["title"] == args.project:
            for task in project["tasks"]:
                if task["title"] == args.task:
                    task["status"] = "Completed"
                    save_json(PROJECTS_FILE, projects)
                    print("Task marked as completed.")
                    return
            print("Task not found.")
            return
    print("Project not found.")
parser = argparse.ArgumentParser(
    description="Project Management CLI Tool"
)
subparsers = parser.add_subparsers()

user_parser = subparsers.add_parser("add-user")
user_parser.add_argument("--name", required=True)
user_parser.add_argument("--email", required=True)
user_parser.set_defaults(func=add_user)

list_users_parser = subparsers.add_parser("list-users")
list_users_parser.set_defaults(func=list_users)

project_parser = subparsers.add_parser("add-project")
project_parser.add_argument("--user", required=True)
project_parser.add_argument("--title", required=True)
project_parser.add_argument("--description", required=True)
project_parser.add_argument("--due-date", required=True)
project_parser.set_defaults(func=add_project)

list_projects_parser = subparsers.add_parser("list-projects")
list_projects_parser.set_defaults(func=list_projects)

task_parser = subparsers.add_parser("add-task")
task_parser.add_argument("--project", required=True)
task_parser.add_argument("--title", required=True)
task_parser.add_argument("--assigned-to", default="")
task_parser.set_defaults(func=add_task)

list_tasks_parser = subparsers.add_parser("list-tasks")
list_tasks_parser.add_argument("--project", required=True)
list_tasks_parser.set_defaults(func=list_tasks)

complete_task_parser = subparsers.add_parser("complete-task")
complete_task_parser.add_argument("--project", required=True)
complete_task_parser.add_argument("--task", required=True)
complete_task_parser.set_defaults(func=complete_task)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()

if __name__ == "__main__":
    pass