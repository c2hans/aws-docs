---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput SourceEndpointRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration"></a>

<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-description"></a>The `SourceEndpointRouterOutputConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterOutput](aws-resource-mediaconnect-routeroutput.md).

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-syntax.json"></a>

```
{
  "[DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryption)" : {{EndpointEncryptionConfiguration}},
  "[DestinationTransitEncryptionType](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryptiontype)" : {{String}},
  "[EndpointLifecycleManagement](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-endpointlifecyclemanagement)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-syntax.yaml"></a>

```
  [DestinationTransitEncryption](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryption): {{
    EndpointEncryptionConfiguration}}
  [DestinationTransitEncryptionType](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryptiontype): {{String}}
  [EndpointLifecycleManagement](#cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-endpointlifecyclemanagement): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-properties"></a>

`DestinationTransitEncryption`  <a name="cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryption"></a>
Property description not available.
*Required*: Yes
*Type*: [EndpointEncryptionConfiguration](aws-properties-mediaconnect-routeroutput-endpointencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationTransitEncryptionType`  <a name="cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-destinationtransitencryptiontype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndpointLifecycleManagement`  <a name="cfn-mediaconnect-routeroutput-sourceendpointrouteroutputconfiguration-endpointlifecyclemanagement"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `MANAGED | UNMANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
