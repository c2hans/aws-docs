---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-assetoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis AssetOptions
<a name="aws-properties-quicksight-analysis-assetoptions"></a>

An array of analysis level configurations.

## Syntax
<a name="aws-properties-quicksight-analysis-assetoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-assetoptions-syntax.json"></a>

```
{
  "[Timezone](#cfn-quicksight-analysis-assetoptions-timezone)" : {{String}},
  "[WeekStart](#cfn-quicksight-analysis-assetoptions-weekstart)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-assetoptions-syntax.yaml"></a>

```
  [Timezone](#cfn-quicksight-analysis-assetoptions-timezone): {{String}}
  [WeekStart](#cfn-quicksight-analysis-assetoptions-weekstart): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-assetoptions-properties"></a>

`Timezone`  <a name="cfn-quicksight-analysis-assetoptions-timezone"></a>
Determines the timezone for the analysis.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeekStart`  <a name="cfn-quicksight-analysis-assetoptions-weekstart"></a>
Determines the week start day for an analysis.
*Required*: No
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
