---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-directconnect-transitvirtualinterface-bgppeer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DirectConnect::TransitVirtualInterface BgpPeer
<a name="aws-properties-directconnect-transitvirtualinterface-bgppeer"></a>

Information about a BGP peer.

## Syntax
<a name="aws-properties-directconnect-transitvirtualinterface-bgppeer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-directconnect-transitvirtualinterface-bgppeer-syntax.json"></a>

```
{
  "[AddressFamily](#cfn-directconnect-transitvirtualinterface-bgppeer-addressfamily)" : {{String}},
  "[AmazonAddress](#cfn-directconnect-transitvirtualinterface-bgppeer-amazonaddress)" : {{String}},
  "[Asn](#cfn-directconnect-transitvirtualinterface-bgppeer-asn)" : {{String}},
  "[AuthKey](#cfn-directconnect-transitvirtualinterface-bgppeer-authkey)" : {{String}},
  "[BgpPeerId](#cfn-directconnect-transitvirtualinterface-bgppeer-bgppeerid)" : {{String}},
  "[CustomerAddress](#cfn-directconnect-transitvirtualinterface-bgppeer-customeraddress)" : {{String}}
}
```

### YAML
<a name="aws-properties-directconnect-transitvirtualinterface-bgppeer-syntax.yaml"></a>

```
  [AddressFamily](#cfn-directconnect-transitvirtualinterface-bgppeer-addressfamily): {{String}}
  [AmazonAddress](#cfn-directconnect-transitvirtualinterface-bgppeer-amazonaddress): {{String}}
  [Asn](#cfn-directconnect-transitvirtualinterface-bgppeer-asn): {{String}}
  [AuthKey](#cfn-directconnect-transitvirtualinterface-bgppeer-authkey): {{String}}
  [BgpPeerId](#cfn-directconnect-transitvirtualinterface-bgppeer-bgppeerid): {{String}}
  [CustomerAddress](#cfn-directconnect-transitvirtualinterface-bgppeer-customeraddress): {{String}}
```

## Properties
<a name="aws-properties-directconnect-transitvirtualinterface-bgppeer-properties"></a>

`AddressFamily`  <a name="cfn-directconnect-transitvirtualinterface-bgppeer-addressfamily"></a>
The address family for the BGP peer.
*Required*: Yes
*Type*: String
*Pattern*: `^(ipv4)|(ipv6)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AmazonAddress`  <a name="cfn-directconnect-transitvirtualinterface-bgppeer-amazonaddress"></a>
The IP address assigned to the Amazon interface.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-fA-F:.]+/[0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Asn`  <a name="cfn-directconnect-transitvirtualinterface-bgppeer-asn"></a>
The autonomous system number (ASN). The valid range is from 1 to 4294967294 for Border Gateway Protocol (BGP) configuration. If you provide a number greater than the maximum, an error is returned.
This is configured as a string to support long ASNs. For more details about long ASN support, see [Long ASN support in Direct Connect ](https://docs.aws.amazon.com/directconnect/latest/UserGuide/long-asn-support.html) in the * Direct Connect User Guide *.
*Required*: Yes
*Type*: String
*Pattern*: `^[1-9][0-9]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthKey`  <a name="cfn-directconnect-transitvirtualinterface-bgppeer-authkey"></a>
The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximun lenth of 80 characters.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9\\!"#$%&'()*+,\-./:;<=>?@\[\]\^_`{|}~]{6,80}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BgpPeerId`  <a name="cfn-directconnect-transitvirtualinterface-bgppeer-bgppeerid"></a>
The ID of the BGP peer.
*Required*: No
*Type*: String
*Pattern*: `^dxpeer-[a-z0-9]{8}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomerAddress`  <a name="cfn-directconnect-transitvirtualinterface-bgppeer-customeraddress"></a>
The IP address assigned to the customer interface.
*Required*: No
*Type*: String
*Pattern*: `^[0-9a-fA-F:.]+/[0-9]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
