---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/va-task-result-poll.html
---

# Polling for task results for the Amazon Chime SDK
<a name="va-task-result-poll"></a>

**Important**
By default, voice analytics makes results available for 7 days, then it deletes the data automatically. You must store your task data if you want to use it for a longer time, or to comply with data-retention laws. For more information, see [Understanding data retention for Amazon Chime SDK voice analytics](va-data-retention.md), later in this guide.

Voice analytics tries to ensure at least one delivery of each task result. However, network issues can increase latency. To work around potential problems, or if you prefer synchronous processes, you can use the following APIs in either the [Media pipelines SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Media_Pipelines.html) or the [Voice SDK](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_Operations_Amazon_Chime_SDK_Voice.html):
+  [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetSpeakerSearchTask.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetSpeakerSearchTask.html)
+  [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetVoiceToneAnalysisTask.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetVoiceToneAnalysisTask.html)
**Important**
The `GetVoiceToneAnalysisTask` API only returns a task's status. It doesn't return task results. To see results, use an Amazon SQS, Amazon SNS, or AWS Lambda notification target.

The `GetSpeakerSearchTask` API gets the latest results synchronously for a task ID, delayed messages, or messages that arrive out of order. However, we recommend using notification targets and asynchronous processing. Doing so consumes fewer computing resources.
