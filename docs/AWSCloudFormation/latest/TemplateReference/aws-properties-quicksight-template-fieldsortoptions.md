---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-fieldsortoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FieldSortOptions
<a name="aws-properties-quicksight-template-fieldsortoptions"></a>

The field sort options in a chart configuration.

## Syntax
<a name="aws-properties-quicksight-template-fieldsortoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-fieldsortoptions-syntax.json"></a>

```
{
  "[ColumnSort](#cfn-quicksight-template-fieldsortoptions-columnsort)" : {{ColumnSort}},
  "[FieldSort](#cfn-quicksight-template-fieldsortoptions-fieldsort)" : {{FieldSort}}
}
```

### YAML
<a name="aws-properties-quicksight-template-fieldsortoptions-syntax.yaml"></a>

```
  [ColumnSort](#cfn-quicksight-template-fieldsortoptions-columnsort): {{
    ColumnSort}}
  [FieldSort](#cfn-quicksight-template-fieldsortoptions-fieldsort): {{
    FieldSort}}
```

## Properties
<a name="aws-properties-quicksight-template-fieldsortoptions-properties"></a>

`ColumnSort`  <a name="cfn-quicksight-template-fieldsortoptions-columnsort"></a>
The sort configuration for a column that is not used in a field well.
*Required*: No
*Type*: [ColumnSort](aws-properties-quicksight-template-columnsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldSort`  <a name="cfn-quicksight-template-fieldsortoptions-fieldsort"></a>
The sort configuration for a field in a field well.
*Required*: No
*Type*: [FieldSort](aws-properties-quicksight-template-fieldsort.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
