---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/associate-channel-flow.html
---

# Associating and disassociating channel flows for Amazon Chime SDK messaging
<a name="associate-channel-flow"></a>

When you associate a channel is associated with a channel flow, the processor(s) in the channel flow pre-process all messages sent to the channel. You must be a channel moderator or administrator to invoke the channel flow association and disassociation APIs. Remember these facts as you go.
+ You can associate a maximum of 1 channel flow with a channel at any given time. To associate a channel flow, call the [AssociateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AssociateChannelFlow.html) API.
+ To disassociate a channel flow and stop preprocessing of channel messages, call the [DisassociateChannelFlow](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DisassociateChannelFlow.html) API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
