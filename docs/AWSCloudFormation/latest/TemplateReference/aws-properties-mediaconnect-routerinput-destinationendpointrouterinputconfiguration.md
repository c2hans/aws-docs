---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput DestinationEndpointRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration"></a>

<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-description"></a>The `DestinationEndpointRouterInputConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::RouterInput](aws-resource-mediaconnect-routerinput.md).

## Syntax
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-syntax.json"></a>

```
{
  "[EndpointLifecycleManagement](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-endpointlifecyclemanagement)" : {{String}},
  "[SourceTransitDecryption](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryption)" : {{EndpointEncryptionConfiguration}},
  "[SourceTransitDecryptionType](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryptiontype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-syntax.yaml"></a>

```
  [EndpointLifecycleManagement](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-endpointlifecyclemanagement): {{String}}
  [SourceTransitDecryption](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryption): {{
    EndpointEncryptionConfiguration}}
  [SourceTransitDecryptionType](#cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryptiontype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-properties"></a>

`EndpointLifecycleManagement`  <a name="cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-endpointlifecyclemanagement"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `MANAGED | UNMANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryption`  <a name="cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryption"></a>
Property description not available.
*Required*: Yes
*Type*: [EndpointEncryptionConfiguration](aws-properties-mediaconnect-routerinput-endpointencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceTransitDecryptionType`  <a name="cfn-mediaconnect-routerinput-destinationendpointrouterinputconfiguration-sourcetransitdecryptiontype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `SECRETS_MANAGER | AUTOMATIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
