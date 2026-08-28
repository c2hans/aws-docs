---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::DecoderManifest ObdSignalDecoder
<a name="aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder"></a>

A list of information about signal decoders.

## Syntax
<a name="aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder-syntax.json"></a>

```
{
  "[FullyQualifiedName](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-fullyqualifiedname)" : {{String}},
  "[InterfaceId](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-interfaceid)" : {{String}},
  "[ObdSignal](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-obdsignal)" : {{ObdSignal}},
  "[Type](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder-syntax.yaml"></a>

```
  [FullyQualifiedName](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-fullyqualifiedname): {{String}}
  [InterfaceId](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-interfaceid): {{String}}
  [ObdSignal](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-obdsignal): {{
    ObdSignal}}
  [Type](#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-type): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder-properties"></a>

`FullyQualifiedName`  <a name="cfn-iotfleetwise-decodermanifest-obdsignaldecoder-fullyqualifiedname"></a>
The fully qualified name of a signal decoder as defined in a vehicle model.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InterfaceId`  <a name="cfn-iotfleetwise-decodermanifest-obdsignaldecoder-interfaceid"></a>
The ID of a network interface that specifies what network protocol a vehicle follows.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObdSignal`  <a name="cfn-iotfleetwise-decodermanifest-obdsignaldecoder-obdsignal"></a>
Information about signal messages using the on-board diagnostics (OBD) II protocol in a vehicle.
*Required*: Yes
*Type*: [ObdSignal](aws-properties-iotfleetwise-decodermanifest-obdsignal.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-iotfleetwise-decodermanifest-obdsignaldecoder-type"></a>
The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.
*Required*: Yes
*Type*: String
*Allowed values*: `OBD_SIGNAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
