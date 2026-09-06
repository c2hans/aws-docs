---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-doublecriteriacondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule DoubleCriteriaCondition
<a name="aws-properties-computeoptimizer-automationrule-doublecriteriacondition"></a>

Defines a condition for filtering based on double/floating-point numeric values with comparison operators.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-doublecriteriacondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-doublecriteriacondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-computeoptimizer-automationrule-doublecriteriacondition-comparison)" : {{String}},
  "[Values](#cfn-computeoptimizer-automationrule-doublecriteriacondition-values)" : {{[ Number, ... ]}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-doublecriteriacondition-syntax.yaml"></a>

```
  [Comparison](#cfn-computeoptimizer-automationrule-doublecriteriacondition-comparison): {{String}}
  [Values](#cfn-computeoptimizer-automationrule-doublecriteriacondition-values): {{
    - Number}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-doublecriteriacondition-properties"></a>

`Comparison`  <a name="cfn-computeoptimizer-automationrule-doublecriteriacondition-comparison"></a>
The comparison operator to use, such as equals, greater than, less than, etc.
*Required*: No
*Type*: String
*Allowed values*: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-computeoptimizer-automationrule-doublecriteriacondition-values"></a>
The list of double values to compare against using the specified comparison operator.
*Required*: No
*Type*: Array of Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
