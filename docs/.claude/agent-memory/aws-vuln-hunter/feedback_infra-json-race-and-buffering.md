---
name: infra-json-race-and-buffering
description: Two operational traps that bit during the Bedrock KB run - shared state file races and buffered background python
metadata:
  type: feedback
---

Two self-inflicted traps to avoid on long AWS hunts with background jobs.

**Rule 1: Do not let multiple concurrent background jobs read-modify-write one shared JSON state file.**
**Why:** During the Bedrock KB run (finding 16), background waiter loops each loaded `infra.json`, then re-dumped it with stale in-memory values, silently reverting fields (dropped `sf_secret_arn`, and corrupted the KB IAM role to point `aoss:APIAccessAll` at the WRONG collection -> persistent 403s that looked like a service bug but were self-contamination).
**How to apply:** Have background jobs write to their OWN result files (e.g. `t1_result.txt`), never to the shared state file. Rebuild the shared state authoritatively from live AWS (`get_knowledge_base` storageConfiguration, `describe_secret`) when in doubt. Always run the "rule out your own contamination" check before believing a 403/permission anomaly.

**Rule 2: Background python stdout is block-buffered; add `flush=True` or expect empty output files until exit.**
**Why:** `until grep FINAL ...` waits stalled because prints never flushed. Also prefer an independent API status poll over trusting the buffered file.
**How to apply:** `print(..., flush=True)` in any backgrounded python, or query the API directly to check progress.
