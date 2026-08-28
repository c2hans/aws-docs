---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayConnectPeer TransitGatewayAttachmentBgpConfiguration
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration"></a>

The BGP configuration information.

## Syntax
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-syntax.json"></a>

```
{
  "[BgpStatus](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-bgpstatus)" : {{String}},
  "[PeerAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-peeraddress)" : {{String}},
  "[PeerAsn](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-peerasn)" : {{Number}},
  "[TransitGatewayAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-transitgatewayaddress)" : {{String}},
  "[TransitGatewayAsn](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-transitgatewayasn)" : {{Number}}
}
```

### YAML
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-syntax.yaml"></a>

```
  [BgpStatus](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-bgpstatus): {{String}}
  [PeerAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-peeraddress): {{String}}
  [PeerAsn](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-peerasn): {{Number}}
  [TransitGatewayAddress](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-transitgatewayaddress): {{String}}
  [TransitGatewayAsn](#cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-transitgatewayasn): {{Number}}
```

## Properties
<a name="aws-properties-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-properties"></a>

`BgpStatus`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-bgpstatus"></a>
The BGP status.
*Required*: No
*Type*: String
*Allowed values*: `up | down`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAddress`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-peeraddress"></a>
The interior BGP peer IP address for the appliance.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PeerAsn`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-peerasn"></a>
The peer Autonomous System Number (ASN).
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayAddress`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-transitgatewayaddress"></a>
The interior BGP peer IP address for the transit gateway.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayAsn`  <a name="cfn-ec2-transitgatewayconnectpeer-transitgatewayattachmentbgpconfiguration-transitgatewayasn"></a>
The transit gateway Autonomous System Number (ASN).
*Required*: No
*Type*: Number
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
