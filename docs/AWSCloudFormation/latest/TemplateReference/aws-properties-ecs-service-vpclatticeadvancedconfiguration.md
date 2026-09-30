---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-vpclatticeadvancedconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service VpcLatticeAdvancedConfiguration
<a name="aws-properties-ecs-service-vpclatticeadvancedconfiguration"></a>

The advanced settings for VPC Lattice used in blue/green deployments. Specify the alternate target group and listener rules required for traffic shifting during blue/green deployments. For more information, see [Required resources for Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-deployment-implementation.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-vpclatticeadvancedconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-vpclatticeadvancedconfiguration-syntax.json"></a>

```
{
  "[AlternateTargetGroupArn](#cfn-ecs-service-vpclatticeadvancedconfiguration-alternatetargetgrouparn)" : {{String}},
  "[ProductionListenerRule](#cfn-ecs-service-vpclatticeadvancedconfiguration-productionlistenerrule)" : {{String}},
  "[TestListenerRule](#cfn-ecs-service-vpclatticeadvancedconfiguration-testlistenerrule)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-service-vpclatticeadvancedconfiguration-syntax.yaml"></a>

```
  [AlternateTargetGroupArn](#cfn-ecs-service-vpclatticeadvancedconfiguration-alternatetargetgrouparn): {{String}}
  [ProductionListenerRule](#cfn-ecs-service-vpclatticeadvancedconfiguration-productionlistenerrule): {{String}}
  [TestListenerRule](#cfn-ecs-service-vpclatticeadvancedconfiguration-testlistenerrule): {{String}}
```

## Properties
<a name="aws-properties-ecs-service-vpclatticeadvancedconfiguration-properties"></a>

`AlternateTargetGroupArn`  <a name="cfn-ecs-service-vpclatticeadvancedconfiguration-alternatetargetgrouparn"></a>
The Amazon Resource Name (ARN) of the alternate target group associated with the VPC Lattice Configuration for Amazon ECS blue/green deployments.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProductionListenerRule`  <a name="cfn-ecs-service-vpclatticeadvancedconfiguration-productionlistenerrule"></a>
The Amazon Resource Name (ARN) that identifies the production listener rule or listener for routing production traffic.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TestListenerRule`  <a name="cfn-ecs-service-vpclatticeadvancedconfiguration-testlistenerrule"></a>
The Amazon Resource Name (ARN) that identifies the test listener rule or listener for routing test traffic.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
