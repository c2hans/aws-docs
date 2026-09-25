---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-tilestyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme TileStyle
<a name="aws-properties-quicksight-theme-tilestyle"></a>

Display options related to tiles on a sheet.

## Syntax
<a name="aws-properties-quicksight-theme-tilestyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-tilestyle-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-theme-tilestyle-backgroundcolor)" : {{String}},
  "[Border](#cfn-quicksight-theme-tilestyle-border)" : {{BorderStyle}},
  "[BorderRadius](#cfn-quicksight-theme-tilestyle-borderradius)" : {{String}},
  "[Padding](#cfn-quicksight-theme-tilestyle-padding)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-tilestyle-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-theme-tilestyle-backgroundcolor): {{String}}
  [Border](#cfn-quicksight-theme-tilestyle-border): {{
    BorderStyle}}
  [BorderRadius](#cfn-quicksight-theme-tilestyle-borderradius): {{String}}
  [Padding](#cfn-quicksight-theme-tilestyle-padding): {{String}}
```

## Properties
<a name="aws-properties-quicksight-theme-tilestyle-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-theme-tilestyle-backgroundcolor"></a>
The background color of a tile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Border`  <a name="cfn-quicksight-theme-tilestyle-border"></a>
The border around a tile.
*Required*: No
*Type*: [BorderStyle](aws-properties-quicksight-theme-borderstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorderRadius`  <a name="cfn-quicksight-theme-tilestyle-borderradius"></a>
The border radius of a tile.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Padding`  <a name="cfn-quicksight-theme-tilestyle-padding"></a>
The padding of a tile.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
