---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-datapartitionuploadoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign DataPartitionUploadOptions
<a name="aws-properties-iotfleetwise-campaign-datapartitionuploadoptions"></a>

The upload options for the data partition. If upload options are specified, you must also specify storage options. See [DataPartitionStorageOptions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DataPartitionStorageOptions.html).

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-datapartitionuploadoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-datapartitionuploadoptions-syntax.json"></a>

```
{
  "[ConditionLanguageVersion](#cfn-iotfleetwise-campaign-datapartitionuploadoptions-conditionlanguageversion)" : {{Integer}},
  "[Expression](#cfn-iotfleetwise-campaign-datapartitionuploadoptions-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-datapartitionuploadoptions-syntax.yaml"></a>

```
  [ConditionLanguageVersion](#cfn-iotfleetwise-campaign-datapartitionuploadoptions-conditionlanguageversion): {{Integer}}
  [Expression](#cfn-iotfleetwise-campaign-datapartitionuploadoptions-expression): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-datapartitionuploadoptions-properties"></a>

`ConditionLanguageVersion`  <a name="cfn-iotfleetwise-campaign-datapartitionuploadoptions-conditionlanguageversion"></a>
The version of the condition language. Defaults to the most recent condition language version.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Expression`  <a name="cfn-iotfleetwise-campaign-datapartitionuploadoptions-expression"></a>
The logical expression used to recognize what data to collect. For example, `$variable.`Vehicle.OutsideAirTemperature` >= 105.0`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
