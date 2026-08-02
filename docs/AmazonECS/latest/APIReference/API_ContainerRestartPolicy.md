---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerRestartPolicy.html
---

# ContainerRestartPolicy
<a name="API_ContainerRestartPolicy"></a>

You can enable a restart policy for each container defined in your task definition, to overcome transient failures faster and maintain task availability. When you enable a restart policy for a container, Amazon ECS can restart the container if it exits, without needing to replace the task. For more information, see [Restart individual containers in Amazon ECS tasks with container restart policies](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-restart-policy.html) in the *Amazon Elastic Container Service Developer Guide*.

## Contents
<a name="API_ContainerRestartPolicy_Contents"></a>

 ** enabled **   <a name="ECS-Type-ContainerRestartPolicy-enabled"></a>
Specifies whether a restart policy is enabled for the container.
Type: Boolean
Required: Yes

 ** ignoredExitCodes **   <a name="ECS-Type-ContainerRestartPolicy-ignoredExitCodes"></a>
A list of exit codes that Amazon ECS will ignore and not attempt a restart on. You can specify a maximum of 50 container exit codes. By default, Amazon ECS does not ignore any exit codes.
Type: Array of integers
Required: No

 ** restartAttemptPeriod **   <a name="ECS-Type-ContainerRestartPolicy-restartAttemptPeriod"></a>
A period of time (in seconds) that the container must run for before a restart can be attempted. A container can be restarted only once every `restartAttemptPeriod` seconds. If a container isn't able to run for this time period and exits early, it will not be restarted. You can set a minimum `restartAttemptPeriod` of 60 seconds and a maximum `restartAttemptPeriod` of 1800 seconds. By default, a container must run for 300 seconds before it can be restarted.
Type: Integer
Required: No

## See Also
<a name="API_ContainerRestartPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/ContainerRestartPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/ContainerRestartPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/ContainerRestartPolicy)
