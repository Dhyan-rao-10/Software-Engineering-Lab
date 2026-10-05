# Requirements Table

## Academic Elective Bidding & Allocation System

**Student:** Dhyan Rao  
**SRN:** PES1UG24AM090  
**Course:** Software Engineering, Section B

## Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall allow a student to distribute 100 bidding credits across ranked elective preferences and validate prerequisite completion before submission. | High | Pass: credits total exactly 100 or the system clearly reports the remaining/excess amount, and each selected elective's prerequisites are checked. Fail: invalid credit totals or unmet prerequisites are accepted. | Credit validation and eligibility checking prevent invalid bids and unfair allocation inputs. |
| FR-002 | Functional | The system shall allow a student to create, save, edit, and submit a ranked list of elective preferences before the bidding deadline. | High | Pass: a student can reorder preferences, save a draft, submit once valid, and receive a submission timestamp. Fail: an invalid draft is submitted or a submitted list can be changed without authorization. | Students need a controlled way to express their preferences. |
| FR-003 | Functional | The system shall allocate eligible students to electives using bid values, preference rank, seat capacity, and timetable-conflict rules. | High | Pass: allocation never exceeds course capacity, excludes unmet prerequisites, and does not assign timetable clashes. Fail: any constraint is violated or the allocation result cannot be explained. | Constraint-aware allocation is the core purpose of the system. |
| FR-004 | Functional | The system shall allow the Academic Registrar to configure elective offerings, capacities, prerequisites, bidding windows, and timetable information. | High | Pass: an authorized registrar can create or update each configuration item and the changes are recorded. Fail: an unauthorized user changes configuration or an invalid configuration is published. | Academic rules change each term and must be managed without code changes. |
| FR-005 | Functional | The system shall publish allocation results to students and provide the Academic Registrar with allocation, waitlist, conflict, and audit views. | Medium | Pass: students see their allocated electives or waitlist status, and the registrar can inspect aggregate results and exceptions. Fail: a result is missing, exposed to the wrong student, or absent from the audit view. | Clear results and oversight support student planning and administrative review. |

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Performance | The final elective allocation solver shall process 5,000 student bids and resolve schedule conflicts in under 30 seconds. | High | Pass: benchmark tests complete the allocation and conflict-resolution workload in less than 30 seconds under the defined 5,000-bid load. Fail: the execution time is 30 seconds or more or results are incomplete. | Allocation occurs at a deadline and must finish quickly enough for timely publication. |
| NFR-002 | Security & Auditability | The system shall enforce role-based access for students and registrars, encrypt bid data in transit and at rest, and retain an immutable audit trail of bid and allocation changes. | High | Pass: security tests confirm role restrictions and encryption, and every create/update/submit/allocation action has a timestamped actor record. Fail: unauthorized access, unencrypted sensitive data, or missing audit evidence is found. | Bids and academic records are sensitive and allocation decisions must be traceable. |

