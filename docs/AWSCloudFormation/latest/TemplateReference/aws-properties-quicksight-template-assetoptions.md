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
  "[CustomActionDefaults](#cfn-quicksight-template-assetoptions-customactiondefaults)" : {{VisualCustomActionDefaults}},
  "[Timezone](#cfn-quicksight-template-assetoptions-timezone)" : {{String}},
  "[VisualMessages](#cfn-quicksight-template-assetoptions-visualmessages)" : {{VisualMessages}},
  "[WeekStart](#cfn-quicksight-template-assetoptions-weekstart)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-assetoptions-syntax.yaml"></a>

```
  [CustomActionDefaults](#cfn-quicksight-template-assetoptions-customactiondefaults): {{
    VisualCustomActionDefaults}}
  [Timezone](#cfn-quicksight-template-assetoptions-timezone): {{String}}
  [VisualMessages](#cfn-quicksight-template-assetoptions-visualmessages): {{
    VisualMessages}}
  [WeekStart](#cfn-quicksight-template-assetoptions-weekstart): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-assetoptions-properties"></a>

`CustomActionDefaults`  <a name="cfn-quicksight-template-assetoptions-customactiondefaults"></a>
A list of visual custom actions for the analysis.
*Required*: No
*Type*: [VisualCustomActionDefaults](aws-properties-quicksight-template-visualcustomactiondefaults.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Timezone`  <a name="cfn-quicksight-template-assetoptions-timezone"></a>
Determines the timezone for the analysis.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualMessages`  <a name="cfn-quicksight-template-assetoptions-visualmessages"></a>
The configuration options for the messages that are displayed on visuals in the analysis.
*Required*: No
*Type*: [VisualMessages](aws-properties-quicksight-template-visualmessages.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WeekStart`  <a name="cfn-quicksight-template-assetoptions-weekstart"></a>
Determines the week start day for an analysis.
*Required*: No
*Type*: String
*Allowed values*: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
