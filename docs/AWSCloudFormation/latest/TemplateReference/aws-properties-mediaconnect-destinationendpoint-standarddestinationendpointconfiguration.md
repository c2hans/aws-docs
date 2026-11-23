---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint StandardDestinationEndpointConfiguration

The configuration settings for a standard destination endpoint.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-syntax.json"></a>

```json
{
  "[DestinationNetworkingConfiguration](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingconfiguration)" : {{StandardDestinationEndpointNetworkingConfiguration}},
  "[DestinationNetworkingType](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingtype)" : {{String}},
  "[Name](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-name)" : {{String}},
  "[Protocol](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocol)" : {{String}},
  "[ProtocolConfiguration](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocolconfiguration)" : {{StandardDestinationEndpointProtocolConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-syntax.yaml"></a>

```yaml
  [DestinationNetworkingConfiguration](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingconfiguration): {{
    StandardDestinationEndpointNetworkingConfiguration}}
  [DestinationNetworkingType](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingtype): {{String}}
  [Name](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-name): {{String}}
  [Protocol](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocol): {{String}}
  [ProtocolConfiguration](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocolconfiguration): {{
    StandardDestinationEndpointProtocolConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-properties"></a>

`DestinationNetworkingConfiguration`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingconfiguration"></a>
The networking configuration for the destination endpoint, which determines whether it is publicly accessible or in a virtual private cloud (VPC).
*Required*: Yes
*Type*: [StandardDestinationEndpointNetworkingConfiguration](aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationNetworkingType`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingtype"></a>
The networking type of the destination endpoint. Valid values include the following:
+ `PUBLIC` – The destination endpoint is publicly accessible.
+ `VPC` – The destination endpoint is in a virtual private cloud (VPC).
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-name"></a>
The name of the destination endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `164`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocol"></a>
The protocol used by the destination endpoint. Valid values include the following:
+ `RTP` – Real-time Transport Protocol.
+ `RIST` – Reliable Internet Stream Transport.
+ `SRT_CALLER` – Secure Reliable Transport (SRT) in caller mode.
+ `SRT_LISTENER` – Secure Reliable Transport (SRT) in listener mode.
*Required*: No
*Type*: String
*Allowed values*: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocolconfiguration"></a>
The protocol configuration for the destination endpoint.
*Required*: Yes
*Type*: [StandardDestinationEndpointProtocolConfiguration](aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
