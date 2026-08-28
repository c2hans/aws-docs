---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/about-batch-update-schedule.html
---

# Creating and deleting using a batch command
<a name="about-batch-update-schedule"></a>

To create and delete actions in the schedule for a channel, you use the batch update schedule command. This command lets you perform multiple actions in one request. There isn't one command for creating actions and another for deleting actions.

**Important**
When working with a started and running channel, use the **batch-update-schedule** command to add or remove actions. Use the **delete-schedule** command only on idle channels. The **delete-schedule** command will delete all scheduled actions and could cause service interruptions if used on a live channel.

You can use the command as follows:
+ Submit a *single* request such as a request to do the following:
  + Create one action.
  + Delete one action.
+ Submit a *batch* request such as one request to do the following:
  + Create several actions.
  + Delete several actions.
  + Create one or more actions and delete one or more actions.

**Important**
In a command that combines create actions and delete actions, the delete actions are *always* performed before the create actions. This means that MediaLive removes the delete actions from the schedule before it adds the create actions to the schedule.

**Topics**
+ [How a batch request works](how-batch-schedule-requests-work.md)
+ [Batch command in different interfaces](batchupdatecommand-interfaces.md)
+ [JSON payload in different interfaces](batchupdatecommand-payloads.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
