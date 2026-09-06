---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-serversideencryptionrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket ServerSideEncryptionRule
<a name="aws-properties-s3express-directorybucket-serversideencryptionrule"></a>

Specifies the default server-side encryption configuration.

## Syntax
<a name="aws-properties-s3express-directorybucket-serversideencryptionrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-serversideencryptionrule-syntax.json"></a>

```
{
  "[BucketKeyEnabled](#cfn-s3express-directorybucket-serversideencryptionrule-bucketkeyenabled)" : {{Boolean}},
  "[ServerSideEncryptionByDefault](#cfn-s3express-directorybucket-serversideencryptionrule-serversideencryptionbydefault)" : {{ServerSideEncryptionByDefault}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-serversideencryptionrule-syntax.yaml"></a>

```
  [BucketKeyEnabled](#cfn-s3express-directorybucket-serversideencryptionrule-bucketkeyenabled): {{Boolean}}
  [ServerSideEncryptionByDefault](#cfn-s3express-directorybucket-serversideencryptionrule-serversideencryptionbydefault): {{
    ServerSideEncryptionByDefault}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-serversideencryptionrule-properties"></a>

`BucketKeyEnabled`  <a name="cfn-s3express-directorybucket-serversideencryptionrule-bucketkeyenabled"></a>
Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS) for new objects in the bucket. S3 Bucket Keys are always enabled for `GET` and `PUT` operations on a directory bucket and can’t be disabled. It's only allowed to set the `BucketKeyEnabled` element to `true`.
S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html), [UploadPartCopy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops), or [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.
For more information, see [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-UsingKMSEncryption.html#s3-express-sse-kms-bucket-keys) in the *Amazon S3 User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerSideEncryptionByDefault`  <a name="cfn-s3express-directorybucket-serversideencryptionrule-serversideencryptionbydefault"></a>
Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied.
*Required*: No
*Type*: [ServerSideEncryptionByDefault](aws-properties-s3express-directorybucket-serversideencryptionbydefault.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
