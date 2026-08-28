---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kafkaconnect-connector-customplugin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KafkaConnect::Connector CustomPlugin
<a name="aws-properties-kafkaconnect-connector-customplugin"></a>

A plugin is an AWS resource that contains the code that defines a connector's logic.

## Syntax
<a name="aws-properties-kafkaconnect-connector-customplugin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kafkaconnect-connector-customplugin-syntax.json"></a>

```
{
  "[CustomPluginArn](#cfn-kafkaconnect-connector-customplugin-custompluginarn)" : {{String}},
  "[Revision](#cfn-kafkaconnect-connector-customplugin-revision)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-kafkaconnect-connector-customplugin-syntax.yaml"></a>

```
  [CustomPluginArn](#cfn-kafkaconnect-connector-customplugin-custompluginarn): {{String}}
  [Revision](#cfn-kafkaconnect-connector-customplugin-revision): {{Integer}}
```

## Properties
<a name="aws-properties-kafkaconnect-connector-customplugin-properties"></a>

`CustomPluginArn`  <a name="cfn-kafkaconnect-connector-customplugin-custompluginarn"></a>
The Amazon Resource Name (ARN) of the custom plugin.
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):kafkaconnect:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Revision`  <a name="cfn-kafkaconnect-connector-customplugin-revision"></a>
The revision of the custom plugin.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
