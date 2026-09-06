---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement.html
---

# MediaInsightsPipelineConfigurationElement
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement"></a>

An element in a media insights pipeline configuration.

## Contents
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement_Contents"></a>

 ** Type **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-Type"></a>
The element type.
Type: String
Valid Values: `AmazonTranscribeCallAnalyticsProcessor | VoiceAnalyticsProcessor | AmazonTranscribeProcessor | KinesisDataStreamSink | LambdaFunctionSink | SqsQueueSink | SnsTopicSink | S3RecordingSink | VoiceEnhancementSink`
Required: Yes

 ** AmazonTranscribeCallAnalyticsProcessorConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-AmazonTranscribeCallAnalyticsProcessorConfiguration"></a>
The analytics configuration settings for transcribing audio in a media insights pipeline configuration element.
Type: [AmazonTranscribeCallAnalyticsProcessorConfiguration](API_media-pipelines-chime_AmazonTranscribeCallAnalyticsProcessorConfiguration.md) object
Required: No

 ** AmazonTranscribeProcessorConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-AmazonTranscribeProcessorConfiguration"></a>
The transcription processor configuration settings in a media insights pipeline configuration element.
Type: [AmazonTranscribeProcessorConfiguration](API_media-pipelines-chime_AmazonTranscribeProcessorConfiguration.md) object
Required: No

 ** KinesisDataStreamSinkConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-KinesisDataStreamSinkConfiguration"></a>
The configuration settings for the Kinesis Data Stream Sink in a media insights pipeline configuration element.
Type: [KinesisDataStreamSinkConfiguration](API_media-pipelines-chime_KinesisDataStreamSinkConfiguration.md) object
Required: No

 ** LambdaFunctionSinkConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-LambdaFunctionSinkConfiguration"></a>
The configuration settings for the AWS Lambda sink in a media insights pipeline configuration element.
Type: [LambdaFunctionSinkConfiguration](API_media-pipelines-chime_LambdaFunctionSinkConfiguration.md) object
Required: No

 ** S3RecordingSinkConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-S3RecordingSinkConfiguration"></a>
The configuration settings for the Amazon S3 recording bucket in a media insights pipeline configuration element.
Type: [S3RecordingSinkConfiguration](API_media-pipelines-chime_S3RecordingSinkConfiguration.md) object
Required: No

 ** SnsTopicSinkConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-SnsTopicSinkConfiguration"></a>
The configuration settings for an SNS topic sink in a media insights pipeline configuration element.
Type: [SnsTopicSinkConfiguration](API_media-pipelines-chime_SnsTopicSinkConfiguration.md) object
Required: No

 ** SqsQueueSinkConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-SqsQueueSinkConfiguration"></a>
The configuration settings for an SQS queue sink in a media insights pipeline configuration element.
Type: [SqsQueueSinkConfiguration](API_media-pipelines-chime_SqsQueueSinkConfiguration.md) object
Required: No

 ** VoiceAnalyticsProcessorConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-VoiceAnalyticsProcessorConfiguration"></a>
The voice analytics configuration settings in a media insights pipeline configuration element.
Type: [VoiceAnalyticsProcessorConfiguration](API_media-pipelines-chime_VoiceAnalyticsProcessorConfiguration.md) object
Required: No

 ** VoiceEnhancementSinkConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationElement-VoiceEnhancementSinkConfiguration"></a>
The configuration settings for voice enhancement sink in a media insights pipeline configuration element.
Type: [VoiceEnhancementSinkConfiguration](API_media-pipelines-chime_VoiceEnhancementSinkConfiguration.md) object
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfigurationElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfigurationElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfigurationElement)
