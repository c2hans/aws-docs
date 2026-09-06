---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/pausing-and-resuming-call-analytics-pipelines.html
---

# Pausing and resuming call analytics pipelines for the Amazon Chime SDK
<a name="pausing-and-resuming-call-analytics-pipelines"></a>

To pause and resume a media insights pipeline, invoke the [UpdateMediaInsightsPipelineStatus](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineStatus.html) API with a `Pause` or `Resume` action. To do so, you pass either the pipeline's ID or ARN in the `Identifier` field.

**Warning**
Warning: The `UpdateMediaInsightsPipelineStatus` API *stops* all voice analytics tasks started on a media insights pipeline when a `Pause` status is provided. When the `Resume` status is provided, tasks are not resumed and must be started again. You must provide all necessary notices and obtain all necessary consents from the speakers prior to re-starting the tasks. For more information, refer to [StartSpeakerSearchTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html) or [StartVoiceToneAnalysisTask](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartVoiceToneAnalysisTask.html), in the *Amazon Chime SDK API Reference*.

While paused, the pipeline stops sending media to processors and writing data to Kinesis Data Streams and data warehouses. When you `Resume` the pipeline, the service sends the latest chunk available on the stream. Media insights pipelines stop automatically when paused for more than 2 hours. **Please note**, call recording does not support pause and resume.

 For more, see the following topics:
+ [Using EventBridge notifications](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-eventbridge-notifications.html).
+ [StartSelectorType.NOW](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_StartSelector.html#KinesisVideo-Type-dataplane_StartSelector-StartSelectorType) in the *Amazon Kinesis Video Streams Developer Guide*.
+ [Amazon Transcribe call analytics processor](https://docs.aws.amazon.com/chime-sdk/latest/dg/ca-processors-sinks.html#ca-transcribe-analytics-processor).

**Note**
 You are billed for call analytics usage while a pipeline is paused. However, you aren't billed for AWS services accessed via the resource access role, such as Amazon Transcribe and Amazon Kinesis.

 You can read, update, and delete existing call analytics configurations using [GetMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaInsightsPipelineConfiguration.html), [UpdateMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_UpdateMediaInsightsPipelineConfiguration.html), and [DeleteMediaInsightsPipelineConfiguration](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaInsightsPipelineConfiguration.html) APIs by passing the configuration name or ARN in the Identifier field.

 You can list configurations by calling the [ListMediaInsightsPipelineConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_media-pipelines-chime_ListMediaInsightsPipelineConfiguration.html) API.
