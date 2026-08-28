---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-fieldsortoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FieldSortOptions
<a name="aws-properties-quicksight-analysis-fieldsortoptions"></a>

The field sort options in a chart configuration.

## Syntax
<a name="aws-properties-quicksight-analysis-fieldsortoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-fieldsortoptions-syntax.json"></a>

```
{
  "[ColumnSort](#cfn-quicksight-analysis-fieldsortoptions-columnsort)" : {{ColumnSort}},
  "[FieldSort](#cfn-quicksight-analysis-fieldsortoptions-fieldsort)" : {{FieldSort}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-fieldsortoptions-syntax.yaml"></a>

```
  [ColumnSort](#cfn-quicksight-analysis-fieldsortoptions-columnsort): {{
    ColumnSort}}
  [FieldSort](#cfn-quicksight-analysis-fieldsortoptions-fieldsort): {{
    FieldSort}}
```

## Properties
<a name="aws-properties-quicksight-analysis-fieldsortoptions-properties"></a>

`ColumnSort`  <a name="cfn-quicksight-analysis-fieldsortoptions-columnsort"></a>
The sort configuration for a column that is not used in a field well.
*Required*: No
*Type*: [ColumnSort](aws-properties-quicksight-analysis-columnsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldSort`  <a name="cfn-quicksight-analysis-fieldsortoptions-fieldsort"></a>
The sort configuration for a field in a field well.
*Required*: No
*Type*: [FieldSort](aws-properties-quicksight-analysis-fieldsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
