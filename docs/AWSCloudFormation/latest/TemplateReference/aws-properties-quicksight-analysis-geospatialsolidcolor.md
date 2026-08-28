---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialsolidcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialSolidColor
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor"></a>

The definition for a solid color.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-syntax.json"></a>

```
{
  "[Color](#cfn-quicksight-analysis-geospatialsolidcolor-color)" : {{String}},
  "[State](#cfn-quicksight-analysis-geospatialsolidcolor-state)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-syntax.yaml"></a>

```
  [Color](#cfn-quicksight-analysis-geospatialsolidcolor-color): {{String}}
  [State](#cfn-quicksight-analysis-geospatialsolidcolor-state): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialsolidcolor-properties"></a>

`Color`  <a name="cfn-quicksight-analysis-geospatialsolidcolor-color"></a>
The color and opacity values for the color.
*Required*: Yes
*Type*: String
*Pattern*: `^#[A-F0-9]{6}(?:[A-F0-9]{2})?$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-quicksight-analysis-geospatialsolidcolor-state"></a>
Enables and disables the view state of the color.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
