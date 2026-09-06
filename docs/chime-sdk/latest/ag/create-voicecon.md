---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/create-voicecon.html
---

# Creating an Amazon Chime SDK Voice Connector
<a name="create-voicecon"></a>

You use the Amazon Chime SDK console to create Amazon Chime SDK Voice Connectors.

**To create a Voice Connector**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose **Create new voice connector**.

1. Under **Voice connector name**, enter a name for the Voice Connector.

1. Under **Encryption**, select **Enabled** or **Disabled**.

1. Under **Network Type**, select **DUAL\_STACK** or **IPV4\_ONLY**.

   1. You can apply **DUAL\_STACK** (IPv4/IPv6) only to newly created Voice Connectors.

   1. Existing Voice Connectors use **IPV4\_ONLY** as the Network Type.

1. (Optional) Under **Tags**, choose **Add new tag**, then do the following.

   1. Under **Key**, enter the tag's key.

   1. Under **Value**, enter the tag's value.

   1. As needed, choose **Add new tag** to add more tags to the Voice Connector.

   For more information about tags, refer to [Adding tags to Voice Connectors](use-tags-voice-con.md#add-tags-voice-con).

1. Choose **Create Voice Connector**.

**Note**
Enabling encryption configures your Voice Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use TLS transport, and unencrypted outbound calls are blocked.
