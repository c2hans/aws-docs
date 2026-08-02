---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest SignalDecodersItems
<a name="aws-properties-iotfleetwise-decodermanifest-signaldecodersitems"></a>

Information about a signal decoder.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-signaldecodersitems-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-signaldecodersitems-syntax.json"></a>

```
{
  "[CanSignalDecoder](#cfn-iotfleetwise-decodermanifest-signaldecodersitems-cansignaldecoder)" : {{CanSignalDecoder}},
  "[CustomDecodingSignalDecoder](#cfn-iotfleetwise-decodermanifest-signaldecodersitems-customdecodingsignaldecoder)" : {{CustomDecodingSignalDecoder}},
  "[ObdSignalDecoder](#cfn-iotfleetwise-decodermanifest-signaldecodersitems-obdsignaldecoder)" : {{ObdSignalDecoder}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-signaldecodersitems-syntax.yaml"></a>

```
  [CanSignalDecoder](#cfn-iotfleetwise-decodermanifest-signaldecodersitems-cansignaldecoder): {{
    CanSignalDecoder}}
  [CustomDecodingSignalDecoder](#cfn-iotfleetwise-decodermanifest-signaldecodersitems-customdecodingsignaldecoder): {{
    CustomDecodingSignalDecoder}}
  [ObdSignalDecoder](#cfn-iotfleetwise-decodermanifest-signaldecodersitems-obdsignaldecoder): {{
    ObdSignalDecoder}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-signaldecodersitems-properties"></a>

`CanSignalDecoder`  <a name="cfn-iotfleetwise-decodermanifest-signaldecodersitems-cansignaldecoder"></a>
Information about signal decoder using the Controller Area Network (CAN) protocol.
*Required*: No
*Type*: [CanSignalDecoder](aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomDecodingSignalDecoder`  <a name="cfn-iotfleetwise-decodermanifest-signaldecodersitems-customdecodingsignaldecoder"></a>
Information about a [custom signal decoder](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingSignal.html).
*Required*: No
*Type*: [CustomDecodingSignalDecoder](aws-properties-iotfleetwise-decodermanifest-customdecodingsignaldecoder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObdSignalDecoder`  <a name="cfn-iotfleetwise-decodermanifest-signaldecodersitems-obdsignaldecoder"></a>
Information about signal decoder using the on-board diagnostic (OBD) II protocol.
*Required*: No
*Type*: [ObdSignalDecoder](aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
