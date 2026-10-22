---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2DeploymentOptions.html
---

# EC2DeploymentOptions
<a name="API_EC2DeploymentOptions"></a>

Options that control how AWS CodeDeploy manages Amazon EC2 resources during a deployment.

## Contents
<a name="API_EC2DeploymentOptions_Contents"></a>

 ** autoScalingGroupProcessesToSuspend **   <a name="CodeDeploy-Type-EC2DeploymentOptions-autoScalingGroupProcessesToSuspend"></a>
The Amazon EC2 Auto Scaling processes to suspend during the deployment. AWS CodeDeploy suspends these processes before it deploys to instances in an Auto Scaling group, and resumes them when the deployment succeeds, fails, or is stopped. Valid values are `Terminate`, `AZRebalance`, `InstanceRefresh`, and `ScheduledActions`.
This parameter applies only to in-place deployments to Amazon EC2 instances in Auto Scaling groups. If the list is empty, no processes are suspended. If the list isn't empty and the deployment group doesn't use in-place deployments or doesn't include an Auto Scaling group, the request fails with `InvalidAutoScalingGroupProcessToSuspendException`.
The service role for the deployment group must have permission to call `autoscaling:SuspendProcesses` and `autoscaling:ResumeProcesses` on the target Auto Scaling groups. If the processes cannot be suspended, the deployment fails before any instance is updated.
If you suspend `ScheduledActions`, scheduled actions with a start time during the deployment are skipped and do not run after the process resumes.
If CodeDeploy cannot resume the processes, the deployment fails and the processes stay suspended until you resume them with the Auto Scaling `ResumeProcesses` action. While `Terminate` is suspended, Auto Scaling does not replace unhealthy instances. If you suspend `Terminate`, configure a trigger that notifies you when a deployment fails.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Valid Values: `Terminate | AZRebalance | InstanceRefresh | ScheduledActions`
Required: No

## See Also
<a name="API_EC2DeploymentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/EC2DeploymentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/EC2DeploymentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/EC2DeploymentOptions)
