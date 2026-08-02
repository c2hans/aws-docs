---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-blockedencryptiontypes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket BlockedEncryptionTypes
<a name="aws-properties-s3-bucket-blockedencryptiontypes"></a>

A bucket-level setting for Amazon S3 general purpose buckets used to prevent the upload of new objects encrypted with the specified server-side encryption type. For example, blocking an encryption type will block `PutObject`, `CopyObject`, `PostObject`, multipart upload, and replication requests to the bucket for objects with the specified encryption type. However, you can continue to read and list any pre-existing objects already encrypted with the specified encryption type. For more information, see [Blocking or unblocking SSE-C for a general purpose bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/blocking-unblocking-s3-c-encryption-gpb.html).

This data type is used with the following actions:
+  [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html)
+  [GetBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html)
+  [DeleteBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html)

Permissions
You must have the `s3:PutEncryptionConfiguration` permission to block or unblock an encryption type for a bucket.
You must have the `s3:GetEncryptionConfiguration` permission to view a bucket's encryption type.

## Syntax
<a name="aws-properties-s3-bucket-blockedencryptiontypes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-blockedencryptiontypes-syntax.json"></a>

```
{
  "[EncryptionType](#cfn-s3-bucket-blockedencryptiontypes-encryptiontype)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-s3-bucket-blockedencryptiontypes-syntax.yaml"></a>

```
  [EncryptionType](#cfn-s3-bucket-blockedencryptiontypes-encryptiontype): {{
    - String}}
```

## Properties
<a name="aws-properties-s3-bucket-blockedencryptiontypes-properties"></a>

`EncryptionType`  <a name="cfn-s3-bucket-blockedencryptiontypes-encryptiontype"></a>
The object encryption type that you want to block or unblock for an Amazon S3 general purpose bucket.
Currently, this parameter only supports blocking or unblocking server side encryption with customer-provided keys (SSE-C). For more information about SSE-C, see [Using server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html).
*Required*: No
*Type*: Array of String
*Allowed values*: `NONE | SSE-C`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
