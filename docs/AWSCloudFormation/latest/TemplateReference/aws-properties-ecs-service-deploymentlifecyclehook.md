---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-service-deploymentlifecyclehook.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::Service DeploymentLifecycleHook
<a name="aws-properties-ecs-service-deploymentlifecyclehook"></a>

A deployment lifecycle hook runs custom logic or pauses the deployment at specific stages of the deployment process. You can use Lambda functions or pause hooks as hook targets.

For more information, see [Lifecycle hooks for Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-lifecycle-hooks.html) in the * Amazon Elastic Container Service Developer Guide*.

## Syntax
<a name="aws-properties-ecs-service-deploymentlifecyclehook-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-service-deploymentlifecyclehook-syntax.json"></a>

```
{
  "[HookDetails](#cfn-ecs-service-deploymentlifecyclehook-hookdetails)" : {{Json}},
  "[HookTargetArn](#cfn-ecs-service-deploymentlifecyclehook-hooktargetarn)" : {{String}},
  "[LifecycleStages](#cfn-ecs-service-deploymentlifecyclehook-lifecyclestages)" : {{[ String, ... ]}},
  "[RoleArn](#cfn-ecs-service-deploymentlifecyclehook-rolearn)" : {{String}},
  "[TargetType](#cfn-ecs-service-deploymentlifecyclehook-targettype)" : {{String}},
  "[TimeoutConfiguration](#cfn-ecs-service-deploymentlifecyclehook-timeoutconfiguration)" : {{HookTimeoutConfig}}
}
```

### YAML
<a name="aws-properties-ecs-service-deploymentlifecyclehook-syntax.yaml"></a>

```
  [HookDetails](#cfn-ecs-service-deploymentlifecyclehook-hookdetails): {{Json}}
  [HookTargetArn](#cfn-ecs-service-deploymentlifecyclehook-hooktargetarn): {{String}}
  [LifecycleStages](#cfn-ecs-service-deploymentlifecyclehook-lifecyclestages): {{
    - String}}
  [RoleArn](#cfn-ecs-service-deploymentlifecyclehook-rolearn): {{String}}
  [TargetType](#cfn-ecs-service-deploymentlifecyclehook-targettype): {{String}}
  [TimeoutConfiguration](#cfn-ecs-service-deploymentlifecyclehook-timeoutconfiguration): {{
    HookTimeoutConfig}}
```

## Properties
<a name="aws-properties-ecs-service-deploymentlifecyclehook-properties"></a>

`HookDetails`  <a name="cfn-ecs-service-deploymentlifecyclehook-hookdetails"></a>
 Use this field to specify custom parameters that Amazon ECS passes to your hook target invocations (such as a Lambda function).
This field must be a JSON object as a string.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HookTargetArn`  <a name="cfn-ecs-service-deploymentlifecyclehook-hooktargetarn"></a>
The Amazon Resource Name (ARN) of the hook target. For `AWS_LAMBDA` hooks, this is the Lambda function ARN. This field is not applicable for `PAUSE` hooks.
You must provide this parameter when configuring an `AWS_LAMBDA` lifecycle hook.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LifecycleStages`  <a name="cfn-ecs-service-deploymentlifecyclehook-lifecyclestages"></a>
The lifecycle stages at which to run the hook. Choose from these valid values:
+ RECONCILE\_SERVICE

  The reconciliation stage that only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state.

  You can use a lifecycle hook for this stage.
+ PRE\_SCALE\_UP

  The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic.

  You can use a lifecycle hook for this stage.
+ POST\_SCALE\_UP

  The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic.

  You can use a lifecycle hook for this stage.
+ TEST\_TRAFFIC\_SHIFT

  The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic.

  You can use a lifecycle hook for this stage.
+ POST\_TEST\_TRAFFIC\_SHIFT

  The test traffic shift is complete. The green service revision handles 100% of the test traffic.

  You can use a lifecycle hook for this stage.
+ PRE\_PRODUCTION\_TRAFFIC\_SHIFT

  Occurs before production traffic shift. For linear and canary deployments, this stage is invoked before every traffic shift step.

  You can use a lifecycle hook for this stage.
+ PRODUCTION\_TRAFFIC\_SHIFT

  Production traffic is shifting to the green service revision. The green service revision is migrating from 0% to 100% of production traffic. For linear and canary deployments, this stage is invoked at every traffic shift step.

  You can use a lifecycle hook for this stage.
+ POST\_PRODUCTION\_TRAFFIC\_SHIFT

  The production traffic shift is complete.

  You can use a lifecycle hook for this stage.
`PAUSE` hooks cannot be configured at `TEST_TRAFFIC_SHIFT` or `PRODUCTION_TRAFFIC_SHIFT` stages. These stages are only valid for `AWS_LAMBDA` hooks.
You must provide this parameter when configuring a deployment lifecycle hook.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `RECONCILE_SERVICE | PRE_SCALE_UP | POST_SCALE_UP | TEST_TRAFFIC_SHIFT | POST_TEST_TRAFFIC_SHIFT | PRE_PRODUCTION_TRAFFIC_SHIFT | PRODUCTION_TRAFFIC_SHIFT | POST_PRODUCTION_TRAFFIC_SHIFT`
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ecs-service-deploymentlifecyclehook-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call Lambda functions on your behalf.
For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-permissions.html) in the * Amazon Elastic Container Service Developer Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetType`  <a name="cfn-ecs-service-deploymentlifecyclehook-targettype"></a>
The type of action the lifecycle hook performs. Valid values are:
+ `AWS_LAMBDA` - Invokes a Lambda function at the specified lifecycle stage. This is the default value.
+ `PAUSE` - Pauses the deployment at the specified lifecycle stage until you call `ContinueServiceDeployment` to continue or roll back.
This field is optional. If not specified, the default value is `AWS_LAMBDA`.
*Required*: No
*Type*: String
*Allowed values*: `AWS_LAMBDA | PAUSE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutConfiguration`  <a name="cfn-ecs-service-deploymentlifecyclehook-timeoutconfiguration"></a>
The timeout configuration for the lifecycle hook. This specifies how long Amazon ECS waits before taking the timeout action if the hook is not resolved.
*Required*: No
*Type*: [HookTimeoutConfig](aws-properties-ecs-service-hooktimeoutconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
