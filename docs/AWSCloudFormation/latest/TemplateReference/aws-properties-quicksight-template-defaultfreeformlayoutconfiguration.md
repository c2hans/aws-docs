---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaultfreeformlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultFreeFormLayoutConfiguration
<a name="aws-properties-quicksight-template-defaultfreeformlayoutconfiguration"></a>

The options that determine the default settings of a free-form layout configuration.

## Syntax
<a name="aws-properties-quicksight-template-defaultfreeformlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaultfreeformlayoutconfiguration-syntax.json"></a>

```
{
  "[CanvasSizeOptions](#cfn-quicksight-template-defaultfreeformlayoutconfiguration-canvassizeoptions)" : {{FreeFormLayoutCanvasSizeOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaultfreeformlayoutconfiguration-syntax.yaml"></a>

```
  [CanvasSizeOptions](#cfn-quicksight-template-defaultfreeformlayoutconfiguration-canvassizeoptions): {{
    FreeFormLayoutCanvasSizeOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-defaultfreeformlayoutconfiguration-properties"></a>

`CanvasSizeOptions`  <a name="cfn-quicksight-template-defaultfreeformlayoutconfiguration-canvassizeoptions"></a>
Determines the screen canvas size options for a free-form layout.
*Required*: Yes
*Type*: [FreeFormLayoutCanvasSizeOptions](aws-properties-quicksight-template-freeformlayoutcanvassizeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
