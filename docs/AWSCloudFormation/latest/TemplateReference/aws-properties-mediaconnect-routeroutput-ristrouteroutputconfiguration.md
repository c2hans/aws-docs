---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput RistRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration"></a>

The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration-syntax.json"></a>

```
{
  "[DestinationAddress](#cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationaddress)" : {{String}},
  "[DestinationPort](#cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration-syntax.yaml"></a>

```
  [DestinationAddress](#cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationaddress): {{String}}
  [DestinationPort](#cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationport): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration-properties"></a>

`DestinationAddress`  <a name="cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationaddress"></a>
The destination IP address for the RIST protocol in the router output configuration.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DestinationPort`  <a name="cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationport"></a>
The destination port number for the RIST protocol in the router output configuration.
*Required*: Yes
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
