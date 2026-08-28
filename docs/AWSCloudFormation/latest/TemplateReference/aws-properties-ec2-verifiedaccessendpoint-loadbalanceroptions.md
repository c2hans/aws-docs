---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint LoadBalancerOptions
<a name="aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions"></a>

Describes the load balancer options when creating an AWS Verified Access endpoint using the `load-balancer` type.

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions-syntax.json"></a>

```
{
  "[LoadBalancerArn](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-loadbalancerarn)" : {{String}},
  "[Port](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-port)" : {{Integer}},
  "[PortRanges](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-portranges)" : {{[ PortRange, ... ]}},
  "[Protocol](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-protocol)" : {{String}},
  "[SubnetIds](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-subnetids)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions-syntax.yaml"></a>

```
  [LoadBalancerArn](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-loadbalancerarn): {{String}}
  [Port](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-port): {{Integer}}
  [PortRanges](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-portranges): {{
    - PortRange}}
  [Protocol](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-protocol): {{String}}
  [SubnetIds](#cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-subnetids): {{
    - String}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-loadbalanceroptions-properties"></a>

`LoadBalancerArn`  <a name="cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-loadbalancerarn"></a>
The ARN of the load balancer.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Port`  <a name="cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-port"></a>
The IP port number.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PortRanges`  <a name="cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-portranges"></a>
The port ranges.
*Required*: No
*Type*: Array of [PortRange](aws-properties-ec2-verifiedaccessendpoint-portrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocol`  <a name="cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-protocol"></a>
The IP protocol.
*Required*: No
*Type*: String
*Allowed values*: `http | https | tcp`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-ec2-verifiedaccessendpoint-loadbalanceroptions-subnetids"></a>
The IDs of the subnets. You can specify only one subnet per Availability Zone.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
