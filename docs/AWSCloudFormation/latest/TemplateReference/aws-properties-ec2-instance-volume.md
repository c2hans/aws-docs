---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-volume.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance Volume
<a name="aws-properties-ec2-instance-volume"></a>

Specifies a volume to attach to an instance.

`Volume` is an embedded property of the [ AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

## Syntax
<a name="aws-properties-ec2-instance-volume-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-volume-syntax.json"></a>

```
{
  "[Device](#cfn-ec2-instance-volume-device)" : {{String}},
  "[VolumeId](#cfn-ec2-instance-volume-volumeid)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-instance-volume-syntax.yaml"></a>

```
  [Device](#cfn-ec2-instance-volume-device): {{String}}
  [VolumeId](#cfn-ec2-instance-volume-volumeid): {{String}}
```

## Properties
<a name="aws-properties-ec2-instance-volume-properties"></a>

`Device`  <a name="cfn-ec2-instance-volume-device"></a>
The device name (for example, `/dev/sdh` or `xvdh`).
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeId`  <a name="cfn-ec2-instance-volume-volumeid"></a>
The ID of the EBS volume. The volume and instance must be within the same Availability Zone.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
