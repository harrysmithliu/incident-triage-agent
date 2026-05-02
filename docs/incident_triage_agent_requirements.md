# Incident Triage Agent Requirements Master (English)

## 1. Purpose

This document is the source requirements specification for the Incident Triage Agent.
It is the authoritative baseline for scope, architecture direction, and phased delivery.

## 2. System Boundary and Target Signals

The Incident Triage Agent is built to process operational signals produced by the
`modern-user-product-order-system`, specifically:

- tickets generated from incidents
- alerts generated from runtime and operational monitoring

The project goal is to automate the downstream handling of these two signal types through
triage workflow, review, and controlled execution paths.

The agent can consume:

- ticket payloads
- alert payloads
- approved workflow APIs
- approved review decisions

The agent is a decision-support and workflow-orchestration layer, not a replacement for monitoring, ticketing, or core transaction systems.

## 3. Reduced Scope: Two Primary Scenarios

Only the following two scenarios are in scope for this stage.

### Scenario 1

`Ticket -> Workflow -> Review -> Automation Requirements Document`

Meaning:

1. Intake a ticket incident.
2. Convert it into a structured triage workflow instance.
3. Generate a human-readable review report for reviewer(s) to approve or correct.
4. Produce an automation requirements document only after human review approval.

### Scenario 2

`Alert -> Workflow -> Review -> Automated Remediation`

Meaning:

1. Intake an alert incident.
2. Convert it into a structured triage workflow instance.
3. Generate a human-readable review report for reviewer(s) to approve or correct.
4. Trigger controlled automated remediation only after human review approval.
