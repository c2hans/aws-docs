---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iotfleetwise-campaign-datapartitionstorageoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTFleetWise::Campaign DataPartitionStorageOptions
<a name="aws-properties-iotfleetwise-campaign-datapartitionstorageoptions"></a>

Size, time, and location options for the data partition.

## Syntax
<a name="aws-properties-iotfleetwise-campaign-datapartitionstorageoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iotfleetwise-campaign-datapartitionstorageoptions-syntax.json"></a>

```
{
  "[MaximumSize](#cfn-iotfleetwise-campaign-datapartitionstorageoptions-maximumsize)" : {{StorageMaximumSize}},
  "[MinimumTimeToLive](#cfn-iotfleetwise-campaign-datapartitionstorageoptions-minimumtimetolive)" : {{StorageMinimumTimeToLive}},
  "[StorageLocation](#cfn-iotfleetwise-campaign-datapartitionstorageoptions-storagelocation)" : {{String}}
}
```

### YAML
<a name="aws-properties-iotfleetwise-campaign-datapartitionstorageoptions-syntax.yaml"></a>

```
  [MaximumSize](#cfn-iotfleetwise-campaign-datapartitionstorageoptions-maximumsize): {{
    StorageMaximumSize}}
  [MinimumTimeToLive](#cfn-iotfleetwise-campaign-datapartitionstorageoptions-minimumtimetolive): {{
    StorageMinimumTimeToLive}}
  [StorageLocation](#cfn-iotfleetwise-campaign-datapartitionstorageoptions-storagelocation): {{String}}
```

## Properties
<a name="aws-properties-iotfleetwise-campaign-datapartitionstorageoptions-properties"></a>

`MaximumSize`  <a name="cfn-iotfleetwise-campaign-datapartitionstorageoptions-maximumsize"></a>
The maximum storage size of the data stored in the data partition.
Newer data overwrites older data when the partition reaches the maximum size.
*Required*: Yes
*Type*: [StorageMaximumSize](aws-properties-iotfleetwise-campaign-storagemaximumsize.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinimumTimeToLive`  <a name="cfn-iotfleetwise-campaign-datapartitionstorageoptions-minimumtimetolive"></a>
The amount of time that data in this partition will be kept on disk.
+ After the designated amount of time passes, the data can be removed, but it's not guaranteed to be removed.
+ Before the time expires, data in this partition can still be deleted if the partition reaches its configured maximum size.
+ Newer data will overwrite older data when the partition reaches the maximum size.
*Required*: Yes
*Type*: [StorageMinimumTimeToLive](aws-properties-iotfleetwise-campaign-storageminimumtimetolive.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StorageLocation`  <a name="cfn-iotfleetwise-campaign-datapartitionstorageoptions-storagelocation"></a>
The folder name for the data partition under the campaign storage folder.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
