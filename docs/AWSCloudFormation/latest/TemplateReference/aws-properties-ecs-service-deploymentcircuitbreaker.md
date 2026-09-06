---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentcircuitbreaker.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service DeploymentCircuitBreaker
<a name="aws-properties-ecs-service-deploymentcircuitbreaker"></a>

**Note**
The deployment circuit breaker can only be used for services using the rolling update (`ECS`) deployment type.

The **deployment circuit breaker** determines whether a service deployment will fail if the service can't reach a steady state. If it is turned on, a service deployment will transition to a failed state and stop launching new tasks. You can also configure Amazon ECS to roll back your service to the last completed deployment after a failure. For more information, see [Rolling update](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-ecs.html) in the *Amazon Elastic Container Service Developer Guide*.

For more information about API failure reasons, see [API failure reasons](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/api_failures_messages.html) in the *Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-deploymentcircuitbreaker-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-deploymentcircuitbreaker-syntax.json"></a>

```
{
  "[Enable](#cfn-ecs-service-deploymentcircuitbreaker-enable)" : {{Boolean}},
  "[ResetOnHealthyTask](#cfn-ecs-service-deploymentcircuitbreaker-resetonhealthytask)" : {{Boolean}},
  "[Rollback](#cfn-ecs-service-deploymentcircuitbreaker-rollback)" : {{Boolean}},
  "[ThresholdConfiguration](#cfn-ecs-service-deploymentcircuitbreaker-thresholdconfiguration)" : {{ThresholdConfiguration}}
}
```

### YAML
<a name="aws-properties-ecs-service-deploymentcircuitbreaker-syntax.yaml"></a>

```
  [Enable](#cfn-ecs-service-deploymentcircuitbreaker-enable): {{Boolean}}
  [ResetOnHealthyTask](#cfn-ecs-service-deploymentcircuitbreaker-resetonhealthytask): {{Boolean}}
  [Rollback](#cfn-ecs-service-deploymentcircuitbreaker-rollback): {{Boolean}}
  [ThresholdConfiguration](#cfn-ecs-service-deploymentcircuitbreaker-thresholdconfiguration): {{
    ThresholdConfiguration}}
```

## Properties
<a name="aws-properties-ecs-service-deploymentcircuitbreaker-properties"></a>

`Enable`  <a name="cfn-ecs-service-deploymentcircuitbreaker-enable"></a>
Determines whether to use the deployment circuit breaker logic for the service.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResetOnHealthyTask`  <a name="cfn-ecs-service-deploymentcircuitbreaker-resetonhealthytask"></a>
Specifies whether the deployment circuit breaker resets its failure count when a task reaches a healthy state. When set to `true`, a task that reaches a healthy state resets the failure count to `0`. When set to `false`, Amazon ECS does not reset the failure count. The default is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rollback`  <a name="cfn-ecs-service-deploymentcircuitbreaker-rollback"></a>
Determines whether to configure Amazon ECS to roll back the service if a service deployment fails. If rollback is on, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThresholdConfiguration`  <a name="cfn-ecs-service-deploymentcircuitbreaker-thresholdconfiguration"></a>
The threshold configuration that controls when the deployment circuit breaker triggers. The `type` and `value` together determine how many task failures are tolerated before the circuit breaker activates.
*Required*: No
*Type*: [ThresholdConfiguration](aws-properties-ecs-service-thresholdconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-ecs-service-deploymentcircuitbreaker--seealso"></a>
+  [Associate an Application Load Balancer with a service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html#aws-resource-ecs-service--examples--Associate_an_Application_Load_Balancer_with_a_service)
