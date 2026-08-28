---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream SchemaEvolutionConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration"></a>

The configuration to enable schema evolution.

Amazon Data Firehose is in preview release and is subject to change.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-kinesisfirehose-deliverystream-schemaevolutionconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-kinesisfirehose-deliverystream-schemaevolutionconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-schemaevolutionconfiguration-properties"></a>

`Enabled`  <a name="cfn-kinesisfirehose-deliverystream-schemaevolutionconfiguration-enabled"></a>
 Specify whether you want to enable schema evolution.
Amazon Data Firehose is in preview release and is subject to change.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
