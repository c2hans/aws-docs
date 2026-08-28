---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest CanNetworkInterface
<a name="aws-properties-iotfleetwise-decodermanifest-cannetworkinterface"></a>

Represents a node and its specifications in an in-vehicle communication network. All signal decoders must be associated with a network node.

 To return this information about all the network interfaces specified in a decoder manifest, use the [ListDecoderManifestNetworkInterfaces](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestNetworkInterfaces.html) in the *AWS IoT FleetWise API Reference*.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-cannetworkinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-cannetworkinterface-syntax.json"></a>

```
{
  "[CanInterface](#cfn-iotfleetwise-decodermanifest-cannetworkinterface-caninterface)" : {{CanInterface}},
  "[InterfaceId](#cfn-iotfleetwise-decodermanifest-cannetworkinterface-interfaceid)" : {{String}},
  "[Type](#cfn-iotfleetwise-decodermanifest-cannetworkinterface-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-cannetworkinterface-syntax.yaml"></a>

```
  [CanInterface](#cfn-iotfleetwise-decodermanifest-cannetworkinterface-caninterface): {{
    CanInterface}}
  [InterfaceId](#cfn-iotfleetwise-decodermanifest-cannetworkinterface-interfaceid): {{String}}
  [Type](#cfn-iotfleetwise-decodermanifest-cannetworkinterface-type): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-cannetworkinterface-properties"></a>

`CanInterface`  <a name="cfn-iotfleetwise-decodermanifest-cannetworkinterface-caninterface"></a>
Information about a network interface specified by the Controller Area Network (CAN) protocol.
*Required*: Yes
*Type*: [CanInterface](aws-properties-iotfleetwise-decodermanifest-caninterface.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceId`  <a name="cfn-iotfleetwise-decodermanifest-cannetworkinterface-interfaceid"></a>
The ID of the network interface.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotfleetwise-decodermanifest-cannetworkinterface-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
*Required*: Yes
*Type*: String
*Allowed values*: `CAN_INTERFACE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
