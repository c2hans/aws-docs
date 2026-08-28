---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput RtpRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration"></a>

The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration-syntax.json"></a>

```
{
  "[DestinationAddress](#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationaddress)" : {{String}},
  "[DestinationPort](#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationport)" : {{Integer}},
  "[ForwardErrorCorrection](#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-forwarderrorcorrection)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration-syntax.yaml"></a>

```
  [DestinationAddress](#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationaddress): {{String}}
  [DestinationPort](#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationport): {{Integer}}
  [ForwardErrorCorrection](#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-forwarderrorcorrection): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration-properties"></a>

`DestinationAddress`  <a name="cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationaddress"></a>
The destination IP address for the RTP protocol in the router output configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPort`  <a name="cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationport"></a>
The destination port number for the RTP protocol in the router output configuration.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65531`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForwardErrorCorrection`  <a name="cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-forwarderrorcorrection"></a>
The state of forward error correction for the RTP protocol in the router output configuration.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
