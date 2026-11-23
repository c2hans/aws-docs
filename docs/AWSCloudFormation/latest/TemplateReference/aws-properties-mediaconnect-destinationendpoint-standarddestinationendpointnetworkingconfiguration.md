---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint StandardDestinationEndpointNetworkingConfiguration

The networking configuration for a standard destination endpoint. This is a union type, so exactly one of its members is set: `public` for a publicly accessible endpoint, or `vpc` for an endpoint in a virtual private cloud (VPC).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-syntax.json"></a>

```json
{
  "[Public](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-public)" : {{PublicDestinationEndpointNetworkingConfiguration}},
  "[Vpc](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-vpc)" : {{VpcDestinationEndpointNetworkingConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-syntax.yaml"></a>

```yaml
  [Public](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-public): {{
    PublicDestinationEndpointNetworkingConfiguration}}
  [Vpc](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-vpc): {{
    VpcDestinationEndpointNetworkingConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-properties"></a>

`Public`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-public"></a>
The configuration for a publicly accessible destination endpoint.
*Required*: No
*Type*: [PublicDestinationEndpointNetworkingConfiguration](aws-properties-mediaconnect-destinationendpoint-publicdestinationendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Vpc`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration-vpc"></a>
The configuration for a destination endpoint in a virtual private cloud (VPC).
*Required*: No
*Type*: [VpcDestinationEndpointNetworkingConfiguration](aws-properties-mediaconnect-destinationendpoint-vpcdestinationendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
