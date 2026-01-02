import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.cli.todo_cli import TodoCLI
from src.services.todo_service import TodoService


class TestAddCommand:
    """Integration tests for the add command."""

    def test_add_command_creates_task_with_title_only(self):
        """Test that the add command creates a task with only a title."""
        service = TodoService()
        cli = TodoCLI(service)

        # Mock sys.argv to simulate command line input
        with patch('sys.argv', ['todo', 'add', 'Test Task']):
            # Capture stdout
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                exit_code = cli.run(['add', 'Test Task'])

            output = captured_output.getvalue().strip()

            assert exit_code == 0
            assert "Task added successfully" in output
            assert len(service.get_all_tasks()) == 1

            task = service.get_all_tasks()[0]
            assert task.title == "Test Task"
            assert task.description == ""

    def test_add_command_creates_task_with_title_and_description(self):
        """Test that the add command creates a task with title and description."""
        service = TodoService()
        cli = TodoCLI(service)

        # Test with -d flag
        with patch('sys.argv', ['todo', 'add', 'Test Task', '-d', 'Test Description']):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                exit_code = cli.run(['add', 'Test Task', '-d', 'Test Description'])

            output = captured_output.getvalue().strip()

            assert exit_code == 0
            assert "Task added successfully" in output
            assert len(service.get_all_tasks()) == 1

            task = service.get_all_tasks()[0]
            assert task.title == "Test Task"
            assert task.description == "Test Description"

        # Test with --description flag
        service = TodoService()  # Fresh service
        cli = TodoCLI(service)
        with patch('sys.argv', ['todo', 'add', 'Test Task 2', '--description', 'Test Description 2']):
            captured_output = StringIO()
            with patch('sys.stdout', captured_output):
                exit_code = cli.run(['add', 'Test Task 2', '--description', 'Test Description 2'])

            output = captured_output.getvalue().strip()

            assert exit_code == 0
            assert "Task added successfully" in output
            assert len(service.get_all_tasks()) == 1

            task = service.get_all_tasks()[0]
            assert task.title == "Test Task 2"
            assert task.description == "Test Description 2"

    def test_add_command_fails_with_empty_title(self):
        """Test that the add command fails with an empty title."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['add', ''])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output
        assert len(service.get_all_tasks()) == 0

    def test_add_command_fails_with_whitespace_only_title(self):
        """Test that the add command fails with a whitespace-only title."""
        service = TodoService()
        cli = TodoCLI(service)

        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['add', '   '])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output
        assert len(service.get_all_tasks()) == 0

    def test_add_command_fails_with_long_title(self):
        """Test that the add command fails with a title longer than 200 characters."""
        service = TodoService()
        cli = TodoCLI(service)

        long_title = "A" * 201  # 201 characters, which exceeds the limit
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['add', long_title])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output
        assert len(service.get_all_tasks()) == 0

    def test_add_command_fails_with_long_description(self):
        """Test that the add command fails with a description longer than 1000 characters."""
        service = TodoService()
        cli = TodoCLI(service)

        long_description = "A" * 1001  # 1001 characters, which exceeds the limit
        captured_output = StringIO()
        with patch('sys.stderr', captured_output):
            exit_code = cli.run(['add', 'Test Task', '--description', long_description])

        output = captured_output.getvalue().strip()

        assert exit_code == 1
        assert "Error:" in output
        assert len(service.get_all_tasks()) == 0