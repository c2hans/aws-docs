---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/quotas.html
---

# Quotas
<a name="quotas"></a>

The solution uses Trusted Advisor and Service Quotas to check quotas against resource utilization.
+  **Trusted Advisor** - This solution supports 50 quota checks offered by Trusted Advisor. For more information, refer to [Quota checks with Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/service-limits.html).
+  **Service Quotas** - This solution supports all quotas that allow resource usage monitoring using Amazon CloudWatch. When more quotas from different services start supporting resource usage monitoring, the solution automatically updates to support these new quotas. For details, refer to [Service Quotas and Amazon CloudWatch alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Quota Monitor for AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
