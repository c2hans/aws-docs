---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-diskiopsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem DiskIopsConfiguration
<a name="aws-properties-fsx-filesystem-diskiopsconfiguration"></a>

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

## Syntax
<a name="aws-properties-fsx-filesystem-diskiopsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-diskiopsconfiguration-syntax.json"></a>

```
{
  "[Iops](#cfn-fsx-filesystem-diskiopsconfiguration-iops)" : {{Integer}},
  "[Mode](#cfn-fsx-filesystem-diskiopsconfiguration-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-diskiopsconfiguration-syntax.yaml"></a>

```
  [Iops](#cfn-fsx-filesystem-diskiopsconfiguration-iops): {{Integer}}
  [Mode](#cfn-fsx-filesystem-diskiopsconfiguration-mode): {{String}}
```

## Properties
<a name="aws-properties-fsx-filesystem-diskiopsconfiguration-properties"></a>

`Iops`  <a name="cfn-fsx-filesystem-diskiopsconfiguration-iops"></a>
The total number of SSD IOPS provisioned for the file system.
The minimum and maximum values for this property depend on the value of `HAPairs` and `StorageCapacity`. The minimum value is calculated as `StorageCapacity` \* 3 \* `HAPairs` (3 IOPS per GB of `StorageCapacity`). The maximum value is calculated as 200,000 \* `HAPairs`.
Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `Iops` is outside of the minimum or maximum values.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-fsx-filesystem-diskiopsconfiguration-mode"></a>
Specifies whether the file system is using the `AUTOMATIC` setting of SSD IOPS of 3 IOPS per GB of storage capacity, or if it using a `USER_PROVISIONED` value.
*Required*: No
*Type*: String
*Allowed values*: `AUTOMATIC | USER_PROVISIONED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
