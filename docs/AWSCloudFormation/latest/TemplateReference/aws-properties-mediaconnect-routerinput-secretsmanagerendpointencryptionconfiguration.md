---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SecretsManagerEndpointEncryptionConfiguration
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration"></a>

<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-description"></a>The `SecretsManagerEndpointEncryptionConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterInput](aws-resource-mediaconnect-routerinput.md).

## Syntax
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-syntax.json"></a>

```
{
  "[EncryptionSecret](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecret)" : {{EndpointEncryptionSecretConfiguration}},
  "[EncryptionSecretType](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecrettype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-syntax.yaml"></a>

```
  [EncryptionSecret](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecret): {{
    EndpointEncryptionSecretConfiguration}}
  [EncryptionSecretType](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecrettype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-properties"></a>

`EncryptionSecret`  <a name="cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecret"></a>
Property description not available.
*Required*: Yes
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-routerinput-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionSecretType`  <a name="cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecrettype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `AES_128_KEY | AES_192_KEY | AES_256_KEY | SRT_PASSPHRASE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
