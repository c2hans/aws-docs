---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-caserule-booleanoperands.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule BooleanOperands
<a name="aws-properties-cases-caserule-booleanoperands"></a>

Boolean operands for a condition. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Syntax
<a name="aws-properties-cases-caserule-booleanoperands-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-caserule-booleanoperands-syntax.json"></a>

```
{
  "[OperandOne](#cfn-cases-caserule-booleanoperands-operandone)" : {{OperandOne}},
  "[OperandTwo](#cfn-cases-caserule-booleanoperands-operandtwo)" : {{OperandTwo}},
  "[Result](#cfn-cases-caserule-booleanoperands-result)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cases-caserule-booleanoperands-syntax.yaml"></a>

```
  [OperandOne](#cfn-cases-caserule-booleanoperands-operandone): {{
    OperandOne}}
  [OperandTwo](#cfn-cases-caserule-booleanoperands-operandtwo): {{
    OperandTwo}}
  [Result](#cfn-cases-caserule-booleanoperands-result): {{Boolean}}
```

## Properties
<a name="aws-properties-cases-caserule-booleanoperands-properties"></a>

`OperandOne`  <a name="cfn-cases-caserule-booleanoperands-operandone"></a>
Represents the left hand operand in the condition.
*Required*: Yes
*Type*: [OperandOne](aws-properties-cases-caserule-operandone.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperandTwo`  <a name="cfn-cases-caserule-booleanoperands-operandtwo"></a>
Represents the right hand operand in the condition.
*Required*: Yes
*Type*: [OperandTwo](aws-properties-cases-caserule-operandtwo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Result`  <a name="cfn-cases-caserule-booleanoperands-result"></a>
The value of the outer rule if the condition evaluates to true.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
