---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-guard-duty-configure-manual-existing-tasks.html
---

# Adding Runtime Monitoring to existing Amazon ECS tasks
<a name="ecs-guard-duty-configure-manual-existing-tasks"></a>

When you turn on Runtime Monitoring, all new standalone tasks, and new service deployments in the cluster are protected automatically. In order to preserve the immutability constraint, existing tasks are not affected.

## Prerequisites
<a name="ecs-guard-duty-configure-manual-existing-tasks-prerequisites"></a>
+ Turn on Runtime Monitoring. For more information, see [Turning on Runtime Monitoring for Amazon ECS](ecs-guard-duty-configure-manual-guard-duty.md).

## Procedure
<a name="ecs-guard-duty-configure-manual-existing-tasks-procedure"></a>
+  To immediately protect a task, you need to perform one of the following actions:
  + For standalone tasks, stop the tasks, and then start them. For more information, see [Stopping an Amazon ECS task](standalone-task-stop.md) and [Running an application as an Amazon ECS task](standalone-task-create.md).
  + For tasks that are part of a service, update the service with the "force new deployment" option. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
