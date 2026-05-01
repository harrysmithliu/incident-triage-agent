# Agent Development Guidelines

This repository is a Python-based AI agent project for incident triage.

## Language Policy

- All new repository content must be written in English.
- This includes code comments, docstrings, README updates, design notes, issue drafts, and any newly added documentation.
- Keep identifiers in English and prefer clear, descriptive names.

## Project Principles

- Favor small, well-scoped modules with single responsibilities.
- Keep the agent architecture explicit: intake, enrichment, reasoning, action planning, and auditability should remain separable concerns.
- Prefer typed Python code and predictable control flow.
- Make failure modes visible and handle external-system errors gracefully.
- Never hardcode secrets, tokens, or environment-specific credentials.

## Development Baseline

- Target modern Python 3.x and keep the codebase packaging-friendly.
- Add tests for behavior that can regress, especially parsing, routing, policy decisions, and prompt assembly.
- Keep the README in sync with major structural changes.
- Prefer incremental changes over broad rewrites.
- When adding new files, ensure they follow the English-only policy above.

## Operational Discipline

- Preserve auditability for any triage decision or workflow action.
- Separate model outputs from deterministic business rules.
- Keep any production-write capability behind explicit approvals and configuration.
- Optimize for maintainability first, then automation depth.

