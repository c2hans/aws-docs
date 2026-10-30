---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint StandardDestinationEndpointConfiguration
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-description"></a>The `StandardDestinationEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::DestinationEndpoint](aws-resource-mediaconnect-destinationendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-syntax.json"></a>

```
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

```
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
Property description not available.
*Required*: Yes
*Type*: [StandardDestinationEndpointNetworkingConfiguration](aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationNetworkingType`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-destinationnetworkingtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `164`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointconfiguration-protocolconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [StandardDestinationEndpointProtocolConfiguration](aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
