---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruleverdictexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleVerdictExpression
<a name="aws-properties-ses-mailmanagerruleset-ruleverdictexpression"></a>

A verdict expression is evaluated against verdicts of the email.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruleverdictexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruleverdictexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagerruleset-ruleverdictexpression-evaluate)" : {{RuleVerdictToEvaluate}},
  "[Operator](#cfn-ses-mailmanagerruleset-ruleverdictexpression-operator)" : {{String}},
  "[Values](#cfn-ses-mailmanagerruleset-ruleverdictexpression-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruleverdictexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagerruleset-ruleverdictexpression-evaluate): {{
    RuleVerdictToEvaluate}}
  [Operator](#cfn-ses-mailmanagerruleset-ruleverdictexpression-operator): {{String}}
  [Values](#cfn-ses-mailmanagerruleset-ruleverdictexpression-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruleverdictexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagerruleset-ruleverdictexpression-evaluate"></a>
The verdict to evaluate in a verdict condition expression.
*Required*: Yes
*Type*: [RuleVerdictToEvaluate](aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagerruleset-ruleverdictexpression-operator"></a>
The matching operator for a verdict condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ses-mailmanagerruleset-ruleverdictexpression-values"></a>
The values to match with the email's verdict using the given operator. For the EQUALS operator, if multiple values are given, the condition is deemed to match if any of the given verdicts match that of the email. For the NOT\_EQUALS operator, if multiple values are given, the condition is deemed to match of none of the given verdicts match the verdict of the email.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
