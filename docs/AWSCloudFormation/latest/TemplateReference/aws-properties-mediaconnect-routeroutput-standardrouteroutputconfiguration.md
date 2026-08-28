---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::RouterOutput StandardRouterOutputConfiguration
<a name="aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration"></a>

The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.

## Syntax
<a name="aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration-syntax.json"></a>

```
{
  "[NetworkInterfaceArn](#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-networkinterfacearn)" : {{String}},
  "[Protocol](#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocol)" : {{String}},
  "[ProtocolConfiguration](#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocolconfiguration)" : {{RouterOutputProtocolConfiguration}}
}
```

### YAML
<a name="aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration-syntax.yaml"></a>

```
  [NetworkInterfaceArn](#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-networkinterfacearn): {{String}}
  [Protocol](#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocol): {{String}}
  [ProtocolConfiguration](#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocolconfiguration): {{
    RouterOutputProtocolConfiguration}}
```

## Properties
<a name="aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration-properties"></a>

`NetworkInterfaceArn`  <a name="cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-networkinterfacearn"></a>
The Amazon Resource Name (ARN) of the network interface associated with the standard router output.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocol"></a>
The protocol used by the standard router output.
*Required*: No
*Type*: String
*Allowed values*: `RTP | RIST | SRT_CALLER | SRT_LISTENER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolConfiguration`  <a name="cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocolconfiguration"></a>
The configuration settings for the protocol used by the standard router output.
*Required*: Yes
*Type*: [RouterOutputProtocolConfiguration](aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
