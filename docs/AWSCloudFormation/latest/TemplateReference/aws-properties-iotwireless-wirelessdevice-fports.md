---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-fports.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice FPorts
<a name="aws-properties-iotwireless-wirelessdevice-fports"></a>

List of FPorts assigned for different LoRaWAN application packages to use.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-fports-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-fports-syntax.json"></a>

```
{
  "[Applications](#cfn-iotwireless-wirelessdevice-fports-applications)" : {{[ Application, ... ]}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-fports-syntax.yaml"></a>

```
  [Applications](#cfn-iotwireless-wirelessdevice-fports-applications): {{
    - Application}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-fports-properties"></a>

`Applications`  <a name="cfn-iotwireless-wirelessdevice-fports-applications"></a>
LoRaWAN application configuration, which can be used to perform geolocation.
*Required*: No
*Type*: Array of [Application](aws-properties-iotwireless-wirelessdevice-application.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
