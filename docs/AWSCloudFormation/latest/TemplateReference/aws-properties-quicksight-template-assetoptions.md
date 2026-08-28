---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-assetoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template AssetOptions
<a name="aws-properties-quicksight-template-assetoptions"></a>

An array of analysis level configurations.

## Syntax
<a name="aws-properties-quicksight-template-assetoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-assetoptions-syntax.json"></a>

```
{
  "[Timezone](#cfn-quicksight-template-assetoptions-timezone)" : {{String}},
  "[WeekStart](#cfn-quicksight-template-assetoptions-weekstart)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-assetoptions-syntax.yaml"></a>

```
  [Timezone](#cfn-quicksight-template-assetoptions-timezone): {{String}}
  [WeekStart](#cfn-quicksight-template-assetoptions-weekstart): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-assetoptions-properties"></a>

`Timezone`  <a name="cfn-quicksight-template-assetoptions-timezone"></a>
Determines the timezone for the analysis.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeekStart`  <a name="cfn-quicksight-template-assetoptions-weekstart"></a>
Determines the week start day for an analysis.
*Required*: No
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
