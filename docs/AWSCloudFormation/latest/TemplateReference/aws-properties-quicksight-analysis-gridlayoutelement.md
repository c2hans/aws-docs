---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-gridlayoutelement.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GridLayoutElement
<a name="aws-properties-quicksight-analysis-gridlayoutelement"></a>

An element within a grid layout.

## Syntax
<a name="aws-properties-quicksight-analysis-gridlayoutelement-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-gridlayoutelement-syntax.json"></a>

```
{
  "[BackgroundStyle](#cfn-quicksight-analysis-gridlayoutelement-backgroundstyle)" : {{GridLayoutElementBackgroundStyle}},
  "[BorderRadius](#cfn-quicksight-analysis-gridlayoutelement-borderradius)" : {{String}},
  "[BorderStyle](#cfn-quicksight-analysis-gridlayoutelement-borderstyle)" : {{GridLayoutElementBorderStyle}},
  "[ColumnIndex](#cfn-quicksight-analysis-gridlayoutelement-columnindex)" : {{Number}},
  "[ColumnSpan](#cfn-quicksight-analysis-gridlayoutelement-columnspan)" : {{Number}},
  "[ElementId](#cfn-quicksight-analysis-gridlayoutelement-elementid)" : {{String}},
  "[ElementType](#cfn-quicksight-analysis-gridlayoutelement-elementtype)" : {{String}},
  "[LoadingAnimation](#cfn-quicksight-analysis-gridlayoutelement-loadinganimation)" : {{LoadingAnimation}},
  "[Padding](#cfn-quicksight-analysis-gridlayoutelement-padding)" : {{String}},
  "[RowIndex](#cfn-quicksight-analysis-gridlayoutelement-rowindex)" : {{Number}},
  "[RowSpan](#cfn-quicksight-analysis-gridlayoutelement-rowspan)" : {{Number}},
  "[SelectedBorderStyle](#cfn-quicksight-analysis-gridlayoutelement-selectedborderstyle)" : {{GridLayoutElementBorderStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-gridlayoutelement-syntax.yaml"></a>

```
  [BackgroundStyle](#cfn-quicksight-analysis-gridlayoutelement-backgroundstyle): {{
    GridLayoutElementBackgroundStyle}}
  [BorderRadius](#cfn-quicksight-analysis-gridlayoutelement-borderradius): {{String}}
  [BorderStyle](#cfn-quicksight-analysis-gridlayoutelement-borderstyle): {{
    GridLayoutElementBorderStyle}}
  [ColumnIndex](#cfn-quicksight-analysis-gridlayoutelement-columnindex): {{Number}}
  [ColumnSpan](#cfn-quicksight-analysis-gridlayoutelement-columnspan): {{Number}}
  [ElementId](#cfn-quicksight-analysis-gridlayoutelement-elementid): {{String}}
  [ElementType](#cfn-quicksight-analysis-gridlayoutelement-elementtype): {{String}}
  [LoadingAnimation](#cfn-quicksight-analysis-gridlayoutelement-loadinganimation): {{
    LoadingAnimation}}
  [Padding](#cfn-quicksight-analysis-gridlayoutelement-padding): {{String}}
  [RowIndex](#cfn-quicksight-analysis-gridlayoutelement-rowindex): {{Number}}
  [RowSpan](#cfn-quicksight-analysis-gridlayoutelement-rowspan): {{Number}}
  [SelectedBorderStyle](#cfn-quicksight-analysis-gridlayoutelement-selectedborderstyle): {{
    GridLayoutElementBorderStyle}}
```

## Properties
<a name="aws-properties-quicksight-analysis-gridlayoutelement-properties"></a>

`BackgroundStyle`  <a name="cfn-quicksight-analysis-gridlayoutelement-backgroundstyle"></a>
The background style configuration of a grid layout element.
*Required*: No
*Type*: [GridLayoutElementBackgroundStyle](aws-properties-quicksight-analysis-gridlayoutelementbackgroundstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorderRadius`  <a name="cfn-quicksight-analysis-gridlayoutelement-borderradius"></a>
The border radius of a grid layout element.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BorderStyle`  <a name="cfn-quicksight-analysis-gridlayoutelement-borderstyle"></a>
The border style configuration of a grid layout element.
*Required*: No
*Type*: [GridLayoutElementBorderStyle](aws-properties-quicksight-analysis-gridlayoutelementborderstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnIndex`  <a name="cfn-quicksight-analysis-gridlayoutelement-columnindex"></a>
The column index for the upper left corner of an element.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `35`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnSpan`  <a name="cfn-quicksight-analysis-gridlayoutelement-columnspan"></a>
The width of a grid element expressed as a number of grid columns.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElementId`  <a name="cfn-quicksight-analysis-gridlayoutelement-elementid"></a>
A unique identifier for an element within a grid layout.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ElementType`  <a name="cfn-quicksight-analysis-gridlayoutelement-elementtype"></a>
The type of element.
*Required*: Yes
*Type*: String
*Allowed values*: `VISUAL | FILTER_CONTROL | PARAMETER_CONTROL | TEXT_BOX | IMAGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadingAnimation`  <a name="cfn-quicksight-analysis-gridlayoutelement-loadinganimation"></a>
Property description not available.
*Required*: No
*Type*: [LoadingAnimation](aws-properties-quicksight-analysis-loadinganimation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Padding`  <a name="cfn-quicksight-analysis-gridlayoutelement-padding"></a>
The padding of a grid layout element.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowIndex`  <a name="cfn-quicksight-analysis-gridlayoutelement-rowindex"></a>
The row index for the upper left corner of an element.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `9009`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowSpan`  <a name="cfn-quicksight-analysis-gridlayoutelement-rowspan"></a>
The height of a grid element expressed as a number of grid rows.
*Required*: Yes
*Type*: Number
*Minimum*: `1`
*Maximum*: `21`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedBorderStyle`  <a name="cfn-quicksight-analysis-gridlayoutelement-selectedborderstyle"></a>
The border style configuration of a grid layout element. This border style is used when the element is selected.
*Required*: No
*Type*: [GridLayoutElementBorderStyle](aws-properties-quicksight-analysis-gridlayoutelementborderstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
