---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cannot-start-container.html
---

# Troubleshooting Amazon ECS CannotStartContainerError errors
<a name="cannot-start-container"></a>

The following are some CannotStartContainerError error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## failed to get container status: {{<reason>}}
<a name="cannot-start-container-1"></a>

This error occurs when a container can't be started.

If your container attempts to exceed the memory specified here, the container is stopped. Increase the memory presented to the container. This is the `memory` parameter in the task definition. For more information, see [Memory](task_definition_parameters.md#container_definition_memory).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
