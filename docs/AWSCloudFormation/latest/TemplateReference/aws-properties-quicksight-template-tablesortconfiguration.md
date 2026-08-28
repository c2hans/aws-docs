---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablesortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableSortConfiguration
<a name="aws-properties-quicksight-template-tablesortconfiguration"></a>

The sort configuration for a `TableVisual`.

## Syntax
<a name="aws-properties-quicksight-template-tablesortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablesortconfiguration-syntax.json"></a>

```
{
  "[PaginationConfiguration](#cfn-quicksight-template-tablesortconfiguration-paginationconfiguration)" : {{PaginationConfiguration}},
  "[RowSort](#cfn-quicksight-template-tablesortconfiguration-rowsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablesortconfiguration-syntax.yaml"></a>

```
  [PaginationConfiguration](#cfn-quicksight-template-tablesortconfiguration-paginationconfiguration): {{
    PaginationConfiguration}}
  [RowSort](#cfn-quicksight-template-tablesortconfiguration-rowsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-tablesortconfiguration-properties"></a>

`PaginationConfiguration`  <a name="cfn-quicksight-template-tablesortconfiguration-paginationconfiguration"></a>
The pagination configuration (page size, page number) for the table.
*Required*: No
*Type*: [PaginationConfiguration](aws-properties-quicksight-template-paginationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowSort`  <a name="cfn-quicksight-template-tablesortconfiguration-rowsort"></a>
The field sort options for rows in the table.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-template-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
