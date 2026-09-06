---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest ObdNetworkInterface
<a name="aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface"></a>

Information about a network interface specified by the On-board diagnostic (OBD) II protocol.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface-syntax.json"></a>

```
{
  "[InterfaceId](#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-interfaceid)" : {{String}},
  "[ObdInterface](#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-obdinterface)" : {{ObdInterface}},
  "[Type](#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface-syntax.yaml"></a>

```
  [InterfaceId](#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-interfaceid): {{String}}
  [ObdInterface](#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-obdinterface): {{
    ObdInterface}}
  [Type](#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-type): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface-properties"></a>

`InterfaceId`  <a name="cfn-iotfleetwise-decodermanifest-obdnetworkinterface-interfaceid"></a>
The ID of the network interface.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObdInterface`  <a name="cfn-iotfleetwise-decodermanifest-obdnetworkinterface-obdinterface"></a>
 Information about a network interface specified by the On-board diagnostic (OBD) II protocol.
*Required*: Yes
*Type*: [ObdInterface](aws-properties-iotfleetwise-decodermanifest-obdinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotfleetwise-decodermanifest-obdnetworkinterface-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
*Required*: Yes
*Type*: String
*Allowed values*: `OBD_INTERFACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
