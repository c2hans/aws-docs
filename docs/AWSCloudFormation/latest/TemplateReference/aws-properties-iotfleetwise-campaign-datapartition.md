---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-datapartition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign DataPartition
<a name="aws-properties-iotfleetwise-campaign-datapartition"></a>

The configuration for signal data storage and upload options. You can only specify these options when the campaign's spooling mode is `TO_DISK`.

**Important**
AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Syntax
<a name="aws-properties-iotfleetwise-campaign-datapartition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-datapartition-syntax.json"></a>

```
{
  "[Id](#cfn-iotfleetwise-campaign-datapartition-id)" : {{String}},
  "[StorageOptions](#cfn-iotfleetwise-campaign-datapartition-storageoptions)" : {{DataPartitionStorageOptions}},
  "[UploadOptions](#cfn-iotfleetwise-campaign-datapartition-uploadoptions)" : {{DataPartitionUploadOptions}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-datapartition-syntax.yaml"></a>

```
  [Id](#cfn-iotfleetwise-campaign-datapartition-id): {{String}}
  [StorageOptions](#cfn-iotfleetwise-campaign-datapartition-storageoptions): {{
    DataPartitionStorageOptions}}
  [UploadOptions](#cfn-iotfleetwise-campaign-datapartition-uploadoptions): {{
    DataPartitionUploadOptions}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-datapartition-properties"></a>

`Id`  <a name="cfn-iotfleetwise-campaign-datapartition-id"></a>
The ID of the data partition. The data partition ID must be unique within a campaign. You can establish a data partition as the default partition for a campaign by using `default` as the ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageOptions`  <a name="cfn-iotfleetwise-campaign-datapartition-storageoptions"></a>
The storage options for a data partition.
*Required*: Yes
*Type*: [DataPartitionStorageOptions](aws-properties-iotfleetwise-campaign-datapartitionstorageoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UploadOptions`  <a name="cfn-iotfleetwise-campaign-datapartition-uploadoptions"></a>
The upload options for the data partition.
*Required*: No
*Type*: [DataPartitionUploadOptions](aws-properties-iotfleetwise-campaign-datapartitionuploadoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
