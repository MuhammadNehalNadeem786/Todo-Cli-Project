import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.cli.todo_cli import TodoCLI
from src.services.todo_service import TodoService


class TestCompleteCommand:
    """Integration tests for the complete and incomplete commands."""

    def test_complete_command_marks_task_as_complete(self):
        """Test that the complete command marks a task as complete."""
        service = TodoService()
        task = service.add_task("Test Task")
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['complete', task.id])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task.id} marked as complete" in output

        # Verify the task is actually marked as complete
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.completed is True

    def test_incomplete_command_marks_task_as_incomplete(self):
        """Test that the incomplete command marks a task as incomplete."""
        service = TodoService()
        task = service.add_task("Test Task")
        service.complete_task(task.id)  # First mark as complete
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['incomplete', task.id])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task.id} marked as incomplete" in output

        # Verify the task is actually marked as incomplete
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.completed is False

    def test_complete_command_fails_for_nonexistent_task(self):
        """Test that the complete command fails for a nonexistent task."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['complete', 'nonexistent-id'])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error: Task with ID nonexistent-id not found" in output

    def test_incomplete_command_fails_for_nonexistent_task(self):
        """Test that the incomplete command fails for a nonexistent task."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['incomplete', 'nonexistent-id'])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error: Task with ID nonexistent-id not found" in output