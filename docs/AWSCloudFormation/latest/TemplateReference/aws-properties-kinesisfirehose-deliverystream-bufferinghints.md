---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream BufferingHints
<a name="aws-properties-kinesisfirehose-deliverystream-bufferinghints"></a>

The `BufferingHints` property type specifies how Amazon Kinesis Data Firehose (Kinesis Data Firehose) buffers incoming data before delivering it to the destination. The first buffer condition that is satisfied triggers Kinesis Data Firehose to deliver the data.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-bufferinghints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-bufferinghints-syntax.json"></a>

```
{
  "[IntervalInSeconds](#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds)" : {{Integer}},
  "[SizeInMBs](#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-bufferinghints-syntax.yaml"></a>

```
  [IntervalInSeconds](#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds): {{Integer}}
  [SizeInMBs](#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-bufferinghints-properties"></a>

`IntervalInSeconds`  <a name="cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds"></a>
The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination. For valid values, see the `IntervalInSeconds` content for the [BufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html) data type in the *Amazon Kinesis Data Firehose API Reference*.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeInMBs`  <a name="cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs"></a>
The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination. For valid values, see the `SizeInMBs` content for the [BufferingHints](https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html) data type in the *Amazon Kinesis Data Firehose API Reference*.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
