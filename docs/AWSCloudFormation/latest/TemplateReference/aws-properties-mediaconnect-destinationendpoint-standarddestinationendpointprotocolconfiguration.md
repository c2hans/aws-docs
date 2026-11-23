---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::DestinationEndpoint StandardDestinationEndpointProtocolConfiguration

The protocol configuration for a standard destination endpoint. This is a union type, so exactly one of its members is set, depending on the protocol that the destination endpoint uses.

## Syntax
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-syntax.json"></a>

```json
{
  "[Rist](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-rist)" : {{RistStandardDestinationEndpointConfiguration}},
  "[Rtp](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-rtp)" : {{RtpStandardDestinationEndpointConfiguration}},
  "[SrtCaller](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-srtcaller)" : {{SrtCallerStandardDestinationEndpointConfiguration}},
  "[SrtListener](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-srtlistener)" : {{SrtListenerStandardDestinationEndpointConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-syntax.yaml"></a>

```yaml
  [Rist](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-rist): {{
    RistStandardDestinationEndpointConfiguration}}
  [Rtp](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-rtp): {{
    RtpStandardDestinationEndpointConfiguration}}
  [SrtCaller](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-srtcaller): {{
    SrtCallerStandardDestinationEndpointConfiguration}}
  [SrtListener](#cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-srtlistener): {{
    SrtListenerStandardDestinationEndpointConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-properties"></a>

`Rist`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-rist"></a>
The configuration settings for a destination endpoint that uses the RIST protocol.
*Required*: No
*Type*: [RistStandardDestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-riststandarddestinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rtp`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-rtp"></a>
The configuration settings for a destination endpoint that uses the RTP protocol.
*Required*: No
*Type*: [RtpStandardDestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-rtpstandarddestinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtCaller`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-srtcaller"></a>
The configuration settings for a destination endpoint that uses SRT in caller mode.
*Required*: No
*Type*: [SrtCallerStandardDestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-srtcallerstandarddestinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListener`  <a name="cfn-mediaconnect-destinationendpoint-standarddestinationendpointprotocolconfiguration-srtlistener"></a>
The configuration settings for a destination endpoint that uses SRT in listener mode.
*Required*: No
*Type*: [SrtListenerStandardDestinationEndpointConfiguration](aws-properties-mediaconnect-destinationendpoint-srtlistenerstandarddestinationendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
