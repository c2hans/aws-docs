---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest CanSignalDecoder
<a name="aws-properties-iotfleetwise-decodermanifest-cansignaldecoder"></a>

Information about signal decoder using the Controller Area Network (CAN) protocol.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-cansignaldecoder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-cansignaldecoder-syntax.json"></a>

```
{
  "[CanSignal](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-cansignal)" : {{CanSignal}},
  "[FullyQualifiedName](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-fullyqualifiedname)" : {{String}},
  "[InterfaceId](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-interfaceid)" : {{String}},
  "[Type](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-cansignaldecoder-syntax.yaml"></a>

```
  [CanSignal](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-cansignal): {{
    CanSignal}}
  [FullyQualifiedName](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-fullyqualifiedname): {{String}}
  [InterfaceId](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-interfaceid): {{String}}
  [Type](#cfn-iotfleetwise-decodermanifest-cansignaldecoder-type): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-cansignaldecoder-properties"></a>

`CanSignal`  <a name="cfn-iotfleetwise-decodermanifest-cansignaldecoder-cansignal"></a>
Information about a single controller area network (CAN) signal and the messages it receives and transmits.
*Required*: Yes
*Type*: [CanSignal](aws-properties-iotfleetwise-decodermanifest-cansignal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FullyQualifiedName`  <a name="cfn-iotfleetwise-decodermanifest-cansignaldecoder-fullyqualifiedname"></a>
The fully qualified name of a signal decoder as defined in a vehicle model.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceId`  <a name="cfn-iotfleetwise-decodermanifest-cansignaldecoder-interfaceid"></a>
The ID of a network interface that specifies what network protocol a vehicle follows.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotfleetwise-decodermanifest-cansignaldecoder-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
*Required*: Yes
*Type*: String
*Allowed values*: `CAN_SIGNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
