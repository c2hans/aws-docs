---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-visualinteractionoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard VisualInteractionOptions
<a name="aws-properties-quicksight-dashboard-visualinteractionoptions"></a>

The general visual interactions setup for visual publish options

## Syntax
<a name="aws-properties-quicksight-dashboard-visualinteractionoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-visualinteractionoptions-syntax.json"></a>

```
{
  "[ContextMenuOption](#cfn-quicksight-dashboard-visualinteractionoptions-contextmenuoption)" : {{ContextMenuOption}},
  "[VisualMenuOption](#cfn-quicksight-dashboard-visualinteractionoptions-visualmenuoption)" : {{VisualMenuOption}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-visualinteractionoptions-syntax.yaml"></a>

```
  [ContextMenuOption](#cfn-quicksight-dashboard-visualinteractionoptions-contextmenuoption): {{
    ContextMenuOption}}
  [VisualMenuOption](#cfn-quicksight-dashboard-visualinteractionoptions-visualmenuoption): {{
    VisualMenuOption}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-visualinteractionoptions-properties"></a>

`ContextMenuOption`  <a name="cfn-quicksight-dashboard-visualinteractionoptions-contextmenuoption"></a>
The context menu options for a visual.
*Required*: No
*Type*: [ContextMenuOption](aws-properties-quicksight-dashboard-contextmenuoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualMenuOption`  <a name="cfn-quicksight-dashboard-visualinteractionoptions-visualmenuoption"></a>
The on-visual menu options for a visual.
*Required*: No
*Type*: [VisualMenuOption](aws-properties-quicksight-dashboard-visualmenuoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
