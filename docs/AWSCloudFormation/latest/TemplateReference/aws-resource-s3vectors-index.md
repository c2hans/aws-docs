---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3vectors-index.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::Index
<a name="aws-resource-s3vectors-index"></a>

The `AWS::S3Vectors::Index` resource defines a vector index within an Amazon S3 vector bucket. For more information, see [Creating a vector index in a vector bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-create-index.html) in the *Amazon Simple Storage Service User Guide*.

You must specify either `VectorBucketName` or `VectorBucketArn` to identify the bucket that contains the index.

To control how AWS CloudFormation handles the vector index when the stack is deleted, you can set a deletion policy for your index. You can choose to *retain* the index or to *delete* the index. For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

Permissions
The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
+ Create
  + s3vectors:CreateIndex
  + s3vectors:GetIndex
+ Read
  + s3vectors:GetIndex
+ Delete
  + s3vectors:DeleteIndex
  + s3vectors:GetIndex
+ List
  + s3vectors:ListIndexes

## Syntax
<a name="aws-resource-s3vectors-index-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3vectors-index-syntax.json"></a>

```
{
  "Type" : "AWS::S3Vectors::Index",
  "Properties" : {
      "[DataType](#cfn-s3vectors-index-datatype)" : {{String}},
      "[Dimension](#cfn-s3vectors-index-dimension)" : {{Integer}},
      "[DistanceMetric](#cfn-s3vectors-index-distancemetric)" : {{String}},
      "[EncryptionConfiguration](#cfn-s3vectors-index-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[IndexName](#cfn-s3vectors-index-indexname)" : {{String}},
      "[MetadataConfiguration](#cfn-s3vectors-index-metadataconfiguration)" : {{MetadataConfiguration}},
      "[Tags](#cfn-s3vectors-index-tags)" : {{[ Tag, ... ]}},
      "[VectorBucketArn](#cfn-s3vectors-index-vectorbucketarn)" : {{String}},
      "[VectorBucketName](#cfn-s3vectors-index-vectorbucketname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3vectors-index-syntax.yaml"></a>

```
Type: AWS::S3Vectors::Index
Properties:
  [DataType](#cfn-s3vectors-index-datatype): {{String}}
  [Dimension](#cfn-s3vectors-index-dimension): {{Integer}}
  [DistanceMetric](#cfn-s3vectors-index-distancemetric): {{String}}
  [EncryptionConfiguration](#cfn-s3vectors-index-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [IndexName](#cfn-s3vectors-index-indexname): {{String}}
  [MetadataConfiguration](#cfn-s3vectors-index-metadataconfiguration): {{
    MetadataConfiguration}}
  [Tags](#cfn-s3vectors-index-tags): {{
    - Tag}}
  [VectorBucketArn](#cfn-s3vectors-index-vectorbucketarn): {{String}}
  [VectorBucketName](#cfn-s3vectors-index-vectorbucketname): {{String}}
```

## Properties
<a name="aws-resource-s3vectors-index-properties"></a>

`DataType`  <a name="cfn-s3vectors-index-datatype"></a>
The data type of the vectors to be inserted into the vector index. Currently, only `float32` is supported, which represents 32-bit floating-point numbers.
*Required*: Yes
*Type*: String
*Allowed values*: `float32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Dimension`  <a name="cfn-s3vectors-index-dimension"></a>
The dimensions of the vectors to be inserted into the vector index. This value must be between 1 and 4096, inclusive. All vectors stored in the index must have the same number of dimensions.
The dimension value affects the storage requirements and search performance. Higher dimensions require more storage space and may impact search latency.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DistanceMetric`  <a name="cfn-s3vectors-index-distancemetric"></a>
The distance metric to be used for similarity search. Valid values are:
+ `cosine` - Measures the cosine of the angle between two vectors.
+ `euclidean` - Measures the straight-line distance between two points in multi-dimensional space. Lower values indicate greater similarity.
*Required*: Yes
*Type*: String
*Allowed values*: `cosine | euclidean`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionConfiguration`  <a name="cfn-s3vectors-index-encryptionconfiguration"></a>
The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-s3vectors-index-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IndexName`  <a name="cfn-s3vectors-index-indexname"></a>
The name of the vector index to create. The index name must be between 3 and 63 characters long and can contain only lowercase letters, numbers, hyphens (-), and dots (.). The index name must be unique within the vector bucket.
If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the index name.
If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetadataConfiguration`  <a name="cfn-s3vectors-index-metadataconfiguration"></a>
The metadata configuration for the vector index.
*Required*: No
*Type*: [MetadataConfiguration](aws-properties-s3vectors-index-metadataconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-s3vectors-index-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-s3vectors-index-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VectorBucketArn`  <a name="cfn-s3vectors-index-vectorbucketarn"></a>
The Amazon Resource Name (ARN) of the vector bucket that contains the vector index.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorBucketName`  <a name="cfn-s3vectors-index-vectorbucketname"></a>
The name of the vector bucket that contains the vector index.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3vectors-index-return-values"></a>

### Ref
<a name="aws-resource-s3vectors-index-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the index ARN.

Example: `arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket/index/my-index`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-s3vectors-index-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-s3vectors-index-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Returns the date and time when the vector index was created.
Example: `2024-12-21T10:30:00Z`

`IndexArn`  <a name="IndexArn-fn::getatt"></a>
Returns the Amazon Resource Name (ARN) of the specified index.
Example: `arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket/index/my-index`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
