---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-freeformlayoutcanvassizeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FreeFormLayoutCanvasSizeOptions
<a name="aws-properties-quicksight-template-freeformlayoutcanvassizeoptions"></a>

Configuration options for the canvas of a free-form layout.

## Syntax
<a name="aws-properties-quicksight-template-freeformlayoutcanvassizeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-freeformlayoutcanvassizeoptions-syntax.json"></a>

```
{
  "[ScreenCanvasSizeOptions](#cfn-quicksight-template-freeformlayoutcanvassizeoptions-screencanvassizeoptions)" : {{FreeFormLayoutScreenCanvasSizeOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-freeformlayoutcanvassizeoptions-syntax.yaml"></a>

```
  [ScreenCanvasSizeOptions](#cfn-quicksight-template-freeformlayoutcanvassizeoptions-screencanvassizeoptions): {{
    FreeFormLayoutScreenCanvasSizeOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-freeformlayoutcanvassizeoptions-properties"></a>

`ScreenCanvasSizeOptions`  <a name="cfn-quicksight-template-freeformlayoutcanvassizeoptions-screencanvassizeoptions"></a>
The options that determine the sizing of the canvas used in a free-form layout.
*Required*: No
*Type*: [FreeFormLayoutScreenCanvasSizeOptions](aws-properties-quicksight-template-freeformlayoutscreencanvassizeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
