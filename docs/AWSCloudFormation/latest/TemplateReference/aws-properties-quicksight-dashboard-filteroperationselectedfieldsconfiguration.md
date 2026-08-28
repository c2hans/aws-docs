---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard FilterOperationSelectedFieldsConfiguration
<a name="aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration"></a>

The configuration of selected fields in the`CustomActionFilterOperation`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration-syntax.json"></a>

```
{
  "[SelectedColumns](#cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedcolumns)" : {{[ ColumnIdentifier, ... ]}},
  "[SelectedFieldOptions](#cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedfieldoptions)" : {{String}},
  "[SelectedFields](#cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedfields)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration-syntax.yaml"></a>

```
  [SelectedColumns](#cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedcolumns): {{
    - ColumnIdentifier}}
  [SelectedFieldOptions](#cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedfieldoptions): {{String}}
  [SelectedFields](#cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedfields): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-filteroperationselectedfieldsconfiguration-properties"></a>

`SelectedColumns`  <a name="cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedcolumns"></a>
The selected columns of a dataset.
*Required*: No
*Type*: Array of [ColumnIdentifier](aws-properties-quicksight-dashboard-columnidentifier.md)
*Minimum*: `0`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedFieldOptions`  <a name="cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedfieldoptions"></a>
A structure that contains the options that choose which fields are filtered in the `CustomActionFilterOperation`.
Valid values are defined as follows:
+ `ALL_FIELDS`: Applies the filter operation to all fields.
*Required*: No
*Type*: String
*Allowed values*: `ALL_FIELDS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelectedFields`  <a name="cfn-quicksight-dashboard-filteroperationselectedfieldsconfiguration-selectedfields"></a>
Chooses the fields that are filtered in `CustomActionFilterOperation`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `512 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
