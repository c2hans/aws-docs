---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3vectors-vectorbucket.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::VectorBucket
<a name="aws-resource-s3vectors-vectorbucket"></a>

Defines an Amazon S3 vector bucket in the same AWS Region where you create the AWS CloudFormation stack.

Vector buckets are specialized storage containers designed for storing and managing vector data used in machine learning and AI applications. They provide optimized storage and retrieval capabilities for high-dimensional vector data.

To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

**Important**
You can only delete empty vector buckets. Deletion fails for buckets that have contents.

Permissions
The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
+ Create
  + s3vectors:CreateVectorBucket
  + s3vectors:GetVectorBucket
  + kms:GenerateDataKey (if using KMS encryption)
+ Read
  + s3vectors:GetVectorBucket
  + kms:GenerateDataKey (if using KMS encryption)
+ Delete
  + s3vectors:DeleteVectorBucket
  + s3vectors:GetVectorBucket
  + kms:GenerateDataKey (if using KMS encryption)
+ List
  + s3vectors:ListVectorBuckets
  + kms:GenerateDataKey (if using KMS encryption)

## Syntax
<a name="aws-resource-s3vectors-vectorbucket-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3vectors-vectorbucket-syntax.json"></a>

```
{
  "Type" : "AWS::S3Vectors::VectorBucket",
  "Properties" : {
      "[EncryptionConfiguration](#cfn-s3vectors-vectorbucket-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[Tags](#cfn-s3vectors-vectorbucket-tags)" : {{[ Tag, ... ]}},
      "[VectorBucketName](#cfn-s3vectors-vectorbucket-vectorbucketname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3vectors-vectorbucket-syntax.yaml"></a>

```
Type: AWS::S3Vectors::VectorBucket
Properties:
  [EncryptionConfiguration](#cfn-s3vectors-vectorbucket-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [Tags](#cfn-s3vectors-vectorbucket-tags): {{
    - Tag}}
  [VectorBucketName](#cfn-s3vectors-vectorbucket-vectorbucketname): {{String}}
```

## Properties
<a name="aws-resource-s3vectors-vectorbucket-properties"></a>

`EncryptionConfiguration`  <a name="cfn-s3vectors-vectorbucket-encryptionconfiguration"></a>
The encryption configuration for the vector bucket.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-s3vectors-vectorbucket-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-s3vectors-vectorbucket-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3vectors-vectorbucket-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VectorBucketName`  <a name="cfn-s3vectors-vectorbucket-vectorbucketname"></a>
A name for the vector bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). The bucket name must be unique in the same AWS account for each AWS Region. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name.
The bucket name must be between 3 and 63 characters long and must not contain uppercase characters or underscores.
If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3vectors-vectorbucket-return-values"></a>

### Ref
<a name="aws-resource-s3vectors-vectorbucket-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the vector bucket ARN.

Example: `arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3vectors-vectorbucket-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3vectors-vectorbucket-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Returns the date and time when the vector bucket was created.
Example: `2024-12-21T10:30:00Z`

`VectorBucketArn`  <a name="VectorBucketArn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified vector bucket.
Example: `arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket`
