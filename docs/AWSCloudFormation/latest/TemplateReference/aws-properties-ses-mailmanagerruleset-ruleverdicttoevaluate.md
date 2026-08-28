---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleVerdictToEvaluate
<a name="aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate"></a>

The verdict to evaluate in a verdict condition expression.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate-syntax.json"></a>

```
{
  "[Analysis](#cfn-ses-mailmanagerruleset-ruleverdicttoevaluate-analysis)" : {{Analysis}},
  "[Attribute](#cfn-ses-mailmanagerruleset-ruleverdicttoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate-syntax.yaml"></a>

```
  [Analysis](#cfn-ses-mailmanagerruleset-ruleverdicttoevaluate-analysis): {{
    Analysis}}
  [Attribute](#cfn-ses-mailmanagerruleset-ruleverdicttoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruleverdicttoevaluate-properties"></a>

`Analysis`  <a name="cfn-ses-mailmanagerruleset-ruleverdicttoevaluate-analysis"></a>
The Add On ARN and its returned value to evaluate in a verdict condition expression.
*Required*: No
*Type*: [Analysis](aws-properties-ses-mailmanagerruleset-analysis.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Attribute`  <a name="cfn-ses-mailmanagerruleset-ruleverdicttoevaluate-attribute"></a>
The email verdict attribute to evaluate in a string verdict expression.
*Required*: No
*Type*: String
*Allowed values*: `SPF | DKIM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
