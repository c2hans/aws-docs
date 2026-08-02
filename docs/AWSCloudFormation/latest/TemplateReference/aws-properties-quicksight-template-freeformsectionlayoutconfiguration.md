---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-freeformsectionlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FreeFormSectionLayoutConfiguration
<a name="aws-properties-quicksight-template-freeformsectionlayoutconfiguration"></a>

The free-form layout configuration of a section.

## Syntax
<a name="aws-properties-quicksight-template-freeformsectionlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-freeformsectionlayoutconfiguration-syntax.json"></a>

```
{
  "[Elements](#cfn-quicksight-template-freeformsectionlayoutconfiguration-elements)" : {{[ FreeFormLayoutElement, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-freeformsectionlayoutconfiguration-syntax.yaml"></a>

```
  [Elements](#cfn-quicksight-template-freeformsectionlayoutconfiguration-elements): {{
    - FreeFormLayoutElement}}
```

## Properties
<a name="aws-properties-quicksight-template-freeformsectionlayoutconfiguration-properties"></a>

`Elements`  <a name="cfn-quicksight-template-freeformsectionlayoutconfiguration-elements"></a>
The elements that are included in the free-form layout.
*Required*: Yes
*Type*: Array of [FreeFormLayoutElement](aws-properties-quicksight-template-freeformlayoutelement.md)
*Minimum*: `0`
*Maximum*: `430`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
