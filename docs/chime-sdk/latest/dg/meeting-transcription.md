---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html
---

# Using Amazon Chime SDK live transcription
<a name="meeting-transcription"></a>

You use Amazon Chime SDK live transcription to generate live, user-attributed transcripts of your meetings. Amazon Chime SDK live transcription integrates with the Amazon Transcribe and Amazon Transcribe Medical services to generate transcripts of Amazon Chime SDK meetings while they're in progress.

Amazon Chime SDK live transcription processes each user’s audio separately for improved accuracy in multi-speaker scenarios. The Amazon Chime SDK uses its active talker algorithm to select the top two active talkers, and then sends their audio to Amazon Transcribe, in separate channels, via a single stream. Meeting participants receive user-attributed transcriptions via Amazon Chime SDK data messages. You can use transcriptions in a variety of ways, such as displaying subtitles, creating meeting transcripts, or using the transcriptions for content analysis.

Live transcription uses one stream to Amazon Transcribe for the duration of the meeting transcription. Standard Amazon Transcribe and Amazon Transcribe Medical costs apply. For more information, refer to [Amazon Transcribe Pricing](https://aws.amazon.com/transcribe/pricing/). For questions about usage or billing, contact your AWS account manager.

**Important**
By default, Amazon Transcribe may use and store audio content processed by the service to develop and improve AWS AI/ML services as further described in section 50 of the [AWS Service Terms](https://aws.amazon.com/service-terms/). Using Amazon Transcribe may be subject to federal and state laws or regulations regarding the recording or interception of electronic communications. It is your and your end users’ responsibility to comply with all applicable laws regarding the recording, including properly notifying all participants in a recorded session or communication that the session or communication is being recorded, and obtaining all necessary consents. You can opt out from AWS using audio content to develop and improve AWS AI/ML services by configuring an AI services opt out policy using AWS Organizations.

**Topics**
+ [System architecture](#sys-architecture)
+ [Billing and usage](#billing-and-usage)
+ [Configuring your account for Amazon Chime SDK live transcription](configure-transcribe.md)
+ [Choosing Amazon Chime SDK live transcription options](transcription-options.md)
+ [Starting and stopping Amazon Chime SDK live transcription](initiate-transcription.md)
+ [Amazon Chime SDK live transcription parameters](#transcription-parameters)
+ [Understanding Amazon Chime SDK live transcription events](transcription-events.md)
+ [Understanding Amazon Chime SDK live transcription messages](process-msgs.md)
+ [Processing a received Amazon Chime SDK live transcript event](delivery-examples.md)
+ [Parsing Amazon Chime SDK transcripts](parse-transcripts.md)

## System architecture
<a name="sys-architecture"></a>

The Amazon Chime SDK creates real-time meeting transcriptions, without audio leaving the AWS network, via a service-side integration with your Amazon Transcribe or Amazon Transcribe Medical account. For improved accuracy, users’ audio is processed separately, then mixed into the meeting. The Amazon Chime SDK uses its active talker algorithm to select the top two active talkers, and then sends their audio to Amazon Transcribe or Amazon Transcribe Medical in separate channels via a single stream. For reduced latency, user-attributed transcriptions are sent directly to every meeting participant via data messages. When using a media pipeline to capture meeting audio, the meeting’s transcription information is also captured.

![A diagram showing the data flow of meeting transcription.](https://docs.aws.amazon.com/chime-sdk/latest/dg/images/transcription-architecture.png)

## Billing and usage
<a name="billing-and-usage"></a>

Live transcription uses one stream to Amazon Transcribe or Amazon Transcribe Medical for the duration of the meeting transcription. Standard Amazon Transcribe and Amazon Transcribe Medical costs apply. For more information, see [Amazon Transcribe Pricing](https://aws.amazon.com/transcribe/pricing/).. For questions about usage or billing, contact your AWS account manager.

## Amazon Chime SDK live transcription parameters
<a name="transcription-parameters"></a>

The Amazon Transcribe and Amazon Transcribe Medical APIs offer a number of parameters when initiating streaming transcription, such as [StartStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartStreamTranscription.html) and [StartMedicalStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartMedicalStreamTranscription.html). You can use t hose parameters in the `StartMeetingTranscription` API unless the Amazon Chime SDK predetermines the parameter’s value. For example, the `MediaEncoding` and `MediaSampleRateHertz` parameters are not available because the Amazon Chime SDK sets them automatically.

Amazon Transcribe and Amazon Transcribe Medical validate the parameters, and that allows you to use new parameter values as soon as they become available. For example, if Amazon Transcribe Medical launches support for a new language, you only need to specify the new language value in the `LanguageCode` parameter.
