---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-gaugechartfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GaugeChartFieldWells
<a name="aws-properties-quicksight-template-gaugechartfieldwells"></a>

The field well configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-gaugechartfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-gaugechartfieldwells-syntax.json"></a>

```
{
  "[TargetValues](#cfn-quicksight-template-gaugechartfieldwells-targetvalues)" : {{[ MeasureField, ... ]}},
  "[Values](#cfn-quicksight-template-gaugechartfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-gaugechartfieldwells-syntax.yaml"></a>

```
  [TargetValues](#cfn-quicksight-template-gaugechartfieldwells-targetvalues): {{
    - MeasureField}}
  [Values](#cfn-quicksight-template-gaugechartfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-gaugechartfieldwells-properties"></a>

`TargetValues`  <a name="cfn-quicksight-template-gaugechartfieldwells-targetvalues"></a>
The target value field wells of a `GaugeChartVisual`.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-gaugechartfieldwells-values"></a>
The value field wells of a `GaugeChartVisual`.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
