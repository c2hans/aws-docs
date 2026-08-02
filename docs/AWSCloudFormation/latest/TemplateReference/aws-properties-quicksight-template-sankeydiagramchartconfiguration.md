---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sankeydiagramchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SankeyDiagramChartConfiguration
<a name="aws-properties-quicksight-template-sankeydiagramchartconfiguration"></a>

The configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-template-sankeydiagramchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sankeydiagramchartconfiguration-syntax.json"></a>

```
{
  "[DataLabels](#cfn-quicksight-template-sankeydiagramchartconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-template-sankeydiagramchartconfiguration-fieldwells)" : {{SankeyDiagramFieldWells}},
  "[Interactions](#cfn-quicksight-template-sankeydiagramchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[SortConfiguration](#cfn-quicksight-template-sankeydiagramchartconfiguration-sortconfiguration)" : {{SankeyDiagramSortConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sankeydiagramchartconfiguration-syntax.yaml"></a>

```
  [DataLabels](#cfn-quicksight-template-sankeydiagramchartconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-template-sankeydiagramchartconfiguration-fieldwells): {{
    SankeyDiagramFieldWells}}
  [Interactions](#cfn-quicksight-template-sankeydiagramchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [SortConfiguration](#cfn-quicksight-template-sankeydiagramchartconfiguration-sortconfiguration): {{
    SankeyDiagramSortConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-sankeydiagramchartconfiguration-properties"></a>

`DataLabels`  <a name="cfn-quicksight-template-sankeydiagramchartconfiguration-datalabels"></a>
The data label configuration of a sankey diagram.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-template-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-template-sankeydiagramchartconfiguration-fieldwells"></a>
The field well configuration of a sankey diagram.
*Required*: No
*Type*: [SankeyDiagramFieldWells](aws-properties-quicksight-template-sankeydiagramfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-sankeydiagramchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-template-sankeydiagramchartconfiguration-sortconfiguration"></a>
The sort configuration of a sankey diagram.
*Required*: No
*Type*: [SankeyDiagramSortConfiguration](aws-properties-quicksight-template-sankeydiagramsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
