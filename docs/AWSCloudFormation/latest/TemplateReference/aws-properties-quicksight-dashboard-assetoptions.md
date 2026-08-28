---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-assetoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard AssetOptions
<a name="aws-properties-quicksight-dashboard-assetoptions"></a>

An array of analysis level configurations.

## Syntax
<a name="aws-properties-quicksight-dashboard-assetoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-assetoptions-syntax.json"></a>

```
{
  "[ExcludedDataSetArns](#cfn-quicksight-dashboard-assetoptions-excludeddatasetarns)" : {{[ String, ... ]}},
  "[QBusinessInsightsStatus](#cfn-quicksight-dashboard-assetoptions-qbusinessinsightsstatus)" : {{String}},
  "[Timezone](#cfn-quicksight-dashboard-assetoptions-timezone)" : {{String}},
  "[WeekStart](#cfn-quicksight-dashboard-assetoptions-weekstart)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-assetoptions-syntax.yaml"></a>

```
  [ExcludedDataSetArns](#cfn-quicksight-dashboard-assetoptions-excludeddatasetarns): {{
    - String}}
  [QBusinessInsightsStatus](#cfn-quicksight-dashboard-assetoptions-qbusinessinsightsstatus): {{String}}
  [Timezone](#cfn-quicksight-dashboard-assetoptions-timezone): {{String}}
  [WeekStart](#cfn-quicksight-dashboard-assetoptions-weekstart): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-assetoptions-properties"></a>

`ExcludedDataSetArns`  <a name="cfn-quicksight-dashboard-assetoptions-excludeddatasetarns"></a>
A list of dataset ARNS to exclude from Dashboard Q&A.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QBusinessInsightsStatus`  <a name="cfn-quicksight-dashboard-assetoptions-qbusinessinsightsstatus"></a>
Determines whether insight summaries from Amazon Q Business are allowed in Dashboard Q&A.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-quicksight-dashboard-assetoptions-timezone"></a>
Determines the timezone for the analysis.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeekStart`  <a name="cfn-quicksight-dashboard-assetoptions-weekstart"></a>
Determines the week start day for an analysis.
*Required*: No
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
