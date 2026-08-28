---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-defaultsectionbasedlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template DefaultSectionBasedLayoutConfiguration
<a name="aws-properties-quicksight-template-defaultsectionbasedlayoutconfiguration"></a>

The options that determine the default settings for a section-based layout configuration.

## Syntax
<a name="aws-properties-quicksight-template-defaultsectionbasedlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-defaultsectionbasedlayoutconfiguration-syntax.json"></a>

```
{
  "[CanvasSizeOptions](#cfn-quicksight-template-defaultsectionbasedlayoutconfiguration-canvassizeoptions)" : {{SectionBasedLayoutCanvasSizeOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-template-defaultsectionbasedlayoutconfiguration-syntax.yaml"></a>

```
  [CanvasSizeOptions](#cfn-quicksight-template-defaultsectionbasedlayoutconfiguration-canvassizeoptions): {{
    SectionBasedLayoutCanvasSizeOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-defaultsectionbasedlayoutconfiguration-properties"></a>

`CanvasSizeOptions`  <a name="cfn-quicksight-template-defaultsectionbasedlayoutconfiguration-canvassizeoptions"></a>
Determines the screen canvas size options for a section-based layout.
*Required*: Yes
*Type*: [SectionBasedLayoutCanvasSizeOptions](aws-properties-quicksight-template-sectionbasedlayoutcanvassizeoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
