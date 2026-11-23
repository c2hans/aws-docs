---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::SourceEndpoint StandardSourceEndpointProtocolConfiguration

The protocol configuration for a standard source endpoint. This is a union type, so exactly one of its members is set, depending on the protocol that the source endpoint uses.

## Syntax
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-syntax.json"></a>

```json
{
  "[Rist](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-rist)" : {{RistStandardSourceEndpointConfiguration}},
  "[Rtp](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-rtp)" : {{RtpStandardSourceEndpointConfiguration}},
  "[SrtCaller](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-srtcaller)" : {{SrtCallerStandardSourceEndpointConfiguration}},
  "[SrtListener](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-srtlistener)" : {{SrtListenerStandardSourceEndpointConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-syntax.yaml"></a>

```yaml
  [Rist](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-rist): {{
    RistStandardSourceEndpointConfiguration}}
  [Rtp](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-rtp): {{
    RtpStandardSourceEndpointConfiguration}}
  [SrtCaller](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-srtcaller): {{
    SrtCallerStandardSourceEndpointConfiguration}}
  [SrtListener](#cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-srtlistener): {{
    SrtListenerStandardSourceEndpointConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-properties"></a>

`Rist`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-rist"></a>
The configuration settings for a source endpoint that uses the RIST protocol.
*Required*: No
*Type*: [RistStandardSourceEndpointConfiguration](aws-properties-mediaconnect-sourceendpoint-riststandardsourceendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rtp`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-rtp"></a>
The configuration settings for a source endpoint that uses the RTP protocol.
*Required*: No
*Type*: [RtpStandardSourceEndpointConfiguration](aws-properties-mediaconnect-sourceendpoint-rtpstandardsourceendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtCaller`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-srtcaller"></a>
The configuration settings for a source endpoint that uses SRT in caller mode.
*Required*: No
*Type*: [SrtCallerStandardSourceEndpointConfiguration](aws-properties-mediaconnect-sourceendpoint-srtcallerstandardsourceendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListener`  <a name="cfn-mediaconnect-sourceendpoint-standardsourceendpointprotocolconfiguration-srtlistener"></a>
The configuration settings for a source endpoint that uses SRT in listener mode.
*Required*: No
*Type*: [SrtListenerStandardSourceEndpointConfiguration](aws-properties-mediaconnect-sourceendpoint-srtlistenerstandardsourceendpointconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
