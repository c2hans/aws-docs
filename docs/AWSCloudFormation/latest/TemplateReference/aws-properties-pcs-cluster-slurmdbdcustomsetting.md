---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-slurmdbdcustomsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster SlurmdbdCustomSetting
<a name="aws-properties-pcs-cluster-slurmdbdcustomsetting"></a>

Additional settings that directly map to SlurmDBD settings.

**Important**
AWS PCS supports a subset of SlurmDBD settings. For more information, see [Configuring custom SlurmDBD settings in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurmdbd-custom-settings.html) in the *AWS PCS User Guide*.

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
AWS PCS supports custom SlurmDBD settings for clusters. For more information, see [Configuring custom SlurmDBD settings in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurmdbd-custom-settings.html) in the *AWS PCS User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterValue`  <a name="cfn-pcs-cluster-slurmdbdcustomsetting-parametervalue"></a>
The values for the configured SlurmDBD settings.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
