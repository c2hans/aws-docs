---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottablesortby.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTableSortBy
<a name="aws-properties-quicksight-analysis-pivottablesortby"></a>

The sort by field for the field sort options.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottablesortby-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottablesortby-syntax.json"></a>

```
{
  "[Column](#cfn-quicksight-analysis-pivottablesortby-column)" : {{ColumnSort}},
  "[DataPath](#cfn-quicksight-analysis-pivottablesortby-datapath)" : {{DataPathSort}},
  "[Field](#cfn-quicksight-analysis-pivottablesortby-field)" : {{FieldSort}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottablesortby-syntax.yaml"></a>

```
  [Column](#cfn-quicksight-analysis-pivottablesortby-column): {{
    ColumnSort}}
  [DataPath](#cfn-quicksight-analysis-pivottablesortby-datapath): {{
    DataPathSort}}
  [Field](#cfn-quicksight-analysis-pivottablesortby-field): {{
    FieldSort}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottablesortby-properties"></a>

`Column`  <a name="cfn-quicksight-analysis-pivottablesortby-column"></a>
The column sort (field id, direction) for the pivot table sort by options.
*Required*: No
*Type*: [ColumnSort](aws-properties-quicksight-analysis-columnsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataPath`  <a name="cfn-quicksight-analysis-pivottablesortby-datapath"></a>
The data path sort (data path value, direction) for the pivot table sort by options.
*Required*: No
*Type*: [DataPathSort](aws-properties-quicksight-analysis-datapathsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Field`  <a name="cfn-quicksight-analysis-pivottablesortby-field"></a>
The field sort (field id, direction) for the pivot table sort by options.
*Required*: No
*Type*: [FieldSort](aws-properties-quicksight-analysis-fieldsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
