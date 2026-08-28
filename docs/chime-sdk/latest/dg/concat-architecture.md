---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/concat-architecture.html
---

# Amazon Chime SDK concatenation pipeline architecture
<a name="concat-architecture"></a>

The following diagram shows the architecture of a media concatenation pipeline.

![Diagram showing the architecture of a media concatenation pipeline.](http://docs.aws.amazon.com/chime-sdk/latest/dg/images/concatenation-pipe-architecture-2.png)

In the diagram, on receiving a [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html) request, the media pipeline control plane starts a media capture pipeline in the media pipeline data plane. The data plane then pushes captured chunks to the capture bucket every 5 seconds. On receiving a [CreateMediaConcatenationPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html) request, the media pipeline control plane waits for the specified media capture pipeline to finish, then starts a media concatenation pipeline in the media pipeline data plane. The data plane then reads the captured chunks in the bucket and pushes the concatenated artifacts to the concatenation bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
