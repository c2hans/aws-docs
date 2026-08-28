---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpifieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPIFieldWells
<a name="aws-properties-quicksight-template-kpifieldwells"></a>

The field well configuration of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpifieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpifieldwells-syntax.json"></a>

```
{
  "[TargetValues](#cfn-quicksight-template-kpifieldwells-targetvalues)" : {{[ MeasureField, ... ]}},
  "[TrendGroups](#cfn-quicksight-template-kpifieldwells-trendgroups)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-template-kpifieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpifieldwells-syntax.yaml"></a>

```
  [TargetValues](#cfn-quicksight-template-kpifieldwells-targetvalues): {{
    - MeasureField}}
  [TrendGroups](#cfn-quicksight-template-kpifieldwells-trendgroups): {{
    - DimensionField}}
  [Values](#cfn-quicksight-template-kpifieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-kpifieldwells-properties"></a>

`TargetValues`  <a name="cfn-quicksight-template-kpifieldwells-targetvalues"></a>
The target value field wells of a KPI visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrendGroups`  <a name="cfn-quicksight-template-kpifieldwells-trendgroups"></a>
The trend group field wells of a KPI visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-kpifieldwells-values"></a>
The value field wells of a KPI visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
