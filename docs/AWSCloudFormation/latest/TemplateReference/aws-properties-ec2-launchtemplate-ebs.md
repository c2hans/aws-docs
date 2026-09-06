---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-ebs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate Ebs
<a name="aws-properties-ec2-launchtemplate-ebs"></a>

Parameters for a block device for an EBS volume in an Amazon EC2 launch template.

`Ebs` is a property of [ AWS::EC2::LaunchTemplate BlockDeviceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-blockdevicemapping.html).

## Syntax
<a name="aws-properties-ec2-launchtemplate-ebs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-ebs-syntax.json"></a>

```
{
  "[DeleteOnTermination](#cfn-ec2-launchtemplate-ebs-deleteontermination)" : {{Boolean}},
  "[EbsCardIndex](#cfn-ec2-launchtemplate-ebs-ebscardindex)" : {{Integer}},
  "[Encrypted](#cfn-ec2-launchtemplate-ebs-encrypted)" : {{Boolean}},
  "[Iops](#cfn-ec2-launchtemplate-ebs-iops)" : {{Integer}},
  "[KmsKeyId](#cfn-ec2-launchtemplate-ebs-kmskeyid)" : {{String}},
  "[SnapshotId](#cfn-ec2-launchtemplate-ebs-snapshotid)" : {{String}},
  "[Throughput](#cfn-ec2-launchtemplate-ebs-throughput)" : {{Integer}},
  "[VolumeInitializationRate](#cfn-ec2-launchtemplate-ebs-volumeinitializationrate)" : {{Integer}},
  "[VolumeSize](#cfn-ec2-launchtemplate-ebs-volumesize)" : {{Integer}},
  "[VolumeType](#cfn-ec2-launchtemplate-ebs-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-ebs-syntax.yaml"></a>

```
  [DeleteOnTermination](#cfn-ec2-launchtemplate-ebs-deleteontermination): {{Boolean}}
  [EbsCardIndex](#cfn-ec2-launchtemplate-ebs-ebscardindex): {{Integer}}
  [Encrypted](#cfn-ec2-launchtemplate-ebs-encrypted): {{Boolean}}
  [Iops](#cfn-ec2-launchtemplate-ebs-iops): {{Integer}}
  [KmsKeyId](#cfn-ec2-launchtemplate-ebs-kmskeyid): {{String}}
  [SnapshotId](#cfn-ec2-launchtemplate-ebs-snapshotid): {{String}}
  [Throughput](#cfn-ec2-launchtemplate-ebs-throughput): {{Integer}}
  [VolumeInitializationRate](#cfn-ec2-launchtemplate-ebs-volumeinitializationrate): {{Integer}}
  [VolumeSize](#cfn-ec2-launchtemplate-ebs-volumesize): {{Integer}}
  [VolumeType](#cfn-ec2-launchtemplate-ebs-volumetype): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-ebs-properties"></a>

`DeleteOnTermination`  <a name="cfn-ec2-launchtemplate-ebs-deleteontermination"></a>
Indicates whether the EBS volume is deleted on instance termination.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsCardIndex`  <a name="cfn-ec2-launchtemplate-ebs-ebscardindex"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Encrypted`  <a name="cfn-ec2-launchtemplate-ebs-encrypted"></a>
Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you can't specify an encryption value.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Iops`  <a name="cfn-ec2-launchtemplate-ebs-iops"></a>
The number of I/O operations per second (IOPS). For `gp3`, `io1`, and `io2` volumes, this represents the number of IOPS that are provisioned for the volume. For `gp2` volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.
The following are the supported values for each volume type:
+ `gp3`: 3,000 - 80,000 IOPS
+ `io1`: 100 - 64,000 IOPS
+ `io2`: 100 - 256,000 IOPS
For `io2` volumes, you can achieve up to 256,000 IOPS on [instances built on the Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html). On other instances, you can achieve performance up to 32,000 IOPS.
This parameter is supported for `io1`, `io2`, and `gp3` volumes only.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-ec2-launchtemplate-ebs-kmskeyid"></a>
Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotId`  <a name="cfn-ec2-launchtemplate-ebs-snapshotid"></a>
The ID of the snapshot.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Throughput`  <a name="cfn-ec2-launchtemplate-ebs-throughput"></a>
The throughput to provision for a `gp3` volume, with a maximum of 2,000 MiB/s.
Valid Range: Minimum value of 125. Maximum value of 2,000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeInitializationRate`  <a name="cfn-ec2-launchtemplate-ebs-volumeinitializationrate"></a>
Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as *volume initialization*. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.
This parameter is supported only for volumes created from snapshots. Omit this parameter if:
+ You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.
**Note**
If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.
+ You want to create a volume that is initialized at the default rate.
For more information, see [ Initialize Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html) in the *Amazon EC2 User Guide*.
Valid range: 100 - 300 MiB/s
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeSize`  <a name="cfn-ec2-launchtemplate-ebs-volumesize"></a>
The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. The following are the supported volumes sizes for each volume type:
+ `gp2`: 1 - 16,384 GiB
+ `gp3`: 1 - 65,536 GiB
+ `io1`: 4 - 16,384 GiB
+ `io2`: 4 - 65,536 GiB
+ `st1` and `sc1`: 125 - 16,384 GiB
+ `standard`: 1 - 1024 GiB
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeType`  <a name="cfn-ec2-launchtemplate-ebs-volumetype"></a>
The volume type. For more information, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.
*Required*: No
*Type*: String
*Allowed values*: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ec2-launchtemplate-ebs--seealso"></a>
+ [ LaunchTemplateEbsBlockDeviceRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateEbsBlockDeviceRequest.html) in the *Amazon EC2 API Reference*
