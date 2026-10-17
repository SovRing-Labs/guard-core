> **Status: under development — pre-alpha.** Interfaces, numbers and file layout can change without notice.

## Works today
- G1: PASS — Isolated quick test; evidence: results/2026-10-17-G1.log.
- G2: PASS — CLI help without baseline access; evidence: results/2026-10-17-G2.log.
- G3: PASS — G0 excludes process monitoring and automatic enforcement; evidence: STATUS.md.

## Not yet tested
Production and adversarial security evaluation. Stage about 30 % (author estimate).
External rows need their named prerequisite.

## Known failures and honest negatives
G0 file-integrity only. No process monitor, malware detector, rules engine or automatic enforcement. The historical Python lookup missed its one-microsecond target; this export makes no latency claim.

## Corrections
Historical plans predate some existing code. Historical measurements are not current reruns.
Publication path rewrites and scratch harnesses replace private assumptions.

## How to re-check
python3 tests/guard_demo.py; all row commands are in suite.json.

## Defensive publication
TECHNICAL-DISCLOSURE.md dated 2026-10-16; DOI pending first release.
