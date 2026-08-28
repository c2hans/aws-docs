---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream KinesisStreamSourceConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration"></a>

The `KinesisStreamSourceConfiguration` property type specifies the stream and role Amazon Resource Names (ARNs) for a Kinesis stream used as the source for a delivery stream.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-syntax.json"></a>

```
{
  "[KinesisStreamARN](#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn)" : {{String}},
  "[RoleARN](#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-syntax.yaml"></a>

```
  [KinesisStreamARN](#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn): {{String}}
  [RoleARN](#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-properties"></a>

`KinesisStreamARN`  <a name="cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn"></a>
The ARN of the source Kinesis data stream.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleARN`  <a name="cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn"></a>
The ARN of the role that provides access to the source Kinesis data stream.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
