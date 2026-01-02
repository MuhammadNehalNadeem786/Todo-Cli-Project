# Quickstart Guide: Todo CLI

## Getting Started

This guide will help you set up and start using the Todo CLI application.

### Prerequisites

- Python 3.13+ installed on your system
- pip (Python package installer)

### Installation

1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or if using pyproject.toml:
   ```bash
   pip install .
   ```

### Basic Usage

#### Adding a Task
```bash
python -m todo add "Buy groceries"
```

With description:
```bash
python -m todo add "Buy groceries" --description "Milk, bread, eggs"
```

#### Listing All Tasks
```bash
python -m todo list
```

#### Updating a Task
```bash
python -m todo update 1 --title "Updated task title"
```

Or update description:
```bash
python -m todo update 1 --description "Updated description"
```

#### Marking a Task Complete
```bash
python -m todo complete 1
```

#### Marking a Task Incomplete
```bash
python -m todo incomplete 1
```

#### Deleting a Task
```bash
python -m todo delete 1
```

### Available Commands

- `add`: Add a new task with title and optional description
- `list`: Display all tasks with their status
- `update`: Update task title or description by ID
- `complete`: Mark a task as complete by ID
- `incomplete`: Mark a task as incomplete by ID
- `delete`: Remove a task by ID

### Example Workflow

1. Add some tasks:
   ```bash
   python -m todo add "Complete project proposal"
   python -m todo add "Review code" --description "Review the new feature implementation"
   python -m todo add "Schedule team meeting"
   ```

2. View your tasks:
   ```bash
   python -m todo list
   ```

3. Mark a task complete:
   ```bash
   python -m todo complete 1
   ```

4. Update a task:
   ```bash
   python -m todo update 2 --title "Review feature implementation"
   ```

5. Delete a completed task:
   ```bash
   python -m todo delete 1
   ```

### Troubleshooting

- If you get a "command not found" error, ensure you're running the command from the project directory
- If you encounter import errors, verify that all dependencies are installed
- For any operation on non-existent tasks, the application will show an appropriate error message

### Development Setup

For developers contributing to the project:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

### Running Tests

The project includes comprehensive tests:

- Unit tests: `pytest tests/unit/`
- Integration tests: `pytest tests/integration/`
- End-to-end tests: `pytest tests/e2e/`
- All tests: `pytest`

Code coverage: `pytest --cov=src/`