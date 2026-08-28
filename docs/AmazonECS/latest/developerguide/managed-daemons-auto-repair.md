---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-daemons-auto-repair.html
---

# Daemon auto repair
<a name="managed-daemons-auto-repair"></a>

Amazon ECS treats all daemons as critical to instance health. If any daemon task stops or becomes unhealthy, Amazon ECS considers the instance impaired and automatically drains and replaces it. The daemon auto repair actions are as follows:

1. Amazon ECS detects when a daemon task stops or becomes unhealthy.

1. Amazon ECS marks the instance as draining, which prevents it from accepting new application tasks.

1. Amazon ECS provisions a replacement instance and starts the daemon task on it.

1. After the daemon task reaches a healthy state, Amazon ECS schedules the application tasks from the draining instance onto the replacement.

1. Amazon ECS terminates the original instance.

**Important**
Daemon health checks are optional but highly recommended. Without a health check, Amazon ECS can only detect failures when the daemon task stops.

You can monitor daemon health using the `DescribeContainerInstances` API or `DescribeTasks` API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
