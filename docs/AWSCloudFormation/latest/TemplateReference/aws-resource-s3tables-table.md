---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3tables-table.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::Table
<a name="aws-resource-s3tables-table"></a>

Creates a new table associated with the given namespace in a table bucket. For more information, see [Creating an Amazon S3 table](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-create.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
+ You must have the `s3tables:CreateTable` permission to use this operation.
+ If you use this operation with the optional `metadata` request parameter you must have the `s3tables:PutTableData` permission.
+ If you use this operation with the optional `encryptionConfiguration` request parameter you must have the `s3tables:PutTableEncryption` permission.
Additionally, If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-kms-permissions.html).

 AWS Cloud Development Kit (AWS CDK)
To use S3 Tables AWS CDK constructs, add the `@aws-cdk/aws-s3tables-alpha` dependency with one of the following options:
+ NPM: `npm i @aws-cdk/aws-s3tables-alpha`
+ Yarn:`yarn add @aws-cdk/aws-s3tables-alpha`

## Syntax
<a name="aws-resource-s3tables-table-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3tables-table-syntax.json"></a>

```
{
  "Type" : "AWS::S3Tables::Table",
  "Properties" : {
      "[Compaction](#cfn-s3tables-table-compaction)" : {{Compaction}},
      "[IcebergMetadata](#cfn-s3tables-table-icebergmetadata)" : {{IcebergMetadata}},
      "[Namespace](#cfn-s3tables-table-namespace)" : {{String}},
      "[OpenTableFormat](#cfn-s3tables-table-opentableformat)" : {{String}},
      "[SnapshotManagement](#cfn-s3tables-table-snapshotmanagement)" : {{SnapshotManagement}},
      "[StorageClassConfiguration](#cfn-s3tables-table-storageclassconfiguration)" : {{StorageClassConfiguration}},
      "[TableBucketARN](#cfn-s3tables-table-tablebucketarn)" : {{String}},
      "[TableName](#cfn-s3tables-table-tablename)" : {{String}},
      "[Tags](#cfn-s3tables-table-tags)" : {{[ Tag, ... ]}},
      "[WithoutMetadata](#cfn-s3tables-table-withoutmetadata)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3tables-table-syntax.yaml"></a>

```
Type: AWS::S3Tables::Table
Properties:
  [Compaction](#cfn-s3tables-table-compaction): {{
    Compaction}}
  [IcebergMetadata](#cfn-s3tables-table-icebergmetadata): {{
    IcebergMetadata}}
  [Namespace](#cfn-s3tables-table-namespace): {{String}}
  [OpenTableFormat](#cfn-s3tables-table-opentableformat): {{String}}
  [SnapshotManagement](#cfn-s3tables-table-snapshotmanagement): {{
    SnapshotManagement}}
  [StorageClassConfiguration](#cfn-s3tables-table-storageclassconfiguration): {{
    StorageClassConfiguration}}
  [TableBucketARN](#cfn-s3tables-table-tablebucketarn): {{String}}
  [TableName](#cfn-s3tables-table-tablename): {{String}}
  [Tags](#cfn-s3tables-table-tags): {{
    - Tag}}
  [WithoutMetadata](#cfn-s3tables-table-withoutmetadata): {{String}}
```

## Properties
<a name="aws-resource-s3tables-table-properties"></a>

`Compaction`  <a name="cfn-s3tables-table-compaction"></a>
Contains details about the compaction settings for an Iceberg table.
*Required*: No
*Type*: [Compaction](aws-properties-s3tables-table-compaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IcebergMetadata`  <a name="cfn-s3tables-table-icebergmetadata"></a>
Contains details about the metadata for an Iceberg table.
*Required*: No
*Type*: [IcebergMetadata](aws-properties-s3tables-table-icebergmetadata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-s3tables-table-namespace"></a>
The name of the namespace.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenTableFormat`  <a name="cfn-s3tables-table-opentableformat"></a>
The format of the table.
*Required*: Yes
*Type*: String
*Allowed values*: `ICEBERG`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotManagement`  <a name="cfn-s3tables-table-snapshotmanagement"></a>
Contains details about the Iceberg snapshot management settings for the table.
*Required*: No
*Type*: [SnapshotManagement](aws-properties-s3tables-table-snapshotmanagement.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageClassConfiguration`  <a name="cfn-s3tables-table-storageclassconfiguration"></a>
The configuration details for the storage class of tables or table buckets. This allows you to optimize storage costs by selecting the appropriate storage class based on your access patterns and performance requirements.
*Required*: No
*Type*: [StorageClassConfiguration](aws-properties-s3tables-table-storageclassconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableBucketARN`  <a name="cfn-s3tables-table-tablebucketarn"></a>
The Amazon Resource Name (ARN) of the table bucket to create the table in.
*Required*: Yes
*Type*: String
*Pattern*: `(arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:bucket/[a-z0-9_-]{3,63})`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-s3tables-table-tablename"></a>
The name for the table.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-z_]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3tables-table-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3tables-table-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WithoutMetadata`  <a name="cfn-s3tables-table-withoutmetadata"></a>
Indicates that you don't want to specify a schema for the table. This property is mutually exclusive to `IcebergMetadata`, and its only possible value is `Yes`.
*Required*: No
*Type*: String
*Allowed values*: `Yes`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3tables-table-return-values"></a>

### Ref
<a name="aws-resource-s3tables-table-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the table name.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3tables-table-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3tables-table-return-values-fn--getatt-fn--getatt"></a>

`TableARN`  <a name="TableARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the table.

`VersionToken`  <a name="VersionToken-fn::getatt"></a>
The version token of the table.

`WarehouseLocation`  <a name="WarehouseLocation-fn::getatt"></a>
The warehouse location of the table.
