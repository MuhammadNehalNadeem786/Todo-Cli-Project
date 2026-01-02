import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.cli.todo_cli import TodoCLI
from src.services.todo_service import TodoService


class TestUpdateCommand:
    """Integration tests for the update command."""

    def test_update_command_updates_task_title(self):
        """Test that the update command updates a task's title."""
        service = TodoService()
        task = service.add_task("Old Title", "Old Description")
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['update', task.id, '--title', 'New Title'])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task.id} updated successfully" in output

        # Verify the task was actually updated
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "Old Description"  # Description should remain unchanged

    def test_update_command_updates_task_description(self):
        """Test that the update command updates a task's description."""
        service = TodoService()
        task = service.add_task("Old Title", "Old Description")
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['update', task.id, '--description', 'New Description'])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task.id} updated successfully" in output

        # Verify the task was actually updated
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.title == "Old Title"  # Title should remain unchanged
        assert updated_task.description == "New Description"

    def test_update_command_updates_both_title_and_description(self):
        """Test that the update command updates both title and description."""
        service = TodoService()
        task = service.add_task("Old Title", "Old Description")
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stdout', captured_output):
            exit_code = cli.run(['update', task.id, '--title', 'New Title', '--description', 'New Description'])

        output = captured_output.getvalue().strip()

        assert exit_code == 0
        assert f"Task {task.id} updated successfully" in output

        # Verify the task was actually updated
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"

    def test_update_command_fails_for_nonexistent_task(self):
        """Test that the update command fails for a nonexistent task."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['update', 'nonexistent-id', '--title', 'New Title'])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error: Task with ID nonexistent-id not found" in output

    def test_update_command_fails_with_empty_title(self):
        """Test that the update command fails when updating title to empty string."""
        service = TodoService()
        task = service.add_task("Old Title")
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['update', task.id, '--title', ''])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output

    def test_update_command_fails_with_long_title(self):
        """Test that the update command fails when updating title to a string longer than 200 characters."""
        service = TodoService()
        task = service.add_task("Old Title")
        cli = TodoCLI(service)

        long_title = "A" * 201  # 201 characters, which exceeds the limit
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['update', task.id, '--title', long_title])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output

    def test_update_command_fails_with_long_description(self):
        """Test that the update command fails when updating description to a string longer than 1000 characters."""
        service = TodoService()
        task = service.add_task("Old Title")
        cli = TodoCLI(service)

        long_description = "A" * 1001  # 1001 characters, which exceeds the limit
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['update', task.id, '--description', long_description])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output