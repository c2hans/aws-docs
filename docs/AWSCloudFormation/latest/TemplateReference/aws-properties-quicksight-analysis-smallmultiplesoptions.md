---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-smallmultiplesoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SmallMultiplesOptions
<a name="aws-properties-quicksight-analysis-smallmultiplesoptions"></a>

Options that determine the layout and display options of a chart's small multiples.

## Syntax
<a name="aws-properties-quicksight-analysis-smallmultiplesoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-smallmultiplesoptions-syntax.json"></a>

```
{
  "[MaxVisibleColumns](#cfn-quicksight-analysis-smallmultiplesoptions-maxvisiblecolumns)" : {{Number}},
  "[MaxVisibleRows](#cfn-quicksight-analysis-smallmultiplesoptions-maxvisiblerows)" : {{Number}},
  "[PanelConfiguration](#cfn-quicksight-analysis-smallmultiplesoptions-panelconfiguration)" : {{PanelConfiguration}},
  "[XAxis](#cfn-quicksight-analysis-smallmultiplesoptions-xaxis)" : {{SmallMultiplesAxisProperties}},
  "[YAxis](#cfn-quicksight-analysis-smallmultiplesoptions-yaxis)" : {{SmallMultiplesAxisProperties}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-smallmultiplesoptions-syntax.yaml"></a>

```
  [MaxVisibleColumns](#cfn-quicksight-analysis-smallmultiplesoptions-maxvisiblecolumns): {{Number}}
  [MaxVisibleRows](#cfn-quicksight-analysis-smallmultiplesoptions-maxvisiblerows): {{Number}}
  [PanelConfiguration](#cfn-quicksight-analysis-smallmultiplesoptions-panelconfiguration): {{
    PanelConfiguration}}
  [XAxis](#cfn-quicksight-analysis-smallmultiplesoptions-xaxis): {{
    SmallMultiplesAxisProperties}}
  [YAxis](#cfn-quicksight-analysis-smallmultiplesoptions-yaxis): {{
    SmallMultiplesAxisProperties}}
```

## Properties
<a name="aws-properties-quicksight-analysis-smallmultiplesoptions-properties"></a>

`MaxVisibleColumns`  <a name="cfn-quicksight-analysis-smallmultiplesoptions-maxvisiblecolumns"></a>
Sets the maximum number of visible columns to display in the grid of small multiples panels.
The default is `Auto`, which automatically adjusts the columns in the grid to fit the overall layout and size of the given chart.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxVisibleRows`  <a name="cfn-quicksight-analysis-smallmultiplesoptions-maxvisiblerows"></a>
Sets the maximum number of visible rows to display in the grid of small multiples panels.
The default value is `Auto`, which automatically adjusts the rows in the grid to fit the overall layout and size of the given chart.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PanelConfiguration`  <a name="cfn-quicksight-analysis-smallmultiplesoptions-panelconfiguration"></a>
Configures the display options for each small multiples panel.
*Required*: No
*Type*: [PanelConfiguration](aws-properties-quicksight-analysis-panelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxis`  <a name="cfn-quicksight-analysis-smallmultiplesoptions-xaxis"></a>
The properties of a small multiples X axis.
*Required*: No
*Type*: [SmallMultiplesAxisProperties](aws-properties-quicksight-analysis-smallmultiplesaxisproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxis`  <a name="cfn-quicksight-analysis-smallmultiplesoptions-yaxis"></a>
The properties of a small multiples Y axis.
*Required*: No
*Type*: [SmallMultiplesAxisProperties](aws-properties-quicksight-analysis-smallmultiplesaxisproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
