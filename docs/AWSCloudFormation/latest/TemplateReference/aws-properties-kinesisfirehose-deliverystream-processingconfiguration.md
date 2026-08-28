---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream ProcessingConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-processingconfiguration"></a>

The `ProcessingConfiguration` property configures data processing for an Amazon Kinesis Data Firehose delivery stream.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-processingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-processingconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled)" : {{Boolean}},
  "[Processors](#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors)" : {{[ Processor, ... ]}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-processingconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled): {{Boolean}}
  [Processors](#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors): {{
    - Processor}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-processingconfiguration-properties"></a>

`Enabled`  <a name="cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled"></a>
Indicates whether data processing is enabled (true) or disabled (false).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Processors`  <a name="cfn-kinesisfirehose-deliverystream-processingconfiguration-processors"></a>
The data processors.
*Required*: No
*Type*: Array of [Processor](aws-properties-kinesisfirehose-deliverystream-processor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
