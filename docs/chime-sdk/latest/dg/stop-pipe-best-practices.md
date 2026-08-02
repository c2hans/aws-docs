---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/stop-pipe-best-practices.html
---

# Best practices for stopping Amazon Chime SDK media pipelines
<a name="stop-pipe-best-practices"></a>

As a best practice for stopping media pipelines, call the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaPipeline.html) API. The API allows you to delete media capture and media live connector pipelines. You can also call the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html) API to delete media capture pipelines. All media pipelines stop when the meeting ends.
