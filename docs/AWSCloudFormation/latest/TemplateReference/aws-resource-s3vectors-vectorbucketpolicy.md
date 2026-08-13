---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3vectors-vectorbucketpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Vectors::VectorBucketPolicy
<a name="aws-resource-s3vectors-vectorbucketpolicy"></a>

The `AWS::S3Vectors::VectorBucketPolicy` resource defines an Amazon S3 vector bucket policy to control access to an Amazon S3 vector bucket.

Vector bucket policies are written in JSON and allow you to grant or deny permissions across all (or a subset of) objects within a vector bucket.

You must specify either `VectorBucketName` or `VectorBucketArn` to identify the target bucket.

To control how AWS CloudFormation handles the vector bucket policy when the stack is deleted, you can set a deletion policy for your policy. You can choose to *retain* the policy or to *delete* the policy. For more information, see [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

Permissions
The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
+ Create
  + s3vectors:GetVectorBucketPolicy
  + s3vectors:PutVectorBucketPolicy
+ Read
  + s3vectors:GetVectorBucketPolicy
+ Update
  + s3vectors:GetVectorBucketPolicy
  + s3vectors:PutVectorBucketPolicy
+ Delete
  + s3vectors:GetVectorBucketPolicy
  + s3vectors:DeleteVectorBucketPolicy
+ List
  + s3vectors:GetVectorBucketPolicy
  + s3vectors:ListVectorBuckets

## Syntax
<a name="aws-resource-s3vectors-vectorbucketpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3vectors-vectorbucketpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::S3Vectors::VectorBucketPolicy",
  "Properties" : {
      "[Policy](#cfn-s3vectors-vectorbucketpolicy-policy)" : {{Json}},
      "[VectorBucketArn](#cfn-s3vectors-vectorbucketpolicy-vectorbucketarn)" : {{String}},
      "[VectorBucketName](#cfn-s3vectors-vectorbucketpolicy-vectorbucketname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-s3vectors-vectorbucketpolicy-syntax.yaml"></a>

```
Type: AWS::S3Vectors::VectorBucketPolicy
Properties:
  [Policy](#cfn-s3vectors-vectorbucketpolicy-policy): {{Json}}
  [VectorBucketArn](#cfn-s3vectors-vectorbucketpolicy-vectorbucketarn): {{String}}
  [VectorBucketName](#cfn-s3vectors-vectorbucketpolicy-vectorbucketname): {{String}}
```

## Properties
<a name="aws-resource-s3vectors-vectorbucketpolicy-properties"></a>

`Policy`  <a name="cfn-s3vectors-vectorbucketpolicy-policy"></a>
A policy document containing permissions to add to the specified vector bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VectorBucketArn`  <a name="cfn-s3vectors-vectorbucketpolicy-vectorbucketarn"></a>
The Amazon Resource Name (ARN) of the S3 vector bucket to which the policy applies.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VectorBucketName`  <a name="cfn-s3vectors-vectorbucketpolicy-vectorbucketname"></a>
The name of the S3 vector bucket to which the policy applies.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-s3vectors-vectorbucketpolicy-return-values"></a>

### Ref
<a name="aws-resource-s3vectors-vectorbucketpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the vector bucket ARN.

Example: `arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
