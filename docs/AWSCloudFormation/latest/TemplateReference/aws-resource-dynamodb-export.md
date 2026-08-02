---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-dynamodb-export.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Export
<a name="aws-resource-dynamodb-export"></a>

<a name="aws-resource-dynamodb-export-description"></a>The `AWS::DynamoDB::Export` resource Property description not available. for DynamoDB.

## Syntax
<a name="aws-resource-dynamodb-export-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-dynamodb-export-syntax.json"></a>

```
{
  "Type" : "AWS::DynamoDB::Export",
  "Properties" : {
      "[ExportFormat](#cfn-dynamodb-export-exportformat)" : {{String}},
      "[ExportType](#cfn-dynamodb-export-exporttype)" : {{String}},
      "[S3Bucket](#cfn-dynamodb-export-s3bucket)" : {{String}},
      "[S3BucketOwner](#cfn-dynamodb-export-s3bucketowner)" : {{String}},
      "[S3Prefix](#cfn-dynamodb-export-s3prefix)" : {{String}},
      "[S3SseAlgorithm](#cfn-dynamodb-export-s3ssealgorithm)" : {{String}},
      "[TableArn](#cfn-dynamodb-export-tablearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-dynamodb-export-syntax.yaml"></a>

```
Type: AWS::DynamoDB::Export
Properties:
  [ExportFormat](#cfn-dynamodb-export-exportformat): {{String}}
  [ExportType](#cfn-dynamodb-export-exporttype): {{String}}
  [S3Bucket](#cfn-dynamodb-export-s3bucket): {{String}}
  [S3BucketOwner](#cfn-dynamodb-export-s3bucketowner): {{String}}
  [S3Prefix](#cfn-dynamodb-export-s3prefix): {{String}}
  [S3SseAlgorithm](#cfn-dynamodb-export-s3ssealgorithm): {{String}}
  [TableArn](#cfn-dynamodb-export-tablearn): {{String}}
```

## Properties
<a name="aws-resource-dynamodb-export-properties"></a>

`ExportFormat`  <a name="cfn-dynamodb-export-exportformat"></a>
The format of the exported data. Valid values for `ExportFormat` are `DYNAMODB_JSON` or `ION`.
*Required*: No
*Type*: String
*Allowed values*: `DYNAMODB_JSON | ION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExportType`  <a name="cfn-dynamodb-export-exporttype"></a>
The type of export that was performed. Valid values are `FULL_EXPORT` or `INCREMENTAL_EXPORT`.
*Required*: No
*Type*: String
*Allowed values*: `FULL_EXPORT | INCREMENTAL_EXPORT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Bucket`  <a name="cfn-dynamodb-export-s3bucket"></a>
The name of the Amazon S3 bucket containing the export.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9A-Z]+[\.\-\w]*[a-z0-9A-Z]+$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3BucketOwner`  <a name="cfn-dynamodb-export-s3bucketowner"></a>
The ID of the AWS account that owns the bucket containing the export.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Prefix`  <a name="cfn-dynamodb-export-s3prefix"></a>
The Amazon S3 bucket prefix used as the file name and path of the exported snapshot.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3SseAlgorithm`  <a name="cfn-dynamodb-export-s3ssealgorithm"></a>
Type of encryption used on the bucket where export data is stored. Valid values for `S3SseAlgorithm` are:
+ `AES256` - server-side encryption with Amazon S3 managed keys
+ `KMS` - server-side encryption with AWS KMS managed keys
*Required*: No
*Type*: String
*Allowed values*: `AES256 | KMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableArn`  <a name="cfn-dynamodb-export-tablearn"></a>
The Amazon Resource Name (ARN) of the table that was exported.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-dynamodb-export-return-values"></a>

### Ref
<a name="aws-resource-dynamodb-export-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-dynamodb-export-return-values-fn--getatt"></a>

####
<a name="aws-resource-dynamodb-export-return-values-fn--getatt-fn--getatt"></a>

`BilledSizeBytes`  <a name="BilledSizeBytes-fn::getatt"></a>
The billable size of the table export.

`EndTime`  <a name="EndTime-fn::getatt"></a>
The time at which the export task completed.

`ExportArn`  <a name="ExportArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the table export.

`ExportId`  <a name="ExportId-fn::getatt"></a>
Property description not available.

`ExportManifest`  <a name="ExportManifest-fn::getatt"></a>
The name of the manifest file for the export task.

`ExportStatus`  <a name="ExportStatus-fn::getatt"></a>
Export can be in one of the following states: IN\_PROGRESS, COMPLETED, or FAILED.

`ExportTime`  <a name="ExportTime-fn::getatt"></a>
Point in time from which table data was exported.

`ItemCount`  <a name="ItemCount-fn::getatt"></a>
The number of items exported.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time at which the export task began.

`TableId`  <a name="TableId-fn::getatt"></a>
Unique ID of the table that was exported.

`TableName`  <a name="TableName-fn::getatt"></a>
Property description not available.
