---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable IntermediateTableAnalysisRulePolicyV1
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1"></a>

Contains the version 1 policy for an intermediate table analysis rule.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-syntax.json"></a>

```
{
  "[Custom](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-custom)" : {{IntermediateTableAnalysisRuleCustom}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-syntax.yaml"></a>

```
  [Custom](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-custom): {{
    IntermediateTableAnalysisRuleCustom}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-properties"></a>

`Custom`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicyv1-custom"></a>
The custom analysis rule policy.
*Required*: Yes
*Type*: [IntermediateTableAnalysisRuleCustom](aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulecustom.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
