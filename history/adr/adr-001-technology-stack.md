# ADR-001: Technology Stack Decision

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2026-01-01
- **Feature:** Todo CLI
- **Context:** Need to select a technology stack that enables rapid development of a cross-platform CLI application with good performance characteristics and maintainability.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- **Language**: Python 3.13+ (with type hints and modern features)
- **CLI Framework**: argparse for command-line parsing
- **Testing**: pytest for comprehensive testing
- **Data Structures**: dataclasses for models
- **Target Platform**: Cross-platform (Linux, macOS, Windows)

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- Python's extensive standard library and ecosystem support
- argparse provides robust command-line argument parsing
- pytest offers comprehensive testing capabilities with fixtures and plugins
- dataclasses provide clean, concise model definitions with built-in methods
- Cross-platform compatibility out of the box
- Strong type hinting support for better maintainability
- Large community and extensive documentation

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- Python performance limitations compared to compiled languages
- Potential dependency management challenges in deployment
- Need to ensure Python 3.13+ availability on target systems
- Memory usage may be higher than lower-level languages

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative Stack A**: Node.js with commander.js for CLI
  - Why rejected: Would require Node.js runtime instead of Python, different ecosystem
- **Alternative Stack B**: Go with cobra CLI framework
  - Why rejected: Would require learning Go, different ecosystem, more complex for simple CLI app
- **Alternative Stack C**: Rust with clap CLI framework
  - Why rejected: Higher complexity for simple CLI application, steeper learning curve
- **Alternative Stack D**: Java with picocli
  - Why rejected: Requires JVM, higher memory footprint, more verbose syntax

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs-history/phase1-spec-v1.md
- Implementation Plan: specs-history/plan.md
- Related ADRs: none
- Evaluator Evidence: history/prompts/tasks/1-generate-tasks.tasks.prompt.md