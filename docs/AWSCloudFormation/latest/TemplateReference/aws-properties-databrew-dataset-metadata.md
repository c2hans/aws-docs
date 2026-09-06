---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-metadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset Metadata
<a name="aws-properties-databrew-dataset-metadata"></a>

Contains additional resource information needed for specific datasets.

## Syntax
<a name="aws-properties-databrew-dataset-metadata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-metadata-syntax.json"></a>

```
{
  "[SourceArn](#cfn-databrew-dataset-metadata-sourcearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-metadata-syntax.yaml"></a>

```
  [SourceArn](#cfn-databrew-dataset-metadata-sourcearn): {{String}}
```

## Properties
<a name="aws-properties-databrew-dataset-metadata-properties"></a>

`SourceArn`  <a name="cfn-databrew-dataset-metadata-sourcearn"></a>
The Amazon Resource Name (ARN) associated with the dataset. Currently, DataBrew only supports ARNs from Amazon AppFlow.
*Required*: No
*Type*: String
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
