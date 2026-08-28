---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/ml-based-analytics.html
---

# Understanding workflows for machine-learning based analytics for the Amazon Chime SDK
<a name="ml-based-analytics"></a>

The following sections describe how to use the machine-learning analytics features provide by Amazon Chime SDK call analytics.

**Note**
If you plan to run multiple machine-learning analytics on the same Kinesis Video Stream, you may need to increase the connection-level limit for `GetMedia` and `GetMediaForFragmentList` for the video stream. For more information, refer to [Kinesis Video Streams limits](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/limits.html) in the *Kinesis Video Streams Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
