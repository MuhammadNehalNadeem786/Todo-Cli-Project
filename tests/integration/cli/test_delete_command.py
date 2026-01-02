import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.cli.todo_cli import TodoCLI
from src.services.todo_service import TodoService


class TestDeleteCommand:
    """Integration tests for the delete command."""

    def test_delete_command_removes_task(self):
        """Test that the delete command removes a task."""
        service = TodoService()
        task = service.add_task("Task to Delete")
        cli = TodoCLI(service)

        # Verify task exists before deletion
        assert service.get_task_by_id(task.id) is not None
        assert len(service.get_all_tasks()) == 1

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['delete', task.id])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task.id} deleted successfully" in output

        # Verify the task was actually deleted
        assert service.get_task_by_id(task.id) is None
        assert len(service.get_all_tasks()) == 0

    def test_delete_command_fails_for_nonexistent_task(self):
        """Test that the delete command fails for a nonexistent task."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['delete', 'nonexistent-id'])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error: Task with ID nonexistent-id not found" in output

    def test_delete_command_with_multiple_tasks(self):
        """Test that the delete command works correctly with multiple tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        task3 = service.add_task("Task 3")
        cli = TodoCLI(service)

        # Verify all tasks exist
        assert len(service.get_all_tasks()) == 3

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['delete', task2.id])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task2.id} deleted successfully" in output

        # Verify only the specified task was deleted
        assert service.get_task_by_id(task1.id) is not None
        assert service.get_task_by_id(task2.id) is None
        assert service.get_task_by_id(task3.id) is not None
        assert len(service.get_all_tasks()) == 2