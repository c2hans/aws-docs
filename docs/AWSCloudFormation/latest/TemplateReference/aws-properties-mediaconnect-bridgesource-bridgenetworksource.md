---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::BridgeSource BridgeNetworkSource
<a name="aws-properties-mediaconnect-bridgesource-bridgenetworksource"></a>

 The source of the bridge. A network source originates at your premises.

## Syntax
<a name="aws-properties-mediaconnect-bridgesource-bridgenetworksource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-bridgesource-bridgenetworksource-syntax.json"></a>

```
{
  "[MulticastIp](#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastip)" : {{String}},
  "[MulticastSourceSettings](#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastsourcesettings)" : {{MulticastSourceSettings}},
  "[NetworkName](#cfn-mediaconnect-bridgesource-bridgenetworksource-networkname)" : {{String}},
  "[Port](#cfn-mediaconnect-bridgesource-bridgenetworksource-port)" : {{Integer}},
  "[Protocol](#cfn-mediaconnect-bridgesource-bridgenetworksource-protocol)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-bridgesource-bridgenetworksource-syntax.yaml"></a>

```
  [MulticastIp](#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastip): {{String}}
  [MulticastSourceSettings](#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastsourcesettings): {{
    MulticastSourceSettings}}
  [NetworkName](#cfn-mediaconnect-bridgesource-bridgenetworksource-networkname): {{String}}
  [Port](#cfn-mediaconnect-bridgesource-bridgenetworksource-port): {{Integer}}
  [Protocol](#cfn-mediaconnect-bridgesource-bridgenetworksource-protocol): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-bridgesource-bridgenetworksource-properties"></a>

`MulticastIp`  <a name="cfn-mediaconnect-bridgesource-bridgenetworksource-multicastip"></a>
 The network source multicast IP.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MulticastSourceSettings`  <a name="cfn-mediaconnect-bridgesource-bridgenetworksource-multicastsourcesettings"></a>
The settings related to the multicast source.
*Required*: No
*Type*: [MulticastSourceSettings](aws-properties-mediaconnect-bridgesource-multicastsourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkName`  <a name="cfn-mediaconnect-bridgesource-bridgenetworksource-networkname"></a>
 The network source's gateway network name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-mediaconnect-bridgesource-bridgenetworksource-port"></a>
 The network source port.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-mediaconnect-bridgesource-bridgenetworksource-protocol"></a>
 The network source protocol.
AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
*Required*: Yes
*Type*: String
*Allowed values*: `rtp-fec | rtp | udp`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
