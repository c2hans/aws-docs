---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentLifecycleHook.html
---

# DeploymentLifecycleHook
<a name="API_DeploymentLifecycleHook"></a>

A deployment lifecycle hook runs custom logic or pauses the deployment at specific stages of the deployment process. You can use Lambda functions or pause hooks as hook targets.

For more information, see [Lifecycle hooks for Amazon ECS service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-lifecycle-hooks.html) in the * Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_DeploymentLifecycleHook_Contents"></a>

 ** hookDetails **   <a name="ECS-Type-DeploymentLifecycleHook-hookDetails"></a>
Use this field to specify custom parameters that Amazon ECS passes to your Lambda function on each invocation. This field is not used for `PAUSE` hooks.
Type: JSON value
Required: No

 ** hookTargetArn **   <a name="ECS-Type-DeploymentLifecycleHook-hookTargetArn"></a>
The Amazon Resource Name (ARN) of the hook target. For `AWS_LAMBDA` hooks, this is the Lambda function ARN. This field is not applicable for `PAUSE` hooks.
You must provide this parameter when configuring an `AWS_LAMBDA` lifecycle hook.
Type: String
Required: No

 ** lifecycleStages **   <a name="ECS-Type-DeploymentLifecycleHook-lifecycleStages"></a>
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
Type: Array of strings
Valid Values: `RECONCILE_SERVICE | PRE_SCALE_UP | POST_SCALE_UP | TEST_TRAFFIC_SHIFT | POST_TEST_TRAFFIC_SHIFT | PRE_PRODUCTION_TRAFFIC_SHIFT | PRODUCTION_TRAFFIC_SHIFT | POST_PRODUCTION_TRAFFIC_SHIFT`
Required: No

 ** roleArn **   <a name="ECS-Type-DeploymentLifecycleHook-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon ECS permission to call Lambda functions on your behalf.
For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/blue-green-permissions.html) in the * Amazon Elastic Container Service Developer Guide*.
Type: String
Required: No

 ** targetType **   <a name="ECS-Type-DeploymentLifecycleHook-targetType"></a>
The type of action the lifecycle hook performs. Valid values are:
+  `AWS_LAMBDA` - Invokes a Lambda function at the specified lifecycle stage. This is the default value.
+  `PAUSE` - Pauses the deployment at the specified lifecycle stage until you call `ContinueServiceDeployment` to continue or roll back.
This field is optional. If not specified, the default value is `AWS_LAMBDA`.
Type: String
Valid Values: `AWS_LAMBDA | PAUSE`
Required: No

 ** timeoutConfiguration **   <a name="ECS-Type-DeploymentLifecycleHook-timeoutConfiguration"></a>
The timeout configuration for the lifecycle hook. This specifies how long Amazon ECS waits before taking the timeout action if the hook is not resolved.
Type: [DeploymentLifecycleHookTimeoutConfiguration](API_DeploymentLifecycleHookTimeoutConfiguration.md) object
Required: No

## See Also
<a name="API_DeploymentLifecycleHook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeploymentLifecycleHook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeploymentLifecycleHook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeploymentLifecycleHook)
