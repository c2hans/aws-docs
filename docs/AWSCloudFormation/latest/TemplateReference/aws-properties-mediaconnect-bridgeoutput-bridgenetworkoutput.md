---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::BridgeOutput BridgeNetworkOutput
<a name="aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput"></a>

 The output of the bridge. A network output is delivered to your premises.

## Syntax
<a name="aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput-syntax.json"></a>

```
{
  "[IpAddress](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ipaddress)" : {{String}},
  "[NetworkName](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-networkname)" : {{String}},
  "[Port](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-port)" : {{Integer}},
  "[Protocol](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-protocol)" : {{String}},
  "[Ttl](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ttl)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput-syntax.yaml"></a>

```
  [IpAddress](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ipaddress): {{String}}
  [NetworkName](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-networkname): {{String}}
  [Port](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-port): {{Integer}}
  [Protocol](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-protocol): {{String}}
  [Ttl](#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ttl): {{Integer}}
```

## Properties
<a name="aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput-properties"></a>

`IpAddress`  <a name="cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ipaddress"></a>
 The network output IP address.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkName`  <a name="cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-networkname"></a>
 The network output's gateway network name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-port"></a>
 The network output's port.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-protocol"></a>
 The network output protocol.
AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
*Required*: Yes
*Type*: String
*Allowed values*: `rtp-fec | rtp | udp`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ttl`  <a name="cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ttl"></a>
 The network output TTL.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
