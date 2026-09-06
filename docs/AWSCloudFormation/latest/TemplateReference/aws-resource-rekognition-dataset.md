---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rekognition-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Rekognition::Dataset
<a name="aws-resource-rekognition-dataset"></a>

**Note**
This operation applies only to Amazon Rekognition Custom Labels.

Creates a new Amazon Rekognition Custom Labels dataset. You can create a dataset by using an Amazon Sagemaker format manifest file or by copying an existing Amazon Rekognition Custom Labels dataset.

To create a training dataset for a project, specify `TRAIN` for the value of `DatasetType`. To create the test dataset for a project, specify `TEST` for the value of `DatasetType`.

The response from `CreateDataset` is the Amazon Resource Name (ARN) for the dataset. Creating a dataset takes a while to complete. Use DescribeDataset to check the current status. The dataset created successfully if the value of `Status` is `CREATE_COMPLETE`.

To check if any non-terminal errors occurred, call ListDatasetEntries and check for the presence of `errors` lists in the JSON Lines.

Dataset creation fails if a terminal error occurs (`Status` = `CREATE_FAILED`). Currently, you can't access the terminal error information.

For more information, see [Creating datasets](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html).

This operation requires permissions to perform the `rekognition:CreateDataset` action. If you want to copy an existing dataset, you also require permission to perform the `rekognition:ListDatasetEntries` action.

## Syntax
<a name="aws-resource-rekognition-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-rekognition-dataset-syntax.json"></a>

```
{
  "Type" : "AWS::Rekognition::Dataset",
  "Properties" : {
      "[DatasetType](#cfn-rekognition-dataset-datasettype)" : {{String}},
      "[ProjectArn](#cfn-rekognition-dataset-projectarn)" : {{String}},
      "[Tags](#cfn-rekognition-dataset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-rekognition-dataset-syntax.yaml"></a>

```
Type: AWS::Rekognition::Dataset
Properties:
  [DatasetType](#cfn-rekognition-dataset-datasettype): {{String}}
  [ProjectArn](#cfn-rekognition-dataset-projectarn): {{String}}
  [Tags](#cfn-rekognition-dataset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-rekognition-dataset-properties"></a>

`DatasetType`  <a name="cfn-rekognition-dataset-datasettype"></a>
 The type of the dataset.
*Required*: Yes
*Type*: String
*Allowed values*: `TRAIN | TEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProjectArn`  <a name="cfn-rekognition-dataset-projectarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-rekognition-dataset-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-rekognition-dataset-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-rekognition-dataset-return-values"></a>

### Ref
<a name="aws-resource-rekognition-dataset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-rekognition-dataset-return-values-fn--getatt"></a>

####
<a name="aws-resource-rekognition-dataset-return-values-fn--getatt-fn--getatt"></a>

`DatasetArn`  <a name="DatasetArn-fn::getatt"></a>
 The Amazon Resource Name (ARN) for the dataset.
