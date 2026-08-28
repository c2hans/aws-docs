---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-joinoperandproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet JoinOperandProperties
<a name="aws-properties-quicksight-dataset-joinoperandproperties"></a>

Properties that control how columns are handled for a join operand, including column name overrides.

## Syntax
<a name="aws-properties-quicksight-dataset-joinoperandproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-joinoperandproperties-syntax.json"></a>

```
{
  "[OutputColumnNameOverrides](#cfn-quicksight-dataset-joinoperandproperties-outputcolumnnameoverrides)" : {{[ OutputColumnNameOverride, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-joinoperandproperties-syntax.yaml"></a>

```
  [OutputColumnNameOverrides](#cfn-quicksight-dataset-joinoperandproperties-outputcolumnnameoverrides): {{
    - OutputColumnNameOverride}}
```

## Properties
<a name="aws-properties-quicksight-dataset-joinoperandproperties-properties"></a>

`OutputColumnNameOverrides`  <a name="cfn-quicksight-dataset-joinoperandproperties-outputcolumnnameoverrides"></a>
A list of column name overrides to apply to the join operand's output columns.
*Required*: Yes
*Type*: Array of [OutputColumnNameOverride](aws-properties-quicksight-dataset-outputcolumnnameoverride.md)
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
