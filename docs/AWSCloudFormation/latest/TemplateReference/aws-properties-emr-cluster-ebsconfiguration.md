---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-ebsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster EbsConfiguration
<a name="aws-properties-emr-cluster-ebsconfiguration"></a>

`EbsConfiguration` is a subproperty of `InstanceFleetConfig` or `InstanceGroupConfig`. `EbsConfiguration` determines the EBS volumes to attach to EMR cluster instances.

## Syntax
<a name="aws-properties-emr-cluster-ebsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-ebsconfiguration-syntax.json"></a>

```
{
  "[EbsBlockDeviceConfigs](#cfn-emr-cluster-ebsconfiguration-ebsblockdeviceconfigs)" : {{[ EbsBlockDeviceConfig, ... ]}},
  "[EbsOptimized](#cfn-emr-cluster-ebsconfiguration-ebsoptimized)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emr-cluster-ebsconfiguration-syntax.yaml"></a>

```
  [EbsBlockDeviceConfigs](#cfn-emr-cluster-ebsconfiguration-ebsblockdeviceconfigs): {{
    - EbsBlockDeviceConfig}}
  [EbsOptimized](#cfn-emr-cluster-ebsconfiguration-ebsoptimized): {{Boolean}}
```

## Properties
<a name="aws-properties-emr-cluster-ebsconfiguration-properties"></a>

`EbsBlockDeviceConfigs`  <a name="cfn-emr-cluster-ebsconfiguration-ebsblockdeviceconfigs"></a>
An array of Amazon EBS volume specifications attached to a cluster instance.
*Required*: No
*Type*: Array of [EbsBlockDeviceConfig](aws-properties-emr-cluster-ebsblockdeviceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsOptimized`  <a name="cfn-emr-cluster-ebsconfiguration-ebsoptimized"></a>
Indicates whether an Amazon EBS volume is EBS-optimized. The default is false. You should explicitly set this value to true to enable the Amazon EBS-optimized setting for an EC2 instance.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
