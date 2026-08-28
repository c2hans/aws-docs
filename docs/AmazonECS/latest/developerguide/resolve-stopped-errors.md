---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/resolve-stopped-errors.html
---

# Resolve Amazon ECS stopped task errors
<a name="resolve-stopped-errors"></a>

When your task fails to start, you see an error message in the console and in the `describe-tasks` output parameters (`stoppedReason` and `stopCode`).

You can view stopped tasks in the console for one hour. In order to see stopped tasks, you must change the filter option. For more information, see [Viewing Amazon ECS stopped task errors](stopped-task-errors.md).

The following pages provide information about stopped tasks.
+ Learn about changes to stopped task error messages.

  [Amazon ECS stopped task error messages updates](stopped-tasks-error-messages-updates.md)
+ View your stopped tasks so you can get information about the cause.

  [Viewing Amazon ECS stopped task errors](stopped-task-errors.md)
+ Learn about the stopped tasks error messages and possible reasons for the errors.

  [Amazon ECS stopped tasks error messages](stopped-task-error-codes.md)
+ Learn how to verify stopped task connectivity and fix the errors.

  [Verifying Amazon ECS stopped task connectivity](verify-connectivity.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
