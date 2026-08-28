---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-treemapsortconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TreeMapSortConfiguration
<a name="aws-properties-quicksight-analysis-treemapsortconfiguration"></a>

The sort configuration of a tree map.

## Syntax
<a name="aws-properties-quicksight-analysis-treemapsortconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-treemapsortconfiguration-syntax.json"></a>

```
{
  "[TreeMapGroupItemsLimitConfiguration](#cfn-quicksight-analysis-treemapsortconfiguration-treemapgroupitemslimitconfiguration)" : {{ItemsLimitConfiguration}},
  "[TreeMapSort](#cfn-quicksight-analysis-treemapsortconfiguration-treemapsort)" : {{[ FieldSortOptions, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-treemapsortconfiguration-syntax.yaml"></a>

```
  [TreeMapGroupItemsLimitConfiguration](#cfn-quicksight-analysis-treemapsortconfiguration-treemapgroupitemslimitconfiguration): {{
    ItemsLimitConfiguration}}
  [TreeMapSort](#cfn-quicksight-analysis-treemapsortconfiguration-treemapsort): {{
    - FieldSortOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-treemapsortconfiguration-properties"></a>

`TreeMapGroupItemsLimitConfiguration`  <a name="cfn-quicksight-analysis-treemapsortconfiguration-treemapgroupitemslimitconfiguration"></a>
The limit on the number of groups that are displayed.
*Required*: No
*Type*: [ItemsLimitConfiguration](aws-properties-quicksight-analysis-itemslimitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TreeMapSort`  <a name="cfn-quicksight-analysis-treemapsortconfiguration-treemapsort"></a>
The sort configuration of group by fields.
*Required*: No
*Type*: Array of [FieldSortOptions](aws-properties-quicksight-analysis-fieldsortoptions.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
