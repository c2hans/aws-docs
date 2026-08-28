---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-ruledmarcexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet RuleDmarcExpression
<a name="aws-properties-ses-mailmanagerruleset-ruledmarcexpression"></a>

A DMARC policy expression. The condition matches if the given DMARC policy matches that of the incoming email.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-ruledmarcexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-ruledmarcexpression-syntax.json"></a>

```
{
  "[Operator](#cfn-ses-mailmanagerruleset-ruledmarcexpression-operator)" : {{String}},
  "[Values](#cfn-ses-mailmanagerruleset-ruledmarcexpression-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-ruledmarcexpression-syntax.yaml"></a>

```
  [Operator](#cfn-ses-mailmanagerruleset-ruledmarcexpression-operator): {{String}}
  [Values](#cfn-ses-mailmanagerruleset-ruledmarcexpression-values): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-ruledmarcexpression-properties"></a>

`Operator`  <a name="cfn-ses-mailmanagerruleset-ruledmarcexpression-operator"></a>
The operator to apply to the DMARC policy of the incoming email.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | NOT_EQUALS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-ses-mailmanagerruleset-ruledmarcexpression-values"></a>
The values to use for the given DMARC policy operator. For the operator EQUALS, if multiple values are given, they are evaluated as an OR. That is, if any of the given values match, the condition is deemed to match. For the operator NOT\_EQUALS, if multiple values are given, they are evaluated as an AND. That is, only if the email's DMARC policy is not equal to any of the given values, then the condition is deemed to match.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
