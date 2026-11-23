---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SecretsManagerEndpointEncryptionConfiguration

The endpoint encryption configuration for connections that use a key or passphrase that you store in AWS Secrets Manager.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-syntax.json"></a>

```json
{
  "[EncryptionSecret](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecret)" : {{EndpointEncryptionSecretConfiguration}},
  "[EncryptionSecretType](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecrettype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-syntax.yaml"></a>

```yaml
  [EncryptionSecret](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecret): {{
    EndpointEncryptionSecretConfiguration}}
  [EncryptionSecretType](#cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecrettype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-properties"></a>

`EncryptionSecret`  <a name="cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecret"></a>
The AWS Secrets Manager secret that holds the key or passphrase used to encrypt the connection.
*Required*: Yes
*Type*: [EndpointEncryptionSecretConfiguration](aws-properties-mediaconnect-routerinput-endpointencryptionsecretconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionSecretType`  <a name="cfn-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration-encryptionsecrettype"></a>
The type of secret used to encrypt the connection. Valid values include the following:
+ `AES_128_KEY` – A 128-bit AES encryption key.
+ `AES_192_KEY` – A 192-bit AES encryption key.
+ `AES_256_KEY` – A 256-bit AES encryption key.
+ `SRT_PASSPHRASE` – An SRT passphrase.
*Required*: No
*Type*: String
*Allowed values*: `AES_128_KEY | AES_192_KEY | AES_256_KEY | SRT_PASSPHRASE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
