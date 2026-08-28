---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleNumberToEvaluate
<a name="aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate"></a>

The number to evaluate in a numeric condition expression.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagerruleset-rulenumbertoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagerruleset-rulenumbertoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-rulenumbertoevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagerruleset-rulenumbertoevaluate-attribute"></a>
An email attribute that is used as the number to evaluate.
*Required*: Yes
*Type*: String
*Allowed values*: `MESSAGE_SIZE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
