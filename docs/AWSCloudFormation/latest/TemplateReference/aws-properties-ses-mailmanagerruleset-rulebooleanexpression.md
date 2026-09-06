---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulebooleanexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleBooleanExpression
<a name="aws-properties-ses-mailmanagerruleset-rulebooleanexpression"></a>

A boolean expression to be used in a rule condition.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulebooleanexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulebooleanexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagerruleset-rulebooleanexpression-evaluate)" : {{RuleBooleanToEvaluate}},
  "[Operator](#cfn-ses-mailmanagerruleset-rulebooleanexpression-operator)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulebooleanexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagerruleset-rulebooleanexpression-evaluate): {{
    RuleBooleanToEvaluate}}
  [Operator](#cfn-ses-mailmanagerruleset-rulebooleanexpression-operator): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulebooleanexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagerruleset-rulebooleanexpression-evaluate"></a>
The operand on which to perform a boolean condition operation.
*Required*: Yes
*Type*: [RuleBooleanToEvaluate](aws-properties-ses-mailmanagerruleset-rulebooleantoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagerruleset-rulebooleanexpression-operator"></a>
The matching operator for a boolean condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `IS_TRUE | IS_FALSE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
