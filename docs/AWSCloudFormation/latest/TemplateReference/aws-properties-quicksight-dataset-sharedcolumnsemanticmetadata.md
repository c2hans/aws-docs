---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet SharedColumnSemanticMetadata
<a name="aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata"></a>

Semantic metadata shared across one or more columns.

## Syntax
<a name="aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata-syntax.json"></a>

```
{
  "[ColumnNames](#cfn-quicksight-dataset-sharedcolumnsemanticmetadata-columnnames)" : {{[ String, ... ]}},
  "[ColumnProperties](#cfn-quicksight-dataset-sharedcolumnsemanticmetadata-columnproperties)" : {{[ ColumnSemanticProperty, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata-syntax.yaml"></a>

```
  [ColumnNames](#cfn-quicksight-dataset-sharedcolumnsemanticmetadata-columnnames): {{
    - String}}
  [ColumnProperties](#cfn-quicksight-dataset-sharedcolumnsemanticmetadata-columnproperties): {{
    - ColumnSemanticProperty}}
```

## Properties
<a name="aws-properties-quicksight-dataset-sharedcolumnsemanticmetadata-properties"></a>

`ColumnNames`  <a name="cfn-quicksight-dataset-sharedcolumnsemanticmetadata-columnnames"></a>
The names of the columns this metadata applies to.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnProperties`  <a name="cfn-quicksight-dataset-sharedcolumnsemanticmetadata-columnproperties"></a>
The semantic properties for the specified columns.
*Required*: Yes
*Type*: Array of [ColumnSemanticProperty](aws-properties-quicksight-dataset-columnsemanticproperty.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
