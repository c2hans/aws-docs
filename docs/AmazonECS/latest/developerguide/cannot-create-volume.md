---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cannot-create-volume.html
---

# Troubleshooting Amazon ECS CannotCreateVolumeError errors
<a name="cannot-create-volume"></a>

The following are some CannotCreateVolumeError error messages and actions that you can take to fix the errors.

To check your stopped tasks for an error message using the AWS Management Console, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

## CannotCreateVolumeError
<a name="cannot-create-volume-1"></a>

This error occurs when the agent can't create the volume mount specified in the task definition.

This error only occurs if you use platform version `1.4.0` or later (Linux) or `1.0.0` or later (Windows).

For information about how to debug and fix this issue, see [Why is my Amazon ECS task Stopped](https://repost.aws/knowledge-center/ecs-task-stopped) on AWS re:Post.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
