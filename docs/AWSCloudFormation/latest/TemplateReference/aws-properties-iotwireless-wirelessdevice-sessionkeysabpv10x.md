---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice SessionKeysAbpV10x
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x"></a>

Session keys for ABP v1.0.x.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x-syntax.json"></a>

```
{
  "[AppSKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey)" : {{String}},
  "[NwkSKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x-syntax.yaml"></a>

```
  [AppSKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey): {{String}}
  [NwkSKey](#cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-sessionkeysabpv10x-properties"></a>

`AppSKey`  <a name="cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-appskey"></a>
The AppSKey value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NwkSKey`  <a name="cfn-iotwireless-wirelessdevice-sessionkeysabpv10x-nwkskey"></a>
The NwkKey value.
*Required*: Yes
*Type*: String
*Pattern*: `[a-fA-F0-9]{32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
