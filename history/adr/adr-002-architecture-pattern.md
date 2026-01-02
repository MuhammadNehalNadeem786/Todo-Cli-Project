# ADR-002: Clean Architecture Pattern

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2026-01-01
- **Feature:** Todo CLI
- **Context:** Need to structure the application with clear separation of concerns to ensure maintainability, testability, and scalability of the codebase.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- **Models Layer**: Data representation with validation (Task model)
- **Services Layer**: Business logic and data operations (TodoService)
- **CLI Layer**: User interface and command handling (TodoCLI)
- **Application Layer**: Main entry point and component integration (app.py)
- **Testing Layer**: Unit, integration, and end-to-end tests

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- Clear separation of concerns makes code easier to understand and maintain
- Business logic is isolated from UI concerns, enabling easier testing
- Models encapsulate data validation and representation
- Services provide a clean API for business operations
- CLI layer focuses solely on user interaction
- Easier to write unit tests for business logic without UI dependencies
- Future changes to UI or data storage can be made independently

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- More complex initial setup compared to monolithic approach
- Additional layers of abstraction may slightly impact performance
- Requires more files and directories to navigate
- May be over-engineering for a simple application

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative Pattern A**: Monolithic approach with all logic in single file
  - Why rejected: Would result in tightly coupled code, difficult to test, hard to maintain
- **Alternative Pattern B**: MVC (Model-View-Controller) pattern
  - Why rejected: Not well-suited for CLI applications, View component doesn't map well to CLI
- **Alternative Pattern C**: Functional approach with pure functions
  - Why rejected: Doesn't provide clear separation of concerns, harder to manage state

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs-history/phase1-spec-v1.md
- Implementation Plan: specs-history/plan.md
- Related ADRs: ADR-001 (Technology Stack)
- Evaluator Evidence: history/prompts/tasks/1-generate-tasks.tasks.prompt.md