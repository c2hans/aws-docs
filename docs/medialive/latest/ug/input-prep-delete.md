---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/input-prep-delete.html
---

# Deleting and stopping input prepare actions in the MediaLive schedule
<a name="input-prep-delete"></a>

You can delete input prepare actions from the schedule. There are different rules for deleting actions depending on the current state of the channel. The channel can be running, idle, or recovering. The channel is idle if you manually stopped it. The channel is recovering if it failed and MediaLive is automatically restarting it.

For detailed information on deleting an action, see [Deleting actions from the schedule (console)](schedule-using-console-delete.md).

**Deleting actions while the channel is running**
When the channel is running, you can't delete the most recent input prepare action that is in the past. This rule exists because the associated input switch might be in the future. When MediaLive automatically restarts the channel, it must also restart the input prepare, to ensure that the input for the immediate input switch will be prepared.

**Deleting actions while the channel is idle**
When the channel is idle, you can delete any input prepare action.

**Stopping an input prepare**
To stop an active input prepare, add an immediate input prepare with no input specified.

For detailed information on adding an action, see [Creating actions in the schedule (console)](schedule-using-console-create.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
