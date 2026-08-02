---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-freeformlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FreeFormLayoutConfiguration
<a name="aws-properties-quicksight-analysis-freeformlayoutconfiguration"></a>

The configuration of a free-form layout.

## Syntax
<a name="aws-properties-quicksight-analysis-freeformlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-freeformlayoutconfiguration-syntax.json"></a>

```
{
  "[CanvasSizeOptions](#cfn-quicksight-analysis-freeformlayoutconfiguration-canvassizeoptions)" : {{FreeFormLayoutCanvasSizeOptions}},
  "[Elements](#cfn-quicksight-analysis-freeformlayoutconfiguration-elements)" : {{[ FreeFormLayoutElement, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-freeformlayoutconfiguration-syntax.yaml"></a>

```
  [CanvasSizeOptions](#cfn-quicksight-analysis-freeformlayoutconfiguration-canvassizeoptions): {{
    FreeFormLayoutCanvasSizeOptions}}
  [Elements](#cfn-quicksight-analysis-freeformlayoutconfiguration-elements): {{
    - FreeFormLayoutElement}}
```

## Properties
<a name="aws-properties-quicksight-analysis-freeformlayoutconfiguration-properties"></a>

`CanvasSizeOptions`  <a name="cfn-quicksight-analysis-freeformlayoutconfiguration-canvassizeoptions"></a>
Property description not available.
*Required*: No
*Type*: [FreeFormLayoutCanvasSizeOptions](aws-properties-quicksight-analysis-freeformlayoutcanvassizeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Elements`  <a name="cfn-quicksight-analysis-freeformlayoutconfiguration-elements"></a>
The elements that are included in a free-form layout.
*Required*: Yes
*Type*: Array of [FreeFormLayoutElement](aws-properties-quicksight-analysis-freeformlayoutelement.md)
*Minimum*: `0`
*Maximum*: `430`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
