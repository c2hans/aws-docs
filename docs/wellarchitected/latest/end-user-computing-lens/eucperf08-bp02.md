---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp02.html
---

# EUCPERF08-BP02 Monitor Amazon WorkSpaces Applications CloudWatch metrics
<a name="eucperf08-bp02"></a>

 Use Amazon CloudWatch to establish and monitor your WorkSpaces Applications workload's performance against the KPIs established for your service. [Use the Automatic dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html) in Amazon CloudWatch to monitor your fleet capacity over time or consider creating a custom dashboard tailored to your environment.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-20"></a>

 Measure your workload's performance across [Amazon AppStream 2.0 fleets and fleet instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
