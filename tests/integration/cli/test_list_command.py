import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.cli.todo_cli import TodoCLI
from src.services.todo_service import TodoService


class TestListCommand:
    """Integration tests for the list command."""

    def test_list_command_with_empty_list(self):
        """Test that the list command shows a message when there are no tasks."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['list'])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert "No tasks found" in output

    def test_list_command_with_single_task(self):
        """Test that the list command shows a single task."""
        service = TodoService()
        task = service.add_task("Test Task", "Test Description")
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['list'])

        output = captured_output.getvalue()

        assert exit_code == 0
        assert "Test Task" in output
        assert "Test Description" in output
        assert "○ Pending" in output  # Task should be pending by default

    def test_list_command_with_multiple_tasks(self):
        """Test that the list command shows multiple tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1", "Description 1")
        task2 = service.add_task("Task 2", "Description 2")
        service.complete_task(task2.id)  # Mark task2 as complete
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['list'])

        output = captured_output.getvalue()

        assert exit_code == 0
        assert "Task 1" in output
        assert "Description 1" in output
        assert "Task 2" in output
        assert "Description 2" in output
        assert "○ Pending" in output  # Task 1 should be pending
        assert "✓ Done" in output  # Task 2 should be done

    def test_list_command_shows_correct_status(self):
        """Test that the list command shows the correct completion status."""
        service = TodoService()
        pending_task = service.add_task("Pending Task")
        completed_task = service.add_task("Completed Task")
        service.complete_task(completed_task.id)
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['list'])

        output = captured_output.getvalue()

        assert exit_code == 0
        assert "○ Pending" in output  # Pending task
        assert "✓ Done" in output  # Completed task