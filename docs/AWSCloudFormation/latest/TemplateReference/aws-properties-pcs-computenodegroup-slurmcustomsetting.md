---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-slurmcustomsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup SlurmCustomSetting
<a name="aws-properties-pcs-computenodegroup-slurmcustomsetting"></a>

Additional settings that directly map to Slurm settings.

**Important**
AWS PCS supports a subset of Slurm settings. For more information, see [Configuring custom Slurm settings in AWS PCS](https://docs.aws.amazon.com//pcs/latest/userguide/slurm-custom-settings.html) in the *AWS PCS User Guide*.

## Syntax
<a name="aws-properties-pcs-computenodegroup-slurmcustomsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-slurmcustomsetting-syntax.json"></a>

```
{
  "[ParameterName](#cfn-pcs-computenodegroup-slurmcustomsetting-parametername)" : {{String}},
  "[ParameterValue](#cfn-pcs-computenodegroup-slurmcustomsetting-parametervalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-slurmcustomsetting-syntax.yaml"></a>

```
  [ParameterName](#cfn-pcs-computenodegroup-slurmcustomsetting-parametername): {{String}}
  [ParameterValue](#cfn-pcs-computenodegroup-slurmcustomsetting-parametervalue): {{String}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-slurmcustomsetting-properties"></a>

`ParameterName`  <a name="cfn-pcs-computenodegroup-slurmcustomsetting-parametername"></a>
AWS PCS supports custom Slurm settings for clusters, compute node groups, and queues. For more information, see [Configuring custom Slurm settings in AWS PCS](https://docs.aws.amazon.com//pcs/latest/userguide/slurm-custom-settings.html) in the *AWS PCS User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-pcs-computenodegroup-slurmcustomsetting-parametervalue"></a>
The values for the configured Slurm settings.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
