---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterInput StandardRouterInputConfiguration
<a name="aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration"></a>

The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.

## Syntax
<a name="aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration-syntax.json"></a>

```
{
  "[NetworkInterfaceArn](#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-networkinterfacearn)" : {{String}},
  "[Protocol](#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocol)" : {{String}},
  "[ProtocolConfiguration](#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocolconfiguration)" : {{RouterInputProtocolConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration-syntax.yaml"></a>

```
  [NetworkInterfaceArn](#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-networkinterfacearn): {{String}}
  [Protocol](#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocol): {{String}}
  [ProtocolConfiguration](#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocolconfiguration): {{
    RouterInputProtocolConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration-properties"></a>

`NetworkInterfaceArn`  <a name="cfn-mediaconnect-routerinput-standardrouterinputconfiguration-networkinterfacearn"></a>
The Amazon Resource Name (ARN) of the network interface associated with the standard router input.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocol"></a>
The protocol used by the standard router input.
*Required*: No
*Type*: String
*Allowed values*: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocolconfiguration"></a>
The configuration settings for the protocol used by the standard router input.
*Required*: Yes
*Type*: [RouterInputProtocolConfiguration](aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
