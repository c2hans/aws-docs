---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::ConfiguredTable ConfiguredTableAnalysisRulePolicy
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy"></a>

Controls on the query specifications that can be run on a configured table.

## Syntax
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-syntax.json"></a>

```
{
  "[V1](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-v1)" : {{ConfiguredTableAnalysisRulePolicyV1}}
}
```

### YAML
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-syntax.yaml"></a>

```
  [V1](#cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-v1): {{
    ConfiguredTableAnalysisRulePolicyV1}}
```

## Properties
<a name="aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-properties"></a>

`V1`  <a name="cfn-cleanrooms-configuredtable-configuredtableanalysisrulepolicy-v1"></a>
Controls on the query specifications that can be run on a configured table.
*Required*: Yes
*Type*: [ConfiguredTableAnalysisRulePolicyV1](aws-properties-cleanrooms-configuredtable-configuredtableanalysisrulepolicyv1.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
