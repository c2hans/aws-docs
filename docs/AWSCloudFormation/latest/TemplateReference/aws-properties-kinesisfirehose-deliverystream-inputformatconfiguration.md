---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisFirehose::DeliveryStream InputFormatConfiguration
<a name="aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration"></a>

Specifies the deserializer you want to use to convert the format of the input data. This parameter is required if `Enabled` is set to true.

## Syntax
<a name="aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration-syntax.json"></a>

```
{
  "[Deserializer](#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer)" : {{Deserializer}}
}
```

### YAML
<a name="aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration-syntax.yaml"></a>

```
  [Deserializer](#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer): {{
    Deserializer}}
```

## Properties
<a name="aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration-properties"></a>

`Deserializer`  <a name="cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer"></a>
Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.
*Required*: No
*Type*: [Deserializer](aws-properties-kinesisfirehose-deliverystream-deserializer.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
