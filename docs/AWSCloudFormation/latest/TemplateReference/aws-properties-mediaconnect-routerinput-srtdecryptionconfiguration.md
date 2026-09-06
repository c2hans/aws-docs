---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SrtDecryptionConfiguration
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration"></a>

Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionKey](#cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey)" : {{SecretsManagerEncryptionKeyConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionKey](#cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey): {{
    SecretsManagerEncryptionKeyConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration-properties"></a>

`EncryptionKey`  <a name="cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey"></a>
Specifies the encryption key configuration used for decrypting SRT streams, including the key source and associated credentials.
*Required*: Yes
*Type*: [SecretsManagerEncryptionKeyConfiguration](aws-properties-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
