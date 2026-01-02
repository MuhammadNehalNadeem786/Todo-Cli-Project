import pytest
from datetime import datetime
from src.models.task import Task


class TestTask:
    """Unit tests for the Task model."""

    def test_create_task_with_valid_data(self):
        """Test creating a task with valid data."""
        task = Task(id="123", title="Test Task", description="Test Description", completed=False)
        assert task.id == "123"
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is False
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)

    def test_create_task_with_required_title(self):
        """Test creating a task requires a title."""
        task = Task(title="Test Task")
        assert task.id is not None
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False
        assert isinstance(task.created_at, datetime)
        assert isinstance(task.updated_at, datetime)

    def test_create_task_with_empty_title_raises_error(self):
        """Test that creating a task with an empty title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(title="")

    def test_create_task_with_whitespace_only_title_raises_error(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            Task(title="   ")

    def test_create_task_with_long_title_raises_error(self):
        """Test that creating a task with a title longer than 200 characters raises ValueError."""
        long_title = "A" * 201
        with pytest.raises(ValueError, match="Task title cannot exceed 200 characters"):
            Task(title=long_title)

    def test_create_task_with_long_description_raises_error(self):
        """Test that creating a task with a description longer than 1000 characters raises ValueError."""
        long_description = "A" * 1001
        with pytest.raises(ValueError, match="Task description cannot exceed 1000 characters"):
            Task(title="Test", description=long_description)

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = Task(title="Test Task")
        assert task.completed is False
        task.mark_complete()
        assert task.completed is True

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = Task(title="Test Task", completed=True)
        assert task.completed is True
        task.mark_incomplete()
        assert task.completed is False

    def test_update_title(self):
        """Test updating the task title."""
        task = Task(title="Old Title")
        task.update_title("New Title")
        assert task.title == "New Title"

    def test_update_title_with_empty_string_raises_error(self):
        """Test that updating title with empty string raises ValueError."""
        task = Task(title="Old Title")
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            task.update_title("")

    def test_update_title_with_long_string_raises_error(self):
        """Test that updating title with a string longer than 200 characters raises ValueError."""
        task = Task(title="Old Title")
        long_title = "A" * 201
        with pytest.raises(ValueError, match="Task title cannot exceed 200 characters"):
            task.update_title(long_title)

    def test_update_description(self):
        """Test updating the task description."""
        task = Task(title="Test Task", description="Old Description")
        task.update_description("New Description")
        assert task.description == "New Description"

    def test_update_description_with_long_string_raises_error(self):
        """Test that updating description with a string longer than 1000 characters raises ValueError."""
        task = Task(title="Test Task")
        long_description = "A" * 1001
        with pytest.raises(ValueError, match="Task description cannot exceed 1000 characters"):
            task.update_description(long_description)

    def test_update_timestamp(self):
        """Test updating the timestamp."""
        task = Task(title="Test Task")
        old_timestamp = task.updated_at
        task.update_timestamp()
        assert task.updated_at > old_timestamp

    def test_str_representation(self):
        """Test string representation of the task."""
        task = Task(title="Test Task")
        task_str = str(task)
        assert "○" in task_str  # Incomplete task
        assert "Test Task" in task_str

        task.mark_complete()
        task_str = str(task)
        assert "✓" in task_str  # Complete task

    def test_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(id="123", title="Test Task", description="Test Description", completed=True)
        task_dict = task.to_dict()
        assert task_dict["id"] == "123"
        assert task_dict["title"] == "Test Task"
        assert task_dict["description"] == "Test Description"
        assert task_dict["completed"] is True
        assert "created_at" in task_dict
        assert "updated_at" in task_dict

    def test_from_dict(self):
        """Test creating a task from dictionary."""
        task_data = {
            "id": "123",
            "title": "Test Task",
            "description": "Test Description",
            "completed": True,
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-01T00:00:00"
        }
        task = Task.from_dict(task_data)
        assert task.id == "123"
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed is True