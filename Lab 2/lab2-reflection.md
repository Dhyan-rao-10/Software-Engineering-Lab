# Lab 2 Reflection

## 1. Did the estimates reflect the actual effort?

The estimates were reasonably aligned with the simulated effort. The smaller notification and response stories were estimated at 3 points, while telemetry ingestion, threshold evaluation, alert generation, and escalation were estimated at 5 points because they involve more rules, integration points, and failure conditions. In a real project, production integration and security testing could increase the effort.

## 2. Was the backlog well-prioritized?

Yes. High-priority items establish the monitoring and emergency-alert path first: ingest readings, evaluate thresholds, generate alerts, notify the caregiver, and escalate when necessary. Viewing and audit-history improvements remain available in the backlog but are less urgent than detecting and communicating a potentially dangerous condition.

## 3. How did the simulated sprint align with the plan?

The sprint completed all six selected stories and delivered 26 story points within the one-week simulation. Work was ordered from the telemetry foundation through detection, notification, escalation, and caregiver response. This sequencing reduced dependency risk because downstream alert behavior relied on the earlier monitoring and threshold capabilities.

## 4. What insights did the burndown chart give about team capacity?

The burndown shows a steady reduction from 26 to 0 points, with a slightly faster finish near the end of the sprint. The simulated capacity was sufficient for the selected commitment, but the two unselected stories show that the team should avoid filling the sprint beyond its demonstrated capacity. A real Jira burndown would also reveal delays, scope changes, and whether work was completed evenly rather than updated in batches.

