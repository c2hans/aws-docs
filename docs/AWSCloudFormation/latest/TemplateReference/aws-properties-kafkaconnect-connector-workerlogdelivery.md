---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-workerlogdelivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector WorkerLogDelivery
<a name="aws-properties-kafkaconnect-connector-workerlogdelivery"></a>

Workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

## Syntax
<a name="aws-properties-kafkaconnect-connector-workerlogdelivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-workerlogdelivery-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs)" : {{CloudWatchLogsLogDelivery}},
  "[Firehose](#cfn-kafkaconnect-connector-workerlogdelivery-firehose)" : {{FirehoseLogDelivery}},
  "[S3](#cfn-kafkaconnect-connector-workerlogdelivery-s3)" : {{S3LogDelivery}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-workerlogdelivery-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs): {{
    CloudWatchLogsLogDelivery}}
  [Firehose](#cfn-kafkaconnect-connector-workerlogdelivery-firehose): {{
    FirehoseLogDelivery}}
  [S3](#cfn-kafkaconnect-connector-workerlogdelivery-s3): {{
    S3LogDelivery}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-workerlogdelivery-properties"></a>

`CloudWatchLogs`  <a name="cfn-kafkaconnect-connector-workerlogdelivery-cloudwatchlogs"></a>
Details about delivering logs to Amazon CloudWatch Logs.
*Required*: No
*Type*: [CloudWatchLogsLogDelivery](aws-properties-kafkaconnect-connector-cloudwatchlogslogdelivery.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Firehose`  <a name="cfn-kafkaconnect-connector-workerlogdelivery-firehose"></a>
Details about delivering logs to Amazon Kinesis Data Firehose.
*Required*: No
*Type*: [FirehoseLogDelivery](aws-properties-kafkaconnect-connector-firehoselogdelivery.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3`  <a name="cfn-kafkaconnect-connector-workerlogdelivery-s3"></a>
Details about delivering logs to Amazon S3.
*Required*: No
*Type*: [S3LogDelivery](aws-properties-kafkaconnect-connector-s3logdelivery.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
