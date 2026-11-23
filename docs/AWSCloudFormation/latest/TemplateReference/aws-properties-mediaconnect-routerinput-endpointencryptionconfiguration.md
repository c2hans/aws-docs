---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput EndpointEncryptionConfiguration

The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration-syntax.json"></a>

```json
{
  "[Automatic](#cfn-mediaconnect-routerinput-endpointencryptionconfiguration-automatic)" : {{Json}},
  "[SecretsManager](#cfn-mediaconnect-routerinput-endpointencryptionconfiguration-secretsmanager)" : {{SecretsManagerEndpointEncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration-syntax.yaml"></a>

```yaml
  [Automatic](#cfn-mediaconnect-routerinput-endpointencryptionconfiguration-automatic): {{Json}}
  [SecretsManager](#cfn-mediaconnect-routerinput-endpointencryptionconfiguration-secretsmanager): {{
    SecretsManagerEndpointEncryptionConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration-properties"></a>

`Automatic`  <a name="cfn-mediaconnect-routerinput-endpointencryptionconfiguration-automatic"></a>
The configuration for automatic encryption, where MediaConnect determines the encryption key when the endpoint connects.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManager`  <a name="cfn-mediaconnect-routerinput-endpointencryptionconfiguration-secretsmanager"></a>
The encryption configuration for a connection that uses a key or passphrase that you store in AWS Secrets Manager.
*Required*: No
*Type*: [SecretsManagerEndpointEncryptionConfiguration](aws-properties-mediaconnect-routerinput-secretsmanagerendpointencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
