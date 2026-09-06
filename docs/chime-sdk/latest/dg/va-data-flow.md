---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-data-flow.html
---

# Understanding speaker search workflow for the Amazon Chime SDK
<a name="va-data-flow"></a>

In this section, we show you an example data and program flow for an Amazon Chime SDK speaker search analysis.

The speaker search function involves the creation of a voice embedding, which can be used compare the voice of a caller against previously stored voice data. The collection, use, storage, and retention of biometric identifiers and biometric information in the form of a digital voiceprint may require the caller's informed consent via a written release. Such consent is required under various state laws, including biometrics laws in Illinois, Texas, Washington and other state privacy laws. Before using the speaker search feature, you must provide all notices, and obtain all consents as required by applicable law, and under the [AWS service terms](https://aws.amazon.com/service-terms/) governing your use of the feature.

The following diagram shows an example data flow through a speaker search analysis task. The numbered descriptions below the diagram describe each step of the process. The diagram assumes you have already configured an Amazon Chime SDK Voice Connector with a call analytics configuration that has a `VoiceAnalyticsProcessor`. For more information, see [Recording Voice Connector calls](record-vc-calls.md).

![A diagram showing the data flow through a speaker search analysis.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/speaker-search-workflow-2.png)

1. You or a system administrator create a voice profile domain for storing voice embeddings and voice profiles. For more information about creating voice profile domains, see [Creating voice profile domains](https://docs.aws.amazon.com/chime-sdk/latest/ag/create-vp-domain.html), in the *Amazon Chime SDK Administrator Guide*. You can also use the [CreateVoiceProfileDomain](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfileDomain.html) API.

1. A caller dials in using a phone number assigned to an Amazon Chime SDK Voice Connector. Or, an agent uses a Voice Connector number to make an outbound call.

1. The Amazon Chime SDK Voice Connector service creates a transaction ID and associates it with the call.

1. Assuming your application subscribes to EventBridge events, your application calls the [CreateMediaInsightsPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaInsightsPipeline.html) API with the with the media insights pipeline configuration and Kinesis Video Stream ARNs for the Voice Connector call.

   For more information about using EventBridge, refer to [Understanding workflows for machine-learning based analytics for the Amazon Chime SDK](ml-based-analytics.md).

1. Your application—such as an Interactive Voice Response system—or agent provides notice to the caller regarding call recording and the use of voice embeddings for voice analytics and seeks their consent to participate.

1. Once the caller provides consent, your application or agent can call the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_StartSpeakerSearchTask.html) API through the [ Voice SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html) if you have a Voice Connector and a transaction ID. Or, if you have a media insights pipeline ID instead of a transaction ID, you call the [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html) API in the [ Media pipelines SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html).

   Once the caller provides consent, your application or agent calls the `StartSpeakerSearchTask` API. You must pass the Voice Connector ID, transaction ID, and voice profile domain ID to the API. A speaker search task ID is returned to identify the asynchronous task.
**Note**
Before invoking the `StartSpeakerSearchTask` API in either of the SDKs, you must provide any necessary notices, and obtain any necessary consents, as required by law and under the [AWS service terms](https://aws.amazon.com/service-terms/).

1. The system accumulates 10 seconds of the caller's voice. The caller must speak for at least that amount of time. The system doesn't capture or analyze silence.

1. The media insights pipeline compares the speech to the voice profiles in the domain and lists top 10 high confidence matches. If it doesn't find a match, the Voice Connector creates a voice profile.

1. The media insights pipeline service sends a notification event to the configured notification targets.

1. The caller continues speaking and provides an additional 10 seconds of non-silence speech.

1. The media insights pipeline generates an enrollment voice embedding that you can use to create a voice profile or update an existing voice profile.

1. The media insights pipeline sends a `VoiceprintGenerationSuccessful` notification to the configured notification targets.

1. Your application calls the [CreateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceProfile.html) or [UpdateVoiceProfile](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceProfile.html) APIs to create or update the profile.

1. Your application calls the [GetSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSpeakerSearchTask.html) API as needed to get the latest status of the speaker search task.
