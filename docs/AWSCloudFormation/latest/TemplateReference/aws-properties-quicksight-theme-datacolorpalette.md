---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-datacolorpalette.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme DataColorPalette
<a name="aws-properties-quicksight-theme-datacolorpalette"></a>

The theme colors that are used for data colors in charts. The colors description is a hexadecimal color code that consists of six alphanumerical characters, prefixed with `#`, for example \#37BFF5.

## Syntax
<a name="aws-properties-quicksight-theme-datacolorpalette-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-datacolorpalette-syntax.json"></a>

```
{
  "[Colors](#cfn-quicksight-theme-datacolorpalette-colors)" : {{[ String, ... ]}},
  "[EmptyFillColor](#cfn-quicksight-theme-datacolorpalette-emptyfillcolor)" : {{String}},
  "[MinMaxGradient](#cfn-quicksight-theme-datacolorpalette-minmaxgradient)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-datacolorpalette-syntax.yaml"></a>

```
  [Colors](#cfn-quicksight-theme-datacolorpalette-colors): {{
    - String}}
  [EmptyFillColor](#cfn-quicksight-theme-datacolorpalette-emptyfillcolor): {{String}}
  [MinMaxGradient](#cfn-quicksight-theme-datacolorpalette-minmaxgradient): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-theme-datacolorpalette-properties"></a>

`Colors`  <a name="cfn-quicksight-theme-datacolorpalette-colors"></a>
The hexadecimal codes for the colors.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmptyFillColor`  <a name="cfn-quicksight-theme-datacolorpalette-emptyfillcolor"></a>
The hexadecimal code of a color that applies to charts where a lack of data is highlighted.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinMaxGradient`  <a name="cfn-quicksight-theme-datacolorpalette-minmaxgradient"></a>
The minimum and maximum hexadecimal codes that describe a color gradient.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
