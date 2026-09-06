---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::NetworkManager::ConnectPeer ConnectPeerBgpConfiguration
<a name="aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration"></a>

Describes a core network BGP configuration.

## Syntax
<a name="aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration-syntax.json"></a>

```
{
  "[CoreNetworkAddress](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkaddress)" : {{String}},
  "[CoreNetworkAsn](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkasn)" : {{Number}},
  "[PeerAddress](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peeraddress)" : {{String}},
  "[PeerAsn](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peerasn)" : {{Number}}
}
```

### YAML
<a name="aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration-syntax.yaml"></a>

```
  [CoreNetworkAddress](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkaddress): {{String}}
  [CoreNetworkAsn](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkasn): {{Number}}
  [PeerAddress](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peeraddress): {{String}}
  [PeerAsn](#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peerasn): {{Number}}
```

## Properties
<a name="aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration-properties"></a>

`CoreNetworkAddress`  <a name="cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkaddress"></a>
The address of a core network.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CoreNetworkAsn`  <a name="cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkasn"></a>
The ASN of the Coret Network.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerAddress`  <a name="cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peeraddress"></a>
The address of a core network Connect peer.
*Required*: No
*Type*: String
*Pattern*: `[\s\S]*`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PeerAsn`  <a name="cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peerasn"></a>
The ASN of the Connect peer.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
