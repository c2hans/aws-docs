---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulestringexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleStringExpression
<a name="aws-properties-ses-mailmanagerruleset-rulestringexpression"></a>

A string expression is evaluated against strings or substrings of the email.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulestringexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulestringexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagerruleset-rulestringexpression-evaluate)" : {{RuleStringToEvaluate}},
  "[Operator](#cfn-ses-mailmanagerruleset-rulestringexpression-operator)" : {{String}},
  "[Values](#cfn-ses-mailmanagerruleset-rulestringexpression-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulestringexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagerruleset-rulestringexpression-evaluate): {{
    RuleStringToEvaluate}}
  [Operator](#cfn-ses-mailmanagerruleset-rulestringexpression-operator): {{String}}
  [Values](#cfn-ses-mailmanagerruleset-rulestringexpression-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulestringexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagerruleset-rulestringexpression-evaluate"></a>
The string to evaluate in a string condition expression.
*Required*: Yes
*Type*: [RuleStringToEvaluate](aws-properties-ses-mailmanagerruleset-rulestringtoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagerruleset-rulestringexpression-operator"></a>
The matching operator for a string condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS | STARTS_WITH | ENDS_WITH | CONTAINS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ses-mailmanagerruleset-rulestringexpression-values"></a>
The string(s) to be evaluated in a string condition expression. For all operators, except for NOT\_EQUALS, if multiple values are given, the values are processed as an OR. That is, if any of the values match the email's string using the given operator, the condition is deemed to match. However, for NOT\_EQUALS, the condition is only deemed to match if none of the given strings match the email's string.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `4096 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
