---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetsemanticdescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetSemanticDescription
<a name="aws-properties-quicksight-dataset-datasetsemanticdescription"></a>

A description structure for dataset-level semantic metadata.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetsemanticdescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetsemanticdescription-syntax.json"></a>

```
{
  "[Text](#cfn-quicksight-dataset-datasetsemanticdescription-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetsemanticdescription-syntax.yaml"></a>

```
  [Text](#cfn-quicksight-dataset-datasetsemanticdescription-text): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetsemanticdescription-properties"></a>

`Text`  <a name="cfn-quicksight-dataset-datasetsemanticdescription-text"></a>
The descriptive text for the dataset.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
