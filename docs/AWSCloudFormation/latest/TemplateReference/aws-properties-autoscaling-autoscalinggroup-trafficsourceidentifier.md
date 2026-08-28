---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-trafficsourceidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup TrafficSourceIdentifier
<a name="aws-properties-autoscaling-autoscalinggroup-trafficsourceidentifier"></a>

Identifying information for a traffic source.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-trafficsourceidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-trafficsourceidentifier-syntax.json"></a>

```
{
  "[Identifier](#cfn-autoscaling-autoscalinggroup-trafficsourceidentifier-identifier)" : {{String}},
  "[Type](#cfn-autoscaling-autoscalinggroup-trafficsourceidentifier-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-trafficsourceidentifier-syntax.yaml"></a>

```
  [Identifier](#cfn-autoscaling-autoscalinggroup-trafficsourceidentifier-identifier): {{String}}
  [Type](#cfn-autoscaling-autoscalinggroup-trafficsourceidentifier-type): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-trafficsourceidentifier-properties"></a>

`Identifier`  <a name="cfn-autoscaling-autoscalinggroup-trafficsourceidentifier-identifier"></a>
Identifies the traffic source.
For Application Load Balancers, Gateway Load Balancers, Network Load Balancers, and VPC Lattice, this will be the Amazon Resource Name (ARN) for a target group in this account and Region. For Classic Load Balancers, this will be the name of the Classic Load Balancer in this account and Region.
For example:
+ Application Load Balancer ARN: `arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/1234567890123456`
+ Classic Load Balancer name: `my-classic-load-balancer`
+ VPC Lattice ARN: `arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-1234567890123456`
To get the ARN of a target group for a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer, or the name of a Classic Load Balancer, use the Elastic Load Balancing [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) and [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operations.
To get the ARN of a target group for VPC Lattice, use the VPC Lattice [GetTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetTargetGroup.html) API operation.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `511`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-autoscaling-autoscalinggroup-trafficsourceidentifier-type"></a>
Provides additional context for the value of `Identifier`.
The following lists the valid values:
+ `elb` if `Identifier` is the name of a Classic Load Balancer.
+ `elbv2` if `Identifier` is the ARN of an Application Load Balancer, Gateway Load Balancer, or Network Load Balancer target group.
+ `vpc-lattice` if `Identifier` is the ARN of a VPC Lattice target group.
Required if the identifier is the name of a Classic Load Balancer.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `511`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
