---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-ingresspatharns.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService IngressPathArns
<a name="aws-properties-ecs-expressgatewayservice-ingresspatharns"></a>

<a name="aws-properties-ecs-expressgatewayservice-ingresspatharns-description"></a>The `IngressPathArns` property type specifies Property description not available. for an [AWS::ECS::ExpressGatewayService](aws-resource-ecs-expressgatewayservice.md).

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-ingresspatharns-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-ingresspatharns-syntax.json"></a>

```
{
  "[CertificateArn](#cfn-ecs-expressgatewayservice-ingresspatharns-certificatearn)" : {{String}},
  "[ListenerArn](#cfn-ecs-expressgatewayservice-ingresspatharns-listenerarn)" : {{String}},
  "[ListenerRuleArn](#cfn-ecs-expressgatewayservice-ingresspatharns-listenerrulearn)" : {{String}},
  "[LoadBalancerArn](#cfn-ecs-expressgatewayservice-ingresspatharns-loadbalancerarn)" : {{String}},
  "[LoadBalancerSecurityGroups](#cfn-ecs-expressgatewayservice-ingresspatharns-loadbalancersecuritygroups)" : {{[ String, ... ]}},
  "[TargetGroupArns](#cfn-ecs-expressgatewayservice-ingresspatharns-targetgrouparns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-ingresspatharns-syntax.yaml"></a>

```
  [CertificateArn](#cfn-ecs-expressgatewayservice-ingresspatharns-certificatearn): {{String}}
  [ListenerArn](#cfn-ecs-expressgatewayservice-ingresspatharns-listenerarn): {{String}}
  [ListenerRuleArn](#cfn-ecs-expressgatewayservice-ingresspatharns-listenerrulearn): {{String}}
  [LoadBalancerArn](#cfn-ecs-expressgatewayservice-ingresspatharns-loadbalancerarn): {{String}}
  [LoadBalancerSecurityGroups](#cfn-ecs-expressgatewayservice-ingresspatharns-loadbalancersecuritygroups): {{
    - String}}
  [TargetGroupArns](#cfn-ecs-expressgatewayservice-ingresspatharns-targetgrouparns): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-ingresspatharns-properties"></a>

`CertificateArn`  <a name="cfn-ecs-expressgatewayservice-ingresspatharns-certificatearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListenerArn`  <a name="cfn-ecs-expressgatewayservice-ingresspatharns-listenerarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListenerRuleArn`  <a name="cfn-ecs-expressgatewayservice-ingresspatharns-listenerrulearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadBalancerArn`  <a name="cfn-ecs-expressgatewayservice-ingresspatharns-loadbalancerarn"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadBalancerSecurityGroups`  <a name="cfn-ecs-expressgatewayservice-ingresspatharns-loadbalancersecuritygroups"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetGroupArns`  <a name="cfn-ecs-expressgatewayservice-ingresspatharns-targetgrouparns"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
