---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-topology-fails.html
---

# Resources discovered but topology generation fails
<a name="next-gen-troubleshoot-topology-fails"></a>

**Symptom:** Resources appear in the list but topology shows no connections.

**Solutions:**
+ Verify the invoker role has `ReadOnlyAccess` (required for topology queries).
+ Check that resources are in a VPC (topology generation maps VPC-based connections).
+ For EKS resources, verify Kubernetes RBAC is configured.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
