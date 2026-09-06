---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-signalinformation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign SignalInformation
<a name="aws-properties-iotfleetwise-campaign-signalinformation"></a>

Information about a signal.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-signalinformation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-signalinformation-syntax.json"></a>

```
{
  "[DataPartitionId](#cfn-iotfleetwise-campaign-signalinformation-datapartitionid)" : {{String}},
  "[MaxSampleCount](#cfn-iotfleetwise-campaign-signalinformation-maxsamplecount)" : {{Number}},
  "[MinimumSamplingIntervalMs](#cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms)" : {{Number}},
  "[Name](#cfn-iotfleetwise-campaign-signalinformation-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-signalinformation-syntax.yaml"></a>

```
  [DataPartitionId](#cfn-iotfleetwise-campaign-signalinformation-datapartitionid): {{String}}
  [MaxSampleCount](#cfn-iotfleetwise-campaign-signalinformation-maxsamplecount): {{Number}}
  [MinimumSamplingIntervalMs](#cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms): {{Number}}
  [Name](#cfn-iotfleetwise-campaign-signalinformation-name): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-signalinformation-properties"></a>

`DataPartitionId`  <a name="cfn-iotfleetwise-campaign-signalinformation-datapartitionid"></a>
The ID of the data partition this signal is associated with.
The ID must match one of the IDs provided in `dataPartitions`. This is accomplished either by specifying a particular data partition ID or by using `default` for an established default partition. You can establish a default partition in the `DataPartition` data type.
If you upload a signal as a condition for a campaign's data partition, the same signal must be included in `signalsToCollect`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxSampleCount`  <a name="cfn-iotfleetwise-campaign-signalinformation-maxsamplecount"></a>
 The maximum number of samples to collect.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `4294967295`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinimumSamplingIntervalMs`  <a name="cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms"></a>
 The minimum duration of time (in milliseconds) between two triggering events to collect data.
If a signal changes often, you might want to collect data at a slower rate.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `4294967295`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-iotfleetwise-campaign-signalinformation-name"></a>
The name of the signal.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w|*|-]+(\.[\w|*|-]+)*$`
*Minimum*: `1`
*Maximum*: `150`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
