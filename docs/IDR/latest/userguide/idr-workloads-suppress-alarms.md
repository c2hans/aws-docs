---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/idr-workloads-suppress-alarms.html
---

# Suppress alarms from engaging Incident Detection and Response
<a name="idr-workloads-suppress-alarms"></a>

Specify which of your onboarded workload alarms engage with AWS Incident Detection and Response monitoring by suppressing them temporarily or on a schedule. For example, you might temporarily suppress workload alarms during planned maintenance to prevent the alarms from engaging Incident Detection and Response. Or, you might suppress alarms on a schedule if you have daily reboot activity. You can suppress alarms at the alarm source, such as Amazon CloudWatch, or you can submit a workload change request.

**Topics**
+ [Suppress alarms at the alarm source](suppress-alarms-at-source.md)
+ [Submit a workload change request to suppress alarms](suppress-alarms-at-source-wcr.md)
+ [Tutorial: Use a metric math function to suppress an alarm](suppress-alarms-tutorial-suppress.md)
+ [Tutorial: Remove a metric math function to un-suppress an alarm](suppress-alarms-tutorial-unsuppress.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
