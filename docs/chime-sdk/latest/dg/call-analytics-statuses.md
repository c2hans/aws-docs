---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/call-analytics-statuses.html
---

# Understanding the call analytics statuses for the Amazon Chime SDK
<a name="call-analytics-statuses"></a>

Media insights pipelines track a set of statuses when you do one or both of the following:
+ Use multiple machine-learning processing elements, such as Amazon Transcribe and voice analytics.
+ Enable call recording with or without machine learning processing.

To get pipeline and element statuses, use the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipeline.html) API and [EventBridge notifications](using-eventbridge-notifications.md).

To get statuses for voice analytics tasks, use the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetSpeakerSearchTask.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetSpeakerSearchTask.html) and [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetVoiceToneAnalysisTask.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetVoiceToneAnalysisTask.html) APIs, and [voice analytics notification targets](va-notification-targets.md).

Media insights pipelines track the following statuses.
+ **Pipeline status** – The overall status of a call analytics pipeline, also known as a media insights pipeline. This is determined by the element statuses.
+ **Element status** – The processing status for the individual media insights pipeline configuration elements.
+ **Task status** – The processing status for a media insights pipeline task started for voice analytics. The `VoiceAnalyticsProcessor` element status is determined by the task statuses. No other element in a call analytics pipeline has a task status.

  For more information about media insights pipeline tasks, refer to [Understanding call analytics terminology for the Amazon Chime SDK](ca-terms-concepts.md), earlier in this guide.

Not all media insights configuration element types have element statuses. In general, only media insights configuration elements of the “processor” type have an element status. Also, the Amazon S3 recording and voice enhancement sinks have processor statuses. Specifically, element statuses exist for the following media insights configuration element types:
+ `AmazonTranscribeProcessor`
+ `AmazonTranscribeCallAnalyticsProcessor`
+ `S3RecordingSink`
+ `VoiceAnalyticsProcessor`
+ `VoiceEnhancementSink`

The pipeline status is determined by the element statuses as follows:

| Pipeline status | Condition |
| --- | --- |
| NotStarted | All element statuses are not started. |
| Initializing | At least one element is initializing and the rest are not started. |
| InProgress | At least one element is in progress.  |
| Failed | At least one element has failed and the remaining elements are stopped. |
| Stopping | Refer to [Managing call analytics pipelines for the Amazon Chime SDK](managing-call-analytics-pipelines.md) for a complete list of stopping conditions. |
| Stopped | All elements are stopped. |
| Paused | All elements are paused. |

Unlike other element statuses, the `VoiceAnalyticsProcessor` element has a few nuances. As mentioned earlier, the `VoiceAnalyticsProcessor` element status, corresponding to the Amazon Chime SDK voice analytics feature, is determined by the task statuses created from [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartSpeakerSearchTask.html) and [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartVoiceToneAnalysisTask.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_StartVoiceToneAnalysisTask.html).
+ The `VoiceAnalyticsProcessor`’s element status begins in a `NotStarted` state, because `StartSpeakerSearchTask` and `StartVoiceToneAnalysisTask` must be called before the element can change the status to `Initializing`, and then `InProgress`.
+ The `VoiceAnalyticsProcessor` stays `InProgress` as long as one task is started and a [stop condition](managing-call-analytics-pipelines.md) is not met while the task is running.
+ Even though the `VoiceAnalyticsProcessor` may be `InProgress`, you will only be charged for the duration that the tasks process.
+ To clean-up media insights pipelines that had at least one voice analytics task started and no more tasks running, you must call `DeleteMediaPipeline`.
+ As long as a task runs or completes successfully, the `VoiceAnalyticsProcessor` element status remains at `InProgress`.
