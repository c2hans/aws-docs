---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DeploymentEarlySuccessCriteria.html
---

# DeploymentEarlySuccessCriteria
<a name="API_DeploymentEarlySuccessCriteria"></a>

**Note**
You can use early success criteria only with rolling deployment strategy.

The configuration that determines when a rolling update deployment is considered successful. Early success criteria defines the percentage of tasks that must be healthy before a deployment completes. It also controls whether Amazon ECS must remove the previous tasks before a deployment completes.

## Contents
<a name="API_DeploymentEarlySuccessCriteria_Contents"></a>

 ** enable **   <a name="ECS-Type-DeploymentEarlySuccessCriteria-enable"></a>
Specifies whether to use the early success criteria for the service deployment. When set to `false`, the deployment uses the default behavior, where Amazon ECS considers the deployment successful when the target service revision fully stabilizes and the previous tasks are removed. The default value is `false`.
When set to `true`, Amazon ECS monitors the deployment to meet early success criteria. You must also specify `healthyPercent` and `sourceServiceRevisionCleanup`.
Type: Boolean
Required: Yes

 ** healthyPercent **   <a name="ECS-Type-DeploymentEarlySuccessCriteria-healthyPercent"></a>
The percentage of healthy tasks that the target service revision must reach before Amazon ECS considers the deployment successful. This percentage is relative to the service's `desiredCount` and must be an integer between `0` and `100`. This value must be greater than or equal to the `minimumHealthyPercent` value.
After this percentage of tasks is healthy and the bake time elapses, Amazon ECS completes the deployment. Amazon ECS continues to scale the target service revision to 100 percent in the background.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** sourceServiceRevisionCleanup **   <a name="ECS-Type-DeploymentEarlySuccessCriteria-sourceServiceRevisionCleanup"></a>
The time when Amazon ECS removes the source revisions' tasks relative to deployment completion. The valid values are:
+  `BLOCKING`—Amazon ECS removes the previous tasks before it marks the deployment as successful.
+  `DEFERRED`—Amazon ECS marks the deployment successful, and then removes the previous tasks in the background.
Type: String
Valid Values: `BLOCKING | DEFERRED`
Required: No

## See Also
<a name="API_DeploymentEarlySuccessCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DeploymentEarlySuccessCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DeploymentEarlySuccessCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DeploymentEarlySuccessCriteria)
