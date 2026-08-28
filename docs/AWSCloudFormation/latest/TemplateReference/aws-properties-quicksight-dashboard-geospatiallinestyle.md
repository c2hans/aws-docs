---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatiallinestyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialLineStyle
<a name="aws-properties-quicksight-dashboard-geospatiallinestyle"></a>

The visualization style for a line layer.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatiallinestyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatiallinestyle-syntax.json"></a>

```
{
  "[LineSymbolStyle](#cfn-quicksight-dashboard-geospatiallinestyle-linesymbolstyle)" : {{GeospatialLineSymbolStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatiallinestyle-syntax.yaml"></a>

```
  [LineSymbolStyle](#cfn-quicksight-dashboard-geospatiallinestyle-linesymbolstyle): {{
    GeospatialLineSymbolStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatiallinestyle-properties"></a>

`LineSymbolStyle`  <a name="cfn-quicksight-dashboard-geospatiallinestyle-linesymbolstyle"></a>
The symbol style for a line style.
*Required*: No
*Type*: [GeospatialLineSymbolStyle](aws-properties-quicksight-dashboard-geospatiallinesymbolstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
