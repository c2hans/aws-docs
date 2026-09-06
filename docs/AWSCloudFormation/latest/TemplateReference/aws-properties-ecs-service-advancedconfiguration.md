---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-advancedconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service AdvancedConfiguration
<a name="aws-properties-ecs-service-advancedconfiguration"></a>

The advanced settings for a load balancer used in blue/green deployments. Specify the alternate target group, listener rules, and IAM role required for traffic shifting during blue/green deployments. For more information, see [Required resources for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-advancedconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-advancedconfiguration-syntax.json"></a>

```
{
  "[AlternateTargetGroupArn](#cfn-ecs-service-advancedconfiguration-alternatetargetgrouparn)" : {{String}},
  "[ProductionListenerRule](#cfn-ecs-service-advancedconfiguration-productionlistenerrule)" : {{String}},
  "[RoleArn](#cfn-ecs-service-advancedconfiguration-rolearn)" : {{String}},
  "[TestListenerRule](#cfn-ecs-service-advancedconfiguration-testlistenerrule)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-advancedconfiguration-syntax.yaml"></a>

```
  [AlternateTargetGroupArn](#cfn-ecs-service-advancedconfiguration-alternatetargetgrouparn): {{String}}
  [ProductionListenerRule](#cfn-ecs-service-advancedconfiguration-productionlistenerrule): {{String}}
  [RoleArn](#cfn-ecs-service-advancedconfiguration-rolearn): {{String}}
  [TestListenerRule](#cfn-ecs-service-advancedconfiguration-testlistenerrule): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-advancedconfiguration-properties"></a>

`AlternateTargetGroupArn`  <a name="cfn-ecs-service-advancedconfiguration-alternatetargetgrouparn"></a>
The Amazon Resource Name (ARN) of the alternate target group for Amazon ECS blue/green deployments.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductionListenerRule`  <a name="cfn-ecs-service-advancedconfiguration-productionlistenerrule"></a>
The Amazon Resource Name (ARN) that that identifies the production listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing production traffic.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ecs-service-advancedconfiguration-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call the Elastic Load Balancing APIs for you.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestListenerRule`  <a name="cfn-ecs-service-advancedconfiguration-testlistenerrule"></a>
The Amazon Resource Name (ARN) that identifies ) that identifies the test listener rule (in the case of an Application Load Balancer) or listener (in the case for an Network Load Balancer) for routing test traffic.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
