---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-freeformsectionlayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FreeFormSectionLayoutConfiguration
<a name="aws-properties-quicksight-analysis-freeformsectionlayoutconfiguration"></a>

The free-form layout configuration of a section.

## Syntax
<a name="aws-properties-quicksight-analysis-freeformsectionlayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-freeformsectionlayoutconfiguration-syntax.json"></a>

```
{
  "[Elements](#cfn-quicksight-analysis-freeformsectionlayoutconfiguration-elements)" : {{[ FreeFormLayoutElement, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-freeformsectionlayoutconfiguration-syntax.yaml"></a>

```
  [Elements](#cfn-quicksight-analysis-freeformsectionlayoutconfiguration-elements): {{
    - FreeFormLayoutElement}}
```

## Properties
<a name="aws-properties-quicksight-analysis-freeformsectionlayoutconfiguration-properties"></a>

`Elements`  <a name="cfn-quicksight-analysis-freeformsectionlayoutconfiguration-elements"></a>
The elements that are included in the free-form layout.
*Required*: Yes
*Type*: Array of [FreeFormLayoutElement](aws-properties-quicksight-analysis-freeformlayoutelement.md)
*Minimum*: `0`
*Maximum*: `430`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
