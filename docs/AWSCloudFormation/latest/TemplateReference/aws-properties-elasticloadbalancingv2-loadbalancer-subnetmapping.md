---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::LoadBalancer SubnetMapping
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping"></a>

Specifies a subnet for a load balancer.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping-syntax.json"></a>

```
{
  "[AllocationId](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-allocationid)" : {{String}},
  "[IPv6Address](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-ipv6address)" : {{String}},
  "[PrivateIPv4Address](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-privateipv4address)" : {{String}},
  "[SourceNatIpv6Prefix](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-sourcenatipv6prefix)" : {{String}},
  "[SubnetId](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-subnetid)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping-syntax.yaml"></a>

```
  [AllocationId](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-allocationid): {{String}}
  [IPv6Address](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-ipv6address): {{String}}
  [PrivateIPv4Address](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-privateipv4address): {{String}}
  [SourceNatIpv6Prefix](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-sourcenatipv6prefix): {{String}}
  [SubnetId](#cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-subnetid): {{String}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-subnetmapping-properties"></a>

`AllocationId`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-allocationid"></a>
[Network Load Balancers] The allocation ID of the Elastic IP address for an internet-facing load balancer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IPv6Address`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-ipv6address"></a>
[Network Load Balancers] The IPv6 address.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivateIPv4Address`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-privateipv4address"></a>
[Network Load Balancers] The private IPv4 address for an internal load balancer.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceNatIpv6Prefix`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-sourcenatipv6prefix"></a>
[Network Load Balancers with UDP listeners] The IPv6 prefix to use for source NAT. Specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or `auto_assigned` to use an IPv6 prefix selected at random from the subnet CIDR block.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-elasticloadbalancingv2-loadbalancer-subnetmapping-subnetid"></a>
The ID of the subnet.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
