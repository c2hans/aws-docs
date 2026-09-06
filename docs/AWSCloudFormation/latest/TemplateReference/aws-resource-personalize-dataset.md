---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-dataset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Dataset
<a name="aws-resource-personalize-dataset"></a>

Creates an empty dataset and adds it to the specified dataset group. Use [CreateDatasetImportJob](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetImportJob.html) to import your training data to a dataset.

There are 5 types of datasets:
+ Item interactions
+ Items
+ Users
+ Action interactions (you can't use CloudFormation to create an Action interactions dataset)
+ Actions (you can't use CloudFormation to create an Actions dataset)

Each dataset type has an associated schema with required field types. Only the `Item interactions` dataset is required in order to train a model (also referred to as creating a solution).

A dataset can be in one of the following states:
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ DELETE PENDING > DELETE IN\_PROGRESS

To get the status of the dataset, call [DescribeDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html).

**Related APIs**
+  [CreateDatasetGroup](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateDatasetGroup.html)
+  [ListDatasets](https://docs.aws.amazon.com/personalize/latest/dg/API_ListDatasets.html)
+  [DescribeDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeDataset.html)
+  [DeleteDataset](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteDataset.html)

## Syntax
<a name="aws-resource-personalize-dataset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-dataset-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::Dataset",
  "Properties" : {
      "[DatasetGroupArn](#cfn-personalize-dataset-datasetgrouparn)" : {{String}},
      "[DatasetImportJob](#cfn-personalize-dataset-datasetimportjob)" : {{DatasetImportJob}},
      "[DatasetType](#cfn-personalize-dataset-datasettype)" : {{String}},
      "[Name](#cfn-personalize-dataset-name)" : {{String}},
      "[SchemaArn](#cfn-personalize-dataset-schemaarn)" : {{String}},
      "[Tags](#cfn-personalize-dataset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-personalize-dataset-syntax.yaml"></a>

```
Type: AWS::Personalize::Dataset
Properties:
  [DatasetGroupArn](#cfn-personalize-dataset-datasetgrouparn): {{String}}
  [DatasetImportJob](#cfn-personalize-dataset-datasetimportjob): {{
    DatasetImportJob}}
  [DatasetType](#cfn-personalize-dataset-datasettype): {{String}}
  [Name](#cfn-personalize-dataset-name): {{String}}
  [SchemaArn](#cfn-personalize-dataset-schemaarn): {{String}}
  [Tags](#cfn-personalize-dataset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-personalize-dataset-properties"></a>

`DatasetGroupArn`  <a name="cfn-personalize-dataset-datasetgrouparn"></a>
The Amazon Resource Name (ARN) of the dataset group.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([a-z\d-]+):personalize:.*:.*:.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatasetImportJob`  <a name="cfn-personalize-dataset-datasetimportjob"></a>
Describes a job that imports training data from a data source (Amazon S3 bucket) to an Amazon Personalize dataset. If you specify a dataset import job as part of a dataset, all dataset import job fields are required.
*Required*: No
*Type*: [DatasetImportJob](aws-properties-personalize-dataset-datasetimportjob.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatasetType`  <a name="cfn-personalize-dataset-datasettype"></a>
One of the following values:
+ Interactions
+ Items
+ Users
You can't use CloudFormation to create an Action Interactions or Actions dataset.
*Required*: Yes
*Type*: String
*Allowed values*: `Interactions | Items | Users`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-personalize-dataset-name"></a>
The name of the dataset.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaArn`  <a name="cfn-personalize-dataset-schemaarn"></a>
The ARN of the associated schema.
*Required*: Yes
*Type*: String
*Pattern*: `arn:([a-z\d-]+):personalize:.*:.*:.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-personalize-dataset-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-personalize-dataset-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-personalize-dataset-return-values"></a>

### Ref
<a name="aws-resource-personalize-dataset-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the resource.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-personalize-dataset-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-personalize-dataset-return-values-fn--getatt-fn--getatt"></a>

`DatasetArn`  <a name="DatasetArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the dataset.

## Examples
<a name="aws-resource-personalize-dataset--examples"></a>

### Creating a dataset
<a name="aws-resource-personalize-dataset--examples--Creating_a_dataset"></a>

The following example creates an Amazon Personalize dataset and a dataset import job. The dataset import job imports data from an Amazon S3 bucket into the dataset.

#### JSON
<a name="aws-resource-personalize-dataset--examples--Creating_a_dataset--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyDataset": {
      "Type": "AWS::Personalize::Dataset",
      "Properties": {
        "Name": "my-dataset-name",
        "DatasetType": "Interactions",
        "DatasetGroupArn": "arn:aws:personalize:us-west-2:123456789012:dataset-group/dataset-group-name",
        "SchemaArn": "arn:aws:personalize:us-west-2:123456789012:schema/schema-name",
        "DatasetImportJob": {
          "JobName": "my-import-job-name",
          "DataSource": {
            "DataLocation": "s3://bucket-name/file-name.csv"
          },
          "RoleArn": "arn:aws:iam::123456789012:role/personalize-role"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-personalize-dataset--examples--Creating_a_dataset--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyDataset:
    Type: 'AWS::Personalize::Dataset'
    Properties:
      Name: my-dataset-name
      DatasetType: Interactions
      DatasetGroupArn: 'arn:aws:personalize:us-west-2:123456789012:dataset-group/dataset-group-name'
      SchemaArn: 'arn:aws:personalize:us-west-2:123456789012:schema/schema-name'
      DatasetImportJob:
        JobName: my-import-job-name
        DataSource:
          DataLocation: 's3://bucket-name/file-name.csv'
        RoleArn: 'arn:aws:iam::123456789012:role/personalize-role'
```
