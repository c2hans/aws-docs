---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/message-appinstancebot.html
---

# Sending messages to an AppInstanceBot for Amazon Chime SDK messaging
<a name="message-appinstancebot"></a>

You use the [SendChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html) API to send messages to an AppInstanceBot. You send the messages to the channel in which the AppInstanceBot is a member. If the [natural language understanding model](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html) recognizes the message content and elicits an Amazon Lex intent, the AppInstanceBot responds with a channel message and initiates a dialog.

You can also send target messages to a member of the channel, which could be an AppInstanceUser or an AppInstanceBot. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.

The following example shows how to use the AWS CLI to send a channel message.

```
aws chime-sdk-messaging send-channel-message \
--chime-bearer {{caller_app_instance_user_arn}} \
--channel-arn {{channel_arn}} \
--content {{content}} \
--type STANDARD \
--persistence PERSISTENT
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
