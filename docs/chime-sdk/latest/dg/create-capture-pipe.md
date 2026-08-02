---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/create-capture-pipe.html
---

# Creating the Amazon Chime SDK media capture pipeline
<a name="create-capture-pipe"></a>

After you create and configure your Amazon S3 bucket or buckets, you create a media capture pipeline.

**To create a media capture pipeline**
+ Call the [https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html) API.

  Use the bucket ARN as the `SinkArn` parameter.

Once successful, the Amazon Chime SDK creates an attendee that joins and captures the meeting.

After you create a media capture pipeline and set its permissions, you create a media concatenation pipeline to concatenate the 5-second media chunks into a single file. For more information, refer to [Creating media concatenation pipelines for Amazon Chime SDK meetings](create-concat-pipe.md), later in this section.
