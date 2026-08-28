---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/msg-types.html
---

# Understanding Amazon Chime SDK message types
<a name="msg-types"></a>

You send messages through channels. You can send `STANDARD`, `CONTROL`, or `SYSTEM` messages.
+ `STANDARD` messages can be up to 4KB in size and contain metadata. Metadata is arbitrary, and you can use it in a variety of ways, such as containing a link to an attachment.
+ `CONTROL` messages are limited to 30 bytes and do not contain metadata.
+ `STANDARD` and `CONTROL` messages can be persistent or non-persistent. Persistent messages are preserved in the history of a channel and viewed by using a `ListChannelMessages` API call. Non persistent messages are sent to every `AppInstanceUser` connected via WebSocket.
+ Amazon Chime SDK sends automated `SYSTEM` messages for events such as members joining or leaving a channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
