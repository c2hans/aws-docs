---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-geospatialcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GeospatialColor
<a name="aws-properties-quicksight-analysis-geospatialcolor"></a>

The visualization properties for solid, gradient, and categorical colors.

## Syntax
<a name="aws-properties-quicksight-analysis-geospatialcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-geospatialcolor-syntax.json"></a>

```
{
  "[Categorical](#cfn-quicksight-analysis-geospatialcolor-categorical)" : {{GeospatialCategoricalColor}},
  "[Gradient](#cfn-quicksight-analysis-geospatialcolor-gradient)" : {{GeospatialGradientColor}},
  "[Solid](#cfn-quicksight-analysis-geospatialcolor-solid)" : {{GeospatialSolidColor}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-geospatialcolor-syntax.yaml"></a>

```
  [Categorical](#cfn-quicksight-analysis-geospatialcolor-categorical): {{
    GeospatialCategoricalColor}}
  [Gradient](#cfn-quicksight-analysis-geospatialcolor-gradient): {{
    GeospatialGradientColor}}
  [Solid](#cfn-quicksight-analysis-geospatialcolor-solid): {{
    GeospatialSolidColor}}
```

## Properties
<a name="aws-properties-quicksight-analysis-geospatialcolor-properties"></a>

`Categorical`  <a name="cfn-quicksight-analysis-geospatialcolor-categorical"></a>
The visualization properties for the categorical color.
*Required*: No
*Type*: [GeospatialCategoricalColor](aws-properties-quicksight-analysis-geospatialcategoricalcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Gradient`  <a name="cfn-quicksight-analysis-geospatialcolor-gradient"></a>
The visualization properties for the gradient color.
*Required*: No
*Type*: [GeospatialGradientColor](aws-properties-quicksight-analysis-geospatialgradientcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Solid`  <a name="cfn-quicksight-analysis-geospatialcolor-solid"></a>
The visualization properties for the solid color.
*Required*: No
*Type*: [GeospatialSolidColor](aws-properties-quicksight-analysis-geospatialsolidcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
