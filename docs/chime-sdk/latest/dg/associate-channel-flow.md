---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/associate-channel-flow.html
---

# Associating and disassociating channel flows for Amazon Chime SDK messaging
<a name="associate-channel-flow"></a>

When you associate a channel is associated with a channel flow, the processor(s) in the channel flow pre-process all messages sent to the channel. You must be a channel moderator or administrator to invoke the channel flow association and disassociation APIs. Remember these facts as you go.
+ You can associate a maximum of 1 channel flow with a channel at any given time. To associate a channel flow, call the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AssociateChannelFlow.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_AssociateChannelFlow.html) API.
+ To disassociate a channel flow and stop preprocessing of channel messages, call the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DisassociateChannelFlow.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DisassociateChannelFlow.html) API.
