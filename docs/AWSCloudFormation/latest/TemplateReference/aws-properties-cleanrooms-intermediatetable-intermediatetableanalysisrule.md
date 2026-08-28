---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable IntermediateTableAnalysisRule
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule"></a>

Contains the details of an analysis rule for an intermediate table.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule-syntax.json"></a>

```
{
  "[Policy](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrule-policy)" : {{IntermediateTableAnalysisRulePolicy}},
  "[Type](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrule-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule-syntax.yaml"></a>

```
  [Policy](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrule-policy): {{
    IntermediateTableAnalysisRulePolicy}}
  [Type](#cfn-cleanrooms-intermediatetable-intermediatetableanalysisrule-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrule-properties"></a>

`Policy`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrule-policy"></a>
Property description not available.
*Required*: Yes
*Type*: [IntermediateTableAnalysisRulePolicy](aws-properties-cleanrooms-intermediatetable-intermediatetableanalysisrulepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cleanrooms-intermediatetable-intermediatetableanalysisrule-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
