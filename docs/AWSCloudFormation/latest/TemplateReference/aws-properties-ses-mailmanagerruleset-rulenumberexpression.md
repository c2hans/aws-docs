---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulenumberexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleNumberExpression
<a name="aws-properties-ses-mailmanagerruleset-rulenumberexpression"></a>

A number expression to match numeric conditions with integers from the incoming email.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulenumberexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulenumberexpression-syntax.json"></a>

```
{
  "[Evaluate](#cfn-ses-mailmanagerruleset-rulenumberexpression-evaluate)" : {{RuleNumberToEvaluate}},
  "[Operator](#cfn-ses-mailmanagerruleset-rulenumberexpression-operator)" : {{String}},
  "[Value](#cfn-ses-mailmanagerruleset-rulenumberexpression-value)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulenumberexpression-syntax.yaml"></a>

```
  [Evaluate](#cfn-ses-mailmanagerruleset-rulenumberexpression-evaluate): {{
    RuleNumberToEvaluate}}
  [Operator](#cfn-ses-mailmanagerruleset-rulenumberexpression-operator): {{String}}
  [Value](#cfn-ses-mailmanagerruleset-rulenumberexpression-value): {{Number}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulenumberexpression-properties"></a>

`Evaluate`  <a name="cfn-ses-mailmanagerruleset-rulenumberexpression-evaluate"></a>
The number to evaluate in a numeric condition expression.
*Required*: Yes
*Type*: [RuleNumberToEvaluate](aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Operator`  <a name="cfn-ses-mailmanagerruleset-rulenumberexpression-operator"></a>
The operator for a numeric condition expression.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ses-mailmanagerruleset-rulenumberexpression-value"></a>
The value to evaluate in a numeric condition expression.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
