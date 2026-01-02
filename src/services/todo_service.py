from typing import List, Optional
from models.task import Task
_tasks_storage: List[Task] = []

class TodoService:
    """
    Service class for managing tasks with business logic.
    Implements the core CRUD operations for tasks.
    """

    def __init__(self):
        """Initialize the service with an empty task list."""
        self._tasks: List[Task] = _tasks_storage

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the list.

        Args:
            title: The title of the task
            description: Optional description of the task

        Returns:
            The newly created Task object

        Raises:
            ValueError: If the title is empty or too long
        """
        task = Task(title=title, description=description)
        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the list.

        Returns:
            List of all Task objects
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: str, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update an existing task.

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            True if the task was updated, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.update_title(title)
        if description is not None:
            task.update_description(description)

        return True

    def complete_task(self, task_id: str) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if the task was marked complete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.mark_complete()
        return True

    def incomplete_task(self, task_id: str) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if the task was marked incomplete, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.mark_incomplete()
        return True

    def delete_task(self, task_id: str) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False if not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def get_completed_tasks(self) -> List[Task]:
        """
        Get all completed tasks.

        Returns:
            List of completed Task objects
        """
        return [task for task in self._tasks if task.completed]

    def get_pending_tasks(self) -> List[Task]:
        """
        Get all pending (not completed) tasks.

        Returns:
            List of pending Task objects
        """
        return [task for task in self._tasks if not task.completed]