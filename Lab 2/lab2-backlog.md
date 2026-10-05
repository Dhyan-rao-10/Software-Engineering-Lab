# Software Engineering Lab 2 - Jira Backlog and Sprint Simulation

**Student:** Dhyan Rao  
**SRN:** PES1UG24AM090  
**Course:** Software Engineering  
**Section:** B  
**Product:** Remote Patient Vitals Alert & Monitoring App

## Jira setup

- Project name: Remote Patient Vitals Monitoring
- Suggested project key: RPVM
- Template: Scrum
- Project type: Company-managed
- Sprint: Sprint 1
- Sprint duration: 1 week

## Epics and user stories

### EPIC-1: Continuous Vital Telemetry

Enable reliable collection and viewing of remote patient vital readings.

| ID | User story | Priority | Story points | Lab 1 link |
|---|---|---:|---:|---|
| US-001 | As a Remote Patient, I want my registered device to send timestamped SpO2, heart-rate, and blood-pressure readings so that my caregiver can monitor me remotely. | High | 5 | FR-001 |
| US-002 | As an On-Call Caregiver, I want to view current and recent patient vitals so that I can assess the patient's condition. | Medium | 3 | FR-005 |

### EPIC-2: Threshold Detection and Alerts

Detect abnormal readings and provide actionable alert information.

| ID | User story | Priority | Story points | Lab 1 link |
|---|---|---:|---:|---|
| US-003 | As an On-Call Caregiver, I want every valid reading evaluated against the patient's active clinical thresholds so that anomalies are detected consistently. | High | 5 | FR-002 |
| US-004 | As an On-Call Caregiver, I want a threshold-breach alert to show the metric, value, threshold, patient, and time so that I can respond quickly. | High | 5 | FR-003 |

### EPIC-3: Caregiver Notification and Escalation

Deliver alerts to the correct caregiver and escalate emergencies when necessary.

| ID | User story | Priority | Story points | Lab 1 link |
|---|---|---:|---:|---|
| US-005 | As an assigned On-Call Caregiver, I want to receive an immediate notification for a critical alert so that I can begin a response. | High | 3 | FR-004 |
| US-006 | As a member of the care team, I want an unacknowledged critical alert escalated through the caregiver matrix so that emergencies are not missed. | High | 5 | FR-004 |

### EPIC-4: Alert Response and Audit

Record the caregiver's response and preserve an accountable history.

| ID | User story | Priority | Story points | Lab 1 link |
|---|---|---:|---:|---|
| US-007 | As an On-Call Caregiver, I want to acknowledge an alert and record an action or note so that the response is documented. | Medium | 3 | FR-005 |
| US-008 | As an On-Call Caregiver, I want alert acknowledgements and notification attempts recorded with timestamps so that the event history is traceable. | Low | 3 | FR-005 |

## Sprint 1 plan

Sprint 1 is a one-week simulation. The selected stories are US-001, US-003, US-004, US-005, US-006, and US-007 for a total commitment of **26 story points**. The lower-priority US-002 and US-008 remain in the backlog.

| Day | Board activity | Remaining points |
|---|---|---:|
| Day 1 | Sprint started; all selected work is To Do | 26 |
| Day 2 | US-001 moved to Done | 21 |
| Day 3 | US-003 moved to Done | 16 |
| Day 4 | US-004 moved to Done | 11 |
| Day 5 | US-005 moved to Done | 8 |
| Day 6 | US-006 moved to Done | 3 |
| Day 7 | US-007 moved to Done; Sprint completed | 0 |

