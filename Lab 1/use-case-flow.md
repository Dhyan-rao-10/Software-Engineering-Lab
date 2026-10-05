# Use-Case Flow Specification

## UC-01: Submit Elective Bids and Preferences

**System:** Academic Elective Bidding & Allocation System  
**Primary actor:** Student  
**Supporting actor:** Academic Registrar

### Goal

Allow a student to submit a valid, ranked elective preference list using exactly 100 bidding credits.

### Preconditions

1. The student is authenticated and enrolled for the term.
2. The registrar has published eligible elective offerings, prerequisites, capacities, and the bidding deadline.
3. The bidding window is open.

### Postconditions

**Success:** The valid preference list is stored with a submission timestamp and becomes available to the allocation process.  
**Failure:** No invalid submission is stored as final; validation messages explain what the student must correct.

### Main Success Scenario

1. The student opens the elective bidding page.
2. The system displays available electives and the student's eligibility status.
3. The student selects electives and assigns a preference rank to each one.
4. The student distributes bidding credits across the selected preferences.
5. The student saves the draft.
6. The system validates that the credit total is exactly 100 and that all prerequisites are satisfied.
7. The student reviews the summary and submits the preferences.
8. The system records the submission timestamp and locks the final submission for allocation.
9. The system displays a confirmation reference to the student.

### Alternate Flow: AF-01 - Invalid Credits or Prerequisite

1. At Step 6, the system detects that the credits do not total 100 or that a selected elective has an unmet prerequisite.
2. The system highlights the invalid elective or credit total and explains the correction required.
3. The student edits the credit distribution or removes/replaces the ineligible elective.
4. The system revalidates the draft.
5. If validation succeeds, the flow resumes at Step 7; otherwise, the system keeps the draft unsubmitted.

