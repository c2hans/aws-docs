---
source_url: https://docs.aws.amazon.com/chime/latest/ug/delete-chat-messages.html
---

# Deleting sent messages
<a name="delete-chat-messages"></a>

By design, Amazon Chime prevents you from deleting chat messages after you send them. This applies to messages sent in conversations, groups, and chat rooms. Amazon Chime does this in order to comply with data retention policies.

If you need to delete a chat message, you must copy the ID of the message, and the ID of the conversation or chat room, and send those values to your Amazon Chime system administrator.

The following steps explain how to find and copy the IDs needed to have a message deleted.

**To copy message IDs**

1. In a conversation, group, or chat room, open the ellipsis menu next to the message that you want to delete.

1. Choose **Copy message ID**.
![Menu showing the Copy message ID command.](http://docs.aws.amazon.com/chime/latest/ug/images/copy-message-id.png)

   Amazon Chime copies the ID of the message and the ID of the conversation or the chat room, depending on the message's location. The administrator needs both values.

1. Send the IDs to your Amazon Chime administrator and request to have the message deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
