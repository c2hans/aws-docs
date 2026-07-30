---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-stringcriteriacondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule StringCriteriaCondition
<a name="aws-properties-computeoptimizer-automationrule-stringcriteriacondition"></a>

Criteria condition for filtering based on string values, including comparison operators and target values.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-stringcriteriacondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-stringcriteriacondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-computeoptimizer-automationrule-stringcriteriacondition-comparison)" : {{String}},
  "[Values](#cfn-computeoptimizer-automationrule-stringcriteriacondition-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-stringcriteriacondition-syntax.yaml"></a>

```
  [Comparison](#cfn-computeoptimizer-automationrule-stringcriteriacondition-comparison): {{String}}
  [Values](#cfn-computeoptimizer-automationrule-stringcriteriacondition-values): {{
    - String}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-stringcriteriacondition-properties"></a>

`Comparison`  <a name="cfn-computeoptimizer-automationrule-stringcriteriacondition-comparison"></a>
The comparison operator used to evaluate the string criteria, such as equals, not equals, or contains.
*Required*: No
*Type*: String
*Allowed values*: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-computeoptimizer-automationrule-stringcriteriacondition-values"></a>
List of string values to compare against when applying the criteria condition.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
