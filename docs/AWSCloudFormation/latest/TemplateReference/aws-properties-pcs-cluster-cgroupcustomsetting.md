---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-cgroupcustomsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster CgroupCustomSetting
<a name="aws-properties-pcs-cluster-cgroupcustomsetting"></a>

Additional settings that directly map to Cgroup settings.

**Important**
AWS PCS supports a subset of Cgroup settings. For more information, see [Configuring custom Cgroup settings in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/cgroup-custom-settings.html) in the *AWS PCS User Guide*.

## Syntax
<a name="aws-properties-pcs-cluster-cgroupcustomsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-cgroupcustomsetting-syntax.json"></a>

```
{
  "[ParameterName](#cfn-pcs-cluster-cgroupcustomsetting-parametername)" : {{String}},
  "[ParameterValue](#cfn-pcs-cluster-cgroupcustomsetting-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-cgroupcustomsetting-syntax.yaml"></a>

```
  [ParameterName](#cfn-pcs-cluster-cgroupcustomsetting-parametername): {{String}}
  [ParameterValue](#cfn-pcs-cluster-cgroupcustomsetting-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-cgroupcustomsetting-properties"></a>

`ParameterName`  <a name="cfn-pcs-cluster-cgroupcustomsetting-parametername"></a>
AWS PCS supports custom Cgroup settings for clusters. For more information, see [Configuring custom Cgroup settings in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/cgroup-custom-settings.html) in the *AWS PCS User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-pcs-cluster-cgroupcustomsetting-parametervalue"></a>
The values for the configured Cgroup settings.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
