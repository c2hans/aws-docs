---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::IntermediateTable DifferentialPrivacyColumn
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn"></a>

Specifies the name of the column that contains the unique identifier of your users, whose privacy you want to protect.

## Syntax
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn-syntax.json"></a>

```
{
  "[Name](#cfn-cleanrooms-intermediatetable-differentialprivacycolumn-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn-syntax.yaml"></a>

```
  [Name](#cfn-cleanrooms-intermediatetable-differentialprivacycolumn-name): {{String}}
```

## Properties
<a name="aws-properties-cleanrooms-intermediatetable-differentialprivacycolumn-properties"></a>

`Name`  <a name="cfn-cleanrooms-intermediatetable-differentialprivacycolumn-name"></a>
The name of the column, such as user\_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
