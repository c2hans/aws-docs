---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/default-agent-whisper.html
---

# Default agent whisper in Connect Customer: name of the queue
<a name="default-agent-whisper"></a>

This flow uses a [Set whisper flow](set-whisper-flow.md) block to play a message for the agent when the customer and agent are joined.

The name of the queue is played to the agent. It identifies the queue that the customer was in. The name of the queue is retrieved from the system variable `$.Queue.Name`.

Use the [Set whisper flow](set-whisper-flow.md) block to override or disable the default agent whisper in a voice conversation.

**Important**
Chat conversations do not include a default whisper. You need to include a [Set whisper flow](set-whisper-flow.md) for default agent or customer whispers to play. For instructions, see [Set the default whisper flow in Connect Customer for a chat conversation](set-default-whisper-flow-for-chat.md).

For more information about system variables, see [System attributes](connect-attrib-list.md#attribs-system-table).

**Tip**
Wondering if a default flow has been changed? Use [flow version control](flow-version-control.md) to view the original version of the flow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
