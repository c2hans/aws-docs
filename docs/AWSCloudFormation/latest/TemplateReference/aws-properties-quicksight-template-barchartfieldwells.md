---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-barchartfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BarChartFieldWells
<a name="aws-properties-quicksight-template-barchartfieldwells"></a>

The field wells of a `BarChartVisual`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-template-barchartfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-barchartfieldwells-syntax.json"></a>

```
{
  "[BarChartAggregatedFieldWells](#cfn-quicksight-template-barchartfieldwells-barchartaggregatedfieldwells)" : {{BarChartAggregatedFieldWells}}
}
```

### YAML
<a name="aws-properties-quicksight-template-barchartfieldwells-syntax.yaml"></a>

```
  [BarChartAggregatedFieldWells](#cfn-quicksight-template-barchartfieldwells-barchartaggregatedfieldwells): {{
    BarChartAggregatedFieldWells}}
```

## Properties
<a name="aws-properties-quicksight-template-barchartfieldwells-properties"></a>

`BarChartAggregatedFieldWells`  <a name="cfn-quicksight-template-barchartfieldwells-barchartaggregatedfieldwells"></a>
The aggregated field wells of a bar chart.
*Required*: No
*Type*: [BarChartAggregatedFieldWells](aws-properties-quicksight-template-barchartaggregatedfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
