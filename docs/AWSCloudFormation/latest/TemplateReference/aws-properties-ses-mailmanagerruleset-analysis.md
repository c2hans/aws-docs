---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagerruleset-analysis.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerRuleSet Analysis
<a name="aws-properties-ses-mailmanagerruleset-analysis"></a>

The result of an analysis can be used in conditions to trigger actions. Analyses can inspect the email content and report a certain aspect of the email.

## Syntax
<a name="aws-properties-ses-mailmanagerruleset-analysis-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagerruleset-analysis-syntax.json"></a>

```
{
  "[Analyzer](#cfn-ses-mailmanagerruleset-analysis-analyzer)" : {{String}},
  "[ResultField](#cfn-ses-mailmanagerruleset-analysis-resultfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagerruleset-analysis-syntax.yaml"></a>

```
  [Analyzer](#cfn-ses-mailmanagerruleset-analysis-analyzer): {{String}}
  [ResultField](#cfn-ses-mailmanagerruleset-analysis-resultfield): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagerruleset-analysis-properties"></a>

`Analyzer`  <a name="cfn-ses-mailmanagerruleset-analysis-analyzer"></a>
The Amazon Resource Name (ARN) of an Add On.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultField`  <a name="cfn-ses-mailmanagerruleset-analysis-resultfield"></a>
The returned value from an Add On.
*Required*: Yes
*Type*: String
*Pattern*: `^(addon\.)?[\sa-zA-Z0-9_]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
