---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-ebsblockdevice.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet EbsBlockDevice
<a name="aws-properties-ec2-spotfleet-ebsblockdevice"></a>

Describes a block device for an EBS volume.

## Syntax
<a name="aws-properties-ec2-spotfleet-ebsblockdevice-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-ebsblockdevice-syntax.json"></a>

```
{
  "[DeleteOnTermination](#cfn-ec2-spotfleet-ebsblockdevice-deleteontermination)" : {{Boolean}},
  "[Encrypted](#cfn-ec2-spotfleet-ebsblockdevice-encrypted)" : {{Boolean}},
  "[Iops](#cfn-ec2-spotfleet-ebsblockdevice-iops)" : {{Integer}},
  "[SnapshotId](#cfn-ec2-spotfleet-ebsblockdevice-snapshotid)" : {{String}},
  "[VolumeSize](#cfn-ec2-spotfleet-ebsblockdevice-volumesize)" : {{Integer}},
  "[VolumeType](#cfn-ec2-spotfleet-ebsblockdevice-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-ebsblockdevice-syntax.yaml"></a>

```
  [DeleteOnTermination](#cfn-ec2-spotfleet-ebsblockdevice-deleteontermination): {{Boolean}}
  [Encrypted](#cfn-ec2-spotfleet-ebsblockdevice-encrypted): {{Boolean}}
  [Iops](#cfn-ec2-spotfleet-ebsblockdevice-iops): {{Integer}}
  [SnapshotId](#cfn-ec2-spotfleet-ebsblockdevice-snapshotid): {{String}}
  [VolumeSize](#cfn-ec2-spotfleet-ebsblockdevice-volumesize): {{Integer}}
  [VolumeType](#cfn-ec2-spotfleet-ebsblockdevice-volumetype): {{String}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-ebsblockdevice-properties"></a>

`DeleteOnTermination`  <a name="cfn-ec2-spotfleet-ebsblockdevice-deleteontermination"></a>
Indicates whether the EBS volume is deleted on instance termination. For more information, see [Preserving Amazon EBS volumes on instance termination](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#preserving-volumes-on-termination) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Encrypted`  <a name="cfn-ec2-spotfleet-ebsblockdevice-encrypted"></a>
Indicates whether the encryption state of an EBS volume is changed while being restored from a backing snapshot. The effect of setting the encryption state to `true` depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-parameters) in the *Amazon EC2 User Guide*.
In no case can you remove encryption from an encrypted volume.
Encrypted volumes can only be attached to instances that support Amazon EBS encryption. For more information, see [Supported Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances).
This parameter is not returned by [DescribeImageAttribute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute.html).
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Iops`  <a name="cfn-ec2-spotfleet-ebsblockdevice-iops"></a>
The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
The following are the supported values for each volume type:
+ `gp3`: 3,000 - 80,000 IOPS
+ `io1`: 100 - 64,000 IOPS
+ `io2`: 100 - 256,000 IOPS
For `io2` volumes, you can achieve up to 256,000 IOPS on [instances built on the Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances). On other instances, you can achieve performance up to 32,000 IOPS.
This parameter is required for `io1` and `io2` volumes. The default for `gp3` volumes is 3,000 IOPS.
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotId`  <a name="cfn-ec2-spotfleet-ebsblockdevice-snapshotid"></a>
The ID of the snapshot.
*Required*: Conditional
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeSize`  <a name="cfn-ec2-spotfleet-ebsblockdevice-volumesize"></a>
The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.
The following are the supported sizes for each volume type:
+ `gp2`: 1 - 16,384 GiB
+ `gp3`: 1 - 65,536 GiB
+ `io1`: 4 - 16,384 GiB
+ `io2`: 4 - 65,536 GiB
+ `st1` and `sc1`: 125 - 16,384 GiB
+ `standard`: 1 - 1024 GiB
*Required*: Conditional
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumeType`  <a name="cfn-ec2-spotfleet-ebsblockdevice-volumetype"></a>
The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
