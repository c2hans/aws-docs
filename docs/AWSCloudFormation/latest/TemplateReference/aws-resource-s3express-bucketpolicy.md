---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3express-bucketpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::BucketPolicy
<a name="aws-resource-s3express-bucketpolicy"></a>

The `AWS::S3Express::BucketPolicy` resource defines an Amazon S3 bucket policy to an Amazon S3 directory bucket.

Permissions
If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must both have the required permissions on the specified bucket and belong to the bucket owner's account in order to use this operation. For more information about directory bucket policies and permissions, see [AWS Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.
To ensure that bucket owners don't inadvertently lock themselves out of their own buckets, the root principal in a bucket owner's AWS account can perform the `GetBucketPolicy`, `PutBucketPolicy`, and `DeleteBucketPolicy` API actions, even if their bucket policy explicitly denies the root principal's access. Bucket owner root principals can only be blocked from performing these API actions by VPC endpoint policies and AWS Organizations policies.
The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
+ Create
  + s3express:GetBucketPolicy
  + s3express:PutBucketPolicy
+ Read
  + s3express:GetBucketPolicy
+ Update
  + s3express:GetBucketPolicy
  + s3express:PutBucketPolicy
+ Delete
  + s3express:GetBucketPolicy
  + s3express:DeleteBucketPolicy
+ List
  + s3express:GetBucketPolicy
  + s3express:ListAllMyDirectoryBuckets

For more information about example bucket policies, see [Example bucket policies for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam-example-bucket-policies.html) in the *Amazon S3 User Guide*.

The following operations are related to `AWS::S3Express::BucketPolicy`:
+  [PutBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html)
+  [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html)
+  [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html)
+  [ListDirectoryBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListDirectoryBuckets.html)

## Syntax
<a name="aws-resource-s3express-bucketpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3express-bucketpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::S3Express::BucketPolicy",
  "Properties" : {
      "[Bucket](#cfn-s3express-bucketpolicy-bucket)" : {{String}},
      "[PolicyDocument](#cfn-s3express-bucketpolicy-policydocument)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-s3express-bucketpolicy-syntax.yaml"></a>

```
Type: AWS::S3Express::BucketPolicy
Properties:
  [Bucket](#cfn-s3express-bucketpolicy-bucket): {{String}}
  [PolicyDocument](#cfn-s3express-bucketpolicy-policydocument): {{Json}}
```

## Properties
<a name="aws-resource-s3express-bucketpolicy-properties"></a>

`Bucket`  <a name="cfn-s3express-bucketpolicy-bucket"></a>
The name of the S3 directory bucket to which the policy applies.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDocument`  <a name="cfn-s3express-bucketpolicy-policydocument"></a>
A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy [PolicyDocument](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument) resource description in this guide and [Policies and Permissions in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the *Amazon S3 User Guide*.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
