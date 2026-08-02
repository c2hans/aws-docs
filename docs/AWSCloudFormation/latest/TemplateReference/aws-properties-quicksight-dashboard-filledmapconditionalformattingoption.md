---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-filledmapconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FilledMapConditionalFormattingOption
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformattingoption"></a>

Conditional formatting options of a `FilledMapVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformattingoption-syntax.json"></a>

```
{
  "[Shape](#cfn-quicksight-dashboard-filledmapconditionalformattingoption-shape)" : {{FilledMapShapeConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformattingoption-syntax.yaml"></a>

```
  [Shape](#cfn-quicksight-dashboard-filledmapconditionalformattingoption-shape): {{
    FilledMapShapeConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-filledmapconditionalformattingoption-properties"></a>

`Shape`  <a name="cfn-quicksight-dashboard-filledmapconditionalformattingoption-shape"></a>
The conditional formatting that determines the shape of the filled map.
*Required*: Yes
*Type*: [FilledMapShapeConditionalFormatting](aws-properties-quicksight-dashboard-filledmapshapeconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
