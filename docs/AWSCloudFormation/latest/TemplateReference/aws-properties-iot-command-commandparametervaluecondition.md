---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-command-commandparametervaluecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Command CommandParameterValueCondition
<a name="aws-properties-iot-command-commandparametervaluecondition"></a>

<a name="aws-properties-iot-command-commandparametervaluecondition-description"></a>The `CommandParameterValueCondition` property type specifies Property description not available. for an [AWS::IoT::Command](aws-resource-iot-command.md).

## Syntax
<a name="aws-properties-iot-command-commandparametervaluecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-command-commandparametervaluecondition-syntax.json"></a>

```
{
  "[ComparisonOperator](#cfn-iot-command-commandparametervaluecondition-comparisonoperator)" : {{String}},
  "[Operand](#cfn-iot-command-commandparametervaluecondition-operand)" : {{CommandParameterValueComparisonOperand}}
}
```

### YAML
<a name="aws-properties-iot-command-commandparametervaluecondition-syntax.yaml"></a>

```
  [ComparisonOperator](#cfn-iot-command-commandparametervaluecondition-comparisonoperator): {{String}}
  [Operand](#cfn-iot-command-commandparametervaluecondition-operand): {{
    CommandParameterValueComparisonOperand}}
```

## Properties
<a name="aws-properties-iot-command-commandparametervaluecondition-properties"></a>

`ComparisonOperator`  <a name="cfn-iot-command-commandparametervaluecondition-comparisonoperator"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS | LESS_THAN | LESS_THAN_EQUALS | GREATER_THAN | GREATER_THAN_EQUALS | IN_SET | NOT_IN_SET | IN_RANGE | NOT_IN_RANGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operand`  <a name="cfn-iot-command-commandparametervaluecondition-operand"></a>
Property description not available.
*Required*: Yes
*Type*: [CommandParameterValueComparisonOperand](aws-properties-iot-command-commandparametervaluecomparisonoperand.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
