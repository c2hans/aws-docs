---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration S3EncryptionConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration"></a>

<a name="aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration-description"></a>The `S3EncryptionConfiguration` property type specifies Property description not available. for an [AWS::EMRContainers::SecurityConfiguration](aws-resource-emrcontainers-securityconfiguration.md).

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionOption](#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-encryptionoption)" : {{String}},
  "[KMSKeyId](#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionOption](#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-encryptionoption): {{String}}
  [KMSKeyId](#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration-properties"></a>

`EncryptionOption`  <a name="cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-encryptionoption"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `SSE-S3 | SSE-KMS | CSE-KMS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KMSKeyId`  <a name="cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-kmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
