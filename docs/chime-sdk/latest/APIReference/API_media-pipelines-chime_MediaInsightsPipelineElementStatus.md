---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineElementStatus.html
---

# MediaInsightsPipelineElementStatus
<a name="API_media-pipelines-chime_MediaInsightsPipelineElementStatus"></a>

The status of the pipeline element.

## Contents
<a name="API_media-pipelines-chime_MediaInsightsPipelineElementStatus_Contents"></a>

 ** Status **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineElementStatus-Status"></a>
The element's status.
Type: String
Valid Values: `NotStarted | NotSupported | Initializing | InProgress | Failed | Stopping | Stopped | Paused`
Required: No

 ** Type **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineElementStatus-Type"></a>
The type of status.
Type: String
Valid Values: `AmazonTranscribeCallAnalyticsProcessor | VoiceAnalyticsProcessor | AmazonTranscribeProcessor | KinesisDataStreamSink | LambdaFunctionSink | SqsQueueSink | SnsTopicSink | S3RecordingSink | VoiceEnhancementSink`
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaInsightsPipelineElementStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineElementStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineElementStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineElementStatus)
