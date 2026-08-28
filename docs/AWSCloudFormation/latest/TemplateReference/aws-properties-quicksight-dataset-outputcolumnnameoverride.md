---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-outputcolumnnameoverride.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet OutputColumnNameOverride
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride"></a>

Specifies a mapping to override the name of an output column from a transform operation.

## Syntax
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-syntax.json"></a>

```
{
  "[OutputColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-outputcolumnname)" : {{String}},
  "[SourceColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-sourcecolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-syntax.yaml"></a>

```
  [OutputColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-outputcolumnname): {{String}}
  [SourceColumnName](#cfn-quicksight-dataset-outputcolumnnameoverride-sourcecolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-outputcolumnnameoverride-properties"></a>

`OutputColumnName`  <a name="cfn-quicksight-dataset-outputcolumnnameoverride-outputcolumnname"></a>
The new name to assign to the column in the output.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceColumnName`  <a name="cfn-quicksight-dataset-outputcolumnnameoverride-sourcecolumnname"></a>
The original name of the column from the source transform operation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
