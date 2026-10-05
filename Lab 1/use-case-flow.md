# Use-Case Flow Specification

## UC-01: Monitor Patient Vitals and Escalate Alerts

**System:** Remote Patient Vitals Alert & Monitoring App  
**Primary actor:** On-Call Caregiver  
**Supporting actors:** Remote Patient, Vital Signs Device, Notification Gateway

### Goal

Continuously evaluate a patient's vital telemetry and notify the appropriate caregiver when a clinical threshold is breached.

### Preconditions

1. The patient is registered and linked to a monitoring device.
2. SpO2, heart-rate, and blood-pressure thresholds are configured.
3. An on-call caregiver and escalation order are configured.
4. The device and telemetry gateway are connected.

### Postconditions

**Success:** The reading is stored, the threshold result is recorded, and any required alert is delivered to the assigned caregiver.  
**Failure:** The system records the failure and makes the telemetry or alert status visible for follow-up.

### Main Success Scenario

1. The Vital Signs Device sends a timestamped SpO2, heart-rate, or blood-pressure reading.
2. The system authenticates the device and associates the reading with the correct patient.
3. The system stores the reading and evaluates it against the patient's active thresholds.
4. The system determines that the reading breaches a threshold.
5. The system creates a critical or non-critical alert containing the metric, value, threshold, patient, and timestamp.
6. The system sends the alert to the assigned On-Call Caregiver through the Notification Gateway.
7. The caregiver views the alert and current patient vitals.
8. The caregiver acknowledges the alert and records the action taken.
9. The system records the acknowledgement, action, and event time in the audit history.

### Alternate Flow: AF-01 - Critical Alert Is Not Acknowledged

1. At Step 7, the caregiver does not acknowledge the critical alert within the configured interval.
2. The system marks the alert as unacknowledged and identifies the next caregiver in the escalation matrix.
3. The system sends the alert and escalation context to the next caregiver.
4. The system repeats escalation according to the configured matrix until a caregiver acknowledges the alert or the escalation list is exhausted.
5. The system records every notification attempt and escalation event.

