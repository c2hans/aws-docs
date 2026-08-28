---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-tone-flow.html
---

# Sample voice tone analysis workflow for the Amazon Chime SDK
<a name="va-tone-flow"></a>

**Important**
Voice tone analysis involves making predictions on a speaker’s sentiment based on linguistic and tonal information. You must not use sentiment analysis in any manner prohibited by law, including in relation to making decisions about an individual that would produce legal or similarly significant impacts on such individuals (e.g., related to employment, housing, credit worthiness, or financial offers, etc.).

Voice tone analysis analyzes the voices of the people on a call and predicts their sentiment, either `positive`, `negative`, or `neutral`.

The following diagram shows an example workflow for a voice tone analysis. Numbered items below the image describe each step of the process.

**Note**
The diagram assumes you have already configured an Amazon Chime SDK Voice Connector with a call analytics configuration that has a `VoiceAnalyticsProcessor`. For more information, see [Recording Voice Connector calls](record-vc-calls.md).

![A diagram showing the data flow through a voice tone analysis.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/voice-tone-workflow-v2.png)

In the diagram:

1. A caller dials in using a phone number assigned to an Amazon Chime SDK Voice Connector. Or, an agent uses a Voice Connector number to make an outbound call.

1. The Voice Connector service creates a transaction ID and associates it with the call.

1. Your application—such as an Interactive Voice Response system—or agent provides notice to the caller regarding call recording and the use of voice embeddings for voice analytics and seeks their consent to participate.

1. Assuming your application subscribes to EventBridge events, your application calls the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API with the with the media insights pipeline configuration and Kinesis Video Stream ARNs for the Voice Connector call.

   For more information about using EventBridge, refer to [Understanding workflows for machine-learning based analytics for the Amazon Chime SDK](ml-based-analytics.md).

1. Once the caller provides consent, your application or agent can call the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask.html) API through the [ Voice SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) if you have a Voice Connector and a transaction ID. Or, if you have a media insights pipeline ID instead of a transaction ID, you call the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html) API in the [ Media pipelines SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html).

   Once the caller provides consent, your application or agent calls the `StartSpeakerSearchTask` API. You must pass the Voice Connector ID, transaction ID, and voice profile domain ID to the API. A speaker search task ID is returned to identify the asynchronous task.

1. The user speaks throughout the call.

1. The agent speaks throughout the call.

1. Every 5 seconds, the media insights pipeline uses a machine learning model to analyze the last 30 seconds of speech and predict the caller's tone for that interval, and for the entire call from the time when `StartVoiceToneAnalysisTask` was first called.

1. The media insights pipeline sends a notification with that information to the configured notification targets. You can identify the notification based on its stream ARN and channel ID. For more information, refer to [Understanding notifications for the Amazon Chime SDK](va-notification-targets.md), later in this section.

1. Repeat steps 9 and 10 until the call ends.

1. At the end of the call, the media insights pipeline sends one final notification with the current average tone prediction for the last 30 seconds, plus the average tone of the entire call.

1. Your application calls the [GetVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceToneAnalysisTask.html) API as needed to get the latest status of the voice tone analysis task.
**Note**
The `GetVoiceToneAnalysisTask` API doesn't stream the tone data.

**Note**
The [GetVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceToneAnalysisTask.html) API doesn't return voice tone data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
