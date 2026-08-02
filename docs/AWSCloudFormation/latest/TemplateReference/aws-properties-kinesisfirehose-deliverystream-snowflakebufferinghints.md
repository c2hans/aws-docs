---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SnowflakeBufferingHints
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints"></a>

 Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints-syntax.json"></a>

```
{
  "[IntervalInSeconds](#cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-intervalinseconds)" : {{Integer}},
  "[SizeInMBs](#cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-sizeinmbs)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints-syntax.yaml"></a>

```
  [IntervalInSeconds](#cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-intervalinseconds): {{Integer}}
  [SizeInMBs](#cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-sizeinmbs): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-snowflakebufferinghints-properties"></a>

`IntervalInSeconds`  <a name="cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-intervalinseconds"></a>
 Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 0.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeInMBs`  <a name="cfn-kinesisfirehose-deliverystream-snowflakebufferinghints-sizeinmbs"></a>
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 128.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
