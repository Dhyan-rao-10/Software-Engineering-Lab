# Requirements Table

## Project

**Remote Patient Vitals Alert & Monitoring App**  
**Student:** Dhyan Rao  
**SRN:** PES1UG24AM090  
**Course:** Software Engineering, Section B

## Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall continuously ingest SpO2, heart-rate, and blood-pressure telemetry from a registered patient-monitoring device. | High | Pass: valid readings are received, timestamped, and associated with the correct patient. Fail: a reading is silently dropped, assigned to the wrong patient, or stored without a timestamp. | Reliable telemetry is the foundation for monitoring and alert generation. |
| FR-002 | Functional | The system shall evaluate each received vital reading against the patient's configured clinical thresholds. | High | Pass: every valid reading is evaluated against the active thresholds. Fail: a valid reading is ignored or evaluated using an outdated or incorrect threshold set. | Threshold evaluation identifies potentially dangerous conditions. |
| FR-003 | Functional | The system shall generate an alert when a vital reading breaches a configured threshold and shall display the breached metric, value, threshold, and time. | High | Pass: a heart rate above 140 BPM, or any configured threshold breach, creates a visible alert containing all four details. Fail: no alert is created or any required alert detail is missing. | Caregivers need precise information to assess the patient's condition quickly. |
| FR-004 | Functional | The system shall notify the assigned on-call caregiver and escalate an unacknowledged critical alert according to the caregiver escalation matrix. | High | Pass: the first assigned caregiver is notified immediately and an unacknowledged critical alert is escalated to the next contact after the configured interval. Fail: notification or escalation does not occur as configured. | Escalation reduces the risk of an emergency being missed. |
| FR-005 | Functional | The system shall allow the on-call caregiver to view patient vitals, acknowledge alerts, and record an action or note. | Medium | Pass: the caregiver can view current and recent readings, acknowledge an alert, and save a note linked to that alert. Fail: any action cannot be completed or is not associated with the correct alert. | A clear response record supports clinical action and traceability. |

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Performance & Availability | The telemetry ingestion gateway shall support at least 500 concurrent continuous telemetry streams with 99.99% monthly uptime. | High | Pass: load testing sustains 500 concurrent streams and service-availability monitoring records at least 99.99% uptime during the measurement period. Fail: either target is not met. | The system must remain dependable while serving many patients. |
| NFR-002 | Security & Performance | The system shall protect patient data using encryption in transit and at rest, role-based access control, and shall evaluate and surface a threshold breach within 2 seconds of receiving the reading. | High | Pass: security testing confirms TLS, encrypted storage, and role restrictions, while latency tests show at least 95% of breach alerts surfaced within 2 seconds. Fail: any security control is absent or the latency target is missed. | Patient information is sensitive, and rapid alerting is essential for safety. |

