---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-gridlayoutscreencanvassizeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GridLayoutScreenCanvasSizeOptions
<a name="aws-properties-quicksight-dashboard-gridlayoutscreencanvassizeoptions"></a>

The options that determine the sizing of the canvas used in a grid layout.

## Syntax
<a name="aws-properties-quicksight-dashboard-gridlayoutscreencanvassizeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-gridlayoutscreencanvassizeoptions-syntax.json"></a>

```
{
  "[OptimizedViewPortWidth](#cfn-quicksight-dashboard-gridlayoutscreencanvassizeoptions-optimizedviewportwidth)" : {{String}},
  "[ResizeOption](#cfn-quicksight-dashboard-gridlayoutscreencanvassizeoptions-resizeoption)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-gridlayoutscreencanvassizeoptions-syntax.yaml"></a>

```
  [OptimizedViewPortWidth](#cfn-quicksight-dashboard-gridlayoutscreencanvassizeoptions-optimizedviewportwidth): {{String}}
  [ResizeOption](#cfn-quicksight-dashboard-gridlayoutscreencanvassizeoptions-resizeoption): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-gridlayoutscreencanvassizeoptions-properties"></a>

`OptimizedViewPortWidth`  <a name="cfn-quicksight-dashboard-gridlayoutscreencanvassizeoptions-optimizedviewportwidth"></a>
The width that the view port will be optimized for when the layout renders.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResizeOption`  <a name="cfn-quicksight-dashboard-gridlayoutscreencanvassizeoptions-resizeoption"></a>
This value determines the layout behavior when the viewport is resized.
+ `FIXED`: A fixed width will be used when optimizing the layout. In the Quick Sight console, this option is called `Classic`.
+ `RESPONSIVE`: The width of the canvas will be responsive and optimized to the view port. In the Quick Sight console, this option is called `Tiled`.
*Required*: Yes
*Type*: String
*Allowed values*: `FIXED | RESPONSIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
