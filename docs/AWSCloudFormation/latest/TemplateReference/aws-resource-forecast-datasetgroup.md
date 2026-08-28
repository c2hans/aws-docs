---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-forecast-datasetgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Forecast::DatasetGroup
<a name="aws-resource-forecast-datasetgroup"></a>

Creates a dataset group, which holds a collection of related datasets. You can add datasets to the dataset group when you create the dataset group, or later by using the [UpdateDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_UpdateDatasetGroup.html) operation.

**Important**
Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

After creating a dataset group and adding datasets, you use the dataset group when you create a predictor. For more information, see [Dataset groups](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html).

To get a list of all your datasets groups, use the [ListDatasetGroups](https://docs.aws.amazon.com/forecast/latest/dg/API_ListDatasetGroups.html) operation.

**Note**
The `Status` of a dataset group must be `ACTIVE` before you can use the dataset group to create a predictor. To get the status, use the [DescribeDatasetGroup](https://docs.aws.amazon.com/forecast/latest/dg/API_DescribeDatasetGroup.html) operation.

## Syntax
<a name="aws-resource-forecast-datasetgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-forecast-datasetgroup-syntax.json"></a>

```
{
  "Type" : "AWS::Forecast::DatasetGroup",
  "Properties" : {
      "[DatasetArns](#cfn-forecast-datasetgroup-datasetarns)" : {{[ String, ... ]}},
      "[DatasetGroupName](#cfn-forecast-datasetgroup-datasetgroupname)" : {{String}},
      "[Domain](#cfn-forecast-datasetgroup-domain)" : {{String}},
      "[Tags](#cfn-forecast-datasetgroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-forecast-datasetgroup-syntax.yaml"></a>

```
Type: AWS::Forecast::DatasetGroup
Properties:
  [DatasetArns](#cfn-forecast-datasetgroup-datasetarns): {{
    - String}}
  [DatasetGroupName](#cfn-forecast-datasetgroup-datasetgroupname): {{String}}
  [Domain](#cfn-forecast-datasetgroup-domain): {{String}}
  [Tags](#cfn-forecast-datasetgroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-forecast-datasetgroup-properties"></a>

`DatasetArns`  <a name="cfn-forecast-datasetgroup-datasetarns"></a>
An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetGroupName`  <a name="cfn-forecast-datasetgroup-datasetgroupname"></a>
The name of the dataset group.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]*`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Domain`  <a name="cfn-forecast-datasetgroup-domain"></a>
The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the `Domain` parameter of the [CreateDataset](https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html) operation must match.
The `Domain` and `DatasetType` that you choose determine the fields that must be present in training data that you import to a dataset. For example, if you choose the `RETAIL` domain and `TARGET_TIME_SERIES` as the `DatasetType`, Amazon Forecast requires that `item_id`, `timestamp`, and `demand` fields are present in your data. For more information, see [Dataset groups](https://docs.aws.amazon.com/forecast/latest/dg/howitworks-datasets-groups.html).
*Required*: Yes
*Type*: String
*Allowed values*: `RETAIL | CUSTOM | INVENTORY_PLANNING | EC2_CAPACITY | WORK_FORCE | WEB_TRAFFIC | METRICS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-forecast-datasetgroup-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-forecast-datasetgroup-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-forecast-datasetgroup-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-forecast-datasetgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-forecast-datasetgroup-return-values-fn--getatt-fn--getatt"></a>

`DatasetGroupArn`  <a name="DatasetGroupArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dataset group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
