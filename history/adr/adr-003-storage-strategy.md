# ADR-003: Storage Strategy - In-Memory vs Persistence

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2026-01-01
- **Feature:** Todo CLI
- **Context:** Need to decide on data storage approach that balances simplicity for Phase 1 with future extensibility to persistent storage.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- **Storage Type**: In-memory Python objects (lists/dictionaries) for Phase 1
- **Interface Design**: Create clear abstraction layer for future persistence
- **Data Format**: Python native data structures with clear serialization path
- **Scope**: Single-user, session-based storage with up to 1000 tasks in memory
- **Future Path**: Well-defined interface for adding file-based or database persistence

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- Simple implementation with minimal complexity for initial version
- Fast read/write operations with no I/O overhead
- Easy to test without external dependencies
- No need to manage database connections or file locks
- Clean separation between business logic and persistence concerns
- Clear interface design that enables future persistence implementation
- No data migration concerns for initial version

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- Data is lost when application exits
- Memory usage increases with data size
- Not suitable for production use where data persistence is required
- No ability to share data between sessions
- Potential memory constraints with large datasets
- Users may expect data to persist between sessions

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative Strategy A**: File-based storage (JSON/CSV files)
  - Why rejected: Adds complexity for Phase 1, requires file I/O handling, error handling for file operations
- **Alternative Strategy B**: Database storage (SQLite)
  - Why rejected: Adds external dependency, requires schema management, more complex setup
- **Alternative Strategy C**: Hybrid approach with auto-save to file
  - Why rejected: Combines complexity of both approaches, over-engineering for Phase 1

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs-history/phase1-spec-v1.md
- Implementation Plan: specs-history/plan.md
- Related ADRs: ADR-002 (Architecture Pattern)
- Evaluator Evidence: history/prompts/tasks/1-generate-tasks.tasks.prompt.md