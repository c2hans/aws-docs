---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-manage-remove-automatic.html
---

# Removing Runtime Monitoring for Amazon ECS from an account
<a name="ecs-guard-duty-manage-remove-automatic"></a>

When you no longer want to use Runtime Monitoring, disable the feature in GuardDuty. For information about how to disable the feature, see [Enabling Runtime Monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring-configuration.html) in the *Amazon GuardDuty User Guide*.

 GuardDuty performs the following operations:
+ Deletes the VPC endpoints for GuardDuty for each VPC that hosts a cluster.
+ No longer deploys the GuardDuty security agent to new standalone Fargate tasks, or new service deployments.

  In order to preserve the immutability constraint, existing tasks and deployments are not affected until they are stopped, replicated, or scaled.
+ Stops billing and no longer accepts run time events for tasks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
