---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3tables-tablebucket.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Tables::TableBucket
<a name="aws-resource-s3tables-tablebucket"></a>

Creates a table bucket. For more information, see [Creating a table bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets-create.html) in the *Amazon Simple Storage Service User Guide*.

Permissions
+ You must have the `s3tables:CreateTableBucket` permission to use this operation.
+ If you use this operation with the optional `encryptionConfiguration` parameter you must have the `s3tables:PutTableBucketEncryption` permission.

 AWS Cloud Development Kit (AWS CDK)
To use S3 Tables AWS CDK constructs, add the `@aws-cdk/aws-s3tables-alpha` dependency with one of the following options:
+ NPM: `npm i @aws-cdk/aws-s3tables-alpha`
+ Yarn:`yarn add @aws-cdk/aws-s3tables-alpha`

## Syntax
<a name="aws-resource-s3tables-tablebucket-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3tables-tablebucket-syntax.json"></a>

```
{
  "Type" : "AWS::S3Tables::TableBucket",
  "Properties" : {
      "[EncryptionConfiguration](#cfn-s3tables-tablebucket-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[MetricsConfiguration](#cfn-s3tables-tablebucket-metricsconfiguration)" : {{MetricsConfiguration}},
      "[ReplicationConfiguration](#cfn-s3tables-tablebucket-replicationconfiguration)" : {{ReplicationConfiguration}},
      "[StorageClassConfiguration](#cfn-s3tables-tablebucket-storageclassconfiguration)" : {{StorageClassConfiguration}},
      "[TableBucketName](#cfn-s3tables-tablebucket-tablebucketname)" : {{String}},
      "[Tags](#cfn-s3tables-tablebucket-tags)" : {{[ Tag, ... ]}},
      "[UnreferencedFileRemoval](#cfn-s3tables-tablebucket-unreferencedfileremoval)" : {{UnreferencedFileRemoval}}
    }
}
```

### YAML
<a name="aws-resource-s3tables-tablebucket-syntax.yaml"></a>

```
Type: AWS::S3Tables::TableBucket
Properties:
  [EncryptionConfiguration](#cfn-s3tables-tablebucket-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [MetricsConfiguration](#cfn-s3tables-tablebucket-metricsconfiguration): {{
    MetricsConfiguration}}
  [ReplicationConfiguration](#cfn-s3tables-tablebucket-replicationconfiguration): {{
    ReplicationConfiguration}}
  [StorageClassConfiguration](#cfn-s3tables-tablebucket-storageclassconfiguration): {{
    StorageClassConfiguration}}
  [TableBucketName](#cfn-s3tables-tablebucket-tablebucketname): {{String}}
  [Tags](#cfn-s3tables-tablebucket-tags): {{
    - Tag}}
  [UnreferencedFileRemoval](#cfn-s3tables-tablebucket-unreferencedfileremoval): {{
    UnreferencedFileRemoval}}
```

## Properties
<a name="aws-resource-s3tables-tablebucket-properties"></a>

`EncryptionConfiguration`  <a name="cfn-s3tables-tablebucket-encryptionconfiguration"></a>
Configuration specifying how data should be encrypted. This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-s3tables-tablebucket-encryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricsConfiguration`  <a name="cfn-s3tables-tablebucket-metricsconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [MetricsConfiguration](aws-properties-s3tables-tablebucket-metricsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationConfiguration`  <a name="cfn-s3tables-tablebucket-replicationconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [ReplicationConfiguration](aws-properties-s3tables-tablebucket-replicationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageClassConfiguration`  <a name="cfn-s3tables-tablebucket-storageclassconfiguration"></a>
The configuration details for the storage class of tables or table buckets. This allows you to optimize storage costs by selecting the appropriate storage class based on your access patterns and performance requirements.
*Required*: No
*Type*: [StorageClassConfiguration](aws-properties-s3tables-tablebucket-storageclassconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableBucketName`  <a name="cfn-s3tables-tablebucket-tablebucketname"></a>
The name for the table bucket.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-s3tables-tablebucket-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3tables-tablebucket-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnreferencedFileRemoval`  <a name="cfn-s3tables-tablebucket-unreferencedfileremoval"></a>
The unreferenced file removal settings for your table bucket. Unreferenced file removal identifies and deletes all objects that are not referenced by any table snapshots. For more information, see the [*Amazon S3 User Guide*](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-table-buckets-maintenance.html).
*Required*: No
*Type*: [UnreferencedFileRemoval](aws-properties-s3tables-tablebucket-unreferencedfileremoval.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-s3tables-tablebucket-return-values"></a>

### Ref
<a name="aws-resource-s3tables-tablebucket-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the table bucket name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3tables-tablebucket-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3tables-tablebucket-return-values-fn--getatt-fn--getatt"></a>

`TableBucketARN`  <a name="TableBucketARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the table bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
