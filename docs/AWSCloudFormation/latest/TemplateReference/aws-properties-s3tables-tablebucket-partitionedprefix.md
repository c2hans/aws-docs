---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3tables-tablebucket-partitionedprefix.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket PartitionedPrefix
<a name="aws-properties-s3tables-tablebucket-partitionedprefix"></a>

Amazon S3 keys for log objects are partitioned in the following format: `[TargetPrefix][SourceAccountId]/[SourceRegion]/[SourceTableBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`

## Syntax
<a name="aws-properties-s3tables-tablebucket-partitionedprefix-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3tables-tablebucket-partitionedprefix-syntax.json"></a>

```
{
  "[PartitionDateSource](#cfn-s3tables-tablebucket-partitionedprefix-partitiondatesource)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3tables-tablebucket-partitionedprefix-syntax.yaml"></a>

```
  [PartitionDateSource](#cfn-s3tables-tablebucket-partitionedprefix-partitiondatesource): {{String}}
```

## Properties
<a name="aws-properties-s3tables-tablebucket-partitionedprefix-properties"></a>

`PartitionDateSource`  <a name="cfn-s3tables-tablebucket-partitionedprefix-partitiondatesource"></a>
The date to use for the log object key partitions. Valid values are `EventTime`, the time that the requests in the log were made, and `DeliveryTime`, the time that the log was delivered.
*Required*: Yes
*Type*: String
*Allowed values*: `EventTime | DeliveryTime`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
