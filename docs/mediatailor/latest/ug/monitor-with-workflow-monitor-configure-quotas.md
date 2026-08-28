---
source_url: https://docs.aws.amazon.com/mediatailor/latest/ug/monitor-with-workflow-monitor-configure-quotas.html
---

# Workflow monitor quotas
<a name="monitor-with-workflow-monitor-configure-quotas"></a>

The following section contains quotas for workflow monitor resources. Each quota is on a "per account" basis. If you need to increase a quota for your account, you can use the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas/home) to request an increase, unless otherwise noted in the following table.

**Quotas**

| Resource type | Quota |
| --- | --- |
| CloudWatch alarm template groups | 20 |
| CloudWatch alarm templates | 200 |
| EventBridge rule template groups | 20 |
| EventBridge rule templates | 200 |
| Signal maps | 30 |
| Signal maps: CloudWatch alarm template groups attached to a single signal map | 5You cannot increase this quota. |
| Signal maps: EventBridge rule template groups attached to a single signal map | 5You cannot increase this quota. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaTailor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediatailor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
