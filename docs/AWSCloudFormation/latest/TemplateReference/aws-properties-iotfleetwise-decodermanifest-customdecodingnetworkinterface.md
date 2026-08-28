---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest CustomDecodingNetworkInterface
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface"></a>

Represents a custom network interface as defined by the customer.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface-syntax.json"></a>

```
{
  "[CustomDecodingInterface](#cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-customdecodinginterface)" : {{CustomDecodingInterface}},
  "[InterfaceId](#cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-interfaceid)" : {{String}},
  "[Type](#cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface-syntax.yaml"></a>

```
  [CustomDecodingInterface](#cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-customdecodinginterface): {{
    CustomDecodingInterface}}
  [InterfaceId](#cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-interfaceid): {{String}}
  [Type](#cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-type): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingnetworkinterface-properties"></a>

`CustomDecodingInterface`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-customdecodinginterface"></a>
Represents a custom network interface as defined by the customer.
*Required*: Yes
*Type*: [CustomDecodingInterface](aws-properties-iotfleetwise-decodermanifest-customdecodinginterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceId`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-interfaceid"></a>
The ID of a network interface that specifies what network protocol a vehicle follows.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingnetworkinterface-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOM_DECODING_INTERFACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
