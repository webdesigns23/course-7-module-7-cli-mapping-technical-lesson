
# Technical Lesson: Mapping Objects with Relations to CLI

## Learning Goals

- Define Python classes to represent real-world entities like users and tasks.
- Use `argparse` to map CLI commands to object-oriented behavior.
- Manage relationships between objects through composition.
- Build maintainable CLI tools that reflect real-world workflows.

---

## Introduction

In this lesson, you’ll build a Python command-line tool that allows users to manage tasks using structured commands. Each user can be assigned tasks, and those tasks can be marked as completed using method calls tied to command-line arguments.

This approach highlights how OOP principles can be tied to CLI interaction logic, offering modular, readable, and testable design.

---

## Project Setup

### 1. Clone the Repository

```bash
git clone <repo-url>
cd course-7-module-7-cli-mapping-technical-lesson
```

### 2. Install Dependencies

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

---

## Running the CLI

To run the CLI tool:

```bash
python lib/cli_tool.py add-task Alice "Submit report"
python lib/cli_tool.py complete-task Alice "Submit report"
```

Each command adds or completes a task for a user stored in memory.

---

## Code Structure

```
.
├── lib/
│   ├── __init__.py
│   ├── cli_tool.py           # Main argparse CLI logic
│   └── models.py             # Contains Task and User classes
├── test_cli_tool.py          # Test CLI logic and behavior
├── Pipfile
├── Pipfile.lock
├── pytest.ini
├── README.md
```

---

## Best Practices for CLI Object Mapping

- Keep CLI logic and object logic in separate modules.
- Map CLI actions to object methods cleanly.
- Use lists and dictionaries to store in-memory state during runtime.
- Include help messages and validation for smoother UX.
- Print confirmations for task actions to simulate persistence.

---

## Conclusion

By completing this lesson, you’ll be able to:

- Build structured CLI tools using `argparse`.
- Apply object-oriented design to real-world command workflows.
- Write testable, modular logic for managing relationships between entities.
- Create professional-grade CLI applications using core Python libraries.

This foundation sets you up for designing scalable and interactive tools across technical environments.
