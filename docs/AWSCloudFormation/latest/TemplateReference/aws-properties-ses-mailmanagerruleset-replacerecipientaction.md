---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-replacerecipientaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet ReplaceRecipientAction
<a name="aws-properties-ses-mailmanagerruleset-replacerecipientaction"></a>

This action replaces the email envelope recipients with the given list of recipients. If the condition of this action applies only to a subset of recipients, only those recipients are replaced with the recipients specified in the action. The message contents and headers are unaffected by this action, only the envelope recipients are updated.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-replacerecipientaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-replacerecipientaction-syntax.json"></a>

```
{
  "[ReplaceWith](#cfn-ses-mailmanagerruleset-replacerecipientaction-replacewith)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-replacerecipientaction-syntax.yaml"></a>

```
  [ReplaceWith](#cfn-ses-mailmanagerruleset-replacerecipientaction-replacewith): {{
    - String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-replacerecipientaction-properties"></a>

`ReplaceWith`  <a name="cfn-ses-mailmanagerruleset-replacerecipientaction-replacewith"></a>
This action specifies the replacement recipient email addresses to insert.
*Required*: No
*Type*: Array of String
*Minimum*: `0 | 1`
*Maximum*: `254 | 100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
