---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-topology-not-found.html
---

# Assessment fails with topology not found
<a name="next-gen-troubleshoot-topology-not-found"></a>

**Symptom:** `StartFailureModeAssessment` returns an error about missing topology.

**Solution:** Run `StartServiceTopologyDiscovery` first and wait for it to complete successfully. Assessments require a completed topology.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
