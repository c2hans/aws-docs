---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/sending-msgs.html
---

# Sending messages in Amazon Chime SDK messaging
<a name="sending-msgs"></a>

You use the `SendChannelMessage` API to send messages to a channel. For a channel associated with a channel flow, the processor assigns one of the following status values.

| Message status | Description |
| --- | --- |
| `SENT` | Message processed successfully. |
| `PENDING` | Ongoing processing. |
| `FAILED` | Processing failed because the processor Lambda function is unreachable. |
| `DENIED` | The message won't be sent. |

**Receiving intermediate status events**
**Websocket events**

Websocket events are sent to a channel after they successfully establish a connection. For more information, refer to [Using WebSockets to receive messages in Amazon Chime SDK messaging](websockets.md).

| Event type | Status | Recipients | Notes |
| --- | --- | --- | --- |
| `CREATE_CHANNEL_MESSAGE` | `SENT` | All channel members | `SendChannelMessage` API with successful preprocessing |
| `UPDATE_CHANNEL_MESSAGE` | `SENT` | All channel members | `UpdateChannelMessage` API with successful preprocessing |
| `PENDING_CREATE_CHANNEL_MESSAGE` | `PENDING` | Message sender only | `SendChannelMessage` API with ongoing preprocessing |
| `PENDING_UPDATE_CHANNEL_MESSAGE` | `PENDING` | Message sender only | `UpdateChannelMessage` API with ongoing preprocessing |
| `FAILED_CREATE_CHANNEL_MESSAGE` | `FAILED` | Message sender only | `SendChannelMessage` API with failed preprocessing |
| `FAILED_UPDATE_CHANNEL_MESSAGE` | `FAILED` | Message sender only | `UpdateChannelMessage` API with failed preprocessing |
| `DENIED_CREATE_CHANNEL_MESSAGE` | `DENIED` | Message sender only | `SendChannelMessage` API with processor denying the message |
| `DENIED_UPDATE_CHANNEL_MESSAGE` | `DENIED` | Message sender only | `UpdateChannelMessage` API with processor denying the message |

**GetChannelMessageStatus API**
This API provides an alternative way to retrieve message status if the event was not received due to a bad websocket connection. For more information, refer to the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessageStatus.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessageStatus.html) API documentation.

**Note**
This API does not return statuses for denied messages, because we don't store them.
