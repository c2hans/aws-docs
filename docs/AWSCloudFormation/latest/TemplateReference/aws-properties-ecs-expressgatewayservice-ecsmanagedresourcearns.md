---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::ExpressGatewayService ECSManagedResourceArns
<a name="aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns"></a>

<a name="aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns-description"></a>The `ECSManagedResourceArns` property type specifies Property description not available. for an [AWS::ECS::ExpressGatewayService](aws-resource-ecs-expressgatewayservice.md).

## Syntax
<a name="aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns-syntax.json"></a>

```
{
  "[AutoScaling](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-autoscaling)" : {{AutoScalingArns}},
  "[IngressPath](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-ingresspath)" : {{IngressPathArns}},
  "[LogGroups](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-loggroups)" : {{[ String, ... ]}},
  "[MetricAlarms](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-metricalarms)" : {{[ String, ... ]}},
  "[ServiceSecurityGroups](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-servicesecuritygroups)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns-syntax.yaml"></a>

```
  [AutoScaling](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-autoscaling): {{
    AutoScalingArns}}
  [IngressPath](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-ingresspath): {{
    IngressPathArns}}
  [LogGroups](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-loggroups): {{
    - String}}
  [MetricAlarms](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-metricalarms): {{
    - String}}
  [ServiceSecurityGroups](#cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-servicesecuritygroups): {{
    - String}}
```

## Properties
<a name="aws-properties-ecs-expressgatewayservice-ecsmanagedresourcearns-properties"></a>

`AutoScaling`  <a name="cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-autoscaling"></a>
Property description not available.
*Required*: No
*Type*: [AutoScalingArns](aws-properties-ecs-expressgatewayservice-autoscalingarns.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IngressPath`  <a name="cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-ingresspath"></a>
Property description not available.
*Required*: No
*Type*: [IngressPathArns](aws-properties-ecs-expressgatewayservice-ingresspatharns.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogGroups`  <a name="cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-loggroups"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricAlarms`  <a name="cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-metricalarms"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceSecurityGroups`  <a name="cfn-ecs-expressgatewayservice-ecsmanagedresourcearns-servicesecuritygroups"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
