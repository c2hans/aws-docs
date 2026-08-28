---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-ebsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig EbsConfiguration
<a name="aws-properties-emr-instancefleetconfig-ebsconfiguration"></a>

`EbsConfiguration` determines the EBS volumes to attach to EMR cluster instances.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-ebsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-ebsconfiguration-syntax.json"></a>

```
{
  "[EbsBlockDeviceConfigs](#cfn-emr-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs)" : {{[ EbsBlockDeviceConfig, ... ]}},
  "[EbsOptimized](#cfn-emr-instancefleetconfig-ebsconfiguration-ebsoptimized)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-ebsconfiguration-syntax.yaml"></a>

```
  [EbsBlockDeviceConfigs](#cfn-emr-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs): {{
    - EbsBlockDeviceConfig}}
  [EbsOptimized](#cfn-emr-instancefleetconfig-ebsconfiguration-ebsoptimized): {{Boolean}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-ebsconfiguration-properties"></a>

`EbsBlockDeviceConfigs`  <a name="cfn-emr-instancefleetconfig-ebsconfiguration-ebsblockdeviceconfigs"></a>
An array of Amazon EBS volume specifications attached to a cluster instance.
*Required*: No
*Type*: Array of [EbsBlockDeviceConfig](aws-properties-emr-instancefleetconfig-ebsblockdeviceconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EbsOptimized`  <a name="cfn-emr-instancefleetconfig-ebsconfiguration-ebsoptimized"></a>
Indicates whether an Amazon EBS volume is EBS-optimized. The default is false. You should explicitly set this value to true to enable the Amazon EBS-optimized setting for an EC2 instance.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
