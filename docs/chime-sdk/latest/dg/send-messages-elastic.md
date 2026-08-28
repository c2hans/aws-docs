---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/send-messages-elastic.html
---

# Sending elastic channel messages in Amazon Chime SDK meetings
<a name="send-messages-elastic"></a>

The [SendChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html) API creates messages at the sub-channel level. To send messages, you must have a `subChannelId`. You can also use the [UpdateChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html), and [RedactChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html) APIs to edit and delete messages, but in all cases, you must have a `subChannelId`.

**Note**
Message senders can only edit or redact messages if they belong the sub-channel that they send messages to. If membership balancing transfers a member to another sub-channel, that member can only edit or redact the messages that they send in that new sub-channel.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
