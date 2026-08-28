---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3express-directorybucket-serversideencryptionbydefault.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Express::DirectoryBucket ServerSideEncryptionByDefault
<a name="aws-properties-s3express-directorybucket-serversideencryptionbydefault"></a>

Describes the default server-side encryption to apply to new objects in the bucket. If a PUT Object request doesn't specify any server-side encryption, this default encryption will be applied. For more information, see [PutBucketEncryption](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTencryption.html) in the *Amazon S3 API Reference*.

## Syntax
<a name="aws-properties-s3express-directorybucket-serversideencryptionbydefault-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3express-directorybucket-serversideencryptionbydefault-syntax.json"></a>

```
{
  "[KMSMasterKeyID](#cfn-s3express-directorybucket-serversideencryptionbydefault-kmsmasterkeyid)" : {{String}},
  "[SSEAlgorithm](#cfn-s3express-directorybucket-serversideencryptionbydefault-ssealgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3express-directorybucket-serversideencryptionbydefault-syntax.yaml"></a>

```
  [KMSMasterKeyID](#cfn-s3express-directorybucket-serversideencryptionbydefault-kmsmasterkeyid): {{String}}
  [SSEAlgorithm](#cfn-s3express-directorybucket-serversideencryptionbydefault-ssealgorithm): {{String}}
```

## Properties
<a name="aws-properties-s3express-directorybucket-serversideencryptionbydefault-properties"></a>

`KMSMasterKeyID`  <a name="cfn-s3express-directorybucket-serversideencryptionbydefault-kmsmasterkeyid"></a>
AWS Key Management Service (KMS) customer managed key ID to use for the default encryption. This parameter is allowed only if `SSEAlgorithm` is set to `aws:kms`.
You can specify this parameter with the key ID or the Amazon Resource Name (ARN) of the KMS key. You can’t use the key alias of the KMS key.
+ Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
+ Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
If you are using encryption with cross-account or AWS service operations, you must use a fully qualified KMS key ARN. For more information, see [Using encryption for cross-account operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-bucket-encryption.html#s3-express-bucket-encryption-update-bucket-policy).
Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) per directory bucket for the lifetime of the bucket. [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) (`aws/s3`) isn't supported. Also, after you specify a customer managed key for SSE-KMS and upload objects with this configuration, you can't override the customer managed key for your SSE-KMS configuration. To use a new customer manager key for your data, we recommend copying your existing objects to a new directory bucket with a new customer managed key.
Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SSEAlgorithm`  <a name="cfn-s3express-directorybucket-serversideencryptionbydefault-ssealgorithm"></a>
Server-side encryption algorithm to use for the default encryption.
For directory buckets, there are only two supported values for server-side encryption: `AES256` and `aws:kms`.
*Required*: Yes
*Type*: String
*Allowed values*: `aws:kms | AES256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
