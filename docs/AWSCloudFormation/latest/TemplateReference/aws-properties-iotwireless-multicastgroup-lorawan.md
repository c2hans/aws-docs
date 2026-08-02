---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotwireless-multicastgroup-lorawan.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTWireless::MulticastGroup LoRaWAN
<a name="aws-properties-iotwireless-multicastgroup-lorawan"></a>

The LoRaWAN information that is to be used with the multicast group.

## Syntax
<a name="aws-properties-iotwireless-multicastgroup-lorawan-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotwireless-multicastgroup-lorawan-syntax.json"></a>

```
{
  "[DlClass](#cfn-iotwireless-multicastgroup-lorawan-dlclass)" : {{String}},
  "[NumberOfDevicesInGroup](#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup)" : {{Integer}},
  "[NumberOfDevicesRequested](#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested)" : {{Integer}},
  "[RfRegion](#cfn-iotwireless-multicastgroup-lorawan-rfregion)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotwireless-multicastgroup-lorawan-syntax.yaml"></a>

```
  [DlClass](#cfn-iotwireless-multicastgroup-lorawan-dlclass): {{String}}
  [NumberOfDevicesInGroup](#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup): {{Integer}}
  [NumberOfDevicesRequested](#cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested): {{Integer}}
  [RfRegion](#cfn-iotwireless-multicastgroup-lorawan-rfregion): {{String}}
```

## Properties
<a name="aws-properties-iotwireless-multicastgroup-lorawan-properties"></a>

`DlClass`  <a name="cfn-iotwireless-multicastgroup-lorawan-dlclass"></a>
DlClass for LoRaWAN. Valid values are ClassB and ClassC.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfDevicesInGroup`  <a name="cfn-iotwireless-multicastgroup-lorawan-numberofdevicesingroup"></a>
Number of devices that are associated to the multicast group.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberOfDevicesRequested`  <a name="cfn-iotwireless-multicastgroup-lorawan-numberofdevicesrequested"></a>
Number of devices that are requested to be associated with the multicast group.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RfRegion`  <a name="cfn-iotwireless-multicastgroup-lorawan-rfregion"></a>
The frequency band (RFRegion) value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
