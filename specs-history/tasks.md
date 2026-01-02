---
description: "Task list for Todo CLI implementation"
---

# Tasks: Todo CLI

**Input**: Design documents from `/specs-history/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are included as requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 Initialize Python 3.13+ project with dependencies in pyproject.toml
- [ ] T003 [P] Configure linting and formatting tools (flake8, black, mypy)
- [ ] T004 Create src/__init__.py file
- [ ] T005 Create src/models/__init__.py file
- [ ] T006 Create src/services/__init__.py file
- [ ] T007 Create src/cli/__init__.py file

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T008 Create Task model with id, title, description, completed attributes in src/models/task.py
- [ ] T009 Create TodoService with in-memory storage in src/services/todo_service.py
- [ ] T010 Setup CLI argument parsing with argparse in src/cli/todo_cli.py
- [ ] T011 Create main application entry point in src/app.py
- [ ] T012 Configure pytest for testing in pyproject.toml

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with a title and optional description

**Independent Test**: Can be fully tested by running the add task command and verifying the task appears in the list, delivering the core value of task creation.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T013 [P] [US1] Unit test for Task model in tests/unit/models/test_task.py
- [ ] T014 [P] [US1] Unit test for TodoService add_task method in tests/unit/services/test_todo_service.py
- [ ] T015 [P] [US1] Integration test for add command in tests/integration/cli/test_add_command.py

### Implementation for User Story 1

- [ ] T016 [US1] Implement Task model with proper validation in src/models/task.py
- [ ] T017 [US1] Implement add_task method in TodoService in src/services/todo_service.py
- [ ] T018 [US1] Implement add command in CLI interface in src/cli/todo_cli.py
- [ ] T019 [US1] Connect CLI add command to service layer in src/cli/todo_cli.py
- [ ] T020 [US1] Add error handling for add command in src/cli/todo_cli.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to see all their tasks in a readable format with status indicators

**Independent Test**: Can be fully tested by adding tasks and then viewing them, delivering the core value of task visibility.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T021 [P] [US2] Unit test for TodoService list_tasks method in tests/unit/services/test_todo_service.py
- [ ] T022 [P] [US2] Integration test for list command in tests/integration/cli/test_list_command.py

### Implementation for User Story 2

- [ ] T023 [US2] Implement list_tasks method in TodoService in src/services/todo_service.py
- [ ] T024 [US2] Implement list command in CLI interface in src/cli/todo_cli.py
- [ ] T025 [US2] Connect CLI list command to service layer in src/cli/todo_cli.py
- [ ] T026 [US2] Format task display with ID, title, description, and completion status in src/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P1)

**Goal**: Enable users to mark tasks as completed or mark completed tasks as incomplete

**Independent Test**: Can be fully tested by marking tasks as complete/incomplete and verifying the status changes, delivering the core value of progress tracking.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T027 [P] [US5] Unit test for TodoService complete_task method in tests/unit/services/test_todo_service.py
- [ ] T028 [P] [US5] Unit test for TodoService incomplete_task method in tests/unit/services/test_todo_service.py
- [ ] T029 [P] [US5] Integration test for complete/incomplete commands in tests/integration/cli/test_complete_command.py

### Implementation for User Story 5

- [ ] T030 [US5] Implement complete_task method in TodoService in src/services/todo_service.py
- [ ] T031 [US5] Implement incomplete_task method in TodoService in src/services/todo_service.py
- [ ] T032 [US5] Implement complete command in CLI interface in src/cli/todo_cli.py
- [ ] T033 [US5] Implement incomplete command in CLI interface in src/cli/todo_cli.py
- [ ] T034 [US5] Connect CLI complete/incomplete commands to service layer in src/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1, 2, AND 5 should all work independently

---

## Phase 6: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Enable users to modify an existing task's title or description

**Independent Test**: Can be fully tested by updating a task and verifying the changes persist, delivering value of task modification.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T035 [P] [US3] Unit test for TodoService update_task method in tests/unit/services/test_todo_service.py
- [ ] T036 [P] [US3] Integration test for update command in tests/integration/cli/test_update_command.py

### Implementation for User Story 3

- [ ] T037 [US3] Implement update_task method in TodoService in src/services/todo_service.py
- [ ] T038 [US3] Implement update command in CLI interface in src/cli/todo_cli.py
- [ ] T039 [US3] Connect CLI update command to service layer in src/cli/todo_cli.py

**Checkpoint**: At this point, User Stories 1, 2, 5, AND 3 should all work independently

---

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Enable users to remove completed or unwanted tasks from their list

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears in the list, delivering value of list maintenance.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T040 [P] [US4] Unit test for TodoService delete_task method in tests/unit/services/test_todo_service.py
- [ ] T041 [P] [US4] Integration test for delete command in tests/integration/cli/test_delete_command.py

### Implementation for User Story 4

- [ ] T042 [US4] Implement delete_task method in TodoService in src/services/todo_service.py
- [ ] T043 [US4] Implement delete command in CLI interface in src/cli/todo_cli.py
- [ ] T044 [US4] Connect CLI delete command to service layer in src/cli/todo_cli.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T045 [P] Add comprehensive error handling across all commands in src/cli/todo_cli.py
- [ ] T046 [P] Add help text and usage examples to CLI in src/cli/todo_cli.py
- [ ] T047 [P] Add type hints throughout the codebase
- [ ] T048 [P] Documentation updates in README.md
- [ ] T049 [P] Add command-line validation for all user inputs
- [ ] T050 [P] Performance testing to ensure sub-second response times
- [ ] T051 [P] Run all tests to ensure 80%+ coverage
- [ ] T052 [P] Create quickstart guide based on spec requirements

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Task model in tests/unit/models/test_task.py"
Task: "Unit test for TodoService add_task method in tests/unit/services/test_todo_service.py"
Task: "Integration test for add command in tests/integration/cli/test_add_command.py"

# Launch all implementation tasks for User Story 1 together:
Task: "Implement Task model with proper validation in src/models/task.py"
Task: "Implement add_task method in TodoService in src/services/todo_service.py"
Task: "Implement add command in CLI interface in src/cli/todo_cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 5 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 5
   - Developer D: User Story 3
   - Developer E: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence