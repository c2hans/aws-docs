---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/monitoring-with-cloudwatch.html
---

# Monitoring call analytics pipelines for the Amazon Chime SDK with Amazon CloudWatch
<a name="monitoring-with-cloudwatch"></a>

You can use Amazon CloudWatch to monitor Amazon Chime SDK call analytics pipelines. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Topics**
+ [Prerequisites](#monitoring-prereqs)
+ [Call analytics metrics](#monitoring-metrics)
+ [CloudWatch dimensions for pipeline metrics](#monitoring-dimensions)

## Prerequisites
<a name="monitoring-prereqs"></a>

To use CloudWatch metrics, you must first create a media pipelines service-linked role that grants permissions to publish service metrics to Amazon CloudWatch. For more information about the service-linked role, see [Creating a service-linked role for Amazon Chime SDK media pipelines](create-pipeline-role.md), in this guide.

## Call analytics metrics
<a name="monitoring-metrics"></a>

Amazon Chime SDK call analytics publishes the following metrics to the `AWS/ChimeSDK` namespace for media insights pipelines that you create by using a media insights configuration.

| Metric | Description |
| --- | --- |
| `MediaInsightsPipelineCreated` | The media insights pipeline was successfully created.<br />Unit: Count |
| `MediaInsightsPipelineStopped` | The media insights pipeline was successfully stopped.<br />Unit: Count |
| `MediaInsightsPipelineFailed` | The media insights pipeline failed.<br />Unit: Count |
| `MediaInsightsPipelineDuration` | The time between pipeline creation and Stopped/Failed.<br />Unit: Seconds |
| `MediaInsightsPipelineBillingDuration` | The billing duration of the media insights pipeline.<br />Unit: Count |
| `RecordingFileSize` | The size of the recording file.<br />Unit: Bytes |
| `RecordingDuration ` | The duration of the recording.<br />Unit: Seconds |

## CloudWatch dimensions for pipeline metrics
<a name="monitoring-dimensions"></a>

The following table lists the CloudWatch dimensions that you can use to monitor call analytics pipelines.

| Dimension | Description |
| --- | --- |
| `MediaInsightsPipelineConfigurationId` | The ID of the media insights pipeline configuration. |
| `MediaInsightsPipelineConfigurationName` | The name of the media insights pipeline configuration. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
