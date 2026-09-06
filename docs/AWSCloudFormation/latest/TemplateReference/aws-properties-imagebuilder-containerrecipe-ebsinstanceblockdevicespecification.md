---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ContainerRecipe EbsInstanceBlockDeviceSpecification
<a name="aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification"></a>

Amazon EBS-specific block device mapping specifications.

## Syntax
<a name="aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-syntax.json"></a>

```
{
  "[DeleteOnTermination](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination)" : {{Boolean}},
  "[Encrypted](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted)" : {{Boolean}},
  "[Iops](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops)" : {{Integer}},
  "[KmsKeyId](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid)" : {{String}},
  "[SnapshotId](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid)" : {{String}},
  "[Throughput](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-throughput)" : {{Integer}},
  "[VolumeSize](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize)" : {{Integer}},
  "[VolumeType](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-syntax.yaml"></a>

```
  [DeleteOnTermination](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination): {{Boolean}}
  [Encrypted](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted): {{Boolean}}
  [Iops](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops): {{Integer}}
  [KmsKeyId](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid): {{String}}
  [SnapshotId](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid): {{String}}
  [Throughput](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-throughput): {{Integer}}
  [VolumeSize](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize): {{Integer}}
  [VolumeType](#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-properties"></a>

`DeleteOnTermination`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination"></a>
Use to configure delete on termination of the associated device.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Encrypted`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted"></a>
Use to configure device encryption.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Iops`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops"></a>
Use to configure device IOPS.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `64000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid"></a>
The Amazon Resource Name (ARN) that uniquely identifies the KMS key to use when encrypting the device. This can be either the Key ARN or the Alias ARN. For more information, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) in the *AWS Key Management Service Developer Guide*.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotId`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid"></a>
The snapshot that defines the device contents.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Throughput`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-throughput"></a>
**For GP3 volumes only** – The throughput in MiB/s that the volume supports.
*Required*: No
*Type*: Integer
*Minimum*: `125`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeSize`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize"></a>
Use to override the device's volume size.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `16000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeType`  <a name="cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype"></a>
Use to override the device's volume type.
*Required*: No
*Type*: String
*Allowed values*: `standard | io1 | io2 | io2a | gp2 | gp3 | gp3a | sc1 | st1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
