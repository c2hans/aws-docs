---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filledmapsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilledMapSortConfiguration
<a name="aws-properties-quicksight-template-filledmapsortconfiguration"></a>

The sort configuration of a `FilledMapVisual`.

## Syntax
<a name="aws-properties-quicksight-template-filledmapsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filledmapsortconfiguration-syntax.json"></a>

```
{
  "[CategorySort](#cfn-quicksight-template-filledmapsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filledmapsortconfiguration-syntax.yaml"></a>

```
  [CategorySort](#cfn-quicksight-template-filledmapsortconfiguration-categorysort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-filledmapsortconfiguration-properties"></a>

`CategorySort`  <a name="cfn-quicksight-template-filledmapsortconfiguration-categorysort"></a>
The sort configuration of the location fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-template-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
