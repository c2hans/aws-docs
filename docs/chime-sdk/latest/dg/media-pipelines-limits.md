---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/media-pipelines-limits.html
---

# Understanding the default limits for active Amazon Chime SDK media pipelines
<a name="media-pipelines-limits"></a>

The following table lists the default limits for active media pipelines in each Region. Each type of pipeline counts toward the limit. If you exceed the limit for any Region, the [CreateMediaCapturePipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline.html), [CreateMediaConcatenationPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaConcatenationPipeline.html), and [CreateMediaLiveConnectorPipeline](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaLiveConnectorPipeline.html) APIs will throw **Resource Limit Exceeded** exceptions.

You can use the **Service Quotas** page in the AWS console to adjust your active pipeline limits, or you can contact your [customer support representative](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html). For more information about the Amazon Chime SDK meeting limits, see [Quotas for the Amazon Chime SDK](meetings-sdk.md#mtg-limits).

| Region | Default active pipeline limit |
| --- | --- |
| us-east-1 | 100 |
| us-west-2 | 10 |
| ap-northeast-1 | 10 |
| ap-northeast-2 | 10 |
| ap-south-1 | 10 |
| ap-southeast-1 | 10 |
| ap-southeast-2 | 10 |
| ca-central-1 | 10 |
| eu-central-1 | 10 |
| eu-west-2 | 10 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
