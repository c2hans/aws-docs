---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-filledmapshapeconditionalformatting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FilledMapShapeConditionalFormatting
<a name="aws-properties-quicksight-analysis-filledmapshapeconditionalformatting"></a>

The conditional formatting that determines the shape of the filled map.

## Syntax
<a name="aws-properties-quicksight-analysis-filledmapshapeconditionalformatting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-filledmapshapeconditionalformatting-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-analysis-filledmapshapeconditionalformatting-fieldid)" : {{String}},
  "[Format](#cfn-quicksight-analysis-filledmapshapeconditionalformatting-format)" : {{ShapeConditionalFormat}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-filledmapshapeconditionalformatting-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-analysis-filledmapshapeconditionalformatting-fieldid): {{String}}
  [Format](#cfn-quicksight-analysis-filledmapshapeconditionalformatting-format): {{
    ShapeConditionalFormat}}
```

## Properties
<a name="aws-properties-quicksight-analysis-filledmapshapeconditionalformatting-properties"></a>

`FieldId`  <a name="cfn-quicksight-analysis-filledmapshapeconditionalformatting-fieldid"></a>
The field ID of the filled map shape.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-quicksight-analysis-filledmapshapeconditionalformatting-format"></a>
The conditional formatting that determines the background color of a filled map's shape.
*Required*: No
*Type*: [ShapeConditionalFormat](aws-properties-quicksight-analysis-shapeconditionalformat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
