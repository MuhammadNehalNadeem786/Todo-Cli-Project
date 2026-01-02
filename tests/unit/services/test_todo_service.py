import pytest
from src.services.todo_service import TodoService
from src.models.task import Task


class TestTodoService:
    """Unit tests for the TodoService."""

    def test_add_task_creates_new_task(self):
        """Test that add_task creates a new task."""
        service = TodoService()
        task = service.add_task("Test Title", "Test Description")

        assert isinstance(task, Task)
        assert task.title == "Test Title"
        assert task.description == "Test Description"
        assert task.completed is False

    def test_add_task_without_description(self):
        """Test that add_task works without a description."""
        service = TodoService()
        task = service.add_task("Test Title")

        assert isinstance(task, Task)
        assert task.title == "Test Title"
        assert task.description == ""
        assert task.completed is False

    def test_get_all_tasks_initially_empty(self):
        """Test that get_all_tasks returns an empty list initially."""
        service = TodoService()
        tasks = service.get_all_tasks()

        assert tasks == []

    def test_get_all_tasks_after_adding_tasks(self):
        """Test that get_all_tasks returns all added tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")

        tasks = service.get_all_tasks()

        assert len(tasks) == 2
        assert task1 in tasks
        assert task2 in tasks

    def test_get_task_by_id_returns_existing_task(self):
        """Test that get_task_by_id returns an existing task."""
        service = TodoService()
        task = service.add_task("Test Task")
        found_task = service.get_task_by_id(task.id)

        assert found_task is not None
        assert found_task.id == task.id
        assert found_task.title == task.title

    def test_get_task_by_id_returns_none_for_nonexistent_task(self):
        """Test that get_task_by_id returns None for a nonexistent task."""
        service = TodoService()
        found_task = service.get_task_by_id("nonexistent-id")

        assert found_task is None

    def test_update_task_title(self):
        """Test updating a task's title."""
        service = TodoService()
        task = service.add_task("Old Title")
        success = service.update_task(task.id, title="New Title")

        assert success is True
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.title == "New Title"

    def test_update_task_description(self):
        """Test updating a task's description."""
        service = TodoService()
        task = service.add_task("Test Title", "Old Description")
        success = service.update_task(task.id, description="New Description")

        assert success is True
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.description == "New Description"

    def test_update_task_both_title_and_description(self):
        """Test updating both title and description of a task."""
        service = TodoService()
        task = service.add_task("Old Title", "Old Description")
        success = service.update_task(task.id, title="New Title", description="New Description")

        assert success is True
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"

    def test_update_nonexistent_task_returns_false(self):
        """Test that updating a nonexistent task returns False."""
        service = TodoService()
        success = service.update_task("nonexistent-id", title="New Title")

        assert success is False

    def test_complete_task(self):
        """Test marking a task as complete."""
        service = TodoService()
        task = service.add_task("Test Task")
        assert task.completed is False

        success = service.complete_task(task.id)

        assert success is True
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.completed is True

    def test_complete_nonexistent_task_returns_false(self):
        """Test that completing a nonexistent task returns False."""
        service = TodoService()
        success = service.complete_task("nonexistent-id")

        assert success is False

    def test_incomplete_task(self):
        """Test marking a task as incomplete."""
        service = TodoService()
        task = service.add_task("Test Task")
        service.complete_task(task.id)  # First mark as complete
        assert task.completed is True

        success = service.incomplete_task(task.id)

        assert success is True
        updated_task = service.get_task_by_id(task.id)
        assert updated_task.completed is False

    def test_incomplete_nonexistent_task_returns_false(self):
        """Test that marking a nonexistent task as incomplete returns False."""
        service = TodoService()
        success = service.incomplete_task("nonexistent-id")

        assert success is False

    def test_delete_task(self):
        """Test deleting a task."""
        service = TodoService()
        task = service.add_task("Test Task")

        success = service.delete_task(task.id)

        assert success is True
        assert service.get_task_by_id(task.id) is None
        assert len(service.get_all_tasks()) == 0

    def test_delete_nonexistent_task_returns_false(self):
        """Test that deleting a nonexistent task returns False."""
        service = TodoService()
        success = service.delete_task("nonexistent-id")

        assert success is False

    def test_get_completed_tasks(self):
        """Test getting all completed tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")

        service.complete_task(task2.id)  # Only task2 is completed

        completed_tasks = service.get_completed_tasks()

        assert len(completed_tasks) == 1
        assert task2 in completed_tasks
        assert task1 not in completed_tasks

    def test_get_pending_tasks(self):
        """Test getting all pending tasks."""
        service = TodoService()
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")

        service.complete_task(task2.id)  # task2 is completed, task1 is pending

        pending_tasks = service.get_pending_tasks()

        assert len(pending_tasks) == 1
        assert task1 in pending_tasks
        assert task2 not in pending_tasks