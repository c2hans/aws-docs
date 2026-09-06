---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig EbsBlockDeviceConfig
<a name="aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig"></a>

`EbsBlockDeviceConfig` is a subproperty of the `EbsConfiguration` property type. `EbsBlockDeviceConfig` defines the number and type of EBS volumes to associate with all EC2 instances in an EMR cluster.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig-syntax.json"></a>

```
{
  "[VolumeSpecification](#cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumespecification)" : {{VolumeSpecification}},
  "[VolumesPerInstance](#cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumesperinstance)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig-syntax.yaml"></a>

```
  [VolumeSpecification](#cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumespecification): {{
    VolumeSpecification}}
  [VolumesPerInstance](#cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumesperinstance): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig-properties"></a>

`VolumeSpecification`  <a name="cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumespecification"></a>
EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.
*Required*: Yes
*Type*: [VolumeSpecification](aws-properties-emr-instancefleetconfig-volumespecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumesPerInstance`  <a name="cfn-emr-instancefleetconfig-ebsblockdeviceconfig-volumesperinstance"></a>
Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
