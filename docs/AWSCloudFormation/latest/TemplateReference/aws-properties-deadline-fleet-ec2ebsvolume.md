---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-ec2ebsvolume.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet Ec2EbsVolume
<a name="aws-properties-deadline-fleet-ec2ebsvolume"></a>

Specifies the EBS volume.

## Syntax
<a name="aws-properties-deadline-fleet-ec2ebsvolume-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-ec2ebsvolume-syntax.json"></a>

```
{
  "[Iops](#cfn-deadline-fleet-ec2ebsvolume-iops)" : {{Integer}},
  "[SizeGiB](#cfn-deadline-fleet-ec2ebsvolume-sizegib)" : {{Integer}},
  "[ThroughputMiB](#cfn-deadline-fleet-ec2ebsvolume-throughputmib)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-ec2ebsvolume-syntax.yaml"></a>

```
  [Iops](#cfn-deadline-fleet-ec2ebsvolume-iops): {{Integer}}
  [SizeGiB](#cfn-deadline-fleet-ec2ebsvolume-sizegib): {{Integer}}
  [ThroughputMiB](#cfn-deadline-fleet-ec2ebsvolume-throughputmib): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-ec2ebsvolume-properties"></a>

`Iops`  <a name="cfn-deadline-fleet-ec2ebsvolume-iops"></a>
The IOPS per volume.
*Required*: No
*Type*: Integer
*Minimum*: `3000`
*Maximum*: `16000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeGiB`  <a name="cfn-deadline-fleet-ec2ebsvolume-sizegib"></a>
The EBS volume size in GiB.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThroughputMiB`  <a name="cfn-deadline-fleet-ec2ebsvolume-throughputmib"></a>
The throughput per volume in MiB.
*Required*: No
*Type*: Integer
*Minimum*: `125`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
