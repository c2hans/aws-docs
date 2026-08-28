---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruleiptoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleIpToEvaluate
<a name="aws-properties-ses-mailmanagerruleset-ruleiptoevaluate"></a>

The IP address to evaluate for this condition.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruleiptoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruleiptoevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagerruleset-ruleiptoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruleiptoevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagerruleset-ruleiptoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruleiptoevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagerruleset-ruleiptoevaluate-attribute"></a>
The attribute of the email to evaluate.
*Required*: Yes
*Type*: String
*Allowed values*: `SOURCE_IP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
