---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotsitewise-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTSiteWise::Dataset
<a name="aws-resource-iotsitewise-dataset"></a>

Creates a dataset to connect an external datasource.

## Syntax
<a name="aws-resource-iotsitewise-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotsitewise-dataset-syntax.json"></a>

```
{
  "Type" : "AWS::IoTSiteWise::Dataset",
  "Properties" : {
      "[DatasetDescription](#cfn-iotsitewise-dataset-datasetdescription)" : {{String}},
      "[DatasetName](#cfn-iotsitewise-dataset-datasetname)" : {{String}},
      "[DatasetSource](#cfn-iotsitewise-dataset-datasetsource)" : {{DatasetSource}},
      "[Tags](#cfn-iotsitewise-dataset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iotsitewise-dataset-syntax.yaml"></a>

```
Type: AWS::IoTSiteWise::Dataset
Properties:
  [DatasetDescription](#cfn-iotsitewise-dataset-datasetdescription): {{String}}
  [DatasetName](#cfn-iotsitewise-dataset-datasetname): {{String}}
  [DatasetSource](#cfn-iotsitewise-dataset-datasetsource): {{
    DatasetSource}}
  [Tags](#cfn-iotsitewise-dataset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-iotsitewise-dataset-properties"></a>

`DatasetDescription`  <a name="cfn-iotsitewise-dataset-datasetdescription"></a>
A description about the dataset, and its functionality.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetName`  <a name="cfn-iotsitewise-dataset-datasetname"></a>
The name of the dataset.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetSource`  <a name="cfn-iotsitewise-dataset-datasetsource"></a>
The data source for the dataset.
*Required*: Yes
*Type*: [DatasetSource](aws-properties-iotsitewise-dataset-datasetsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-iotsitewise-dataset-tags"></a>
A list of key-value pairs that contain metadata for the access policy. For more information, see [Tagging your AWS IoT SiteWise resources](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html) in the *AWS IoT SiteWise User Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-iotsitewise-dataset-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-iotsitewise-dataset-return-values"></a>

### Ref
<a name="aws-resource-iotsitewise-dataset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `DatasetId`.

### Fn::GetAtt
<a name="aws-resource-iotsitewise-dataset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotsitewise-dataset-return-values-fn--getatt-fn--getatt"></a>

`DatasetArn`  <a name="DatasetArn-fn::getatt"></a>
The ARN of the dataset, which has the following format.
 `arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}`
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`DatasetId`  <a name="DatasetId-fn::getatt"></a>
The ID of the dataset.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
