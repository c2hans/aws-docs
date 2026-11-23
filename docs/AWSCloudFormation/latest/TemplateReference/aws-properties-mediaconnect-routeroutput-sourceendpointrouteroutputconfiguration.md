---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput SourceEndpointRouterOutputConfiguration

Configuration settings for a router output that is represented by a source endpoint.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-syntax.json"></a>

```json
{
  "[DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryption)" : {{EndpointEncryptionConfiguration}},
  "[DestinationTransitEncryptionType](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryptiontype)" : {{String}},
  "[EndpointLifecycleManagement](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-endpointlifecyclemanagement)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-syntax.yaml"></a>

```yaml
  [DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryption): {{
    EndpointEncryptionConfiguration}}
  [DestinationTransitEncryptionType](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryptiontype): {{String}}
  [EndpointLifecycleManagement](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-endpointlifecyclemanagement): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-properties"></a>

`DestinationTransitEncryption`  <a name="cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryption"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
*Required*: Yes
*Type*: [EndpointEncryptionConfiguration](aws-properties-mediaconnect-routeroutput-endpointencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationTransitEncryptionType`  <a name="cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryptiontype"></a>
The type of transit encryption applied to the destination content that this router output sends. Valid values include the following:
+ `SECRETS_MANAGER` – The encryption key or passphrase is stored in AWS Secrets Manager.
+ `AUTOMATIC` – MediaConnect determines the encryption key when the endpoint connects.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointLifecycleManagement`  <a name="cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-endpointlifecyclemanagement"></a>
The entity that manages the lifecycle of the associated source endpoint. Valid values include the following:
+ `MANAGED` – MediaConnect manages the lifecycle of the associated source endpoint.
+ `UNMANAGED` – You manage the lifecycle of the associated source endpoint.
*Required*: Yes
*Type*: String
*Allowed values*: `MANAGED | UNMANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
