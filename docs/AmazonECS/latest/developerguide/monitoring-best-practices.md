---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/monitoring-best-practices.html
---

# Best practices for monitoring Amazon ECS
<a name="monitoring-best-practices"></a>

Use the following best practices for monitoring Amazon ECS.
+ Make monitoring a priority to head off small problems before they become big ones
+ Create a monitoring plan that includes answers to the following question
  + What are your monitoring goals?
  + What resources will you monitor?
  + How often will you monitor these resources?
  + What monitoring tools will you use?
  + Who will perform the monitoring tasks?
  + Who should be notified when something goes wrong?
+ Automate monitoring as much as possible.
+ Check the Amazon ECS log files. For more information, see [Viewing Amazon ECS container agent logs](logs.md).
+ Use Runtime Monitoring to help protect your accounts, containers, workloads, and the data within your AWS environment. For more information, see [Identify unauthorized behavior using Runtime Monitoring](ecs-guard-duty-integration.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
