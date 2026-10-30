---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint StandardSourceEndpointConfiguration
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration"></a>

<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-description"></a>The `StandardSourceEndpointConfiguration` property type specifies Property description not available. for an [AWS::MediaConnect::SourceEndpoint](aws-resource-mediaconnect-sourceendpoint.md).

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-syntax.json"></a>

```
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

```
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
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]([a-zA-Z0-9\-_]*[a-zA-Z0-9])?$`
*Minimum*: `1`
*Maximum*: `164`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocol"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-protocolconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [StandardSourceEndpointProtocolConfiguration](aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceNetworkingConfiguration`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [StandardSourceEndpointNetworkingConfiguration](aws-properties-mediaconnect-sourceendpoint-standardsourceendpointnetworkingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceNetworkingType`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointconfiguration-sourcenetworkingtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | VPC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
