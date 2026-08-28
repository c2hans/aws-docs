---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/default-agent-transfer.html
---

# Default agent transfer flow in Connect Customer: "Transferring now"
<a name="default-agent-transfer"></a>

This default transfer flow is what the "from" agent experiences when they transfer a contact to another agent by using [Create quick connects in Connect Customer](quick-connects.md). The "from" agent hears a **Play prompt** play the message "Transferring now." Then the **Transfer to agent** block is used to transfer the contact to the agent.

When the contact is transferred, the "to" agent hears the [Default agent whisper](default-agent-whisper.md).

**Tip**
The **Transfer to Agent** block is a beta feature and only works for voice interactions. To transfer a chat contact to another agent, follow these instructions: [Use contact attributes to route contacts to a specific agent](transfer-to-agent.md#use-attribs-agent-queue).

For instructions about how to override and change a default flow, see [Change a default flow in your Connect Customer contact center](change-default-contact-flow.md).

**Tip**
Wondering if a default flow has been changed? Use [flow version control](flow-version-control.md) to view the original version of the flow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
