# TECHNICAL DISCLOSURE — guard-core
Author: Juan Carlos De Santiago, with the Sovereign Raptor fleet (AI-assisted). Date of disclosure: 2026-10-16.
Published as defensive prior art: the author claims no patent on what is described here and asks that none be granted on it.
Licence of this text: CC BY 4.0.

## Problem and mechanism
Hash each owned file with SHA-256. Hash its absolute path, reduce the first 64 digest bits on moduli (3,29,41,59,101), and pack the residues in mixed radix as a dictionary slot. Keep a bucket list and compare the full path, so a collision never substitutes another file. Persist path, slot, digest, size, mtime, mode and receipt in SQLite. A check rehashes files: unchanged or committed-clean changes yield +1, new/unreceipted changes yield 0, dirty tracked changes and removal yield -1. Git metadata is a receipt, not proof that a change is safe.

## Data layout and reproduction
Source modules and suite.json describe the executable layout. Run: python3 tests/guard_demo.py.
Outputs and temporary stores stay in temporary directories; results/ stores the author's saved command output.

## Measurements
The 2026-10-17 quick-test command and output are preserved in results/2026-10-17-quicktest.log. No throughput or production detection rate is claimed.

## What is not claimed
G0 file-integrity only. No process monitor, malware detector, rules engine or automatic enforcement. The historical Python lookup missed its one-microsecond target; this export makes no latency claim.

## Field lineage
SHA-256: NIST, Secure Hash Standard, 2015. Residue arithmetic: Szabo and Tanaka, Residue Arithmetic and its Applications to Computer Technology, 1967.
HTTP signatures: Backman, Richer and Sporny, HTTP Message Signatures (RFC 9421), 2024. Ed25519: Josefsson and Liusvaara, EdDSA (RFC 8032), 2017.
Conceptual sources; no reference implementation was copied into the authored core.
