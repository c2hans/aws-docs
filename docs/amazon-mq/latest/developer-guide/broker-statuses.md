---
source_url: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-statuses.html
---

# Amazon MQ broker statuses
<a name="broker-statuses"></a>

A broker's current condition is indicated by a *status*. The following table lists the statuses of an Amazon MQ broker.

| Console | API | Description |
| --- | --- | --- |
| Creation failed | CREATION\_FAILED | The broker couldn't be created. |
| Creation in progress | CREATION\_IN\_PROGRESS | The broker is currently being created. |
| Deletion in progress | DELETION\_IN\_PROGRESS | The broker is currently being deleted. |
| Reboot in progress | REBOOT\_IN\_PROGRESS | The broker is currently being rebooted. |
| Running | RUNNING | The broker is operational. |
| Critical action required | CRITICAL\_ACTION\_REQUIRED | The broker is running, but is in a degraded state and requires immediate action. You can find instructions to resolve the issue by chosing the action required code from the list in [Troubleshooting Amazon MQ](troubleshooting.md). |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MQ. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazon-mq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
