---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-boxplotoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BoxPlotOptions
<a name="aws-properties-quicksight-template-boxplotoptions"></a>

The options of a box plot visual.

## Syntax
<a name="aws-properties-quicksight-template-boxplotoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-boxplotoptions-syntax.json"></a>

```
{
  "[AllDataPointsVisibility](#cfn-quicksight-template-boxplotoptions-alldatapointsvisibility)" : {{String}},
  "[OutlierVisibility](#cfn-quicksight-template-boxplotoptions-outliervisibility)" : {{String}},
  "[StyleOptions](#cfn-quicksight-template-boxplotoptions-styleoptions)" : {{BoxPlotStyleOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-boxplotoptions-syntax.yaml"></a>

```
  [AllDataPointsVisibility](#cfn-quicksight-template-boxplotoptions-alldatapointsvisibility): {{String}}
  [OutlierVisibility](#cfn-quicksight-template-boxplotoptions-outliervisibility): {{String}}
  [StyleOptions](#cfn-quicksight-template-boxplotoptions-styleoptions): {{
    BoxPlotStyleOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-boxplotoptions-properties"></a>

`AllDataPointsVisibility`  <a name="cfn-quicksight-template-boxplotoptions-alldatapointsvisibility"></a>
Determines the visibility of all data points of the box plot.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutlierVisibility`  <a name="cfn-quicksight-template-boxplotoptions-outliervisibility"></a>
Determines the visibility of the outlier in a box plot.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleOptions`  <a name="cfn-quicksight-template-boxplotoptions-styleoptions"></a>
The style options of the box plot.
*Required*: No
*Type*: [BoxPlotStyleOptions](aws-properties-quicksight-template-boxplotstyleoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
