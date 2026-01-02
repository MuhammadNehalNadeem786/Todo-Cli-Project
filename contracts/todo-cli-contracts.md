# Todo CLI API Contracts

## Command Interface Specification

This document defines the contract for the Todo CLI application commands and their expected behavior.

### Add Command
**Command**: `todo add <title> [--description DESCRIPTION]`

**Parameters**:
- `title` (required): String representing the task title (1-200 characters)
- `--description` (optional): String representing the task description (up to 1000 characters)

**Success Response**:
- Exit code: 0
- Output: "Task added successfully with ID: {id}"

**Error Responses**:
- Invalid title: Exit code 1, "Error: Title cannot be empty"
- Title too long: Exit code 1, "Error: Title exceeds 200 characters"
- Description too long: Exit code 1, "Error: Description exceeds 1000 characters"

### List Command
**Command**: `todo list`

**Parameters**: None

**Success Response**:
- Exit code: 0
- Output: Formatted list of all tasks with ID, title, description, and completion status
- If no tasks: "No tasks found"

### Update Command
**Command**: `todo update <id> [--title TITLE] [--description DESCRIPTION]`

**Parameters**:
- `id` (required): Integer representing the task ID
- `--title` (optional): String representing the new task title (1-200 characters)
- `--description` (optional): String representing the new task description (up to 1000 characters)

**Success Response**:
- Exit code: 0
- Output: "Task {id} updated successfully"

**Error Responses**:
- Task not found: Exit code 1, "Error: Task with ID {id} not found"
- Invalid title: Exit code 1, "Error: Title cannot be empty"
- Title too long: Exit code 1, "Error: Title exceeds 200 characters"
- Description too long: Exit code 1, "Error: Description exceeds 1000 characters"

### Complete Command
**Command**: `todo complete <id>`

**Parameters**:
- `id` (required): Integer representing the task ID

**Success Response**:
- Exit code: 0
- Output: "Task {id} marked as complete"

**Error Responses**:
- Task not found: Exit code 1, "Error: Task with ID {id} not found"

### Incomplete Command
**Command**: `todo incomplete <id>`

**Parameters**:
- `id` (required): Integer representing the task ID

**Success Response**:
- Exit code: 0
- Output: "Task {id} marked as incomplete"

**Error Responses**:
- Task not found: Exit code 1, "Error: Task with ID {id} not found"

### Delete Command
**Command**: `todo delete <id>`

**Parameters**:
- `id` (required): Integer representing the task ID

**Success Response**:
- Exit code: 0
- Output: "Task {id} deleted successfully"

**Error Responses**:
- Task not found: Exit code 1, "Error: Task with ID {id} not found"

## Data Contracts

### Task Object
```json
{
  "id": "string (UUID format)",
  "title": "string (1-200 characters)",
  "description": "string (0-1000 characters)",
  "completed": "boolean",
  "created_at": "ISO 8601 datetime string",
  "updated_at": "ISO 8601 datetime string"
}
```

### Error Response Format
```json
{
  "error": "string - error message",
  "code": "string - error code",
  "timestamp": "ISO 8601 datetime string"
}
```

## Performance Contracts

- Command execution time: < 100ms for operations on lists up to 1000 tasks
- Memory usage: < 50MB for application runtime
- Startup time: < 500ms

## Validation Rules

- Task titles must be 1-200 characters
- Task descriptions can be 0-1000 characters
- Task IDs must be unique within the application session
- Task IDs are assigned automatically on creation