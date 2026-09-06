---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityagent-agentspace-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::AgentSpace VpcConfig
<a name="aws-properties-securityagent-agentspace-vpcconfig"></a>

The VPC configuration for a pentest, specifying the VPC, security groups, and subnets to use during testing.

## Syntax
<a name="aws-properties-securityagent-agentspace-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityagent-agentspace-vpcconfig-syntax.json"></a>

```
{
  "[SecurityGroupArns](#cfn-securityagent-agentspace-vpcconfig-securitygrouparns)" : {{[ String, ... ]}},
  "[SubnetArns](#cfn-securityagent-agentspace-vpcconfig-subnetarns)" : {{[ String, ... ]}},
  "[VpcArn](#cfn-securityagent-agentspace-vpcconfig-vpcarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-securityagent-agentspace-vpcconfig-syntax.yaml"></a>

```
  [SecurityGroupArns](#cfn-securityagent-agentspace-vpcconfig-securitygrouparns): {{
    - String}}
  [SubnetArns](#cfn-securityagent-agentspace-vpcconfig-subnetarns): {{
    - String}}
  [VpcArn](#cfn-securityagent-agentspace-vpcconfig-vpcarn): {{String}}
```

## Properties
<a name="aws-properties-securityagent-agentspace-vpcconfig-properties"></a>

`SecurityGroupArns`  <a name="cfn-securityagent-agentspace-vpcconfig-securitygrouparns"></a>
The Amazon Resource Names (ARNs) of the security groups for the VPC configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetArns`  <a name="cfn-securityagent-agentspace-vpcconfig-subnetarns"></a>
The Amazon Resource Names (ARNs) of the subnets for the VPC configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcArn`  <a name="cfn-securityagent-agentspace-vpcconfig-vpcarn"></a>
The Amazon Resource Name (ARN) of the VPC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
