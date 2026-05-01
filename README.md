# Incident Triage Agent

Incident Triage Agent is a Python-based AI agent for turning noisy production signals into structured, auditable triage decisions.

It sits between observability, ticketing, and business-event systems and provides a unified triage layer that can:

- normalize incident inputs from multiple sources
- classify incidents and estimate severity
- enrich the incident with related context
- generate structured response recommendations
- pass triage results into downstream workflows

## Scope

This project follows the requirements outlined in `requirements/incident_triage_agent_需求总纲.md` and is focused on the following core capabilities:

- incident intake
- classification and prioritization
- context enrichment
- recommendation generation
- workflow dispatch
- learning and audit

## Planned Project Shape

- `src/incident_triage_agent/`: Python package for the agent implementation
- `requirements/`: source requirements documents and reference notes, excluded from version control
- `resources/`: supporting reference materials and examples, excluded from version control

## Development Rules

See [`AGENTS.md`](./AGENTS.md) for the project-level development contract.

## Initial Roadmap

1. Define the incident data model and triage result schema.
2. Implement intake and normalization utilities.
3. Add a first-pass classifier and severity rubric.
4. Add context enrichment interfaces for services, history, and runbooks.
5. Introduce structured output and audit logging.
