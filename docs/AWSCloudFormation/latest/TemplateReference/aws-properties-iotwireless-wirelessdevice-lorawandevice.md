---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-wirelessdevice-lorawandevice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::WirelessDevice LoRaWANDevice
<a name="aws-properties-iotwireless-wirelessdevice-lorawandevice"></a>

LoRaWAN object for create functions.

## Syntax
<a name="aws-properties-iotwireless-wirelessdevice-lorawandevice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-wirelessdevice-lorawandevice-syntax.json"></a>

```
{
  "[AbpV10x](#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x)" : {{AbpV10x}},
  "[AbpV11](#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11)" : {{AbpV11}},
  "[DevEui](#cfn-iotwireless-wirelessdevice-lorawandevice-deveui)" : {{String}},
  "[DeviceProfileId](#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid)" : {{String}},
  "[FPorts](#cfn-iotwireless-wirelessdevice-lorawandevice-fports)" : {{FPorts}},
  "[OtaaV10x](#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x)" : {{OtaaV10x}},
  "[OtaaV11](#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11)" : {{OtaaV11}},
  "[ServiceProfileId](#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-wirelessdevice-lorawandevice-syntax.yaml"></a>

```
  [AbpV10x](#cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x): {{
    AbpV10x}}
  [AbpV11](#cfn-iotwireless-wirelessdevice-lorawandevice-abpv11): {{
    AbpV11}}
  [DevEui](#cfn-iotwireless-wirelessdevice-lorawandevice-deveui): {{String}}
  [DeviceProfileId](#cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid): {{String}}
  [FPorts](#cfn-iotwireless-wirelessdevice-lorawandevice-fports): {{
    FPorts}}
  [OtaaV10x](#cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x): {{
    OtaaV10x}}
  [OtaaV11](#cfn-iotwireless-wirelessdevice-lorawandevice-otaav11): {{
    OtaaV11}}
  [ServiceProfileId](#cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-wirelessdevice-lorawandevice-properties"></a>

`AbpV10x`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-abpv10x"></a>
ABP device object for LoRaWAN specification v1.0.x.
*Required*: No
*Type*: [AbpV10x](aws-properties-iotwireless-wirelessdevice-abpv10x.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AbpV11`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-abpv11"></a>
ABP device object for create APIs for v1.1.
*Required*: No
*Type*: [AbpV11](aws-properties-iotwireless-wirelessdevice-abpv11.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DevEui`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-deveui"></a>
The DevEUI value.
*Required*: No
*Type*: String
*Pattern*: `[a-f0-9]{16}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceProfileId`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-deviceprofileid"></a>
The ID of the device profile for the new wireless device.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FPorts`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-fports"></a>
List of FPort assigned for different LoRaWAN application packages to use.
*Required*: No
*Type*: [FPorts](aws-properties-iotwireless-wirelessdevice-fports.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OtaaV10x`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-otaav10x"></a>
OTAA device object for create APIs for v1.0.x
*Required*: No
*Type*: [OtaaV10x](aws-properties-iotwireless-wirelessdevice-otaav10x.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OtaaV11`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-otaav11"></a>
OTAA device object for v1.1 for create APIs.
*Required*: No
*Type*: [OtaaV11](aws-properties-iotwireless-wirelessdevice-otaav11.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceProfileId`  <a name="cfn-iotwireless-wirelessdevice-lorawandevice-serviceprofileid"></a>
The ID of the service profile.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
