---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialnulldatasettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialNullDataSettings
<a name="aws-properties-quicksight-dashboard-geospatialnulldatasettings"></a>

The properties for the visualization of null data.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialnulldatasettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialnulldatasettings-syntax.json"></a>

```
{
  "[SymbolStyle](#cfn-quicksight-dashboard-geospatialnulldatasettings-symbolstyle)" : {{GeospatialNullSymbolStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialnulldatasettings-syntax.yaml"></a>

```
  [SymbolStyle](#cfn-quicksight-dashboard-geospatialnulldatasettings-symbolstyle): {{
    GeospatialNullSymbolStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialnulldatasettings-properties"></a>

`SymbolStyle`  <a name="cfn-quicksight-dashboard-geospatialnulldatasettings-symbolstyle"></a>
The symbol style for null data.
*Required*: Yes
*Type*: [GeospatialNullSymbolStyle](aws-properties-quicksight-dashboard-geospatialnullsymbolstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
