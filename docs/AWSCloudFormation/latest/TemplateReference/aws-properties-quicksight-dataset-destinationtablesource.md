---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-destinationtablesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DestinationTableSource
<a name="aws-properties-quicksight-dataset-destinationtablesource"></a>

Specifies the source of data for a destination table, including the transform operation and column mappings.

## Syntax
<a name="aws-properties-quicksight-dataset-destinationtablesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-destinationtablesource-syntax.json"></a>

```
{
  "[TransformOperationId](#cfn-quicksight-dataset-destinationtablesource-transformoperationid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-destinationtablesource-syntax.yaml"></a>

```
  [TransformOperationId](#cfn-quicksight-dataset-destinationtablesource-transformoperationid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-destinationtablesource-properties"></a>

`TransformOperationId`  <a name="cfn-quicksight-dataset-destinationtablesource-transformoperationid"></a>
The identifier of the transform operation that provides data to the destination table.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
