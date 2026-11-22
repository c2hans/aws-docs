---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-imagebuilder-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::ImageBuilder VpcConfig

The VPC configuration for the image builder.

## Syntax
<a name="aws-properties-appstream-imagebuilder-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-imagebuilder-vpcconfig-syntax.json"></a>

```json
{
  "[SecurityGroupIds](#cfn-appstream-imagebuilder-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-appstream-imagebuilder-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appstream-imagebuilder-vpcconfig-syntax.yaml"></a>

```yaml
  [SecurityGroupIds](#cfn-appstream-imagebuilder-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-appstream-imagebuilder-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-appstream-imagebuilder-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-appstream-imagebuilder-vpcconfig-securitygroupids"></a>
The identifiers of the security groups for the image builder.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetIds`  <a name="cfn-appstream-imagebuilder-vpcconfig-subnetids"></a>
The identifier of the subnet to which a network interface is attached from the image builder instance. An image builder instance can use one subnet.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
