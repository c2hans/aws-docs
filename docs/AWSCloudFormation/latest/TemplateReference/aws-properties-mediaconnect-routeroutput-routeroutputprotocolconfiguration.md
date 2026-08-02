---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput RouterOutputProtocolConfiguration
<a name="aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration"></a>

The protocol configuration settings for a router output.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration-syntax.json"></a>

```
{
  "[Rist](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rist)" : {{RistRouterOutputConfiguration}},
  "[Rtp](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rtp)" : {{RtpRouterOutputConfiguration}},
  "[SrtCaller](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtcaller)" : {{SrtCallerRouterOutputConfiguration}},
  "[SrtListener](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtlistener)" : {{SrtListenerRouterOutputConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration-syntax.yaml"></a>

```
  [Rist](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rist): {{
    RistRouterOutputConfiguration}}
  [Rtp](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rtp): {{
    RtpRouterOutputConfiguration}}
  [SrtCaller](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtcaller): {{
    SrtCallerRouterOutputConfiguration}}
  [SrtListener](#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtlistener): {{
    SrtListenerRouterOutputConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration-properties"></a>

`Rist`  <a name="cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rist"></a>
The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.
*Required*: No
*Type*: [RistRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rtp`  <a name="cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rtp"></a>
The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.
*Required*: No
*Type*: [RtpRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtCaller`  <a name="cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtcaller"></a>
The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in caller mode, including the destination address and port, minimum latency, stream ID, and encryption key configuration.
*Required*: No
*Type*: [SrtCallerRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListener`  <a name="cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtlistener"></a>
The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and encryption key configuration.
*Required*: No
*Type*: [SrtListenerRouterOutputConfiguration](aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
