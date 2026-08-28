---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream MSKSourceConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration"></a>

The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration-syntax.json"></a>

```
{
  "[AuthenticationConfiguration](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-authenticationconfiguration)" : {{AuthenticationConfiguration}},
  "[MSKClusterARN](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-mskclusterarn)" : {{String}},
  "[ReadFromTimestamp](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-readfromtimestamp)" : {{String}},
  "[TopicName](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-topicname)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration-syntax.yaml"></a>

```
  [AuthenticationConfiguration](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-authenticationconfiguration): {{
    AuthenticationConfiguration}}
  [MSKClusterARN](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-mskclusterarn): {{String}}
  [ReadFromTimestamp](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-readfromtimestamp): {{String}}
  [TopicName](#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-topicname): {{String}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration-properties"></a>

`AuthenticationConfiguration`  <a name="cfn-kinesisfirehose-deliverystream-msksourceconfiguration-authenticationconfiguration"></a>
The authentication configuration of the Amazon MSK cluster.
*Required*: Yes
*Type*: [AuthenticationConfiguration](aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MSKClusterARN`  <a name="cfn-kinesisfirehose-deliverystream-msksourceconfiguration-mskclusterarn"></a>
The ARN of the Amazon MSK cluster.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReadFromTimestamp`  <a name="cfn-kinesisfirehose-deliverystream-msksourceconfiguration-readfromtimestamp"></a>
The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active.
If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the `ReadFromTimestamp` parameter to Epoch (1970-01-01T00:00:00Z).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicName`  <a name="cfn-kinesisfirehose-deliverystream-msksourceconfiguration-topicname"></a>
The topic name within the Amazon MSK cluster.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9\._\-]+`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
