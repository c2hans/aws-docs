---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/deleting-channels.html
---

# Deleting channels
<a name="deleting-channels"></a>

## Deleting one channel
<a name="delete-channels-one"></a>

You can delete a channel if it isn't running.

1. On the Conductor Live main menu, choose **Channels**.

1. On the **Channels** page, choose the **Delete** icon beside the channel. The channel is deleted immediately.

## Deleting several channels at once
<a name="delete-channels-several"></a>

You can use the **Tasks** feature to delete several channels at once.

1. On the Conductor Live main menu, choose **Channels**.

1. On the **Channels** page, select **Tasks** on the top left. Then choose **Delete Channels**.

1. Select the channels that you want to delete.

1. Choose **Save for Later **or **Process Now**.

   **Process Now**: Conductor Live applies the change. The **Channels** page reappears, showing the change.

   **Save for Later**: This option lets you queue up several tasks and then perform them in one pass.
**Warning**
**Save for Later **is intended to queue for a short time.
Don't use **Save for Later** and then delay process the task in a few hours. Doing so might create undesired consequences.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
