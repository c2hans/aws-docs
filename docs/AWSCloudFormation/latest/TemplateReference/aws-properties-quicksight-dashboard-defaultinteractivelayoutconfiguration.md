---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DefaultInteractiveLayoutConfiguration
<a name="aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration"></a>

The options that determine the default settings for interactive layout configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration-syntax.json"></a>

```
{
  "[FreeForm](#cfn-quicksight-dashboard-defaultinteractivelayoutconfiguration-freeform)" : {{DefaultFreeFormLayoutConfiguration}},
  "[Grid](#cfn-quicksight-dashboard-defaultinteractivelayoutconfiguration-grid)" : {{DefaultGridLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration-syntax.yaml"></a>

```
  [FreeForm](#cfn-quicksight-dashboard-defaultinteractivelayoutconfiguration-freeform): {{
    DefaultFreeFormLayoutConfiguration}}
  [Grid](#cfn-quicksight-dashboard-defaultinteractivelayoutconfiguration-grid): {{
    DefaultGridLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-defaultinteractivelayoutconfiguration-properties"></a>

`FreeForm`  <a name="cfn-quicksight-dashboard-defaultinteractivelayoutconfiguration-freeform"></a>
The options that determine the default settings of a free-form layout configuration.
*Required*: No
*Type*: [DefaultFreeFormLayoutConfiguration](aws-properties-quicksight-dashboard-defaultfreeformlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Grid`  <a name="cfn-quicksight-dashboard-defaultinteractivelayoutconfiguration-grid"></a>
The options that determine the default settings for a grid layout configuration.
*Required*: No
*Type*: [DefaultGridLayoutConfiguration](aws-properties-quicksight-dashboard-defaultgridlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
