---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-loadbalancersconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet LoadBalancersConfig
<a name="aws-properties-ec2-spotfleet-loadbalancersconfig"></a>

Specifies the Classic Load Balancers and target groups to attach to a Spot Fleet request.

## Syntax
<a name="aws-properties-ec2-spotfleet-loadbalancersconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-loadbalancersconfig-syntax.json"></a>

```
{
  "[ClassicLoadBalancersConfig](#cfn-ec2-spotfleet-loadbalancersconfig-classicloadbalancersconfig)" : {{ClassicLoadBalancersConfig}},
  "[TargetGroupsConfig](#cfn-ec2-spotfleet-loadbalancersconfig-targetgroupsconfig)" : {{TargetGroupsConfig}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-loadbalancersconfig-syntax.yaml"></a>

```
  [ClassicLoadBalancersConfig](#cfn-ec2-spotfleet-loadbalancersconfig-classicloadbalancersconfig): {{
    ClassicLoadBalancersConfig}}
  [TargetGroupsConfig](#cfn-ec2-spotfleet-loadbalancersconfig-targetgroupsconfig): {{
    TargetGroupsConfig}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-loadbalancersconfig-properties"></a>

`ClassicLoadBalancersConfig`  <a name="cfn-ec2-spotfleet-loadbalancersconfig-classicloadbalancersconfig"></a>
The Classic Load Balancers.
*Required*: No
*Type*: [ClassicLoadBalancersConfig](aws-properties-ec2-spotfleet-classicloadbalancersconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetGroupsConfig`  <a name="cfn-ec2-spotfleet-loadbalancersconfig-targetgroupsconfig"></a>
The target groups.
*Required*: No
*Type*: [TargetGroupsConfig](aws-properties-ec2-spotfleet-targetgroupsconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
