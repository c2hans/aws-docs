---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-serversideencryptionrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket ServerSideEncryptionRule
<a name="aws-properties-s3-bucket-serversideencryptionrule"></a>

Specifies the default server-side encryption configuration.

**Note**
**General purpose buckets** - If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key alias instead, then AWS KMS resolves the key within the requester’s account. This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket owner.
**Directory buckets** - When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

## Syntax
<a name="aws-properties-s3-bucket-serversideencryptionrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-serversideencryptionrule-syntax.json"></a>

```
{
  "[BlockedEncryptionTypes](#cfn-s3-bucket-serversideencryptionrule-blockedencryptiontypes)" : {{BlockedEncryptionTypes}},
  "[BucketKeyEnabled](#cfn-s3-bucket-serversideencryptionrule-bucketkeyenabled)" : {{Boolean}},
  "[ServerSideEncryptionByDefault](#cfn-s3-bucket-serversideencryptionrule-serversideencryptionbydefault)" : {{ServerSideEncryptionByDefault}}
}
```

### YAML
<a name="aws-properties-s3-bucket-serversideencryptionrule-syntax.yaml"></a>

```
  [BlockedEncryptionTypes](#cfn-s3-bucket-serversideencryptionrule-blockedencryptiontypes): {{
    BlockedEncryptionTypes}}
  [BucketKeyEnabled](#cfn-s3-bucket-serversideencryptionrule-bucketkeyenabled): {{Boolean}}
  [ServerSideEncryptionByDefault](#cfn-s3-bucket-serversideencryptionrule-serversideencryptionbydefault): {{
    ServerSideEncryptionByDefault}}
```

## Properties
<a name="aws-properties-s3-bucket-serversideencryptionrule-properties"></a>

`BlockedEncryptionTypes`  <a name="cfn-s3-bucket-serversideencryptionrule-blockedencryptiontypes"></a>
A bucket-level setting for Amazon S3 general purpose buckets used to prevent the upload of new objects encrypted with the specified server-side encryption type. For example, blocking an encryption type will block `PutObject`, `CopyObject`, `PostObject`, multipart upload, and replication requests to the bucket for objects with the specified encryption type. However, you can continue to read and list any pre-existing objects already encrypted with the specified encryption type. For more information, see [Blocking or unblocking SSE-C for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html).
Currently, this parameter only supports blocking or unblocking server-side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see [Using server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html).
*Required*: No
*Type*: [BlockedEncryptionTypes](aws-properties-s3-bucket-blockedencryptiontypes.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketKeyEnabled`  <a name="cfn-s3-bucket-serversideencryptionrule-bucketkeyenabled"></a>
Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS) for new objects in the bucket. Existing objects are not affected. Setting the `BucketKeyEnabled` element to `true` causes Amazon S3 to use an S3 Bucket Key. By default, S3 Bucket Key is not enabled.
For more information, see [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideEncryptionByDefault`  <a name="cfn-s3-bucket-serversideencryptionrule-serversideencryptionbydefault"></a>
Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied.
*Required*: No
*Type*: [ServerSideEncryptionByDefault](aws-properties-s3-bucket-serversideencryptionbydefault.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples"></a>

**Topics**
+ [Create a bucket with default encryption](#aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_with_default_encryption)
+ [Create a bucket using KMS server-side encryption with an S3 Bucket Key](#aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_using_KMS_server-side_encryption_with_an_S3_Bucket_Key)

### Create a bucket with default encryption
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_with_default_encryption"></a>

The following example creates a bucket with server-side bucket encryption configured. This example uses encryption with KMS keys (SSE-KMS). You can use dual-layer server-side encryption with AWS KMS keys (DSSE-KMS) by specifying `aws:kms:dsse` for `SSEAlgorithm`. You can also use server-side encryption with S3-managed keys (SSE-S3) by modifying the [Amazon S3 Bucket ServerSideEncryptionByDefault](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-serversideencryptionbydefault.html) property to specify `AES256` for `SSEAlgorithm`. For more information, see [Using SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) in the *Amazon S3 User Guide*.

#### JSON
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_with_default_encryption--json"></a>

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
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_with_default_encryption--yaml"></a>

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

### Create a bucket using KMS server-side encryption with an S3 Bucket Key
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_using_KMS_server-side_encryption_with_an_S3_Bucket_Key"></a>

The following example creates a bucket that specifies default encryption using AWS KMS server-side encryption with an S3 Bucket Key. The example uses a customer managed AWS KMS key.

#### JSON
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_using_KMS_server-side_encryption_with_an_S3_Bucket_Key--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "S3 bucket with default encryption using SSE-KMS with an S3 Bucket Key",
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
                            },
                            "BucketKeyEnabled": true
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
<a name="aws-properties-s3-bucket-serversideencryptionrule--examples--Create_a_bucket_using_KMS_server-side_encryption_with_an_S3_Bucket_Key--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: S3 bucket with default encryption using SSE-KMS with an S3 Bucket Key
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
            BucketKeyEnabled: true
    DeletionPolicy: Delete
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
