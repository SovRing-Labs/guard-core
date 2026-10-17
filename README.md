# guard-core

[![status: pre-alpha](https://img.shields.io/badge/status-pre--alpha%20(under%20development)-orange)](STATUS.md)
[![defensive publication](https://img.shields.io/badge/defensive%20publication-TECHNICAL--DISCLOSURE.md-blue)](TECHNICAL-DISCLOSURE.md)

Status: **under development — pre-alpha** (STATUS.md). Defensive publication: TECHNICAL-DISCLOSURE.md (dated 2026-10-16; the DOI is
minted by Zenodo on the first GitHub release).

Receipt-reconciled file-integrity baseline for your own files.

## Run it
Use only files and services you own. Tests use temporary directories.

    git clone https://github.com/SovRing-Labs/guard-core
    cd guard-core
    python3 tests/guard_demo.py

## What it does today
| Capability | Evidence |
|---|---|
| Isolated quick test | results/2026-10-17-quicktest.log |
| Method and scope | TECHNICAL-DISCLOSURE.md |

## Not shown here
G0 file-integrity only. No process monitor, malware detector, rules engine or automatic enforcement. The historical Python lookup missed its one-microsecond target; this export makes no latency claim.

## Files
| Path | Purpose |
|---|---|
| tests/ | Isolated harnesses |
| suite.json | Runnable claims and commands |
| results/ | Dated output and historical records |
| DATA.md | Exclusions and prerequisites |

## Licence and stage
PolyForm Small Business 1.0.0 OR PolyForm Noncommercial 1.0.0 OR PolyForm Free Trial 1.0.0 (code); CC BY 4.0 (documents). See LICENSING.md. Development stage: about 30 %, an author estimate rather than measured coverage.

## Use on your own tree
Set GUARD_ROOT to your owned workspace (bin/ and projects/*/bin are scanned), then run python3 bin/guard-core baseline --stats and python3 bin/guard-core check --json. GUARD_DB optionally selects a baseline file; by default it lives under your home .local/state/guard-core. User configuration and local executable roots are included. Reports never quarantine or block a file.
