---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice Application
<a name="aws-properties-iotwireless-wirelessdevice-application"></a>

A list of optional LoRaWAN application information, which can be used for geolocation.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-application-syntax.json"></a>

```
{
  "[DestinationName](#cfn-iotwireless-wirelessdevice-application-destinationname)" : {{String}},
  "[FPort](#cfn-iotwireless-wirelessdevice-application-fport)" : {{Integer}},
  "[Type](#cfn-iotwireless-wirelessdevice-application-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-application-syntax.yaml"></a>

```
  [DestinationName](#cfn-iotwireless-wirelessdevice-application-destinationname): {{String}}
  [FPort](#cfn-iotwireless-wirelessdevice-application-fport): {{Integer}}
  [Type](#cfn-iotwireless-wirelessdevice-application-type): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-application-properties"></a>

`DestinationName`  <a name="cfn-iotwireless-wirelessdevice-application-destinationname"></a>
The name of the position data destination that describes the IoT rule that processes the device's position data.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9-_]+`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FPort`  <a name="cfn-iotwireless-wirelessdevice-application-fport"></a>
The name of the new destination for the device.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `223`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotwireless-wirelessdevice-application-type"></a>
Application type, which can be specified to obtain real-time position information of your LoRaWAN device.
*Required*: No
*Type*: String
*Allowed values*: `SemtechGeolocation | SemtechGNSS | SemtechGNSSNG | SemtechWiFi`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
