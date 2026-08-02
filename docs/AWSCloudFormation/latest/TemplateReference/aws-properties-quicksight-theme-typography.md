---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-typography.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme Typography
<a name="aws-properties-quicksight-theme-typography"></a>

Determines the typography options.

## Syntax
<a name="aws-properties-quicksight-theme-typography-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-typography-syntax.json"></a>

```
{
  "[FontFamilies](#cfn-quicksight-theme-typography-fontfamilies)" : {{[ Font, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-typography-syntax.yaml"></a>

```
  [FontFamilies](#cfn-quicksight-theme-typography-fontfamilies): {{
    - Font}}
```

## Properties
<a name="aws-properties-quicksight-theme-typography-properties"></a>

`FontFamilies`  <a name="cfn-quicksight-theme-typography-fontfamilies"></a>
Determines the list of font families.
*Required*: No
*Type*: Array of [Font](aws-properties-quicksight-theme-font.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
