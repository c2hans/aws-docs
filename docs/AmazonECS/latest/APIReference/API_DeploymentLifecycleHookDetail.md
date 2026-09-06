---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentLifecycleHookDetail.html
---

# DeploymentLifecycleHookDetail
<a name="API_DeploymentLifecycleHookDetail"></a>

The details of a deployment lifecycle hook that is active during a service deployment.

You can view lifecycle hook details by calling [DescribeServiceDeployments](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeServiceDeployments.html).

## Contents
<a name="API_DeploymentLifecycleHookDetail_Contents"></a>

 ** expiresAt **   <a name="ECS-Type-DeploymentLifecycleHookDetail-expiresAt"></a>
The time when the lifecycle hook times out. If the hook has not been completed by this time, Amazon ECS takes the timeout action.
Type: Timestamp
Required: No

 ** hookId **   <a name="ECS-Type-DeploymentLifecycleHookDetail-hookId"></a>
The ID of the lifecycle hook. Use this value when calling `ContinueServiceDeployment` to continue or roll back a paused deployment.
Type: String
Required: No

 ** status **   <a name="ECS-Type-DeploymentLifecycleHookDetail-status"></a>
The status of the lifecycle hook. Valid values include `AWAITING_ACTION`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, and `TIMED_OUT`.
Type: String
Valid Values: `AWAITING_ACTION | IN_PROGRESS | SUCCEEDED | FAILED | TIMED_OUT`
Required: No

 ** targetArn **   <a name="ECS-Type-DeploymentLifecycleHookDetail-targetArn"></a>
The Amazon Resource Name (ARN) of the hook target. For `AWS_LAMBDA` hooks, this is the Lambda function ARN. For `PAUSE` hooks, this field is not set.
Type: String
Required: No

 ** targetType **   <a name="ECS-Type-DeploymentLifecycleHookDetail-targetType"></a>
The type of action the lifecycle hook performs, such as `AWS_LAMBDA` or `PAUSE`.
Type: String
Valid Values: `AWS_LAMBDA | PAUSE`
Required: No

 ** timeoutAction **   <a name="ECS-Type-DeploymentLifecycleHookDetail-timeoutAction"></a>
The action Amazon ECS takes when the lifecycle hook times out. Valid values are `CONTINUE` and `ROLLBACK`.
Type: String
Valid Values: `ROLLBACK | CONTINUE`
Required: No

## See Also
<a name="API_DeploymentLifecycleHookDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeploymentLifecycleHookDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeploymentLifecycleHookDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeploymentLifecycleHookDetail)
