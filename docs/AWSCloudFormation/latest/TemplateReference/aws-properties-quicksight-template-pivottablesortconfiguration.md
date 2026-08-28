---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-pivottablesortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template PivotTableSortConfiguration
<a name="aws-properties-quicksight-template-pivottablesortconfiguration"></a>

The sort configuration for a `PivotTableVisual`.

## Syntax
<a name="aws-properties-quicksight-template-pivottablesortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-pivottablesortconfiguration-syntax.json"></a>

```
{
  "[FieldSortOptions](#cfn-quicksight-template-pivottablesortconfiguration-fieldsortoptions)" : {{[ PivotFieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-pivottablesortconfiguration-syntax.yaml"></a>

```
  [FieldSortOptions](#cfn-quicksight-template-pivottablesortconfiguration-fieldsortoptions): {{
    - PivotFieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-template-pivottablesortconfiguration-properties"></a>

`FieldSortOptions`  <a name="cfn-quicksight-template-pivottablesortconfiguration-fieldsortoptions"></a>
The field sort options for a pivot table sort configuration.
*Required*: No
*Type*: [Array](aws-properties-quicksight-template-fieldsortoptions.md) of [PivotFieldSortOptions](aws-properties-quicksight-template-pivotfieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
