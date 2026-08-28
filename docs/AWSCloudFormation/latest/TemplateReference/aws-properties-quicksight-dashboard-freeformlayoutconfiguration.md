---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-freeformlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FreeFormLayoutConfiguration
<a name="aws-properties-quicksight-dashboard-freeformlayoutconfiguration"></a>

The configuration of a free-form layout.

## Syntax
<a name="aws-properties-quicksight-dashboard-freeformlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-freeformlayoutconfiguration-syntax.json"></a>

```
{
  "[CanvasSizeOptions](#cfn-quicksight-dashboard-freeformlayoutconfiguration-canvassizeoptions)" : {{FreeFormLayoutCanvasSizeOptions}},
  "[Elements](#cfn-quicksight-dashboard-freeformlayoutconfiguration-elements)" : {{[ FreeFormLayoutElement, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-freeformlayoutconfiguration-syntax.yaml"></a>

```
  [CanvasSizeOptions](#cfn-quicksight-dashboard-freeformlayoutconfiguration-canvassizeoptions): {{
    FreeFormLayoutCanvasSizeOptions}}
  [Elements](#cfn-quicksight-dashboard-freeformlayoutconfiguration-elements): {{
    - FreeFormLayoutElement}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-freeformlayoutconfiguration-properties"></a>

`CanvasSizeOptions`  <a name="cfn-quicksight-dashboard-freeformlayoutconfiguration-canvassizeoptions"></a>
Property description not available.
*Required*: No
*Type*: [FreeFormLayoutCanvasSizeOptions](aws-properties-quicksight-dashboard-freeformlayoutcanvassizeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Elements`  <a name="cfn-quicksight-dashboard-freeformlayoutconfiguration-elements"></a>
The elements that are included in a free-form layout.
*Required*: Yes
*Type*: Array of [FreeFormLayoutElement](aws-properties-quicksight-dashboard-freeformlayoutelement.md)
*Minimum*: `0`
*Maximum*: `430`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
