---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RouterInputProtocolConfiguration
<a name="aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration"></a>

The protocol configuration settings for a router input.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration-syntax.json"></a>

```
{
  "[Rist](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rist)" : {{RistRouterInputConfiguration}},
  "[Rtp](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rtp)" : {{RtpRouterInputConfiguration}},
  "[SrtCaller](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtcaller)" : {{SrtCallerRouterInputConfiguration}},
  "[SrtListener](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtlistener)" : {{SrtListenerRouterInputConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration-syntax.yaml"></a>

```
  [Rist](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rist): {{
    RistRouterInputConfiguration}}
  [Rtp](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rtp): {{
    RtpRouterInputConfiguration}}
  [SrtCaller](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtcaller): {{
    SrtCallerRouterInputConfiguration}}
  [SrtListener](#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtlistener): {{
    SrtListenerRouterInputConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration-properties"></a>

`Rist`  <a name="cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rist"></a>
The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
*Required*: No
*Type*: [RistRouterInputConfiguration](aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rtp`  <a name="cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rtp"></a>
The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
*Required*: No
*Type*: [RtpRouterInputConfiguration](aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtCaller`  <a name="cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtcaller"></a>
The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.
*Required*: No
*Type*: [SrtCallerRouterInputConfiguration](aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListener`  <a name="cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtlistener"></a>
The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.
*Required*: No
*Type*: [SrtListenerRouterInputConfiguration](aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
