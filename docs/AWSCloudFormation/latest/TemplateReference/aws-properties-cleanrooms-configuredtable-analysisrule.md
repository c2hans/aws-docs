---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-analysisrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable AnalysisRule
<a name="aws-properties-cleanrooms-configuredtable-analysisrule"></a>

A specification about how data from the configured table can be used in a query.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-analysisrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-analysisrule-syntax.json"></a>

```
{
  "[Policy](#cfn-cleanrooms-configuredtable-analysisrule-policy)" : {{ConfiguredTableAnalysisRulePolicy}},
  "[Type](#cfn-cleanrooms-configuredtable-analysisrule-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-analysisrule-syntax.yaml"></a>

```
  [Policy](#cfn-cleanrooms-configuredtable-analysisrule-policy): {{
    ConfiguredTableAnalysisRulePolicy}}
  [Type](#cfn-cleanrooms-configuredtable-analysisrule-type): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-analysisrule-properties"></a>

`Policy`  <a name="cfn-cleanrooms-configuredtable-analysisrule-policy"></a>
A policy that describes the associated data usage limitations.
*Required*: Yes
*Type*: [ConfiguredTableAnalysisRulePolicy](aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cleanrooms-configuredtable-analysisrule-type"></a>
The type of analysis rule.
*Required*: Yes
*Type*: String
*Allowed values*: `AGGREGATION | LIST | CUSTOM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
