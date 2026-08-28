---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-synthetics-canary-vpcconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Canary VPCConfig
<a name="aws-properties-synthetics-canary-vpcconfig"></a>

If this canary is to test an endpoint in a VPC, this structure contains information about the subnet and security groups of the VPC endpoint. For more information, see [ Running a Canary in a VPC](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).

## Syntax
<a name="aws-properties-synthetics-canary-vpcconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-synthetics-canary-vpcconfig-syntax.json"></a>

```
{
  "[Ipv6AllowedForDualStack](#cfn-synthetics-canary-vpcconfig-ipv6allowedfordualstack)" : {{Boolean}},
  "[SecurityGroupIds](#cfn-synthetics-canary-vpcconfig-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetIds](#cfn-synthetics-canary-vpcconfig-subnetids)" : {{[ String, ... ]}},
  "[VpcId](#cfn-synthetics-canary-vpcconfig-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-synthetics-canary-vpcconfig-syntax.yaml"></a>

```
  [Ipv6AllowedForDualStack](#cfn-synthetics-canary-vpcconfig-ipv6allowedfordualstack): {{Boolean}}
  [SecurityGroupIds](#cfn-synthetics-canary-vpcconfig-securitygroupids): {{
    - String}}
  [SubnetIds](#cfn-synthetics-canary-vpcconfig-subnetids): {{
    - String}}
  [VpcId](#cfn-synthetics-canary-vpcconfig-vpcid): {{String}}
```

## Properties
<a name="aws-properties-synthetics-canary-vpcconfig-properties"></a>

`Ipv6AllowedForDualStack`  <a name="cfn-synthetics-canary-vpcconfig-ipv6allowedfordualstack"></a>
Set this to `true` to allow outbound IPv6 traffic on VPC canaries that are connected to dual-stack subnets. The default is `false`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-synthetics-canary-vpcconfig-securitygroupids"></a>
The IDs of the security groups for this canary.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-synthetics-canary-vpcconfig-subnetids"></a>
The IDs of the subnets where this canary is to run.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-synthetics-canary-vpcconfig-vpcid"></a>
The ID of the VPC where this canary is to run.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
