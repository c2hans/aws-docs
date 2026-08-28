---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SrtCallerRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration"></a>

The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration-syntax.json"></a>

```
{
  "[DecryptionConfiguration](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-decryptionconfiguration)" : {{SrtDecryptionConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[SourceAddress](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceaddress)" : {{String}},
  "[SourcePort](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceport)" : {{Integer}},
  "[StreamId](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-streamid)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration-syntax.yaml"></a>

```
  [DecryptionConfiguration](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-decryptionconfiguration): {{
    SrtDecryptionConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-minimumlatencymilliseconds): {{Integer}}
  [SourceAddress](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceaddress): {{String}}
  [SourcePort](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceport): {{Integer}}
  [StreamId](#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-streamid): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration-properties"></a>

`DecryptionConfiguration`  <a name="cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-decryptionconfiguration"></a>
Specifies the decryption settings for an SRT caller input, including the encryption key configuration and associated parameters.
*Required*: No
*Type*: [SrtDecryptionConfiguration](aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-minimumlatencymilliseconds"></a>
The minimum latency in milliseconds for the SRT protocol in caller mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceAddress`  <a name="cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceaddress"></a>
The source IP address for the SRT protocol in caller mode.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePort`  <a name="cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceport"></a>
The source port number for the SRT protocol in caller mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamId`  <a name="cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-streamid"></a>
The stream ID for the SRT protocol in caller mode.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
