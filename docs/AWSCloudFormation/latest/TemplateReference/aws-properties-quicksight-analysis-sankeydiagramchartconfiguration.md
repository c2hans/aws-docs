---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sankeydiagramchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SankeyDiagramChartConfiguration
<a name="aws-properties-quicksight-analysis-sankeydiagramchartconfiguration"></a>

The configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-analysis-sankeydiagramchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sankeydiagramchartconfiguration-syntax.json"></a>

```
{
  "[DataLabels](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-fieldwells)" : {{SankeyDiagramFieldWells}},
  "[Interactions](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[SortConfiguration](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-sortconfiguration)" : {{SankeyDiagramSortConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sankeydiagramchartconfiguration-syntax.yaml"></a>

```
  [DataLabels](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-fieldwells): {{
    SankeyDiagramFieldWells}}
  [Interactions](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [SortConfiguration](#cfn-quicksight-analysis-sankeydiagramchartconfiguration-sortconfiguration): {{
    SankeyDiagramSortConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sankeydiagramchartconfiguration-properties"></a>

`DataLabels`  <a name="cfn-quicksight-analysis-sankeydiagramchartconfiguration-datalabels"></a>
The data label configuration of a sankey diagram.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-analysis-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-analysis-sankeydiagramchartconfiguration-fieldwells"></a>
The field well configuration of a sankey diagram.
*Required*: No
*Type*: [SankeyDiagramFieldWells](aws-properties-quicksight-analysis-sankeydiagramfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-sankeydiagramchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-sankeydiagramchartconfiguration-sortconfiguration"></a>
The sort configuration of a sankey diagram.
*Required*: No
*Type*: [SankeyDiagramSortConfiguration](aws-properties-quicksight-analysis-sankeydiagramsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
