---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulecondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleCondition
<a name="aws-properties-ses-mailmanagerruleset-rulecondition"></a>

The conditional expression used to evaluate an email for determining if a rule action should be taken.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulecondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulecondition-syntax.json"></a>

```
{
  "[BooleanExpression](#cfn-ses-mailmanagerruleset-rulecondition-booleanexpression)" : {{RuleBooleanExpression}},
  "[DmarcExpression](#cfn-ses-mailmanagerruleset-rulecondition-dmarcexpression)" : {{RuleDmarcExpression}},
  "[IpExpression](#cfn-ses-mailmanagerruleset-rulecondition-ipexpression)" : {{RuleIpExpression}},
  "[NumberExpression](#cfn-ses-mailmanagerruleset-rulecondition-numberexpression)" : {{RuleNumberExpression}},
  "[StringExpression](#cfn-ses-mailmanagerruleset-rulecondition-stringexpression)" : {{RuleStringExpression}},
  "[VerdictExpression](#cfn-ses-mailmanagerruleset-rulecondition-verdictexpression)" : {{RuleVerdictExpression}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulecondition-syntax.yaml"></a>

```
  [BooleanExpression](#cfn-ses-mailmanagerruleset-rulecondition-booleanexpression): {{
    RuleBooleanExpression}}
  [DmarcExpression](#cfn-ses-mailmanagerruleset-rulecondition-dmarcexpression): {{
    RuleDmarcExpression}}
  [IpExpression](#cfn-ses-mailmanagerruleset-rulecondition-ipexpression): {{
    RuleIpExpression}}
  [NumberExpression](#cfn-ses-mailmanagerruleset-rulecondition-numberexpression): {{
    RuleNumberExpression}}
  [StringExpression](#cfn-ses-mailmanagerruleset-rulecondition-stringexpression): {{
    RuleStringExpression}}
  [VerdictExpression](#cfn-ses-mailmanagerruleset-rulecondition-verdictexpression): {{
    RuleVerdictExpression}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulecondition-properties"></a>

`BooleanExpression`  <a name="cfn-ses-mailmanagerruleset-rulecondition-booleanexpression"></a>
The condition applies to a boolean expression passed in this field.
*Required*: No
*Type*: [RuleBooleanExpression](aws-properties-ses-mailmanagerruleset-rulebooleanexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DmarcExpression`  <a name="cfn-ses-mailmanagerruleset-rulecondition-dmarcexpression"></a>
The condition applies to a DMARC policy expression passed in this field.
*Required*: No
*Type*: [RuleDmarcExpression](aws-properties-ses-mailmanagerruleset-ruledmarcexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpExpression`  <a name="cfn-ses-mailmanagerruleset-rulecondition-ipexpression"></a>
The condition applies to an IP address expression passed in this field.
*Required*: No
*Type*: [RuleIpExpression](aws-properties-ses-mailmanagerruleset-ruleipexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberExpression`  <a name="cfn-ses-mailmanagerruleset-rulecondition-numberexpression"></a>
The condition applies to a number expression passed in this field.
*Required*: No
*Type*: [RuleNumberExpression](aws-properties-ses-mailmanagerruleset-rulenumberexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringExpression`  <a name="cfn-ses-mailmanagerruleset-rulecondition-stringexpression"></a>
The condition applies to a string expression passed in this field.
*Required*: No
*Type*: [RuleStringExpression](aws-properties-ses-mailmanagerruleset-rulestringexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerdictExpression`  <a name="cfn-ses-mailmanagerruleset-rulecondition-verdictexpression"></a>
The condition applies to a verdict expression passed in this field.
*Required*: No
*Type*: [RuleVerdictExpression](aws-properties-ses-mailmanagerruleset-ruleverdictexpression.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
