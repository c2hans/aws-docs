---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-partitionedprefix.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket PartitionedPrefix
<a name="aws-properties-s3-bucket-partitionedprefix"></a>

Amazon S3 keys for log objects are partitioned in the following format:

 `[DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`

PartitionedPrefix defaults to EventTime delivery when server access logs are delivered.

## Syntax
<a name="aws-properties-s3-bucket-partitionedprefix-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-partitionedprefix-syntax.json"></a>

```
{
  "[PartitionDateSource](#cfn-s3-bucket-partitionedprefix-partitiondatesource)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-partitionedprefix-syntax.yaml"></a>

```
  [PartitionDateSource](#cfn-s3-bucket-partitionedprefix-partitiondatesource): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-partitionedprefix-properties"></a>

`PartitionDateSource`  <a name="cfn-s3-bucket-partitionedprefix-partitiondatesource"></a>
Specifies the partition date source for the partitioned prefix. `PartitionDateSource` can be `EventTime` or `DeliveryTime`.
For `DeliveryTime`, the time in the log file names corresponds to the delivery time for the log files.
 For `EventTime`, The logs delivered are for a specific day only. The year, month, and day correspond to the day on which the event occurred, and the hour, minutes and seconds are set to 00 in the key.
*Required*: No
*Type*: String
*Allowed values*: `EventTime | DeliveryTime`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
