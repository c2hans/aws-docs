---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3express-directorybucket.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket
<a name="aws-resource-s3express-directorybucket"></a>

The `AWS::S3Express::DirectoryBucket` resource defines an Amazon S3 directory bucket in the same AWS Region where you create the AWS CloudFormation stack.

To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

**Important**
You can only delete empty buckets. Deletion fails for buckets that have contents.

Permissions
The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
+ Create
  + s3express:CreateBucket
  + s3express:ListAllMyDirectoryBuckets
+ Read
  + s3express:ListAllMyDirectoryBuckets
  + ec2:DescribeAvailabilityZones
+ Delete
  + s3express:DeleteBucket
  + s3express:ListAllMyDirectoryBuckets
+ List
  + s3express:ListAllMyDirectoryBuckets
+ PutBucketEncryption
  + s3express:PutEncryptionConfiguration
  + To set a directory bucket default encryption with SSE-KMS, you must also have the kms:GenerateDataKey and kms:Decrypt permissions in IAM identity-based policies and AWS KMS key policies for the target AWS KMS key.
+ GetBucketEncryption
  + s3express:GetBucketEncryption
+ DeleteBucketEncryption
  + s3express:PutEncryptionConfiguration

The following operations are related to `AWS::S3Express::DirectoryBucket`:
+  [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
+  [ListDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html)
+  [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)

## Syntax
<a name="aws-resource-s3express-directorybucket-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3express-directorybucket-syntax.json"></a>

```
{
  "Type" : "AWS::S3Express::DirectoryBucket",
  "Properties" : {
      "[BucketEncryption](#cfn-s3express-directorybucket-bucketencryption)" : {{BucketEncryption}},
      "[BucketName](#cfn-s3express-directorybucket-bucketname)" : {{String}},
      "[DataRedundancy](#cfn-s3express-directorybucket-dataredundancy)" : {{String}},
      "[InventoryConfigurations](#cfn-s3express-directorybucket-inventoryconfigurations)" : {{[ InventoryConfiguration, ... ]}},
      "[LifecycleConfiguration](#cfn-s3express-directorybucket-lifecycleconfiguration)" : {{LifecycleConfiguration}},
      "[LocationName](#cfn-s3express-directorybucket-locationname)" : {{String}},
      "[MetricsConfigurations](#cfn-s3express-directorybucket-metricsconfigurations)" : {{[ MetricsConfiguration, ... ]}},
      "[Tags](#cfn-s3express-directorybucket-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-s3express-directorybucket-syntax.yaml"></a>

```
Type: AWS::S3Express::DirectoryBucket
Properties:
  [BucketEncryption](#cfn-s3express-directorybucket-bucketencryption): {{
    BucketEncryption}}
  [BucketName](#cfn-s3express-directorybucket-bucketname): {{String}}
  [DataRedundancy](#cfn-s3express-directorybucket-dataredundancy): {{String}}
  [InventoryConfigurations](#cfn-s3express-directorybucket-inventoryconfigurations): {{
    - InventoryConfiguration}}
  [LifecycleConfiguration](#cfn-s3express-directorybucket-lifecycleconfiguration): {{
    LifecycleConfiguration}}
  [LocationName](#cfn-s3express-directorybucket-locationname): {{String}}
  [MetricsConfigurations](#cfn-s3express-directorybucket-metricsconfigurations): {{
    - MetricsConfiguration}}
  [Tags](#cfn-s3express-directorybucket-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-s3express-directorybucket-properties"></a>

`BucketEncryption`  <a name="cfn-s3express-directorybucket-bucketencryption"></a>
Specifies default encryption for a bucket using server-side encryption with Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS). For information about default encryption for directory buckets, see [Setting and monitoring default encryption for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: [BucketEncryption](aws-properties-s3express-directorybucket-bucketencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketName`  <a name="cfn-s3express-directorybucket-bucketname"></a>
A name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Zone (Availability Zone or Local Zone). The bucket name must also follow the format `bucket_base_name--zone_id--x-s3` (for example, `bucket_base_name--usw2-az1--x-s3`). If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*.
If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9][a-z0-9//.//-]*[a-z0-9]$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataRedundancy`  <a name="cfn-s3express-directorybucket-dataredundancy"></a>
The number of Zone (Availability Zone or Local Zone) that's used for redundancy for the bucket.
*Required*: Yes
*Type*: String
*Allowed values*: `SingleAvailabilityZone | SingleLocalZone`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InventoryConfigurations`  <a name="cfn-s3express-directorybucket-inventoryconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [InventoryConfiguration](aws-properties-s3express-directorybucket-inventoryconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleConfiguration`  <a name="cfn-s3express-directorybucket-lifecycleconfiguration"></a>
Container for lifecycle rules. You can add as many as 1000 rules.
For more information see, [Creating and managing a lifecycle configuration for directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-lifecycle.html          ) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: [LifecycleConfiguration](aws-properties-s3express-directorybucket-lifecycleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationName`  <a name="cfn-s3express-directorybucket-locationname"></a>
The name of the location where the bucket will be created.
For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is `usw2-az1`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetricsConfigurations`  <a name="cfn-s3express-directorybucket-metricsconfigurations"></a>
Property description not available.
*Required*: No
*Type*: Array of [MetricsConfiguration](aws-properties-s3express-directorybucket-metricsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3express-directorybucket-tags"></a>
An array of tags that you can apply to the S3 directory bucket. Tags are key-value pairs of metadata used to categorize and organize your buckets, track costs, and control access. For more information, see [Using tags with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-s3express-directorybucket-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-s3express-directorybucket-return-values"></a>

### Ref
<a name="aws-resource-s3express-directorybucket-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the bucket name.

Example: `bucket_base_name--usw2-az1--x-s3`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3express-directorybucket-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3express-directorybucket-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified bucket.
Example: `arn:aws:s3express:us-west-2:account_id:bucket/bucket_base_name--usw2-az1--x-s3`

`AvailabilityZoneName`  <a name="AvailabilityZoneName-fn::getatt"></a>
Returns the code for the Availability Zone or the Local Zone where the directory bucket was created.
Example value for an Availability Zone code: *us-east-1f*
An Availability Zone code might not represent the same physical location for different AWS accounts. For more information, see [Availability Zones and Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html) in the *Amazon S3 User Guide*.
