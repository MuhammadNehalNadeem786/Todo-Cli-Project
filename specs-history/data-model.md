# Data Model: Todo CLI

## Entities

### Task
**Description**: A user-defined item representing work to be done
**Attributes**:
- `id` (UUID/str): Unique identifier for the task
- `title` (str): Required text describing the task
- `description` (str): Optional detailed description of the task
- `completed` (bool): Boolean status indicating completion state
- `created_at` (datetime): Timestamp of when the task was created
- `updated_at` (datetime): Timestamp of when the task was last modified

**Validation Rules**:
- `title` must be non-empty string (1-200 characters)
- `description` can be empty or up to 1000 characters
- `completed` defaults to False
- `id` must be unique within the system
- `created_at` is set on creation and never modified
- `updated_at` is updated on any modification

**State Transitions**:
- `completed = False` → `completed = True` (when marked complete)
- `completed = True` → `completed = False` (when marked incomplete)

### TodoList
**Description**: A collection of Task entities with operations for management
**Attributes**:
- `tasks` (List[Task]): Collection of tasks in the list
- `created_at` (datetime): Timestamp of when the list was created

**Operations**:
- Add task to list
- Remove task from list
- Update task in list
- Find task by ID
- List all tasks
- Filter tasks by completion status

## Relationships
- TodoList contains 0 to many Tasks
- Each Task belongs to exactly one TodoList (in this implementation)

## Constraints
- Task IDs must be unique within the TodoList
- Maximum 1000 tasks allowed in memory (performance constraint)
- Task titles must be unique within the same list (optional requirement)

## Serialization
Tasks can be serialized to/from dictionary format for potential future persistence:
```python
{
    "id": "unique-id",
    "title": "task title",
    "description": "optional description",
    "completed": false,
    "created_at": "2026-01-01T10:00:00Z",
    "updated_at": "2026-01-01T10:00:00Z"
}
```