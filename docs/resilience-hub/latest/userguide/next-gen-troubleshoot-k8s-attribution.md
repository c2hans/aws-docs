---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-k8s-attribution.html
---

# Kubernetes attribution gaps
<a name="next-gen-troubleshoot-k8s-attribution"></a>

**Symptom:** Dependencies are discovered but attributed to the wrong service in a shared EKS cluster.

**Cause:** When multiple services share an EKS cluster, DNS queries are attributed at the node level, not the pod level.

**Solution:** Enhanced pod-level attribution is planned for a future release. Currently, review dependencies manually for shared clusters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
