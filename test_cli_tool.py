# test_cli_tool.py

import subprocess
import os
import sys
import pytest

# Ensure import paths are correctly set up for subprocess scripts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIB_PATH = os.path.abspath(os.path.join(BASE_DIR, "lib"))
sys.path.insert(0, LIB_PATH)

# --- Helper Function ---

def run_cli_command(command):
    """Run CLI command and return CompletedProcess with stdout/stderr."""
    return subprocess.run(command, capture_output=True, text=True)

# --- Tests ---

def test_add_task():
    """Test adding a task prints the correct confirmation message."""
    result = run_cli_command(["python", "lib/cli_tool.py", "add-task", "Alice", "Submit report"])
    assert "📌 Task 'Submit report' added to Alice." in result.stdout

def test_complete_task_with_script(tmp_path):
    """Test that completing a task outputs correct confirmation in a subprocess with shared state."""
    script_path = tmp_path / "script.py"
    script_content = f"""
import sys
import os
sys.path.insert(0, '{LIB_PATH.replace("\\\\", "/")}')

from models import Task, User

users = {{}}
user = User("Bob")
users["Bob"] = user
task = Task("Finish lab")
user.add_task(task)
task.complete()
"""

    script_path.write_text(script_content)

    result = subprocess.run(["python", str(script_path)], capture_output=True, text=True)
    assert "✅ Task 'Finish lab' completed." in result.stdout
