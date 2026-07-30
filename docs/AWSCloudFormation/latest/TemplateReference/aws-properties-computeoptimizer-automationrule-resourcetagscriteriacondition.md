---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule ResourceTagsCriteriaCondition
<a name="aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition"></a>

Criteria condition for filtering resources based on their tags, including comparison operators and values.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition-syntax.json"></a>

```
{
  "[Comparison](#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-comparison)" : {{String}},
  "[Key](#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-key)" : {{String}},
  "[Values](#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition-syntax.yaml"></a>

```
  [Comparison](#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-comparison): {{String}}
  [Key](#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-key): {{String}}
  [Values](#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-values): {{
    - String}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition-properties"></a>

`Comparison`  <a name="cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-comparison"></a>
The comparison operator used to evaluate the tag criteria, such as equals, not equals, or contains.
*Required*: No
*Type*: String
*Allowed values*: `StringEquals | StringNotEquals | StringEqualsIgnoreCase | StringNotEqualsIgnoreCase | StringLike | StringNotLike | NumericEquals | NumericNotEquals | NumericLessThan | NumericLessThanEquals | NumericGreaterThan | NumericGreaterThanEquals`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-key"></a>
The tag key to use for comparison when filtering resources.
*Required*: No
*Type*: String
*Pattern*: `^[\w\s\.\-\:\/\=\+\@\*\?]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-values"></a>
List of tag values to compare against when filtering resources.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
