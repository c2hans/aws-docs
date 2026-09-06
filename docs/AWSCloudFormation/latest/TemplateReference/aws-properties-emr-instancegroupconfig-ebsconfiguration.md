---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-ebsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig EbsConfiguration
<a name="aws-properties-emr-instancegroupconfig-ebsconfiguration"></a>

The Amazon EBS configuration of a cluster instance.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-ebsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-ebsconfiguration-syntax.json"></a>

```
{
  "[EbsBlockDeviceConfigs](#cfn-emr-instancegroupconfig-ebsconfiguration-ebsblockdeviceconfigs)" : {{[ EbsBlockDeviceConfig, ... ]}},
  "[EbsOptimized](#cfn-emr-instancegroupconfig-ebsconfiguration-ebsoptimized)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-ebsconfiguration-syntax.yaml"></a>

```
  [EbsBlockDeviceConfigs](#cfn-emr-instancegroupconfig-ebsconfiguration-ebsblockdeviceconfigs): {{
    - EbsBlockDeviceConfig}}
  [EbsOptimized](#cfn-emr-instancegroupconfig-ebsconfiguration-ebsoptimized): {{Boolean}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-ebsconfiguration-properties"></a>

`EbsBlockDeviceConfigs`  <a name="cfn-emr-instancegroupconfig-ebsconfiguration-ebsblockdeviceconfigs"></a>
An array of Amazon EBS volume specifications attached to a cluster instance.
*Required*: No
*Type*: Array of [EbsBlockDeviceConfig](aws-properties-emr-instancegroupconfig-ebsblockdeviceconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EbsOptimized`  <a name="cfn-emr-instancegroupconfig-ebsconfiguration-ebsoptimized"></a>
Indicates whether an Amazon EBS volume is EBS-optimized. The default is false. You should explicitly set this value to true to enable the Amazon EBS-optimized setting for an EC2 instance.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
