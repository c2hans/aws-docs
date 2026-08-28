---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/channels-and-concurrency.html
---

# Channels and concurrency for routing contacts in Connect Customer
<a name="channels-and-concurrency"></a>

Agents can handle voice, chat, tasks and email in Connect Customer. When you set up a routing profile to handle multiple channels, you have two options:
+ Option 1: Set up agents so they can handle contacts while already on another channel. This is called *cross-channel concurrency*.
+ Option 2: Set up agents so they can be offered voice, chat, tasks, or email if they are fully idle, depending on what is in queue. When you choose this option, after the agent starts work on contacts from one channel they will no longer be offered contacts from any other channels.

When using cross-channel concurrency, Connect Customer checks which contact to offer the agent as follows:

1. It checks what contacts/channels the agent is currently handling.

1. Based on what channels they are currently handling, and the cross-channel configuration in the agent's routing profile, it determines whether the agent can be routed the next contact.

1. Connect Customer prioritizes the longest waiting contact if Priority and Delay are equal. Even though it's evaluating multiple channels at the same time, First-In First-Out is still respected.

For a detailed example of how Connect Customer routes contacts when cross-channel concurrency is set up, see [Example of how a contact is routed with cross-channel concurrency](routing-profiles.md#example-routing-concurrency).

To learn more about what the agent experiences in the Contact Control Panel when handling multiple chats, see [Use the Contact Control Panel (CCP) in Connect Customer to chat with contacts](chat-with-connect-contacts.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
