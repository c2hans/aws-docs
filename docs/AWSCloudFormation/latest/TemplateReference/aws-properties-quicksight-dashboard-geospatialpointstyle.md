---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialpointstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialPointStyle
<a name="aws-properties-quicksight-dashboard-geospatialpointstyle"></a>

The point style for a point layer.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialpointstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialpointstyle-syntax.json"></a>

```
{
  "[CircleSymbolStyle](#cfn-quicksight-dashboard-geospatialpointstyle-circlesymbolstyle)" : {{GeospatialCircleSymbolStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialpointstyle-syntax.yaml"></a>

```
  [CircleSymbolStyle](#cfn-quicksight-dashboard-geospatialpointstyle-circlesymbolstyle): {{
    GeospatialCircleSymbolStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialpointstyle-properties"></a>

`CircleSymbolStyle`  <a name="cfn-quicksight-dashboard-geospatialpointstyle-circlesymbolstyle"></a>
The circle symbol style for a point layer.
*Required*: No
*Type*: [GeospatialCircleSymbolStyle](aws-properties-quicksight-dashboard-geospatialcirclesymbolstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
