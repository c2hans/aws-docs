---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-volumespecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig VolumeSpecification
<a name="aws-properties-emr-instancefleetconfig-volumespecification"></a>

`VolumeSpecification` is a subproperty of the `EbsBlockDeviceConfig` property type. `VolumeSecification` determines the volume type, IOPS, and size (GiB) for EBS volumes attached to EC2 instances.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-volumespecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-volumespecification-syntax.json"></a>

```
{
  "[Iops](#cfn-emr-instancefleetconfig-volumespecification-iops)" : {{Integer}},
  "[SizeInGB](#cfn-emr-instancefleetconfig-volumespecification-sizeingb)" : {{Integer}},
  "[Throughput](#cfn-emr-instancefleetconfig-volumespecification-throughput)" : {{Integer}},
  "[VolumeType](#cfn-emr-instancefleetconfig-volumespecification-volumetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-volumespecification-syntax.yaml"></a>

```
  [Iops](#cfn-emr-instancefleetconfig-volumespecification-iops): {{Integer}}
  [SizeInGB](#cfn-emr-instancefleetconfig-volumespecification-sizeingb): {{Integer}}
  [Throughput](#cfn-emr-instancefleetconfig-volumespecification-throughput): {{Integer}}
  [VolumeType](#cfn-emr-instancefleetconfig-volumespecification-volumetype): {{String}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-volumespecification-properties"></a>

`Iops`  <a name="cfn-emr-instancefleetconfig-volumespecification-iops"></a>
The number of I/O operations per second (IOPS) that the volume supports.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeInGB`  <a name="cfn-emr-instancefleetconfig-volumespecification-sizeingb"></a>
The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Throughput`  <a name="cfn-emr-instancefleetconfig-volumespecification-throughput"></a>
The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeType`  <a name="cfn-emr-instancefleetconfig-volumespecification-volumetype"></a>
The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
