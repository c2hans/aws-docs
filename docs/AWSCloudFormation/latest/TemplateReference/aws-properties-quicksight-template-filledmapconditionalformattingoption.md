---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-filledmapconditionalformattingoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FilledMapConditionalFormattingOption
<a name="aws-properties-quicksight-template-filledmapconditionalformattingoption"></a>

Conditional formatting options of a `FilledMapVisual`.

## Syntax
<a name="aws-properties-quicksight-template-filledmapconditionalformattingoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-filledmapconditionalformattingoption-syntax.json"></a>

```
{
  "[Shape](#cfn-quicksight-template-filledmapconditionalformattingoption-shape)" : {{FilledMapShapeConditionalFormatting}}
}
```

### YAML
<a name="aws-properties-quicksight-template-filledmapconditionalformattingoption-syntax.yaml"></a>

```
  [Shape](#cfn-quicksight-template-filledmapconditionalformattingoption-shape): {{
    FilledMapShapeConditionalFormatting}}
```

## Properties
<a name="aws-properties-quicksight-template-filledmapconditionalformattingoption-properties"></a>

`Shape`  <a name="cfn-quicksight-template-filledmapconditionalformattingoption-shape"></a>
The conditional formatting that determines the shape of the filled map.
*Required*: Yes
*Type*: [FilledMapShapeConditionalFormatting](aws-properties-quicksight-template-filledmapshapeconditionalformatting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
