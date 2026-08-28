---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput SrtListenerRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration"></a>

The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-syntax.json"></a>

```
{
  "[DecryptionConfiguration](#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-decryptionconfiguration)" : {{SrtDecryptionConfiguration}},
  "[MinimumLatencyMilliseconds](#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-minimumlatencymilliseconds)" : {{Integer}},
  "[Port](#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-syntax.yaml"></a>

```
  [DecryptionConfiguration](#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-decryptionconfiguration): {{
    SrtDecryptionConfiguration}}
  [MinimumLatencyMilliseconds](#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-minimumlatencymilliseconds): {{Integer}}
  [Port](#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-port): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-properties"></a>

`DecryptionConfiguration`  <a name="cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-decryptionconfiguration"></a>
Specifies the decryption settings for an SRT listener input, including the encryption key configuration and associated parameters.
*Required*: No
*Type*: [SrtDecryptionConfiguration](aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumLatencyMilliseconds`  <a name="cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-minimumlatencymilliseconds"></a>
The minimum latency in milliseconds for the SRT protocol in listener mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-port"></a>
The port number for the SRT protocol in listener mode.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
