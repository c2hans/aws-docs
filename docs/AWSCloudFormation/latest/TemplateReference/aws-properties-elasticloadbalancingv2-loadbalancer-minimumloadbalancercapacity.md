---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticLoadBalancingV2::LoadBalancer MinimumLoadBalancerCapacity
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity"></a>

The minimum capacity for a load balancer.

## Syntax
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-syntax.json"></a>

```
{
  "[CapacityUnits](#cfn-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-capacityunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-syntax.yaml"></a>

```
  [CapacityUnits](#cfn-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-capacityunits): {{Integer}}
```

## Properties
<a name="aws-properties-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-properties"></a>

`CapacityUnits`  <a name="cfn-elasticloadbalancingv2-loadbalancer-minimumloadbalancercapacity-capacityunits"></a>
The number of capacity units.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
