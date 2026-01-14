import argparse
import sys
from typing import Optional

from services.todo_service import TodoService
from cli.ui import show_tasks, success, error


class TodoCLI:
    """
    TodoCLI provides a command-line interface for managing todo tasks.

    It acts as a bridge between user input (CLI commands)
    and the core business logic implemented in TodoService.
    """

    def __init__(self, service: TodoService):
        """
        Initialize the CLI with a TodoService instance.

        Args:
            service (TodoService): Service layer responsible for task operations.
        """
        self.service = service
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """
        Create and configure the argument parser with all supported commands.

        Returns:
            argparse.ArgumentParser: Configured argument parser instance.
        """
        parser = argparse.ArgumentParser(
            description=(
                "Todo CLI\n\n"
                "A simple yet powerful command-line application "
                "to manage your daily tasks efficiently."
            ),
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  todo add "Buy groceries" -d "Milk, bread, eggs"
  todo list
  todo update 1 --title "Buy groceries today"
  todo complete 1
  todo incomplete 1
  todo delete 1
            """.strip(),
        )

        subparsers = parser.add_subparsers(
            dest="command",
            title="Commands",
            description="Available todo operations",
            help="Use one of the following commands",
            required=True,
        )

        # ---------------- ADD ----------------
        add_parser = subparsers.add_parser(
            "add",
            help="Add a new task",
            description="Create a new todo task with a title and optional description",
        )
        add_parser.add_argument(
            "title",
            help="Short title of the task (required)",
        )
        add_parser.add_argument(
            "--description",
            "-d",
            help="Detailed description of the task (optional)",
        )

        # ---------------- LIST ----------------
        subparsers.add_parser(
            "list",
            help="List all tasks",
            description="Display all todo tasks in a formatted table",
        )

        # ---------------- UPDATE ----------------
        update_parser = subparsers.add_parser(
            "update",
            help="Update an existing task",
            description="Modify the title and/or description of a task",
        )
        update_parser.add_argument(
            "id",
            help="ID of the task to update",
        )
        update_parser.add_argument(
            "--title",
            help="New title for the task (optional)",
        )
        update_parser.add_argument(
            "--description",
            "-d",
            help="New description for the task (optional)",
        )

        # ---------------- COMPLETE ----------------
        complete_parser = subparsers.add_parser(
            "complete",
            help="Mark a task as complete",
            description="Set a task's status to completed",
        )
        complete_parser.add_argument(
            "id",
            help="ID of the task to mark as complete",
        )

        # ---------------- INCOMPLETE ----------------
        incomplete_parser = subparsers.add_parser(
            "incomplete",
            help="Mark a task as incomplete",
            description="Revert a completed task back to incomplete",
        )
        incomplete_parser.add_argument(
            "id",
            help="ID of the task to mark as incomplete",
        )

        # ---------------- DELETE ----------------
        delete_parser = subparsers.add_parser(
            "delete",
            help="Delete a task",
            description="Permanently remove a task from the todo list",
        )
        delete_parser.add_argument(
            "id",
            help="ID of the task to delete",
        )

        return parser

    def run(self, args: Optional[list] = None) -> int:
        """
        Execute the CLI using provided arguments.

        Args:
            args (list | None): Command-line arguments.
                                Defaults to sys.argv[1:].

        Returns:
            int: Exit code (0 = success, 1 = error)
        """
        if args is None:
            args = sys.argv[1:]

        try:
            parsed_args = self.parser.parse_args(args)
            return self._handle_command(parsed_args)
        except SystemExit:
            # argparse handles errors internally using sys.exit
            return 1

    def _handle_command(self, args) -> int:
        """
        Route the parsed command to its corresponding handler.

        Args:
            args: Parsed argparse namespace.

        Returns:
            int: Exit code
        """
        try:
            if args.command == "add":
                return self._handle_add(args)
            if args.command == "list":
                return self._handle_list()
            if args.command == "update":
                return self._handle_update(args)
            if args.command == "complete":
                return self._handle_complete(args)
            if args.command == "incomplete":
                return self._handle_incomplete(args)
            if args.command == "delete":
                return self._handle_delete(args)

            error(f"Unknown command: {args.command}")
            return 1

        except Exception as e:
            error(str(e))
            return 1

    def _handle_add(self, args) -> int:
        """
        Create a new task using the provided title and description.
        """
        try:
            description = args.description or ""
            task = self.service.add_task(args.title, description)
            success(f"Task added successfully (ID: {task.id})")
            return 0
        except ValueError as e:
            error(str(e))
            return 1

    def _handle_list(self) -> int:
        """
        Display all tasks in a table format.
        """
        tasks = self.service.get_all_tasks()

        if not tasks:
            error("No tasks found")
            return 0

        show_tasks(tasks)
        return 0

    def _handle_update(self, args) -> int:
        """
        Update an existing task's title and/or description.
        """
        updated = self.service.update_task(
            args.id,
            title=args.title,
            description=args.description,
        )

        if updated:
            success(f"Task {args.id} updated successfully")
            return 0

        error(f"Task with ID {args.id} not found")
        return 1

    def _handle_complete(self, args) -> int:
        """
        Mark a task as completed.
        """
        completed = self.service.complete_task(args.id)

        if completed:
            success(f"Task {args.id} marked as complete")
            return 0

        error(f"Task with ID {args.id} not found")
        return 1

    def _handle_incomplete(self, args) -> int:
        """
        Mark a completed task as incomplete.
        """
        updated = self.service.incomplete_task(args.id)

        if updated:
            success(f"Task {args.id} marked as incomplete")
            return 0

        error(f"Task with ID {args.id} not found")
        return 1

    def _handle_delete(self, args) -> int:
        """
        Permanently delete a task.
        """
        deleted = self.service.delete_task(args.id)

        if deleted:
            success(f"Task {args.id} deleted successfully")
            return 0

        error(f"Task with ID {args.id} not found")
        return 1
