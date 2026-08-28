---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetsemanticmetadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetSemanticMetadata
<a name="aws-properties-quicksight-dataset-datasetsemanticmetadata"></a>

Semantic metadata for a dataset, including a description and custom instructions.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetsemanticmetadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetsemanticmetadata-syntax.json"></a>

```
{
  "[CustomInstructions](#cfn-quicksight-dataset-datasetsemanticmetadata-custominstructions)" : {{[ CustomInstruction, ... ]}},
  "[Description](#cfn-quicksight-dataset-datasetsemanticmetadata-description)" : {{DataSetSemanticDescription}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetsemanticmetadata-syntax.yaml"></a>

```
  [CustomInstructions](#cfn-quicksight-dataset-datasetsemanticmetadata-custominstructions): {{
    - CustomInstruction}}
  [Description](#cfn-quicksight-dataset-datasetsemanticmetadata-description): {{
    DataSetSemanticDescription}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetsemanticmetadata-properties"></a>

`CustomInstructions`  <a name="cfn-quicksight-dataset-datasetsemanticmetadata-custominstructions"></a>
A list of custom instructions that guide how the dataset should be consumed.
*Required*: No
*Type*: Array of [CustomInstruction](aws-properties-quicksight-dataset-custominstruction.md)
*Minimum*: `1`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-quicksight-dataset-datasetsemanticmetadata-description"></a>
A description of the dataset.
*Required*: No
*Type*: [DataSetSemanticDescription](aws-properties-quicksight-dataset-datasetsemanticdescription.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
