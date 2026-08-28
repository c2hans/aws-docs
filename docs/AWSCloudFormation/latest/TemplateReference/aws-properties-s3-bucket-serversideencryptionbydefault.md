---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-serversideencryptionbydefault.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket ServerSideEncryptionByDefault
<a name="aws-properties-s3-bucket-serversideencryptionbydefault"></a>

Describes the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied. For more information, see [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTencryption.html).

**Note**
**General purpose buckets** - If you don't specify a customer managed key at configuration, Amazon S3 automatically creates an AWS KMS key (`aws/s3`) in your AWS account the first time that you add an object encrypted with SSE-KMS to a bucket. By default, Amazon S3 uses this KMS key for SSE-KMS.
**Directory buckets** - Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucket's lifetime. The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3`) isn't supported.
**Directory buckets** - For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS.

## Syntax
<a name="aws-properties-s3-bucket-serversideencryptionbydefault-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-serversideencryptionbydefault-syntax.json"></a>

```
{
  "[KMSMasterKeyID](#cfn-s3-bucket-serversideencryptionbydefault-kmsmasterkeyid)" : {{String}},
  "[SSEAlgorithm](#cfn-s3-bucket-serversideencryptionbydefault-ssealgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-serversideencryptionbydefault-syntax.yaml"></a>

```
  [KMSMasterKeyID](#cfn-s3-bucket-serversideencryptionbydefault-kmsmasterkeyid): {{String}}
  [SSEAlgorithm](#cfn-s3-bucket-serversideencryptionbydefault-ssealgorithm): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-serversideencryptionbydefault-properties"></a>

`KMSMasterKeyID`  <a name="cfn-s3-bucket-serversideencryptionbydefault-kmsmasterkeyid"></a>
AWS Key Management Service (KMS) customer managed key ID to use for the default encryption.
+ **General purpose buckets** - This parameter is allowed if and only if `SSEAlgorithm` is set to `aws:kms` or `aws:kms:dsse`.
+ **Directory buckets** - This parameter is allowed if and only if `SSEAlgorithm` is set to `aws:kms`.
You can specify the key ID, key alias, or the Amazon Resource Name (ARN) of the KMS key.
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key Alias: `alias/alias-name`
If you are using encryption with cross-account or AWS service operations, you must use a fully qualified KMS key ARN. For more information, see [Using encryption for cross-account operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-update-bucket-policy).
+ **General purpose buckets** - If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key alias instead, then AWS KMS resolves the key within the requester’s account. This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket owner. Also, if you use a key ID, you can run into a LogDestination undeliverable error when creating a VPC flow log.
+ **Directory buckets** - When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.
Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSEAlgorithm`  <a name="cfn-s3-bucket-serversideencryptionbydefault-ssealgorithm"></a>
Server-side encryption algorithm to use for the default encryption.
For directory buckets, there are only two supported values for server-side encryption: `AES256` and `aws:kms`.
*Required*: Yes
*Type*: String
*Allowed values*: `aws:kms | AES256 | aws:kms:dsse`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-serversideencryptionbydefault--examples"></a>

### Create a bucket with default encryption
<a name="aws-properties-s3-bucket-serversideencryptionbydefault--examples--Create_a_bucket_with_default_encryption"></a>

The following example creates a bucket with server-side bucket encryption configured. This example uses encryption with AWS KMS keys (SSE-KMS). You can use dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) by specifying `aws:kms:dsse` for `SSEAlgorithm`. You can also use server-side encryption with S3-managed keys (SSE-S3) by modifying the [Amazon S3 Bucket ServerSideEncryptionByDefault](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html) property to specify `AES256` for `SSEAlgorithm`. For more information, see [Using SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) in the *Amazon S3 User Guide*.

#### JSON
<a name="aws-properties-s3-bucket-serversideencryptionbydefault--examples--Create_a_bucket_with_default_encryption--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "S3 bucket with default encryption",
    "Resources": {
        "EncryptedS3Bucket": {
            "Type": "AWS::S3::Bucket",
            "Properties": {
                "BucketName": {
                    "Fn::Sub": "encryptedbucket-${AWS::Region}-${AWS::AccountId}"
                },
                "BucketEncryption": {
                    "ServerSideEncryptionConfiguration": [
                        {
                            "ServerSideEncryptionByDefault": {
                                "SSEAlgorithm": "aws:kms",
                                "KMSMasterKeyID": "KMS-KEY-ARN"
                            }
                        }
                    ]
                }
            },
            "DeletionPolicy": "Delete"
        }
    }
}
```

#### YAML
<a name="aws-properties-s3-bucket-serversideencryptionbydefault--examples--Create_a_bucket_with_default_encryption--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: S3 bucket with default encryption
Resources:
  EncryptedS3Bucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      BucketName: !Sub 'encryptedbucket-${AWS::Region}-${AWS::AccountId}'
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: 'aws:kms'
              KMSMasterKeyID: KMS-KEY-ARN
    DeletionPolicy: Delete
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
