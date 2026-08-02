---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-targetgroupsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet TargetGroupsConfig
<a name="aws-properties-ec2-spotfleet-targetgroupsconfig"></a>

Describes the target groups to attach to a Spot Fleet. Spot Fleet registers the running Spot Instances with these target groups.

## Syntax
<a name="aws-properties-ec2-spotfleet-targetgroupsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-targetgroupsconfig-syntax.json"></a>

```
{
  "[TargetGroups](#cfn-ec2-spotfleet-targetgroupsconfig-targetgroups)" : {{[ TargetGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-targetgroupsconfig-syntax.yaml"></a>

```
  [TargetGroups](#cfn-ec2-spotfleet-targetgroupsconfig-targetgroups): {{
    - TargetGroup}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-targetgroupsconfig-properties"></a>

`TargetGroups`  <a name="cfn-ec2-spotfleet-targetgroupsconfig-targetgroups"></a>
One or more target groups.
*Required*: Yes
*Type*: Array of [TargetGroup](aws-properties-ec2-spotfleet-targetgroup.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
