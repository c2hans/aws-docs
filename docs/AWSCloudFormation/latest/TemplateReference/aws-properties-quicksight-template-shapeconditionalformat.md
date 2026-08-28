---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-shapeconditionalformat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ShapeConditionalFormat
<a name="aws-properties-quicksight-template-shapeconditionalformat"></a>

The shape conditional formatting of a filled map visual.

## Syntax
<a name="aws-properties-quicksight-template-shapeconditionalformat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-shapeconditionalformat-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-template-shapeconditionalformat-backgroundcolor)" : {{ConditionalFormattingColor}}
}
```

### YAML
<a name="aws-properties-quicksight-template-shapeconditionalformat-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-template-shapeconditionalformat-backgroundcolor): {{
    ConditionalFormattingColor}}
```

## Properties
<a name="aws-properties-quicksight-template-shapeconditionalformat-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-template-shapeconditionalformat-backgroundcolor"></a>
The conditional formatting for the shape background color of a filled map visual.
*Required*: Yes
*Type*: [ConditionalFormattingColor](aws-properties-quicksight-template-conditionalformattingcolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
