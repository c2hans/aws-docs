---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-integercriteriacondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule IntegerCriteriaCondition
<a name="aws-properties-computeoptimizer-automationrule-integercriteriacondition"></a>

Defines a condition for filtering based on integer values with comparison operators.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-integercriteriacondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-integercriteriacondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-computeoptimizer-automationrule-integercriteriacondition-comparison)" : {{String}},
  "[Values](#cfn-computeoptimizer-automationrule-integercriteriacondition-values)" : {{[ Integer, ... ]}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-integercriteriacondition-syntax.yaml"></a>

```
  [Comparison](#cfn-computeoptimizer-automationrule-integercriteriacondition-comparison): {{String}}
  [Values](#cfn-computeoptimizer-automationrule-integercriteriacondition-values): {{
    - Integer}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-integercriteriacondition-properties"></a>

`Comparison`  <a name="cfn-computeoptimizer-automationrule-integercriteriacondition-comparison"></a>
The comparison operator to use, such as equals, greater than, less than, etc.
*Required*: No
*Type*: String
*Allowed values*: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-computeoptimizer-automationrule-integercriteriacondition-values"></a>
The list of integer values to compare against using the specified comparison operator.
*Required*: No
*Type*: Array of Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
