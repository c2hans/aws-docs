---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-flowlog-destinationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FlowLog DestinationOptions
<a name="aws-properties-ec2-flowlog-destinationoptions"></a>

Describes the destination options for a flow log.

## Syntax
<a name="aws-properties-ec2-flowlog-destinationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-flowlog-destinationoptions-syntax.json"></a>

```
{
  "[FileFormat](#cfn-ec2-flowlog-destinationoptions-fileformat)" : {{String}},
  "[HiveCompatiblePartitions](#cfn-ec2-flowlog-destinationoptions-hivecompatiblepartitions)" : {{Boolean}},
  "[PerHourPartition](#cfn-ec2-flowlog-destinationoptions-perhourpartition)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-flowlog-destinationoptions-syntax.yaml"></a>

```
  [FileFormat](#cfn-ec2-flowlog-destinationoptions-fileformat): {{String}}
  [HiveCompatiblePartitions](#cfn-ec2-flowlog-destinationoptions-hivecompatiblepartitions): {{Boolean}}
  [PerHourPartition](#cfn-ec2-flowlog-destinationoptions-perhourpartition): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-flowlog-destinationoptions-properties"></a>

`FileFormat`  <a name="cfn-ec2-flowlog-destinationoptions-fileformat"></a>
The format for the flow log. The default is `plain-text`.
*Required*: Yes
*Type*: String
*Allowed values*: `plain-text | parquet`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`HiveCompatiblePartitions`  <a name="cfn-ec2-flowlog-destinationoptions-hivecompatiblepartitions"></a>
Indicates whether to use Hive-compatible prefixes for flow logs stored in Amazon S3. The default is `false`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PerHourPartition`  <a name="cfn-ec2-flowlog-destinationoptions-perhourpartition"></a>
Indicates whether to partition the flow log per hour. This reduces the cost and response time for queries. The default is `false`.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
