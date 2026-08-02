---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-plugin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector Plugin
<a name="aws-properties-kafkaconnect-connector-plugin"></a>

A plugin is an AWS resource that contains the code that defines your connector logic.

## Syntax
<a name="aws-properties-kafkaconnect-connector-plugin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-plugin-syntax.json"></a>

```
{
  "[CustomPlugin](#cfn-kafkaconnect-connector-plugin-customplugin)" : {{CustomPlugin}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-plugin-syntax.yaml"></a>

```
  [CustomPlugin](#cfn-kafkaconnect-connector-plugin-customplugin): {{
    CustomPlugin}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-plugin-properties"></a>

`CustomPlugin`  <a name="cfn-kafkaconnect-connector-plugin-customplugin"></a>
Details about a custom plugin.
*Required*: Yes
*Type*: [CustomPlugin](aws-properties-kafkaconnect-connector-customplugin.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
