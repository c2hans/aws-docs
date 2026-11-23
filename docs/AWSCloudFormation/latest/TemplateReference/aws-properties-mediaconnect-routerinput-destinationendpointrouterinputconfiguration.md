---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput DestinationEndpointRouterInputConfiguration

Configuration settings for a router input that is represented by a destination endpoint.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-syntax.json"></a>

```json
{
  "[EndpointLifecycleManagement](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-endpointlifecyclemanagement)" : {{String}},
  "[SourceTransitDecryption](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryption)" : {{EndpointEncryptionConfiguration}},
  "[SourceTransitDecryptionType](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryptiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-syntax.yaml"></a>

```yaml
  [EndpointLifecycleManagement](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-endpointlifecyclemanagement): {{String}}
  [SourceTransitDecryption](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryption): {{
    EndpointEncryptionConfiguration}}
  [SourceTransitDecryptionType](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryptiontype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-properties"></a>

`EndpointLifecycleManagement`  <a name="cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-endpointlifecyclemanagement"></a>
The entity that manages the lifecycle of the associated destination endpoint. Valid values include the following:
+ `MANAGED` – MediaConnect manages the lifecycle of the associated destination endpoint.
+ `UNMANAGED` – You manage the lifecycle of the associated destination endpoint.
*Required*: Yes
*Type*: String
*Allowed values*: `MANAGED | UNMANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryption`  <a name="cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryption"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
*Required*: Yes
*Type*: [EndpointEncryptionConfiguration](aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryptionType`  <a name="cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryptiontype"></a>
The type of transit decryption applied to the source content that this router input receives. Valid values include the following:
+ `SECRETS_MANAGER` – The decryption key or passphrase is stored in AWS Secrets Manager.
+ `AUTOMATIC` – MediaConnect determines the decryption key when the endpoint connects.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
