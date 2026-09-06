---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest NetworkInterfacesItems
<a name="aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems"></a>

 A list of information about available network interfaces.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems-syntax.json"></a>

```
{
  "[CanNetworkInterface](#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-cannetworkinterface)" : {{CanNetworkInterface}},
  "[CustomDecodingNetworkInterface](#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-customdecodingnetworkinterface)" : {{CustomDecodingNetworkInterface}},
  "[ObdNetworkInterface](#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-obdnetworkinterface)" : {{ObdNetworkInterface}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems-syntax.yaml"></a>

```
  [CanNetworkInterface](#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-cannetworkinterface): {{
    CanNetworkInterface}}
  [CustomDecodingNetworkInterface](#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-customdecodingnetworkinterface): {{
    CustomDecodingNetworkInterface}}
  [ObdNetworkInterface](#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-obdnetworkinterface): {{
    ObdNetworkInterface}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems-properties"></a>

`CanNetworkInterface`  <a name="cfn-iotfleetwise-decodermanifest-networkinterfacesitems-cannetworkinterface"></a>
A single controller area network (CAN) device interface.
*Required*: No
*Type*: [CanNetworkInterface](aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDecodingNetworkInterface`  <a name="cfn-iotfleetwise-decodermanifest-networkinterfacesitems-customdecodingnetworkinterface"></a>
Represents a custom network interface as defined by the customer.
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).
*Required*: No
*Type*: [CustomDecodingNetworkInterface](aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObdNetworkInterface`  <a name="cfn-iotfleetwise-decodermanifest-networkinterfacesitems-obdnetworkinterface"></a>
A network interface that specifies the on-board diagnostic (OBD) II network protocol.
*Required*: No
*Type*: [ObdNetworkInterface](aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
