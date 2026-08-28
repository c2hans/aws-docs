---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayConnectPeer TransitGatewayConnectPeerConfiguration
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration"></a>

Describes the Connect peer details.

## Syntax
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-syntax.json"></a>

```
{
  "[BgpConfigurations](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-bgpconfigurations)" : {{[ TransitGatewayAttachmentBgpConfiguration, ... ]}},
  "[InsideCidrBlocks](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-insidecidrblocks)" : {{[ String, ... ]}},
  "[PeerAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-peeraddress)" : {{String}},
  "[Protocol](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-protocol)" : {{String}},
  "[TransitGatewayAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-transitgatewayaddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-syntax.yaml"></a>

```
  [BgpConfigurations](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-bgpconfigurations): {{
    - TransitGatewayAttachmentBgpConfiguration}}
  [InsideCidrBlocks](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-insidecidrblocks): {{
    - String}}
  [PeerAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-peeraddress): {{String}}
  [Protocol](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-protocol): {{String}}
  [TransitGatewayAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-transitgatewayaddress): {{String}}
```

## Properties
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-properties"></a>

`BgpConfigurations`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-bgpconfigurations"></a>
The BGP configuration details.
*Required*: No
*Type*: Array of [TransitGatewayAttachmentBgpConfiguration](aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InsideCidrBlocks`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-insidecidrblocks"></a>
The range of interior BGP peer IP addresses.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAddress`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-peeraddress"></a>
The Connect peer IP address on the appliance side of the tunnel.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Protocol`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-protocol"></a>
The tunnel protocol.
*Required*: No
*Type*: String
*Allowed values*: `gre`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayAddress`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayconnectpeerconfiguration-transitgatewayaddress"></a>
The Connect peer IP address on the transit gateway side of the tunnel.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
