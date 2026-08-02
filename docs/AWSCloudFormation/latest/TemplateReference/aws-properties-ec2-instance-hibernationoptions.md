---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-instance-hibernationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Instance HibernationOptions
<a name="aws-properties-ec2-instance-hibernationoptions"></a>

Specifies the hibernation options for the instance.

`HibernationOptions` is a property of the [AWS::EC2::Instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html) resource.

## Syntax
<a name="aws-properties-ec2-instance-hibernationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-instance-hibernationoptions-syntax.json"></a>

```
{
  "[Configured](#cfn-ec2-instance-hibernationoptions-configured)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-instance-hibernationoptions-syntax.yaml"></a>

```
  [Configured](#cfn-ec2-instance-hibernationoptions-configured): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-instance-hibernationoptions-properties"></a>

`Configured`  <a name="cfn-ec2-instance-hibernationoptions-configured"></a>
Set to `true` to enable your instance for hibernation.
For Spot Instances, if you set `Configured` to `true`, either omit the `InstanceInterruptionBehavior` parameter (for [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html)), or set it to `hibernate`. When `Configured` is true:
+ If you omit `InstanceInterruptionBehavior`, it defaults to `hibernate`.
+ If you set `InstanceInterruptionBehavior` to a value other than `hibernate`, you'll get an error.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
