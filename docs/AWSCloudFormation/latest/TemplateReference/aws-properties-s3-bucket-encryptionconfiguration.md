---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket EncryptionConfiguration
<a name="aws-properties-s3-bucket-encryptionconfiguration"></a>

Specifies encryption-related information for an Amazon S3 bucket that is a destination for replicated objects.

**Note**
If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key alias instead, then AWS KMS resolves the key within the requester’s account. This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket owner.

## Syntax
<a name="aws-properties-s3-bucket-encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-encryptionconfiguration-syntax.json"></a>

```
{
  "[ReplicaKmsKeyID](#cfn-s3-bucket-encryptionconfiguration-replicakmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-encryptionconfiguration-syntax.yaml"></a>

```
  [ReplicaKmsKeyID](#cfn-s3-bucket-encryptionconfiguration-replicakmskeyid): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-encryptionconfiguration-properties"></a>

`ReplicaKmsKeyID`  <a name="cfn-s3-bucket-encryptionconfiguration-replicakmskeyid"></a>
Specifies the ID (Key ARN or Alias ARN) of the customer managed AWS KMS key stored in AWS Key Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com//kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-s3-bucket-encryptionconfiguration--seealso"></a>
+ AWS::S3::Bucket [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html#aws-properties-s3-bucket--examples)
