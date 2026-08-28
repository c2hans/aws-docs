---
source_url: https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/operational-observability.html
---

# Operational observability
<a name="operational-observability"></a>

 Observability is required to gain actionable insights into the performance of your environments and help you to detect and investigate problems. It also has a secondary purpose that allows you to define and measure key performance indicators (KPIs) and service level objectives (SLOs) such as uptime. For most organizations, important operations KPIs are mean time to detect (MTTD) and mean time to recover (MTTR) from an incident.

Throughout observability, context is important, because data is collected and then associated tags are gathered. Regardless of the service, application, or application tier that you are focusing on, you can filter and analyze for that specific dataset. Tags can be used to automate onboarding to CloudWatch Alarms so that the right teams can be alerted when certain metric thresholds are breached. For example, a tag key `example-inc:ops:alarm-tag` and the value on it could indicate creation of the CloudWatch Alarm. A solution demonstrating this is described in [Use tags to create and maintain Amazon CloudWatch alarms for Amazon EC2 instances](https://aws.amazon.com/blogs/mt/use-tags-to-create-and-maintain-amazon-cloudwatch-alarms-for-amazon-ec2-instances-part-1/).

 Having too many alarms configured can easily create an alert storm—when a large number of alarms or notifications rapidly overwhelm operators and reduce their overall effectiveness while operators are manually triaging and prioritizing individual alarms. Additional context for the alarms can be provided in the form of tags, which means that rules can be defined within Amazon EventBridge to help ensure that focus is given to the upstream issue rather than downstream dependencies.

 The role of operations alongside DevOps is often overlooked, but for many organizations, central operations teams still provide a critical first response outside of normal business hours. (More details can be found about this model in the [Operational Excellence whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/separated-aeo-ieo-with-cent-gov-and-partner.html).) Unlike the DevOps team that owns the workload, they typically do not have the same depth of knowledge, so the context that tags provide within dashboards and alerts, can direct them to the correct runbook for the issue, or initiate an automated runbook (refer to the blog post [Automating Amazon CloudWatch Alarms with AWS Systems Manager](https://aws.amazon.com/blogs/mt/automating-amazon-cloudwatch-alarms-with-aws-systems-manager/)).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
