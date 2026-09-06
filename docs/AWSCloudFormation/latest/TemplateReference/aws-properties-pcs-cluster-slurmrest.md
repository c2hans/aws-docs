---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-slurmrest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster SlurmRest
<a name="aws-properties-pcs-cluster-slurmrest"></a>

The Slurm REST API configuration includes settings for enabling and configuring the Slurm REST API. It's a property of the [ClusterSlurmConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcs-cluster-slurmconfiguration.html) object.

## Syntax
<a name="aws-properties-pcs-cluster-slurmrest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-slurmrest-syntax.json"></a>

```
{
  "[Mode](#cfn-pcs-cluster-slurmrest-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-slurmrest-syntax.yaml"></a>

```
  [Mode](#cfn-pcs-cluster-slurmrest-mode): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-slurmrest-properties"></a>

`Mode`  <a name="cfn-pcs-cluster-slurmrest-mode"></a>
The default value for `mode` is `NONE`. A value of `STANDARD` means the Slurm REST API is enabled.
*Required*: Yes
*Type*: String
*Allowed values*: `STANDARD | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
