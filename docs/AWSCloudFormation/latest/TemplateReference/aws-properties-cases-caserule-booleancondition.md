---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cases-caserule-booleancondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cases::CaseRule BooleanCondition
<a name="aws-properties-cases-caserule-booleancondition"></a>

Boolean condition for a rule. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Syntax
<a name="aws-properties-cases-caserule-booleancondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cases-caserule-booleancondition-syntax.json"></a>

```
{
  "[EqualTo](#cfn-cases-caserule-booleancondition-equalto)" : {{BooleanOperands}},
  "[NotEqualTo](#cfn-cases-caserule-booleancondition-notequalto)" : {{BooleanOperands}}
}
```

### YAML
<a name="aws-properties-cases-caserule-booleancondition-syntax.yaml"></a>

```
  [EqualTo](#cfn-cases-caserule-booleancondition-equalto): {{
    BooleanOperands}}
  [NotEqualTo](#cfn-cases-caserule-booleancondition-notequalto): {{
    BooleanOperands}}
```

## Properties
<a name="aws-properties-cases-caserule-booleancondition-properties"></a>

`EqualTo`  <a name="cfn-cases-caserule-booleancondition-equalto"></a>
Tests that operandOne is equal to operandTwo.
*Required*: No
*Type*: [BooleanOperands](aws-properties-cases-caserule-booleanoperands.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotEqualTo`  <a name="cfn-cases-caserule-booleancondition-notequalto"></a>
Tests that operandOne is not equal to operandTwo.
*Required*: No
*Type*: [BooleanOperands](aws-properties-cases-caserule-booleanoperands.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
