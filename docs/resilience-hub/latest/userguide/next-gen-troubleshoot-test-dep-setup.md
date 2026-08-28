---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-troubleshoot-test-dep-setup.html
---

# Dependency fault action fails with setup error
<a name="next-gen-troubleshoot-test-dep-setup"></a>

**Symptom:** A dependency fault action fails because the required agent or sidecar is not configured.

**Cause:** Packet loss actions require SSM Agent on Amazon EC2, an SSM container in Amazon ECS task definitions, or a Kubernetes service account for Amazon EKS pods.

**Solution:** Follow the setup steps for your compute type in the [AWS FIS actions reference](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
