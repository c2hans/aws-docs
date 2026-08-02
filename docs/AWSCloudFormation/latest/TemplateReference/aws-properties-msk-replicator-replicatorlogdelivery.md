---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-replicatorlogdelivery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator ReplicatorLogDelivery
<a name="aws-properties-msk-replicator-replicatorlogdelivery"></a>

Configuration for replicator log delivery.

## Syntax
<a name="aws-properties-msk-replicator-replicatorlogdelivery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-replicatorlogdelivery-syntax.json"></a>

```
{
  "[CloudWatchLogs](#cfn-msk-replicator-replicatorlogdelivery-cloudwatchlogs)" : {{CloudWatchLogs}},
  "[Firehose](#cfn-msk-replicator-replicatorlogdelivery-firehose)" : {{Firehose}},
  "[S3](#cfn-msk-replicator-replicatorlogdelivery-s3)" : {{S3}}
}
```

### YAML
<a name="aws-properties-msk-replicator-replicatorlogdelivery-syntax.yaml"></a>

```
  [CloudWatchLogs](#cfn-msk-replicator-replicatorlogdelivery-cloudwatchlogs): {{
    CloudWatchLogs}}
  [Firehose](#cfn-msk-replicator-replicatorlogdelivery-firehose): {{
    Firehose}}
  [S3](#cfn-msk-replicator-replicatorlogdelivery-s3): {{
    S3}}
```

## Properties
<a name="aws-properties-msk-replicator-replicatorlogdelivery-properties"></a>

`CloudWatchLogs`  <a name="cfn-msk-replicator-replicatorlogdelivery-cloudwatchlogs"></a>
Configuration for CloudWatch Logs delivery.
*Required*: No
*Type*: [CloudWatchLogs](aws-properties-msk-replicator-cloudwatchlogs.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Firehose`  <a name="cfn-msk-replicator-replicatorlogdelivery-firehose"></a>
Configuration for Firehose delivery.
*Required*: No
*Type*: [Firehose](aws-properties-msk-replicator-firehose.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-msk-replicator-replicatorlogdelivery-s3"></a>
Configuration for S3 delivery.
*Required*: No
*Type*: [S3](aws-properties-msk-replicator-s3.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
