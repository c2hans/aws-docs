---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-barchartfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis BarChartFieldWells
<a name="aws-properties-quicksight-analysis-barchartfieldwells"></a>

The field wells of a `BarChartVisual`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-barchartfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-barchartfieldwells-syntax.json"></a>

```
{
  "[BarChartAggregatedFieldWells](#cfn-quicksight-analysis-barchartfieldwells-barchartaggregatedfieldwells)" : {{BarChartAggregatedFieldWells}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-barchartfieldwells-syntax.yaml"></a>

```
  [BarChartAggregatedFieldWells](#cfn-quicksight-analysis-barchartfieldwells-barchartaggregatedfieldwells): {{
    BarChartAggregatedFieldWells}}
```

## Properties
<a name="aws-properties-quicksight-analysis-barchartfieldwells-properties"></a>

`BarChartAggregatedFieldWells`  <a name="cfn-quicksight-analysis-barchartfieldwells-barchartaggregatedfieldwells"></a>
The aggregated field wells of a bar chart.
*Required*: No
*Type*: [BarChartAggregatedFieldWells](aws-properties-quicksight-analysis-barchartaggregatedfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
