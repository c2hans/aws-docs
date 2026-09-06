---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-launchtemplate-networkperformanceoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LaunchTemplate NetworkPerformanceOptions
<a name="aws-properties-ec2-launchtemplate-networkperformanceoptions"></a>

Contains settings for the network performance options for the instance.

## Syntax
<a name="aws-properties-ec2-launchtemplate-networkperformanceoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-launchtemplate-networkperformanceoptions-syntax.json"></a>

```
{
  "[BandwidthWeighting](#cfn-ec2-launchtemplate-networkperformanceoptions-bandwidthweighting)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-launchtemplate-networkperformanceoptions-syntax.yaml"></a>

```
  [BandwidthWeighting](#cfn-ec2-launchtemplate-networkperformanceoptions-bandwidthweighting): {{String}}
```

## Properties
<a name="aws-properties-ec2-launchtemplate-networkperformanceoptions-properties"></a>

`BandwidthWeighting`  <a name="cfn-ec2-launchtemplate-networkperformanceoptions-bandwidthweighting"></a>
Specify the bandwidth weighting option to boost the associated type of baseline bandwidth, as follows:
default
This option uses the standard bandwidth configuration for your instance type.
vpc-1
This option boosts your networking baseline bandwidth and reduces your EBS baseline bandwidth.
ebs-1
This option boosts your EBS baseline bandwidth and reduces your networking baseline bandwidth.
*Required*: No
*Type*: String
*Allowed values*: `default | vpc-1 | ebs-1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
