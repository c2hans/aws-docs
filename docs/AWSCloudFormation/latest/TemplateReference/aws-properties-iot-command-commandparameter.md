---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-command-commandparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Command CommandParameter
<a name="aws-properties-iot-command-commandparameter"></a>

<a name="aws-properties-iot-command-commandparameter-description"></a>The `CommandParameter` property type specifies Property description not available. for an [AWS::IoT::Command](aws-resource-iot-command.md).

## Syntax
<a name="aws-properties-iot-command-commandparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-command-commandparameter-syntax.json"></a>

```
{
  "[DefaultValue](#cfn-iot-command-commandparameter-defaultvalue)" : {{CommandParameterValue}},
  "[Description](#cfn-iot-command-commandparameter-description)" : {{String}},
  "[Name](#cfn-iot-command-commandparameter-name)" : {{String}},
  "[Type](#cfn-iot-command-commandparameter-type)" : {{String}},
  "[Value](#cfn-iot-command-commandparameter-value)" : {{CommandParameterValue}},
  "[ValueConditions](#cfn-iot-command-commandparameter-valueconditions)" : {{[ CommandParameterValueCondition, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-command-commandparameter-syntax.yaml"></a>

```
  [DefaultValue](#cfn-iot-command-commandparameter-defaultvalue): {{
    CommandParameterValue}}
  [Description](#cfn-iot-command-commandparameter-description): {{String}}
  [Name](#cfn-iot-command-commandparameter-name): {{String}}
  [Type](#cfn-iot-command-commandparameter-type): {{String}}
  [Value](#cfn-iot-command-commandparameter-value): {{
    CommandParameterValue}}
  [ValueConditions](#cfn-iot-command-commandparameter-valueconditions): {{
    - CommandParameterValueCondition}}
```

## Properties
<a name="aws-properties-iot-command-commandparameter-properties"></a>

`DefaultValue`  <a name="cfn-iot-command-commandparameter-defaultvalue"></a>
Property description not available.
*Required*: No
*Type*: [CommandParameterValue](aws-properties-iot-command-commandparametervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-iot-command-commandparameter-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `2028`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iot-command-commandparameter-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[.$a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iot-command-commandparameter-type"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `STRING | INTEGER | DOUBLE | LONG | UNSIGNEDLONG | BOOLEAN | BINARY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-iot-command-commandparameter-value"></a>
Property description not available.
*Required*: No
*Type*: [CommandParameterValue](aws-properties-iot-command-commandparametervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueConditions`  <a name="cfn-iot-command-commandparameter-valueconditions"></a>
Property description not available.
*Required*: No
*Type*: Array of [CommandParameterValueCondition](aws-properties-iot-command-commandparametervaluecondition.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
