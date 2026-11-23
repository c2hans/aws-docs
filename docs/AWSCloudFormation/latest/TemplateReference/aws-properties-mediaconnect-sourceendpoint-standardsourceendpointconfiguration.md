---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint StandardSourceEndpointConfiguration

The configuration settings for a standard source endpoint.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-syntax.json"></a>

```json
{
  "[Name](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-name)" : {{String}},
  "[Protocol](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocol)" : {{String}},
  "[ProtocolConfiguration](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocolconfiguration)" : {{StandardSourceEndpointProtocolConfiguration}},
  "[SourceNetworkingConfiguration](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingconfiguration)" : {{StandardSourceEndpointNetworkingConfiguration}},
  "[SourceNetworkingType](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-syntax.yaml"></a>

```yaml
  [Name](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-name): {{String}}
  [Protocol](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocol): {{String}}
  [ProtocolConfiguration](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocolconfiguration): {{
    StandardSourceEndpointProtocolConfiguration}}
  [SourceNetworkingConfiguration](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingconfiguration): {{
    StandardSourceEndpointNetworkingConfiguration}}
  [SourceNetworkingType](#cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingtype): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-properties"></a>

`Name`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-name"></a>
The name of the source endpoint.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `164`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocol"></a>
The protocol used by the source endpoint. Valid values include the following:
+ `RTP` – Real-time Transport Protocol.
+ `RIST` – Reliable Internet Stream Transport.
+ `SRT_CALLER` – Secure Reliable Transport (SRT) in caller mode.
+ `SRT_LISTENER` – Secure Reliable Transport (SRT) in listener mode.
*Required*: No
*Type*: String
*Allowed values*: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocolconfiguration"></a>
The protocol configuration for the source endpoint.
*Required*: Yes
*Type*: [StandardSourceEndpointProtocolConfiguration](aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceNetworkingConfiguration`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingconfiguration"></a>
The networking configuration for the source endpoint, which determines whether it is publicly accessible or in a virtual private cloud (VPC).
*Required*: Yes
*Type*: [StandardSourceEndpointNetworkingConfiguration](aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceNetworkingType`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingtype"></a>
The networking type of the source endpoint. Valid values include the following:
+ `PUBLIC` – The source endpoint is publicly accessible.
+ `VPC` – The source endpoint is in a virtual private cloud (VPC).
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
