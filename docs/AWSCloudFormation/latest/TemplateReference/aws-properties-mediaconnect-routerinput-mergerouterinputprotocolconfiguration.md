---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput MergeRouterInputProtocolConfiguration
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration"></a>

Protocol configuration settings for merge router inputs.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-syntax.json"></a>

```
{
  "[Rist](#cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rist)" : {{RistRouterInputConfiguration}},
  "[Rtp](#cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rtp)" : {{RtpRouterInputConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-syntax.yaml"></a>

```
  [Rist](#cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rist): {{
    RistRouterInputConfiguration}}
  [Rtp](#cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rtp): {{
    RtpRouterInputConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-properties"></a>

`Rist`  <a name="cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rist"></a>
The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
*Required*: No
*Type*: [RistRouterInputConfiguration](aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rtp`  <a name="cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rtp"></a>
The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
*Required*: No
*Type*: [RtpRouterInputConfiguration](aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
