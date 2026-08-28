---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-boxplotsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BoxPlotSortConfiguration
<a name="aws-properties-quicksight-template-boxplotsortconfiguration"></a>

The sort configuration of a `BoxPlotVisual`.

## Syntax
<a name="aws-properties-quicksight-template-boxplotsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-boxplotsortconfiguration-syntax.json"></a>

```
{
  "[CategorySort](#cfn-quicksight-template-boxplotsortconfiguration-categorysort)" : {{[ FieldSortOptions, ... ]}},
  "[PaginationConfiguration](#cfn-quicksight-template-boxplotsortconfiguration-paginationconfiguration)" : {{PaginationConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-boxplotsortconfiguration-syntax.yaml"></a>

```
  [CategorySort](#cfn-quicksight-template-boxplotsortconfiguration-categorysort): {{
    - FieldSortOptions}}
  [PaginationConfiguration](#cfn-quicksight-template-boxplotsortconfiguration-paginationconfiguration): {{
    PaginationConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-boxplotsortconfiguration-properties"></a>

`CategorySort`  <a name="cfn-quicksight-template-boxplotsortconfiguration-categorysort"></a>
The sort configuration of a group by fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-template-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaginationConfiguration`  <a name="cfn-quicksight-template-boxplotsortconfiguration-paginationconfiguration"></a>
The pagination configuration of a table visual or box plot.
*Required*: No
*Type*: [PaginationConfiguration](aws-properties-quicksight-template-paginationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
