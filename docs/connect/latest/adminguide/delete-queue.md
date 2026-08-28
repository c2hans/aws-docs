---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/delete-queue.html
---

# Delete a queue from your Connect Customer instance
<a name="delete-queue"></a>

There are three ways to delete a queue from your Connect Customer instance:
+ Connect Customer admin website

  1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an **Admin** account, or an account that has **Routing** - **Queues** - **Delete** permission in its security profile.

  1. On the Connect Customer admin website, on the navigation menu, choose **Routing**, **Queues** and then select the delete icon.
![The Queues page, the Status option and the Delete option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/delete-queue.png)
**Important**
You cannot undo a deleted queue. To temporarily disable a queue, toggle its status to **Disabled**.
+ [DeleteQueue](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteQueue.html) API
+ [delete-queue](https://docs.aws.amazon.com/cli/latest/reference/connect/delete-queue.html) AWS CLI

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
