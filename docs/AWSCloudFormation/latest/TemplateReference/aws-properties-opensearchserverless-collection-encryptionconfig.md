---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-opensearchserverless-collection-encryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OpenSearchServerless::Collection EncryptionConfig
<a name="aws-properties-opensearchserverless-collection-encryptionconfig"></a>

Encryption settings for the collection.

## Syntax
<a name="aws-properties-opensearchserverless-collection-encryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-opensearchserverless-collection-encryptionconfig-syntax.json"></a>

```
{
  "[AWSOwnedKey](#cfn-opensearchserverless-collection-encryptionconfig-awsownedkey)" : {{Boolean}},
  "[KmsKeyArn](#cfn-opensearchserverless-collection-encryptionconfig-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-opensearchserverless-collection-encryptionconfig-syntax.yaml"></a>

```
  [AWSOwnedKey](#cfn-opensearchserverless-collection-encryptionconfig-awsownedkey): {{Boolean}}
  [KmsKeyArn](#cfn-opensearchserverless-collection-encryptionconfig-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-opensearchserverless-collection-encryptionconfig-properties"></a>

`AWSOwnedKey`  <a name="cfn-opensearchserverless-collection-encryptionconfig-awsownedkey"></a>
Indicates whether to use an AWS-owned key for encryption.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyArn`  <a name="cfn-opensearchserverless-collection-encryptionconfig-kmskeyarn"></a>
The ARN of the AWS KMS key used to encrypt the collection.
*Required*: No
*Type*: String
*Pattern*: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):(kms):[a-zA-Z-]+\d{1}:\d{12}:(key)\/.{1,2048}.*`
*Minimum*: `10`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
