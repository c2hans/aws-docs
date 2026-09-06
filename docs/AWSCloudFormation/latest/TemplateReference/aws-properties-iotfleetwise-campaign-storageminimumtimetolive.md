---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-storageminimumtimetolive.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign StorageMinimumTimeToLive
<a name="aws-properties-iotfleetwise-campaign-storageminimumtimetolive"></a>

Information about the minimum amount of time that data will be kept.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-storageminimumtimetolive-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-storageminimumtimetolive-syntax.json"></a>

```
{
  "[Unit](#cfn-iotfleetwise-campaign-storageminimumtimetolive-unit)" : {{String}},
  "[Value](#cfn-iotfleetwise-campaign-storageminimumtimetolive-value)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-storageminimumtimetolive-syntax.yaml"></a>

```
  [Unit](#cfn-iotfleetwise-campaign-storageminimumtimetolive-unit): {{String}}
  [Value](#cfn-iotfleetwise-campaign-storageminimumtimetolive-value): {{Integer}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-storageminimumtimetolive-properties"></a>

`Unit`  <a name="cfn-iotfleetwise-campaign-storageminimumtimetolive-unit"></a>
The time increment type.
*Required*: Yes
*Type*: String
*Allowed values*: `HOURS | DAYS | WEEKS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-iotfleetwise-campaign-storageminimumtimetolive-value"></a>
The minimum amount of time to store the data.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
