# Task Manager - Command Line Application

A simple command-line task management application. Built with Python and JSON.

## 📋 Features

- ✅ Add new tasks
- 📝 View all tasks with status indicators
- ✓ Mark tasks as completed
- 🗑️ Delete tasks
- 💾 Persistent storage using JSON
- ⚠️ Error handling for invalid inputs

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required (uses Python standard library)

## 📦 Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd task-manager
```
2. Ensure you have Python installed:
```bash
python3 --version
```

## 🚀 Usage

### Running the Application

Execute the main script:
```bash
python3 tasks.py
```

### Menu Options

1. **Add new task**: Create a new task with a description
2. **View all tasks**: Display all tasks with their status and creation date
3. **Mark task as done**: Mark a specific task as completed
4. **Delete task**: Remove a task from the list
5. **Exit**: Close the application

### Example Workflow

```
1. Run the application: python3 tasks.py
2. Select option 1 to add a task
3. Enter task description: "Complete Python homework"
4. Select option 2 to view all tasks
5. Select option 3 to mark task as done (enter task ID)
6. Select option 5 to exit
```

## 📁 Project Structure

```
task-manager/
│
├── tasks.py           # Main application file
├── tasks.json         # Data storage file (auto-generated)
└── README.md          # This file
```

## 🗂️ Data Format

Tasks are stored in `tasks.json` with the following structure:

```json
{
  "id": 1,
  "description": "Task description",
  "status": "pending" or "done",
  "created_at": "2026-02-13 10:30:00"
}
```

## 🛠️ Technical Details

- **Language**: Python 3
- **Storage**: JSON file (`tasks.json`)
- **Error Handling**: Validates user input and handles file I/O errors
  
## 🐛 Error Handling

The application handles:
- Invalid task IDs
- Empty task descriptions
- Missing or corrupted JSON files
- Invalid menu choices
- File I/O errors
