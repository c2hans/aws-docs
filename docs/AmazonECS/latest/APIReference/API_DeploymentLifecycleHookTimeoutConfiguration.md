---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentLifecycleHookTimeoutConfiguration.html
---

# DeploymentLifecycleHookTimeoutConfiguration
<a name="API_DeploymentLifecycleHookTimeoutConfiguration"></a>

The timeout configuration for a deployment lifecycle hook. This determines how long Amazon ECS waits for the hook to complete before taking the specified timeout action.

## Contents
<a name="API_DeploymentLifecycleHookTimeoutConfiguration_Contents"></a>

 ** action **   <a name="ECS-Type-DeploymentLifecycleHookTimeoutConfiguration-action"></a>
The action Amazon ECS takes when the lifecycle hook times out. Valid values are:
+  `CONTINUE` - Proceeds the deployment to the next lifecycle stage.
+  `ROLLBACK` - Rolls back the deployment to the previous service revision.
Default: `ROLLBACK`
Type: String
Valid Values: `ROLLBACK | CONTINUE`
Required: No

 ** timeoutInMinutes **   <a name="ECS-Type-DeploymentLifecycleHookTimeoutConfiguration-timeoutInMinutes"></a>
The number of minutes Amazon ECS waits for the lifecycle hook to complete before taking the timeout action.
Default: 1440 (24 hours)
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20160.
Required: No

## See Also
<a name="API_DeploymentLifecycleHookTimeoutConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeploymentLifecycleHookTimeoutConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeploymentLifecycleHookTimeoutConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeploymentLifecycleHookTimeoutConfiguration)
