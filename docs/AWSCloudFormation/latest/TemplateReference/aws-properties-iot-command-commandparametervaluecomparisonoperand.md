---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-command-commandparametervaluecomparisonoperand.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Command CommandParameterValueComparisonOperand
<a name="aws-properties-iot-command-commandparametervaluecomparisonoperand"></a>

<a name="aws-properties-iot-command-commandparametervaluecomparisonoperand-description"></a>The `CommandParameterValueComparisonOperand` property type specifies Property description not available. for an [AWS::IoT::Command](aws-resource-iot-command.md).

## Syntax
<a name="aws-properties-iot-command-commandparametervaluecomparisonoperand-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-command-commandparametervaluecomparisonoperand-syntax.json"></a>

```
{
  "[Number](#cfn-iot-command-commandparametervaluecomparisonoperand-number)" : {{String}},
  "[NumberRange](#cfn-iot-command-commandparametervaluecomparisonoperand-numberrange)" : {{CommandParameterValueNumberRange}},
  "[Numbers](#cfn-iot-command-commandparametervaluecomparisonoperand-numbers)" : {{[ String, ... ]}},
  "[String](#cfn-iot-command-commandparametervaluecomparisonoperand-string)" : {{String}},
  "[Strings](#cfn-iot-command-commandparametervaluecomparisonoperand-strings)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-iot-command-commandparametervaluecomparisonoperand-syntax.yaml"></a>

```
  [Number](#cfn-iot-command-commandparametervaluecomparisonoperand-number): {{String}}
  [NumberRange](#cfn-iot-command-commandparametervaluecomparisonoperand-numberrange): {{
    CommandParameterValueNumberRange}}
  [Numbers](#cfn-iot-command-commandparametervaluecomparisonoperand-numbers): {{
    - String}}
  [String](#cfn-iot-command-commandparametervaluecomparisonoperand-string): {{
    String}}
  [Strings](#cfn-iot-command-commandparametervaluecomparisonoperand-strings): {{
    - String}}
```

## Properties
<a name="aws-properties-iot-command-commandparametervaluecomparisonoperand-properties"></a>

`Number`  <a name="cfn-iot-command-commandparametervaluecomparisonoperand-number"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberRange`  <a name="cfn-iot-command-commandparametervaluecomparisonoperand-numberrange"></a>
Property description not available.
*Required*: No
*Type*: [CommandParameterValueNumberRange](aws-properties-iot-command-commandparametervaluenumberrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Numbers`  <a name="cfn-iot-command-commandparametervaluecomparisonoperand-numbers"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`String`  <a name="cfn-iot-command-commandparametervaluecomparisonoperand-string"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strings`  <a name="cfn-iot-command-commandparametervaluecomparisonoperand-strings"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
