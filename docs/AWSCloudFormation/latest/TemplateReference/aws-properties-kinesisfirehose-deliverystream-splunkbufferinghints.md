---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SplunkBufferingHints
<a name="aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints"></a>

The buffering options. If no value is specified, the default values for Splunk are used.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints-syntax.json"></a>

```
{
  "[IntervalInSeconds](#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-intervalinseconds)" : {{Integer}},
  "[SizeInMBs](#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-sizeinmbs)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints-syntax.yaml"></a>

```
  [IntervalInSeconds](#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-intervalinseconds): {{Integer}}
  [SizeInMBs](#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-sizeinmbs): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints-properties"></a>

`IntervalInSeconds`  <a name="cfn-kinesisfirehose-deliverystream-splunkbufferinghints-intervalinseconds"></a>
Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 60 (1 minute).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeInMBs`  <a name="cfn-kinesisfirehose-deliverystream-splunkbufferinghints-sizeinmbs"></a>
Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
