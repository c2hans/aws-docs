---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialnullsymbolstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialNullSymbolStyle
<a name="aws-properties-quicksight-template-geospatialnullsymbolstyle"></a>

The symbol style for null data.

## Syntax
<a name="aws-properties-quicksight-template-geospatialnullsymbolstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialnullsymbolstyle-syntax.json"></a>

```
{
  "[FillColor](#cfn-quicksight-template-geospatialnullsymbolstyle-fillcolor)" : {{String}},
  "[StrokeColor](#cfn-quicksight-template-geospatialnullsymbolstyle-strokecolor)" : {{String}},
  "[StrokeWidth](#cfn-quicksight-template-geospatialnullsymbolstyle-strokewidth)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialnullsymbolstyle-syntax.yaml"></a>

```
  [FillColor](#cfn-quicksight-template-geospatialnullsymbolstyle-fillcolor): {{String}}
  [StrokeColor](#cfn-quicksight-template-geospatialnullsymbolstyle-strokecolor): {{String}}
  [StrokeWidth](#cfn-quicksight-template-geospatialnullsymbolstyle-strokewidth): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialnullsymbolstyle-properties"></a>

`FillColor`  <a name="cfn-quicksight-template-geospatialnullsymbolstyle-fillcolor"></a>
The color and opacity values for the fill color.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeColor`  <a name="cfn-quicksight-template-geospatialnullsymbolstyle-strokecolor"></a>
The color and opacity values for the stroke color.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StrokeWidth`  <a name="cfn-quicksight-template-geospatialnullsymbolstyle-strokewidth"></a>
The width of the border stroke.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
