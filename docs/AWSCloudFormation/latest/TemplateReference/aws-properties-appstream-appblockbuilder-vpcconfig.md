---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-appblockbuilder-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::AppBlockBuilder VpcConfig
<a name="aws-properties-appstream-appblockbuilder-vpcconfig"></a>

Describes VPC configuration information for fleets and image builders.

## Syntax
<a name="aws-properties-appstream-appblockbuilder-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-appblockbuilder-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-appstream-appblockbuilder-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-appstream-appblockbuilder-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appstream-appblockbuilder-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-appstream-appblockbuilder-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-appstream-appblockbuilder-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-appstream-appblockbuilder-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-appstream-appblockbuilder-vpcconfig-securitygroupids"></a>
The identifiers of the security groups for the fleet or image builder.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-appstream-appblockbuilder-vpcconfig-subnetids"></a>
The identifiers of the subnets to which a network interface is attached from the fleet instance or image builder instance. Fleet instances use one or more subnets. Image builder instances use one subnet.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
