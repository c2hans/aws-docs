---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-instancestorageconfig-encryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::InstanceStorageConfig EncryptionConfig
<a name="aws-properties-connect-instancestorageconfig-encryptionconfig"></a>

The encryption configuration.

## Syntax
<a name="aws-properties-connect-instancestorageconfig-encryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-instancestorageconfig-encryptionconfig-syntax.json"></a>

```
{
  "[EncryptionType](#cfn-connect-instancestorageconfig-encryptionconfig-encryptiontype)" : {{String}},
  "[KeyId](#cfn-connect-instancestorageconfig-encryptionconfig-keyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-connect-instancestorageconfig-encryptionconfig-syntax.yaml"></a>

```
  [EncryptionType](#cfn-connect-instancestorageconfig-encryptionconfig-encryptiontype): {{String}}
  [KeyId](#cfn-connect-instancestorageconfig-encryptionconfig-keyid): {{String}}
```

## Properties
<a name="aws-properties-connect-instancestorageconfig-encryptionconfig-properties"></a>

`EncryptionType`  <a name="cfn-connect-instancestorageconfig-encryptionconfig-encryptiontype"></a>
The type of encryption.
*Required*: Yes
*Type*: String
*Allowed values*: `KMS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyId`  <a name="cfn-connect-instancestorageconfig-encryptionconfig-keyid"></a>
The full ARN of the encryption key.
Be sure to provide the full ARN of the encryption key, not just the ID.
Connect Customer supports only KMS keys with the default key spec of [`SYMMETRIC_DEFAULT`](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric-default).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
