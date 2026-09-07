---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-architecture.html
---

# Understanding voice analytics architecture for the Amazon Chime SDK
<a name="va-architecture"></a>

The topics in this section provide an overview of the Amazon Chime SDK voice analytics architecture, including the data flows for each feature.

This diagram provides a high-level view of how data flows through voice analytics.

![A diagram showing the high-level data flow through voice analytics.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/va-architecture-kvs.png)

In the diagram:

1. Audio is streamed to a Kinesis Video Stream for a caller and agent. You can use a Kinesis Video Streams producer or Amazon Chime SDK Voice Connector streaming to do this. For more information, see [Understanding workflows for machine-learning based analytics for the Amazon Chime SDK](ml-based-analytics.md) in this guide, and [ Streaming Amazon Chime SDK Voice Connector media to Kinesis](https://docs.aws.amazon.com/chime-sdk/latest/ag/start-kinesis-vc.html) in the *Amazon Chime SDK Administrator Guide*.

1. An application or builder triggers speaker search, voice tone analysis, or both, for the audio stream after the caller consents.

1. During the call, voice analytics sends notifications to a target, either Amazon Simple Queue Service (SQS), Amazon Simple Notification Service (SNS), AWS Lambda, or Amazon Kinesis Data Streams.

In addition, voice analytics provides these tools for managing the data that it generates.

**Voice profiles**
The combination of a voice embedding, the embedding's unique ID, and its expiration date. Voice profiles expire after three years for security reasons, and because voices change over time. To avoid re-creating voice profiles, call the [UpdateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html) API. For more information about expiration dates, see [Understanding data retention for Amazon Chime SDK voice analytics](va-data-retention.md).
To enroll a voice embedding, or to update an enrolled voice embedding, you must call the [CreateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html) or [UpdateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html) APIs within 24 hours after the call ends.

**Voice profile domains**
A collection of voice profiles.
