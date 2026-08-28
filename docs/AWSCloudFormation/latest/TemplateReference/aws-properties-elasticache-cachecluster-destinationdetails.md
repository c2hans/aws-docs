---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-cachecluster-destinationdetails.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::CacheCluster DestinationDetails
<a name="aws-properties-elasticache-cachecluster-destinationdetails"></a>

Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.

## Syntax
<a name="aws-properties-elasticache-cachecluster-destinationdetails-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-cachecluster-destinationdetails-syntax.json"></a>

```
{
  "[CloudWatchLogsDetails](#cfn-elasticache-cachecluster-destinationdetails-cloudwatchlogsdetails)" : {{CloudWatchLogsDestinationDetails}},
  "[KinesisFirehoseDetails](#cfn-elasticache-cachecluster-destinationdetails-kinesisfirehosedetails)" : {{KinesisFirehoseDestinationDetails}}
}
```

### YAML
<a name="aws-properties-elasticache-cachecluster-destinationdetails-syntax.yaml"></a>

```
  [CloudWatchLogsDetails](#cfn-elasticache-cachecluster-destinationdetails-cloudwatchlogsdetails): {{
    CloudWatchLogsDestinationDetails}}
  [KinesisFirehoseDetails](#cfn-elasticache-cachecluster-destinationdetails-kinesisfirehosedetails): {{
    KinesisFirehoseDestinationDetails}}
```

## Properties
<a name="aws-properties-elasticache-cachecluster-destinationdetails-properties"></a>

`CloudWatchLogsDetails`  <a name="cfn-elasticache-cachecluster-destinationdetails-cloudwatchlogsdetails"></a>
The configuration details of the CloudWatch Logs destination. Note that this field is marked as required but only if CloudWatch Logs was chosen as the destination.
*Required*: No
*Type*: [CloudWatchLogsDestinationDetails](aws-properties-elasticache-cachecluster-cloudwatchlogsdestinationdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisFirehoseDetails`  <a name="cfn-elasticache-cachecluster-destinationdetails-kinesisfirehosedetails"></a>
The configuration details of the Kinesis Data Firehose destination. Note that this field is marked as required but only if Kinesis Data Firehose was chosen as the destination.
*Required*: No
*Type*: [KinesisFirehoseDestinationDetails](aws-properties-elasticache-cachecluster-kinesisfirehosedestinationdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
