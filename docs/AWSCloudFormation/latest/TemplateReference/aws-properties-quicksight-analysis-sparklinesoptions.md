---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sparklinesoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SparklinesOptions
<a name="aws-properties-quicksight-analysis-sparklinesoptions"></a>

The options for sparklines in a table.

## Syntax
<a name="aws-properties-quicksight-analysis-sparklinesoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sparklinesoptions-syntax.json"></a>

```
{
  "[AllPointsMarker](#cfn-quicksight-analysis-sparklinesoptions-allpointsmarker)" : {{LineChartMarkerStyleSettings}},
  "[FieldId](#cfn-quicksight-analysis-sparklinesoptions-fieldid)" : {{String}},
  "[LineColor](#cfn-quicksight-analysis-sparklinesoptions-linecolor)" : {{String}},
  "[LineInterpolation](#cfn-quicksight-analysis-sparklinesoptions-lineinterpolation)" : {{String}},
  "[MaxValueMarker](#cfn-quicksight-analysis-sparklinesoptions-maxvaluemarker)" : {{LineChartMarkerStyleSettings}},
  "[MinValueMarker](#cfn-quicksight-analysis-sparklinesoptions-minvaluemarker)" : {{LineChartMarkerStyleSettings}},
  "[VisualType](#cfn-quicksight-analysis-sparklinesoptions-visualtype)" : {{String}},
  "[XAxisField](#cfn-quicksight-analysis-sparklinesoptions-xaxisfield)" : {{DimensionField}},
  "[YAxisBehavior](#cfn-quicksight-analysis-sparklinesoptions-yaxisbehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sparklinesoptions-syntax.yaml"></a>

```
  [AllPointsMarker](#cfn-quicksight-analysis-sparklinesoptions-allpointsmarker): {{
    LineChartMarkerStyleSettings}}
  [FieldId](#cfn-quicksight-analysis-sparklinesoptions-fieldid): {{String}}
  [LineColor](#cfn-quicksight-analysis-sparklinesoptions-linecolor): {{String}}
  [LineInterpolation](#cfn-quicksight-analysis-sparklinesoptions-lineinterpolation): {{String}}
  [MaxValueMarker](#cfn-quicksight-analysis-sparklinesoptions-maxvaluemarker): {{
    LineChartMarkerStyleSettings}}
  [MinValueMarker](#cfn-quicksight-analysis-sparklinesoptions-minvaluemarker): {{
    LineChartMarkerStyleSettings}}
  [VisualType](#cfn-quicksight-analysis-sparklinesoptions-visualtype): {{String}}
  [XAxisField](#cfn-quicksight-analysis-sparklinesoptions-xaxisfield): {{
    DimensionField}}
  [YAxisBehavior](#cfn-quicksight-analysis-sparklinesoptions-yaxisbehavior): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sparklinesoptions-properties"></a>

`AllPointsMarker`  <a name="cfn-quicksight-analysis-sparklinesoptions-allpointsmarker"></a>
Property description not available.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-analysis-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldId`  <a name="cfn-quicksight-analysis-sparklinesoptions-fieldid"></a>
The field ID of the value column that the sparkline is applied to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineColor`  <a name="cfn-quicksight-analysis-sparklinesoptions-linecolor"></a>
The color of the sparkline line.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineInterpolation`  <a name="cfn-quicksight-analysis-sparklinesoptions-lineinterpolation"></a>
The interpolation style for the sparkline line.
*Required*: No
*Type*: String
*Allowed values*: `LINEAR | SMOOTH | STEPPED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxValueMarker`  <a name="cfn-quicksight-analysis-sparklinesoptions-maxvaluemarker"></a>
Property description not available.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-analysis-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinValueMarker`  <a name="cfn-quicksight-analysis-sparklinesoptions-minvaluemarker"></a>
Property description not available.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-analysis-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualType`  <a name="cfn-quicksight-analysis-sparklinesoptions-visualtype"></a>
The type of the sparkline. Valid values are `LINE` and `AREA_LINE`.
*Required*: No
*Type*: String
*Allowed values*: `LINE | AREA_LINE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisField`  <a name="cfn-quicksight-analysis-sparklinesoptions-xaxisfield"></a>
Property description not available.
*Required*: Yes
*Type*: [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxisBehavior`  <a name="cfn-quicksight-analysis-sparklinesoptions-yaxisbehavior"></a>
Determines whether the Y axis is shared across all sparklines or independent for each sparkline.
*Required*: No
*Type*: String
*Allowed values*: `SHARED | INDEPENDENT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
