from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar
from uuid import uuid4

@dataclass
class Task:
    # Class-level counter shared across all Task instances
    _task_counter: ClassVar[int] = 0

    id: str = field(init=False)
    title: str = ""
    description: str = ""
    completed: bool = False
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Assign a sequential ID and validate fields."""
        # Increment class-level counter
        Task._task_counter += 1
        self.id = str(Task._task_counter)  # Sequential numeric ID as string

        # Validate fields
        if not self.title.strip():
            raise ValueError("Task title cannot be empty")
        if len(self.title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        if len(self.description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")

    def mark_complete(self) -> None:
        self.completed = True
        self.update_timestamp()

    def mark_incomplete(self) -> None:
        self.completed = False
        self.update_timestamp()

    def update_title(self, title: str) -> None:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        if len(title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        self.title = title
        self.update_timestamp()

    def update_description(self, description: str) -> None:
        if len(description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")
        self.description = description
        self.update_timestamp()

    def update_timestamp(self) -> None:
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id} - {self.title}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        task = cls(title=data["title"], description=data.get("description", ""))
        task.id = data.get("id", str(Task._task_counter + 1))
        task.completed = data.get("completed", False)
        task.created_at = datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now()
        task.updated_at = datetime.fromisoformat(data["updated_at"]) if data.get("updated_at") else datetime.now()
        return task
