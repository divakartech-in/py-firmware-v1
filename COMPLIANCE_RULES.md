SECTION A — Safety Integrity (SIL-Oriented)
SAF-001

Emergency stop must override all operational states.

SAF-002

System must not start if any alarm or fault flag is active.

SAF-003

Over-temperature condition must trigger deterministic shutdown.

SAF-004

Safety-critical flags (alarm, fault) must persist until explicitly cleared.

SAF-005

No downgrade of safety thresholds without documented justification.

SECTION B — Determinism & Real-Time Constraints
RT-001

No blocking calls in control execution paths.

RT-002

Control loops must not contain unbounded delays.

RT-003

No dynamic allocation in safety-critical paths.

SECTION C — Interface & Backward Compatibility
API-001

No breaking API contract changes in released endpoints.

API-002

All input parameters must enforce range validation.

API-003

No silent behavioral change in safety logic.

SECTION D — Fault Handling & Diagnostics
ERR-001

All unsafe conditions must produce explicit error reporting.

ERR-002

Emergency shutdown must log cause of shutdown.

ERR-003

System must enter safe state upon fault detection.

SECTION E — Traceability & Change Impact
CHG-001

All safety-related code changes must be identifiable and documented.

CHG-002

Upgrade must not weaken existing safety controls.
