---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig EbsBlockDeviceConfig
<a name="aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig"></a>

Configuration of requested EBS block device associated with the instance group with count of volumes that are associated to every instance.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig-syntax.json"></a>

```
{
  "[VolumeSpecification](#cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumespecification)" : {{VolumeSpecification}},
  "[VolumesPerInstance](#cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumesperinstance)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig-syntax.yaml"></a>

```
  [VolumeSpecification](#cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumespecification): {{
    VolumeSpecification}}
  [VolumesPerInstance](#cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumesperinstance): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig-properties"></a>

`VolumeSpecification`  <a name="cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumespecification"></a>
EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.
*Required*: Yes
*Type*: [VolumeSpecification](aws-properties-emr-instancegroupconfig-volumespecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VolumesPerInstance`  <a name="cfn-emr-instancegroupconfig-ebsblockdeviceconfig-volumesperinstance"></a>
Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
