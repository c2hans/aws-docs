---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-media.html
---

# Media services
<a name="sns-event-sources-media"></a>

The following table describes how Amazon SNS integrates with Amazon Elastic Transcoder to send notifications when media transcoding jobs change status, enabling you to efficiently monitor and manage the conversion of media files stored in Amazon S3 into formats suitable for consumer playback devices.

This integration helps you streamline media processing workflows by providing real-time alerts on job status.

| AWS service | Benefit of using with Amazon SNS |
| --- | --- |
| [Amazon Elastic Transcoder](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/introduction.html) – Lets you convert media files that you stored in Amazon S3 into media files in the formats required by consumer playback devices. | Receive notifications when jobs change status. For more information, see [Notifications of job status](https://docs.aws.amazon.com/elastictranscoder/latest/developerguide/notifications.html) in the *Amazon Elastic Transcoder Developer Guide*. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
