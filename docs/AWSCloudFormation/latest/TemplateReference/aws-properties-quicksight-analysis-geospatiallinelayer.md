---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatiallinelayer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialLineLayer
<a name="aws-properties-quicksight-analysis-geospatiallinelayer"></a>

The geospatial Line layer.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatiallinelayer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatiallinelayer-syntax.json"></a>

```
{
  "[Style](#cfn-quicksight-analysis-geospatiallinelayer-style)" : {{GeospatialLineStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatiallinelayer-syntax.yaml"></a>

```
  [Style](#cfn-quicksight-analysis-geospatiallinelayer-style): {{
    GeospatialLineStyle}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatiallinelayer-properties"></a>

`Style`  <a name="cfn-quicksight-analysis-geospatiallinelayer-style"></a>
The visualization style for a line layer.
*Required*: Yes
*Type*: [GeospatialLineStyle](aws-properties-quicksight-analysis-geospatiallinestyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
