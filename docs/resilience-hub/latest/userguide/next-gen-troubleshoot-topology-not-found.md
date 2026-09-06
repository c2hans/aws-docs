---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-topology-not-found.html
---

# Assessment fails with topology not found
<a name="next-gen-troubleshoot-topology-not-found"></a>

**Symptom:** `StartFailureModeAssessment` returns an error about missing topology.

**Solution:** Run `StartServiceTopologyDiscovery` first and wait for it to complete successfully. Assessments require a completed topology.
