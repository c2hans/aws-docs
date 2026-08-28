---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-fleet-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Fleet VpcConfig
<a name="aws-properties-appstream-fleet-vpcconfig"></a>

The VPC configuration information for the fleet.

## Syntax
<a name="aws-properties-appstream-fleet-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-fleet-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupIds](#cfn-appstream-fleet-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-appstream-fleet-vpcconfig-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-appstream-fleet-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupIds](#cfn-appstream-fleet-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-appstream-fleet-vpcconfig-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-appstream-fleet-vpcconfig-properties"></a>

`SecurityGroupIds`  <a name="cfn-appstream-fleet-vpcconfig-securitygroupids"></a>
The identifiers of the security groups for the fleet.
*Required*: No
*Type*: Array of String
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-appstream-fleet-vpcconfig-subnetids"></a>
The identifiers of the subnets to which a network interface is attached from the fleet instance. Fleet instances can use one or two subnets.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
