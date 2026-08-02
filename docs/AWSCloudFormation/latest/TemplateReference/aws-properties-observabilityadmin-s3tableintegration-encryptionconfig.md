---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-s3tableintegration-encryptionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::S3TableIntegration EncryptionConfig
<a name="aws-properties-observabilityadmin-s3tableintegration-encryptionconfig"></a>

Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.

## Syntax
<a name="aws-properties-observabilityadmin-s3tableintegration-encryptionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-s3tableintegration-encryptionconfig-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-observabilityadmin-s3tableintegration-encryptionconfig-kmskeyarn)" : {{String}},
  "[SseAlgorithm](#cfn-observabilityadmin-s3tableintegration-encryptionconfig-ssealgorithm)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-s3tableintegration-encryptionconfig-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-observabilityadmin-s3tableintegration-encryptionconfig-kmskeyarn): {{String}}
  [SseAlgorithm](#cfn-observabilityadmin-s3tableintegration-encryptionconfig-ssealgorithm): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-s3tableintegration-encryptionconfig-properties"></a>

`KmsKeyArn`  <a name="cfn-observabilityadmin-s3tableintegration-encryptionconfig-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the KMS key used for encryption when using customer-managed keys.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)$`
*Minimum*: `1`
*Maximum*: `1011`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SseAlgorithm`  <a name="cfn-observabilityadmin-s3tableintegration-encryptionconfig-ssealgorithm"></a>
The server-side encryption algorithm used for encrypting data in the S3 Table integration.
*Required*: Yes
*Type*: String
*Allowed values*: `AES256 | aws:kms`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
