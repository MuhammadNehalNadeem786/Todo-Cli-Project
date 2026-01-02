import argparse
import sys
from typing import Optional
from services.todo_service import TodoService


class TodoCLI:
    """
    Command Line Interface for the Todo application.
    Handles user input and output for all todo operations.
    """

    def __init__(self, service: TodoService):
        """
        Initialize the CLI with a TodoService.

        Args:
            service: The TodoService instance to use for operations
        """
        self.service = service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create the argument parser with all available commands.

        Returns:
            Configured ArgumentParser
        """
        parser = argparse.ArgumentParser(
            description="Todo CLI - A command-line interface for managing todos",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  todo add "Buy groceries" --description "Milk, bread, eggs"
  todo list
  todo update 1 --title "Updated title"
  todo complete 1
  todo incomplete 1
  todo delete 1
            """.strip()
        )

        subparsers = parser.add_subparsers(dest='command', help='Available commands', required=True)

        # Add command
        add_parser = subparsers.add_parser('add', help='Add a new task')
        add_parser.add_argument('title', help='Title of the task')
        add_parser.add_argument('--description', '-d', help='Description of the task')

        # List command
        list_parser = subparsers.add_parser('list', help='List all tasks')

        # Update command
        update_parser = subparsers.add_parser('update', help='Update a task')
        update_parser.add_argument('id', help='ID of the task to update')
        update_parser.add_argument('--title', help='New title for the task')
        update_parser.add_argument('--description', '-d', help='New description for the task')

        # Complete command
        complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
        complete_parser.add_argument('id', help='ID of the task to mark complete')

        # Incomplete command
        incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
        incomplete_parser.add_argument('id', help='ID of the task to mark incomplete')

        # Delete command
        delete_parser = subparsers.add_parser('delete', help='Delete a task')
        delete_parser.add_argument('id', help='ID of the task to delete')

        return parser

    def run(self, args: Optional[list] = None) -> int:
        """
        Run the CLI with the given arguments.

        Args:
            args: List of arguments to parse (default: sys.argv[1:])

        Returns:
            Exit code (0 for success, 1 for error)
        """
        if args is None:
            args = sys.argv[1:]

        try:
            parsed_args = self.parser.parse_args(args)
            return self._handle_command(parsed_args)
        except SystemExit:
            # argparse calls sys.exit on error, so we catch it and return 1
            return 1

    def _handle_command(self, args) -> int:
        """
        Handle the parsed command.

        Args:
            args: Parsed arguments from argparse

        Returns:
            Exit code (0 for success, 1 for error)
        """
        try:
            if args.command == 'add':
                return self._handle_add(args)
            elif args.command == 'list':
                return self._handle_list(args)
            elif args.command == 'update':
                return self._handle_update(args)
            elif args.command == 'complete':
                return self._handle_complete(args)
            elif args.command == 'incomplete':
                return self._handle_incomplete(args)
            elif args.command == 'delete':
                return self._handle_delete(args)
            else:
                print(f"Unknown command: {args.command}")
                return 1
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    def _handle_add(self, args) -> int:
        """
        Handle the add command.

        Args:
            args: Parsed arguments for the add command

        Returns:
            Exit code (0 for success, 1 for error)
        """
        try:
            description = args.description or ""
            task = self.service.add_task(args.title, description)
            print(f"Task added successfully with ID: {task.id}")
            return 0
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    def _handle_list(self, args) -> int:
        """
        Handle the list command.

        Args:
            args: Parsed arguments for the list command (unused)

        Returns:
            Exit code (0 for success, 1 for error)
        """
        tasks = self.service.get_all_tasks()

        if not tasks:
            print("No tasks found")
            return 0

        print(f"{'ID':<6} {'Status':<12} {'Title':<30} {'Description'}")
        print("-" * 80)

        # for task in tasks:
        #     status = "✓ Done" if task.completed else "○ Pending"
        #     title = task.title[:27] + "..." if len(task.title) > 30 else task.title
        #     description = task.description[:30] + "..." if len(task.description) > 30 else task.description
        #     print(f"{task.id} {status:<80} {title:<30} {description}")

        for task in tasks:
            status = "✓ Done" if task.completed else "Pending"
            title = task.title[:27] + "..." if len(task.title) > 30 else task.title
            description = (
                task.description[:30] + "..."
                if task.description and len(task.description) > 33
                else (task.description or "")
            )

            print(f"{str(task.id):<6} {status:<12} {title:<30} {description}")
            
        return 0

    def _handle_update(self, args) -> int:
        """
        Handle the update command.

        Args:
            args: Parsed arguments for the update command

        Returns:
            Exit code (0 for success, 1 for error)
        """
        success = self.service.update_task(
            args.id,
            title=args.title,
            description=args.description
        )

        if success:
            print(f"Task {args.id} updated successfully")
            return 0
        else:
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            return 1

    def _handle_complete(self, args) -> int:
        """
        Handle the complete command.

        Args:
            args: Parsed arguments for the complete command

        Returns:
            Exit code (0 for success, 1 for error)
        """
        success = self.service.complete_task(args.id)

        if success:
            print(f"Task {args.id} marked as complete")
            return 0
        else:
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            return 1

    def _handle_incomplete(self, args) -> int:
        """
        Handle the incomplete command.

        Args:
            args: Parsed arguments for the incomplete command

        Returns:
            Exit code (0 for success, 1 for error)
        """
        success = self.service.incomplete_task(args.id)

        if success:
            print(f"Task {args.id} marked as incomplete")
            return 0
        else:
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            return 1

    def _handle_delete(self, args) -> int:
        """
        Handle the delete command.

        Args:
            args: Parsed arguments for the delete command

        Returns:
            Exit code (0 for success, 1 for error)
        """
        success = self.service.delete_task(args.id)

        if success:
            print(f"Task {args.id} deleted successfully")
            return 0
        else:
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            return 1