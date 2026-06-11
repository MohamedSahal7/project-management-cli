# Project Management CLI Tool

## Overview
This is a Python-based Command-Line Interface (CLI) application that allows users to manage users, projects, and tasks. It demonstrates Object-Oriented Programming (OOP), file handling using JSON, and CLI design using `argparse`.

The system supports:
- Creating and listing users
- Creating and listing projects
- Adding and completing tasks
- Persistent storage using JSON files

## Features

### User Management
- Add new users
- List all users

### Project Management
- Assign projects to users
- List all projects
- Store project details (title, description, due date)

### Task Management
- Add tasks to projects
- View tasks per project
- Mark tasks as completed

### Data Persistence
- All data is stored in JSON files inside the `data/` folder
- Data persists between program runs

## Project Structure
project-management-cli/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│ ├── users.json
│ └── projects.json
│
├── models/
│ ├── person.py
│ ├── user.py
│ ├── project.py
│ └── task.py
│
├── tests/
│ └── test_models.py

## Installation

### 1. Clone the repository
```bash
   git@github.com:sahalmohamed1-lab/project-management-cli.git
```

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

## How to Run
Run the CLI application:
python main.py

## CLI Commands
### Add User
python main.py add-user --name "Alex" --email "alex@example.com"

### List Users
python main.py list-users

### Add Project
python main.py add-project --user "Alex" --title "CLI Tool" --description "Build a CLI system" --due-date "2026-07-01"

### List Projects
python main.py list-projects

### Add Task
python main.py add-task --project "CLI Tool" --title "Implement CLI"

### List Tasks
python main.py list-tasks --project "CLI Tool"

### Complete Task
python main.py complete-task --project "CLI Tool" --task "Implement CLI"

### Author 
- Sahal Mohamed.
