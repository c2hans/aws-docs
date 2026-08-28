---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-differentialprivacy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable DifferentialPrivacy
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacy"></a>

<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacy-description"></a>The `DifferentialPrivacy` property type specifies Property description not available. for an [AWS::CleanRooms::IntermediateTable](aws-resource-cleanrooms-intermediatetable.md).

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacy-syntax.json"></a>

```
{
  "[Columns](#cfn-cleanrooms-intermediatetable-differentialprivacy-columns)" : {{[ DifferentialPrivacyColumn, ... ]}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacy-syntax.yaml"></a>

```
  [Columns](#cfn-cleanrooms-intermediatetable-differentialprivacy-columns): {{
    - DifferentialPrivacyColumn}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacy-properties"></a>

`Columns`  <a name="cfn-cleanrooms-intermediatetable-differentialprivacy-columns"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [DifferentialPrivacyColumn](aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
