---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RtpRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration"></a>

The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration-syntax.json"></a>

```
{
  "[ForwardErrorCorrection](#cfn-mediaconnect-routerinput-rtprouterinputconfiguration-forwarderrorcorrection)" : {{String}},
  "[Port](#cfn-mediaconnect-routerinput-rtprouterinputconfiguration-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration-syntax.yaml"></a>

```
  [ForwardErrorCorrection](#cfn-mediaconnect-routerinput-rtprouterinputconfiguration-forwarderrorcorrection): {{String}}
  [Port](#cfn-mediaconnect-routerinput-rtprouterinputconfiguration-port): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration-properties"></a>

`ForwardErrorCorrection`  <a name="cfn-mediaconnect-routerinput-rtprouterinputconfiguration-forwarderrorcorrection"></a>
The state of forward error correction for the RTP protocol in the router input configuration.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-routerinput-rtprouterinputconfiguration-port"></a>
The port number used for the RTP protocol in the router input configuration.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
