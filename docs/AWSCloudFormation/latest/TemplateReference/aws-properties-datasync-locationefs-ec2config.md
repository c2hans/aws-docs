---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationefs-ec2config.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationEFS Ec2Config
<a name="aws-properties-datasync-locationefs-ec2config"></a>

The subnet and security groups that AWS DataSync uses to connect to one of your Amazon EFS file system's [mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html).

## Syntax
<a name="aws-properties-datasync-locationefs-ec2config-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationefs-ec2config-syntax.json"></a>

```
{
  "[SecurityGroupArns](#cfn-datasync-locationefs-ec2config-securitygrouparns)" : {{[ String, ... ]}},
  "[SubnetArn](#cfn-datasync-locationefs-ec2config-subnetarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationefs-ec2config-syntax.yaml"></a>

```
  [SecurityGroupArns](#cfn-datasync-locationefs-ec2config-securitygrouparns): {{
    - String}}
  [SubnetArn](#cfn-datasync-locationefs-ec2config-subnetarn): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationefs-ec2config-properties"></a>

`SecurityGroupArns`  <a name="cfn-datasync-locationefs-ec2config-securitygrouparns"></a>
Specifies the Amazon Resource Names (ARNs) of the security groups associated with an Amazon EFS file system's mount target.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetArn`  <a name="cfn-datasync-locationefs-ec2config-subnetarn"></a>
Specifies the ARN of a subnet where DataSync creates the [network interfaces](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html#required-network-interfaces.html) for managing traffic during your transfer.
The subnet must be located:
+ In the same virtual private cloud (VPC) as the Amazon EFS file system.
+ In the same Availability Zone as at least one mount target for the Amazon EFS file system.
You don't need to specify a subnet that includes a file system mount target.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:subnet/.*$`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
