---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-accounting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster Accounting
<a name="aws-properties-pcs-cluster-accounting"></a>

The accounting configuration includes configurable settings for Slurm accounting.

## Syntax
<a name="aws-properties-pcs-cluster-accounting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-accounting-syntax.json"></a>

```
{
  "[DefaultPurgeTimeInDays](#cfn-pcs-cluster-accounting-defaultpurgetimeindays)" : {{Integer}},
  "[Mode](#cfn-pcs-cluster-accounting-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-accounting-syntax.yaml"></a>

```
  [DefaultPurgeTimeInDays](#cfn-pcs-cluster-accounting-defaultpurgetimeindays): {{Integer}}
  [Mode](#cfn-pcs-cluster-accounting-mode): {{String}}
```

## Properties
<a name="aws-properties-pcs-cluster-accounting-properties"></a>

`DefaultPurgeTimeInDays`  <a name="cfn-pcs-cluster-accounting-defaultpurgetimeindays"></a>
The default value for all purge settings for `slurmdbd.conf`. For more information, see the [slurmdbd.conf documentation at SchedMD](https://slurm.schedmd.com/slurmdbd.conf.html).
The default value for `defaultPurgeTimeInDays` is `-1`.
A value of `-1` means there is no purge time and records persist as long as the cluster exists.
`0` isn't a valid value.
*Required*: No
*Type*: Integer
*Minimum*: `-1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-pcs-cluster-accounting-mode"></a>
The default value for `mode` is `NONE`. A value of `STANDARD` means Slurm accounting is enabled.
*Required*: Yes
*Type*: String
*Allowed values*: `STANDARD | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
