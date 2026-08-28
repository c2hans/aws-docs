---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/accept-task.html
---

# Accept a task assigned in the Contact Control Panel (CCP)
<a name="accept-task"></a>

The steps in this topic describe how to deliver tasks to an agent when their status is set to **Available** in the Contact Control Panel (CCP).

1. Whenever you set your status in the CCP to **Available**, Connect Customer can deliver tasks to you, based on the settings in your [routing profile](routing-profiles.md).
![The CCP, an incoming task, the accept task button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-tasks-incoming.png)

1. When a task arrives, choose **Accept task**. You have up to 30 seconds to accept a task (10 seconds more than accepting a call or chat).

1. Review the description of the task, and choose the links as needed to complete the task.
![The CCP, an example task, the end task button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-task-end-task.png)

1. When you've completed the task, choose **End task**.

1. You will then be in ACW. When finished, choose **Close contact**.
![After contact work for a task.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-task-close-task.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
