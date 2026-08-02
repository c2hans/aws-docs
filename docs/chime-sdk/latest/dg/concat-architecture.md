---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/concat-architecture.html
---

# Amazon Chime SDK concatenation pipeline architecture
<a name="concat-architecture"></a>

The following diagram shows the architecture of a media concatenation pipeline.

![Diagram showing the architecture of a media concatenation pipeline.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/concatenation-pipe-architecture-2.png)

In the diagram, on receiving a [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html) request, the media pipeline control plane starts a media capture pipeline in the media pipeline data plane. The data plane then pushes captured chunks to the capture bucket every 5 seconds. On receiving a [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html) request, the media pipeline control plane waits for the specified media capture pipeline to finish, then starts a media concatenation pipeline in the media pipeline data plane. The data plane then reads the captured chunks in the bucket and pushes the concatenated artifacts to the concatenation bucket.
