---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/start-kinesis-vc.html
---

# Streaming Amazon Chime SDK Voice Connector media to Kinesis
<a name="start-kinesis-vc"></a>

You can stream phone call audio from Amazon Chime SDK Voice Connectors to Amazon Kinesis Video Streams for analytics, machine learning and other processing. Developers can store and encrypt audio data in Kinesis Video Streams, and access the data using the Kinesis Video Streams API operation. For more information, see the [https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html).

**Note**
Voice Connector streaming does not restrict phone number formats. You can stream calls from numbers in E.164 and non-E.164 formats. For example, Voice Connector streaming can support 4, 5, or 6-digit extension numbers, or 11-digit private wire numbers. For more information, refer to [SIP-based media recording and network-based recording compatibility](#siprec), later in this guide.
Voice Connector streaming supports G.711 A-law and G.711 µ-law audio encoding.

Use the Amazon Chime SDK console to start media streaming for your Voice Connector. When media streaming begins, your Voice Connector uses an AWS Identity and Access Management (IAM) service-linked role to grant permissions to stream media to Kinesis Video Streams. Then, call audio from each Voice Connector telephone call leg is streamed in real time to separate Kinesis Video Streams.

Use the Kinesis Video Streams Parser Library to download the media streams sent from your Voice Connector. Filter the streams by the following persistent fragments metadata:
+ TransactionId
+ VoiceConnectorId

For more information, see [Kinesis Video Streams Parser Library](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/parser-library.html) and [Using streaming metadata with Kinesis Video Streams](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-meta.html) in the *Amazon Kinesis Video Streams Developer Guide*.

For more information about using IAM service-linked roles with Voice Connectors, see [Using the Amazon Chime SDK Voice Connector service linked role policy](using-service-linked-roles-stream.md). For more information about using Amazon CloudWatch with the Amazon Chime SDK, see [Logging and monitoring in the Amazon Chime SDK](monitoring-overview.md).

When you enable media streaming for your Voice Connector, the Amazon Chime SDK creates an IAM service-linked role called AWSServiceRoleForAmazonChimeVoiceConnector. If you have configured call detail record logging for Voice Connectors in the Amazon Chime SDK console, streaming detail records are sent to your configured Amazon S3 bucket. For more information, see [Amazon Chime SDK Voice Connector streaming detail records](manage-global.md#vc-sdr).

## Starting media streaming
<a name="start-kinesis"></a>

You use the Amazon Chime SDK console to start media streaming for a Voice Connector.

**To start media streaming**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector.

1. Choose the **Streaming** tab.

1. In the **Details** section, under **Sending to Kinesis Video Streams**, choose **Start**.

1. Under **Data retention period**, choose **Retain data for**, and enter a retention period.

1. Choose **Save**.

You use the Amazon Chime SDK console to turn off media streaming. If you no longer need to use media streaming for any of your Voice Connectors, we recommend that you also delete the related service-linked role. For more information, see [Deleting a service-linked role for Amazon Chime SDK Voice Connectors](using-service-linked-roles-stream.md#delete-service-linked-role-stream).

**To stop media streaming for your Voice Connector**

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Choose the name of the Voice Connector.

1. Choose the **Streaming** tab.

1. In the **Details** section, under **Sending to Kinesis Video Streams**, choose **Stop**.

1. Choose **Save**.

## SIP-based media recording and network-based recording compatibility
<a name="siprec"></a>

You can use an Amazon Chime SDK Voice Connector to stream audio media to Kinesis Video Streams. You can stream from a SIP-based media recording (SIPREC) compatible voice infrastructure or the network-based recording (NBR) feature associated with Cisco Unified Border Element (CUBE).

**Note**
A maximum of two audio streams per recording session is supported.

You must have a Private Branch Exchange (PBX), Session Border Controller (SBC), or contact center that supports the SIPREC protocol or NBR feature. The PBX or SBC must be able to send signaling and media to AWS public IP addresses. For more information, see [Before you begin](voice-connectors.md#vc-prereq).

**To set up streaming of RTP audio streams forked with SIPREC or NBR**

1. Create a Voice Connector. For more information, see [Creating an Amazon Chime SDK Voice Connector](create-voicecon.md).

1. Start media streaming for your Amazon Chime SDK Voice Connector. For more information, see [Starting media streaming](#start-kinesis).

1. Open the Amazon Chime SDK console at [https://console.aws.amazon.com/chime-sdk/home](https://console.aws.amazon.com/chime-sdk/home).

1. In the navigation pane, under **SIP Trunking**, choose **Voice connectors**.

1. Select the Voice Connector and note its **Outbound host name**. For example, `{{abcdef1ghij2klmno3pqr4}}.voiceconnector.chime.aws`.

1. Do one of the following:
   + **For SIPREC** – Configure your PBX, SBC, or other voice infrastructure to fork RTP streams with SIPREC to the **Outbound host name** of your Voice Connector.
   + **For NBR** – Configure your PBX, SBC, or other voice infrastructure to fork RTP streams with NBR to the **Outbound host name** of your Voice Connector. Send an additional header or URI parameter of `X-Voice-Connector-Record-Only` with the value `true` in the `SIP INVITE`.
