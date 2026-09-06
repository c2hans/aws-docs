---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest CustomDecodingSignalDecoder
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder"></a>

A list of information about signal decoders.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder-syntax.json"></a>

```
{
  "[CustomDecodingSignal](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-customdecodingsignal)" : {{CustomDecodingSignal}},
  "[FullyQualifiedName](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-fullyqualifiedname)" : {{String}},
  "[InterfaceId](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-interfaceid)" : {{String}},
  "[Type](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder-syntax.yaml"></a>

```
  [CustomDecodingSignal](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-customdecodingsignal): {{
    CustomDecodingSignal}}
  [FullyQualifiedName](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-fullyqualifiedname): {{String}}
  [InterfaceId](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-interfaceid): {{String}}
  [Type](#cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-type): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder-properties"></a>

`CustomDecodingSignal`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-customdecodingsignal"></a>
Information about signals using a custom decoding protocol as defined by the customer.
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).
*Required*: Yes
*Type*: [CustomDecodingSignal](aws-properties-iotfleetwise-decodermanifest-customdecodingsignal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FullyQualifiedName`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-fullyqualifiedname"></a>
The fully qualified name of a signal decoder as defined in a vehicle model.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceId`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-interfaceid"></a>
The ID of a network interface that specifies what network protocol a vehicle follows.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotfleetwise-decodermanifest-customdecodingsignaldecoder-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
*Required*: Yes
*Type*: String
*Allowed values*: `CUSTOM_DECODING_SIGNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
