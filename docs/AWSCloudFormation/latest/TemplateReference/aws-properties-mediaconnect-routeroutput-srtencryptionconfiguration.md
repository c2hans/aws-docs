---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput SrtEncryptionConfiguration
<a name="aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration"></a>

Contains the configuration settings for encrypting SRT streams, including the encryption key details and encryption parameters.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionKey](#cfn-mediaconnect-routeroutput-srtencryptionconfiguration-encryptionkey)" : {{SecretsManagerEncryptionKeyConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionKey](#cfn-mediaconnect-routeroutput-srtencryptionconfiguration-encryptionkey): {{
    SecretsManagerEncryptionKeyConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration-properties"></a>

`EncryptionKey`  <a name="cfn-mediaconnect-routeroutput-srtencryptionconfiguration-encryptionkey"></a>
Specifies the encryption key configuration used for encrypting SRT streams, including the key source and associated credentials.
*Required*: Yes
*Type*: [SecretsManagerEncryptionKeyConfiguration](aws-properties-mediaconnect-routeroutput-secretsmanagerencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
