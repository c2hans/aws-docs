---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-provisioning-timeout.html
---

# Configuring provisioning timeouts to control capacity in Amazon EMR
<a name="emr-provisioning-timeout"></a>

When you use instance fleets, you can configure *provisioning timeouts*. A provisioning timeout instructs Amazon EMR to stop provisioning instance capacity if the cluster exceeds a specified time threshold during cluster launch or cluster scaling operations. The following topics cover how to configure a provisioning timeout for cluster launch and for cluster scale-up operations.

**Topics**
+ [Configure provisioning timeouts for cluster launch in Amazon EMR](emr-provisioning-timeout-launch.md)
+ [Customize a provisioning timeout period for cluster resize in Amazon EMR](emr-provisioning-timeout-resize.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
