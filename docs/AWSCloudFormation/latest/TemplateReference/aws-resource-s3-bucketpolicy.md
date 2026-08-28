---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-s3-bucketpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::BucketPolicy
<a name="aws-resource-s3-bucketpolicy"></a>

Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of the AWS account that owns the bucket, the calling identity must have the `PutBucketPolicy` permissions on the specified bucket and belong to the bucket owner's account in order to use this operation.

If you don't have `PutBucketPolicy` permissions, Amazon S3 returns a `403 Access Denied` error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a `405 Method Not Allowed` error.

**Important**
 As a security precaution, the root user of the AWS account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action.

When using the `AWS::S3::BucketPolicy` resource, you can create, update, and delete bucket policies for S3 buckets located in Regions that are different from the stack's Region. However, the CloudFormation stacks should be deployed in the US East (N. Virginia) or `us-east-1` Region. This cross-region bucket policy modification functionality is supported for backward compatibility with existing workflows.

**Important**
If the [DeletionPolicy attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html) is not specified or set to `Delete`, the bucket policy will be removed when the stack is deleted. If set to `Retain`, the bucket policy will be preserved even after the stack is deleted.

For example, a CloudFormation stack in `us-east-1` can use the `AWS::S3::BucketPolicy` resource to manage the bucket policy for an S3 bucket in `us-west-2`. The retention or removal of the bucket policy during the stack deletion is determined by the `DeletionPolicy` attribute specified in the stack template.

For more information, see [Bucket policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html).

The following operations are related to `PutBucketPolicy`:
+  [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html)
+  [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)

## Syntax
<a name="aws-resource-s3-bucketpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-s3-bucketpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::S3::BucketPolicy",
  "Properties" : {
      "[Bucket](#cfn-s3-bucketpolicy-bucket)" : {{String}},
      "[PolicyDocument](#cfn-s3-bucketpolicy-policydocument)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-s3-bucketpolicy-syntax.yaml"></a>

```
Type: AWS::S3::BucketPolicy
Properties:
  [Bucket](#cfn-s3-bucketpolicy-bucket): {{String}}
  [PolicyDocument](#cfn-s3-bucketpolicy-policydocument): {{Json}}
```

## Properties
<a name="aws-resource-s3-bucketpolicy-properties"></a>

`Bucket`  <a name="cfn-s3-bucketpolicy-bucket"></a>
The name of the Amazon S3 bucket to which the policy applies.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDocument`  <a name="cfn-s3-bucketpolicy-policydocument"></a>
 A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy [PolicyDocument](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument) resource description in this guide and [Access Policy Language Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the *Amazon S3 User Guide*.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-resource-s3-bucketpolicy--examples"></a>

### Bucket policy that allows GET requests from specific referers
<a name="aws-resource-s3-bucketpolicy--examples--Bucket_policy_that_allows_GET_requests_from_specific_referers"></a>

The following sample is a bucket policy that is attached to the DOC-EXAMPLE-BUCKET bucket and allows GET requests that originate from www.example.com and example.net:

**Important**
This key should be used carefully. It is dangerous to include a publicly known referer header value. Unauthorized parties can use modified or custom browsers to provide any `aws:referer` value that they choose. As a result, `aws:referer` should not be used to prevent unauthorized parties from making direct AWS requests. It is offered only to allow customers to protect their digital content, such as content stored in Amazon S3, from being referenced on unauthorized third-party sites. For more information, see [`aws:referer`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-referer) in the * IAM User Guide *.

#### JSON
<a name="aws-resource-s3-bucketpolicy--examples--Bucket_policy_that_allows_GET_requests_from_specific_referers--json"></a>

```
{
    "SampleBucketPolicy": {
        "Type": "AWS::S3::BucketPolicy",
        "Properties": {
            "Bucket": {
                "Ref": "DOC-EXAMPLE-BUCKET"
            },
            "PolicyDocument": {
                "Version": "2012-10-17"		 	 	 ,
                "Statement": [
                    {
                        "Action": [
                            "s3:GetObject"
                        ],
                        "Effect": "Allow",
                        "Resource": {
                            "Fn::Join": [
                                "",
                                [
                                    "arn:aws:s3:::",
                                    {
                                        "Ref": "DOC-EXAMPLE-BUCKET"
                                    },
                                    "/*"
                                ]
                            ]
                        },
                        "Principal": "*",
                        "Condition": {
                            "StringLike": {
                                "aws:Referer": [
                                    "http://www.example.com/*",
                                    "http://example.net/*"
                                ]
                            }
                        }
                    }
                ]
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-s3-bucketpolicy--examples--Bucket_policy_that_allows_GET_requests_from_specific_referers--yaml"></a>

```
SampleBucketPolicy:
  Type: AWS::S3::BucketPolicy
  Properties:
    Bucket: !Ref DOC-EXAMPLE-BUCKET
    PolicyDocument:
      Version: 2012-10-17
      Statement:
        - Action:
            - 's3:GetObject'
          Effect: Allow
          Resource: !Join
            - ''
            - - 'arn:aws:s3:::'
              - !Ref DOC-EXAMPLE-BUCKET
              - /*
          Principal: '*'
          Condition:
            StringLike:
              'aws:Referer':
                - 'http://www.example.com/*'
                - 'http://example.net/*'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
