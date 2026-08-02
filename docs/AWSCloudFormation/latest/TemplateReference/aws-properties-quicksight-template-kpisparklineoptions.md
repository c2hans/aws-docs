---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpisparklineoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPISparklineOptions
<a name="aws-properties-quicksight-template-kpisparklineoptions"></a>

The options that determine the visibility, color, type, and tooltip visibility of the sparkline of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpisparklineoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpisparklineoptions-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-template-kpisparklineoptions-color)" : {{String}},
  "[TooltipVisibility](#cfn-quicksight-template-kpisparklineoptions-tooltipvisibility)" : {{String}},
  "[Type](#cfn-quicksight-template-kpisparklineoptions-type)" : {{String}},
  "[Visibility](#cfn-quicksight-template-kpisparklineoptions-visibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpisparklineoptions-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-template-kpisparklineoptions-color): {{String}}
  [TooltipVisibility](#cfn-quicksight-template-kpisparklineoptions-tooltipvisibility): {{String}}
  [Type](#cfn-quicksight-template-kpisparklineoptions-type): {{String}}
  [Visibility](#cfn-quicksight-template-kpisparklineoptions-visibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-kpisparklineoptions-properties"></a>

`Color`  <a name="cfn-quicksight-template-kpisparklineoptions-color"></a>
The color of the sparkline.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipVisibility`  <a name="cfn-quicksight-template-kpisparklineoptions-tooltipvisibility"></a>
The tooltip visibility of the sparkline.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-template-kpisparklineoptions-type"></a>
The type of the sparkline.
*Required*: Yes
*Type*: String
*Allowed values*: `LINE | AREA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Visibility`  <a name="cfn-quicksight-template-kpisparklineoptions-visibility"></a>
The visibility of the sparkline.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
