---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/stopped-task-error-codes.html
---

# Amazon ECS stopped tasks error messages
<a name="stopped-task-error-codes"></a>

The following are the possible error messages you may receive when your task stops unexpectedly.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

**Tip**
You can use the [Amazon ECS MCP server](ecs-mcp-introduction.md) with AI assistants to analyze task failures and container logs using natural language.

Stopped task error codes have a category associated with them, for example "ResourceInitializationError". To get more information about each category, see the following:

| Category | Learn more |
| --- | --- |
| TaskFailedToStart |  [Troubleshooting Amazon ECS TaskFailedToStart errors](failed-to-start-error.md)  |
| ResourceInitializationError |  [Troubleshooting Amazon ECS ResourceInitializationError errors](resource-initialization-error.md)  |
| ResourceNotFoundException |  [Troubleshooting Amazon ECS ResourceNotFoundException errors](resource-not-found-error.md) |
| SpotInterruptionError |  [Troubleshooting Amazon ECS SpotInterruption errors](spot-interruption-errors.md)  |
| InternalError |  [Troubleshooting Amazon ECS InternalError errors](internal-error.md)  |
| OutOfMemoryError |  [Troubleshooting Amazon ECS OutOfMemoryError errors](out-of-memory.md)  |
| ContainerRuntimeError |  [Troubleshooting Amazon ECS ContainerRuntimeError errors](container-runtime-error.md)  |
| ContainerRuntimeTimeoutError |  [Troubleshooting Amazon ECS ContainerRuntimeTimeoutError errors](container-runtime-timeout-error.md)  |
| CannotStartContainerError |  [Troubleshooting Amazon ECS CannotStartContainerError errors](cannot-start-container.md)  |
| CannotStopContainerError |  [Troubleshooting Amazon ECS CannotStopContainerError errors](cannot-stop-container.md)  |
| CannotInspectContainerError |  [Troubleshooting Amazon ECS CannotInspectContainerError errors](cannot-inspect-container.md)  |
| CannotCreateVolumeError |  [Troubleshooting Amazon ECS CannotCreateVolumeError errors](cannot-create-volume.md)  |
| CannotPullContainer |  [CannotPullContainer task errors in Amazon ECS](task_cannot_pull_image.md)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
