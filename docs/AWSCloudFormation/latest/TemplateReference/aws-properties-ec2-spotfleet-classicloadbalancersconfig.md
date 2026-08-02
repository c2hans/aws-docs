---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-classicloadbalancersconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet ClassicLoadBalancersConfig
<a name="aws-properties-ec2-spotfleet-classicloadbalancersconfig"></a>

Specifies the Classic Load Balancers to attach to a Spot Fleet. Spot Fleet registers the running Spot Instances with these Classic Load Balancers.

## Syntax
<a name="aws-properties-ec2-spotfleet-classicloadbalancersconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-classicloadbalancersconfig-syntax.json"></a>

```
{
  "[ClassicLoadBalancers](#cfn-ec2-spotfleet-classicloadbalancersconfig-classicloadbalancers)" : {{[ ClassicLoadBalancer, ... ]}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-classicloadbalancersconfig-syntax.yaml"></a>

```
  [ClassicLoadBalancers](#cfn-ec2-spotfleet-classicloadbalancersconfig-classicloadbalancers): {{
    - ClassicLoadBalancer}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-classicloadbalancersconfig-properties"></a>

`ClassicLoadBalancers`  <a name="cfn-ec2-spotfleet-classicloadbalancersconfig-classicloadbalancers"></a>
One or more Classic Load Balancers.
*Required*: Yes
*Type*: Array of [ClassicLoadBalancer](aws-properties-ec2-spotfleet-classicloadbalancer.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
