---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/managing-call-analytics-pipelines.html
---

# Managing call analytics pipelines for the Amazon Chime SDK
<a name="managing-call-analytics-pipelines"></a>

 You can read, list, and delete media insights pipelines by calling the [GetMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaPipeline.html), [ListMediaPipelines](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaPipelines.html), and [DeleteMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html) APIs.

 Media insights pipelines stop if any of the following conditions are met:
+ Any of the Kinesis Video streams send no new fragments to an `InProgress` pipeline for 15 seconds.
+ The [DeleteMediaPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html) API is called.
+ The media insights pipeline was created more than 8 hours ago. The system stops the pipeline automatically.
+ The media insights pipeline is paused for more than 2 hours. The system stops the pipeline automatically.
