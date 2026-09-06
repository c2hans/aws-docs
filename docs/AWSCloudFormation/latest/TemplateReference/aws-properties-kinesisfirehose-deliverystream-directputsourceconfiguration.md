---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream DirectPutSourceConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration"></a>

The structure that configures parameters such as `ThroughputHintInMBs` for a stream configured with Direct PUT as a source.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration-syntax.json"></a>

```
{
  "[ThroughputHintInMBs](#cfn-kinesisfirehose-deliverystream-directputsourceconfiguration-throughputhintinmbs)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration-syntax.yaml"></a>

```
  [ThroughputHintInMBs](#cfn-kinesisfirehose-deliverystream-directputsourceconfiguration-throughputhintinmbs): {{Integer}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-directputsourceconfiguration-properties"></a>

`ThroughputHintInMBs`  <a name="cfn-kinesisfirehose-deliverystream-directputsourceconfiguration-throughputhintinmbs"></a>
 The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit. You can use the [Firehose Limits form](https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits) to request a throughput limit increase.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
