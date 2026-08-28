---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-gridlayoutcanvassizeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis GridLayoutCanvasSizeOptions
<a name="aws-properties-quicksight-analysis-gridlayoutcanvassizeoptions"></a>

Configuration options for the canvas of a grid layout.

## Syntax
<a name="aws-properties-quicksight-analysis-gridlayoutcanvassizeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-gridlayoutcanvassizeoptions-syntax.json"></a>

```
{
  "[ScreenCanvasSizeOptions](#cfn-quicksight-analysis-gridlayoutcanvassizeoptions-screencanvassizeoptions)" : {{GridLayoutScreenCanvasSizeOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-gridlayoutcanvassizeoptions-syntax.yaml"></a>

```
  [ScreenCanvasSizeOptions](#cfn-quicksight-analysis-gridlayoutcanvassizeoptions-screencanvassizeoptions): {{
    GridLayoutScreenCanvasSizeOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-gridlayoutcanvassizeoptions-properties"></a>

`ScreenCanvasSizeOptions`  <a name="cfn-quicksight-analysis-gridlayoutcanvassizeoptions-screencanvassizeoptions"></a>
The options that determine the sizing of the canvas used in a grid layout.
*Required*: No
*Type*: [GridLayoutScreenCanvasSizeOptions](aws-properties-quicksight-analysis-gridlayoutscreencanvassizeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
