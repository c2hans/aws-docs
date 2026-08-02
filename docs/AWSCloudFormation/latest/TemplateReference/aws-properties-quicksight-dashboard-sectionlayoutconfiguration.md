---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sectionlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SectionLayoutConfiguration
<a name="aws-properties-quicksight-dashboard-sectionlayoutconfiguration"></a>

The layout configuration of a section.

## Syntax
<a name="aws-properties-quicksight-dashboard-sectionlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sectionlayoutconfiguration-syntax.json"></a>

```
{
  "[FreeFormLayout](#cfn-quicksight-dashboard-sectionlayoutconfiguration-freeformlayout)" : {{FreeFormSectionLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sectionlayoutconfiguration-syntax.yaml"></a>

```
  [FreeFormLayout](#cfn-quicksight-dashboard-sectionlayoutconfiguration-freeformlayout): {{
    FreeFormSectionLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sectionlayoutconfiguration-properties"></a>

`FreeFormLayout`  <a name="cfn-quicksight-dashboard-sectionlayoutconfiguration-freeformlayout"></a>
The free-form layout configuration of a section.
*Required*: Yes
*Type*: [FreeFormSectionLayoutConfiguration](aws-properties-quicksight-dashboard-freeformsectionlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
