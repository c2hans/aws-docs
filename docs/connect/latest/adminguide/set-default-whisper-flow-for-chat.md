---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/set-default-whisper-flow-for-chat.html
---

# Set the default whisper flow in Connect Customer for a chat conversation
<a name="set-default-whisper-flow-for-chat"></a>

For chat conversations, you need to include a **Set whisper flow** block for default agent or customer whispers to play.

For example, to set the default whisper flow for chats that use the [Sample inbound flow](sample-inbound-flow.md):

1. Go to **Routing**, **Flows**, and choose the Sample inbound flow.

1. Add a **Set whisper flow** block after the chat channel has branched, as shown in the following image:
![A set whisper flow block in the sample inbound flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-whisper-flow-default-chat-sample.png)

1. In the **Set whisper flow** block, open the properties page, and choose the flow you want to play as the default for chat conversations. For example, you might choose **Default whisper flow** to show agents the name of the originating queue in the chat window. This is helpful when agents are managing more than one queue.
![The properties page of the set whisper flow block, set to default agent whisper.](http://docs.aws.amazon.com/connect/latest/adminguide/images/set-whisper-flow-properties3.png)

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
