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
