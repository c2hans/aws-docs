---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput RistRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration"></a>

The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration-syntax.json"></a>

```
{
  "[Port](#cfn-mediaconnect-routerinput-ristrouterinputconfiguration-port)" : {{Integer}},
  "[RecoveryLatencyMilliseconds](#cfn-mediaconnect-routerinput-ristrouterinputconfiguration-recoverylatencymilliseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration-syntax.yaml"></a>

```
  [Port](#cfn-mediaconnect-routerinput-ristrouterinputconfiguration-port): {{Integer}}
  [RecoveryLatencyMilliseconds](#cfn-mediaconnect-routerinput-ristrouterinputconfiguration-recoverylatencymilliseconds): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration-properties"></a>

`Port`  <a name="cfn-mediaconnect-routerinput-ristrouterinputconfiguration-port"></a>
The port number used for the RIST protocol in the router input configuration.
*Required*: Yes
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecoveryLatencyMilliseconds`  <a name="cfn-mediaconnect-routerinput-ristrouterinputconfiguration-recoverylatencymilliseconds"></a>
The recovery latency in milliseconds for the RIST protocol in the router input configuration.
*Required*: Yes
*Type*: Integer
*Minimum*: `10`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
