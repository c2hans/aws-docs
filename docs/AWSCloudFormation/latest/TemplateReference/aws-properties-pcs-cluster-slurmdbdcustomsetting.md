---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-slurmdbdcustomsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster SlurmdbdCustomSetting
<a name="aws-properties-pcs-cluster-slurmdbdcustomsetting"></a>

Additional settings that directly map to SlurmDBD settings.

**Important**
AWS PCS supports a subset of SlurmDBD settings. For more information, see [Configuring custom SlurmDBD settings in AWS PCS](https://docs.aws.amazon.com//pcs/latest/userguide/slurmdbd-custom-settings.html) in the *AWS PCS User Guide*.

## Syntax
<a name="aws-properties-pcs-cluster-slurmdbdcustomsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-slurmdbdcustomsetting-syntax.json"></a>

```
{
  "[ParameterName](#cfn-pcs-cluster-slurmdbdcustomsetting-parametername)" : {{String}},
  "[ParameterValue](#cfn-pcs-cluster-slurmdbdcustomsetting-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-slurmdbdcustomsetting-syntax.yaml"></a>

```
  [ParameterName](#cfn-pcs-cluster-slurmdbdcustomsetting-parametername): {{String}}
  [ParameterValue](#cfn-pcs-cluster-slurmdbdcustomsetting-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-slurmdbdcustomsetting-properties"></a>

`ParameterName`  <a name="cfn-pcs-cluster-slurmdbdcustomsetting-parametername"></a>
AWS PCS supports custom SlurmDBD settings for clusters. For more information, see [Configuring custom SlurmDBD settings in AWS PCS](https://docs.aws.amazon.com//pcs/latest/userguide/slurmdbd-custom-settings.html) in the *AWS PCS User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-pcs-cluster-slurmdbdcustomsetting-parametervalue"></a>
The values for the configured SlurmDBD settings.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
