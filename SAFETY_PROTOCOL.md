Safety Protocol Specification

Document ID: SPS-001
System: Train Electronic Control Service (Simulation)
Version: 1.0
Safety Alignment Reference:

EN 50128

EN 50129

IEC 61508

MISRA C (inspiration model)

1️⃣ Purpose

This specification defines mandatory software safety rules for the Train Electronic Controller Service.

The objective is to:

Prevent unsafe state transitions

Ensure deterministic behavior

Preserve safety integrity during upgrades

Detect safety regressions early

Provide structured compliance evaluation

This protocol is inspired by MISRA C principles but adapted for Python-based service logic.

2️⃣ System Safety Context

The system simulates a electronic controller responsible for:

Motor control

Temperature monitoring

Alarm handling

Emergency shutdown

Operational state management

This system is assumed to operate under Safety Integrity Level (SIL) 2/3-like constraints (simulation context).

3️⃣ Safety Principles

The system shall adhere to the following core safety principles:

Fail-safe behavior

Deterministic execution

Explicit validation

No silent degradation of safety

Backward compatibility control

Traceable safety changes

4️⃣ Safety Rules
🔐 SECTION A — Safety Integrity Rules
SAF-001

Emergency shutdown shall override all operational states.

Requirement:

Must stop motor

Must reset speed to zero

Must set alarm/fault flag

SAF-002

System shall not start if alarm state is active.

Violation Example (v2.0 risk):

Removal of alarm check in start logic

SAF-003

Over-temperature condition shall trigger deterministic shutdown.

Requirement:

Temperature threshold must not be silently increased

Shutdown must occur immediately

SAF-004

Safety-critical flags (alarm/fault) shall persist until explicitly cleared.

Silent reset is prohibited.

SAF-005

Safety thresholds shall not be relaxed without documented change justification.

Example:

Increasing MAX_TEMP from 100 → 120 is a safety regression unless justified.

⚙ SECTION B — Determinism & Real-Time Safety
RT-001

Blocking calls (e.g., time.sleep) shall not exist in control paths.

RT-002

Control logic shall not introduce unbounded latency.

RT-003

Safety paths shall not depend on external delays or asynchronous uncertainty.

📦 SECTION C — API & Interface Stability
API-001

Released API contracts shall not be modified without version increment.

Example violation:

Changing request schema from speed:int → { rpm:int }

API-002

All input parameters shall enforce range validation.

Example:

Speed must define minimum and maximum constraints.

API-003

No silent behavioral change in safety-related endpoints.

If behavior changes, version must increment.

🛡 SECTION D — Fault Handling & Diagnostics
ERR-001

All unsafe conditions shall produce explicit error responses.

ERR-002

Emergency shutdown shall record cause of fault.

ERR-003

System shall enter safe state upon any detected violation.

Safe state defined as:

running = False

speed = 0

alarm = True

🔄 SECTION E — Upgrade & Change Control
CHG-001

Safety-related logic modifications must be explicitly identified in release notes.

CHG-002

Upgrade shall not weaken existing safety mechanisms.

CHG-003

Any removal of validation logic is classified as HIGH or CRITICAL deviation.

5️⃣ Compliance Classification

Each rule shall be evaluated as:

Status Meaning
PASS Fully compliant
FAIL Non-compliant
PARTIAL Incomplete compliance
N/A Not applicable

Severity classification:

CRITICAL → Direct safety hazard

HIGH → Potential unsafe condition

MEDIUM → Quality or reliability degradation

LOW → Best-practice deviation

6️⃣ Compliance Evaluation Procedure

For each software release:

Perform branch diff analysis

Evaluate rule-by-rule compliance

Generate deviation report

Classify severity

Update Safety Case Impact Summary

Evaluation may be assisted by:

Static inspection

AI-assisted reasoning (Amazon Q)

Manual safety review

7️⃣ Compliance Report Structure

Each release shall produce:

1. Executive Summary
2. Compliance Matrix
3. Critical Deviations
4. Risk Impact Assessment
5. Mitigation Recommendations
6. Approval Recommendation
