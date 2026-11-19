---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterAutoPatchConfigDetails.html
---

# ClusterAutoPatchConfigDetails

The auto-patching configuration details for the instance group, including the patching strategy and schedule.

## Contents
<a name="API_ClusterAutoPatchConfigDetails_Contents"></a>

 ** CurrentPatchSchedule **   <a name="sagemaker-Type-ClusterAutoPatchConfigDetails-CurrentPatchSchedule"></a>
The currently active patch schedule that the system will execute.
Type: [ClusterPatchScheduleDetails](API_ClusterPatchScheduleDetails.md) object
Required: No

 ** DeploymentConfig **   <a name="sagemaker-Type-ClusterAutoPatchConfigDetails-DeploymentConfig"></a>
The deployment configuration for rolling patch updates.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** DesiredPatchSchedule **   <a name="sagemaker-Type-ClusterAutoPatchConfigDetails-DesiredPatchSchedule"></a>
The requested patch schedule. Differs from CurrentPatchSchedule when a reschedule request is pending.
Type: [ClusterPatchScheduleDetails](API_ClusterPatchScheduleDetails.md) object
Required: No

 ** DrainPolicy **   <a name="sagemaker-Type-ClusterAutoPatchConfigDetails-DrainPolicy"></a>
The policy that controls how pods are evicted from an instance before it is patched. Applies only when `PatchingStrategy` is `DrainFirst`.
Type: [ClusterDrainPolicy](API_ClusterDrainPolicy.md) object
Required: No

 ** IdleWaitWindowInSeconds **   <a name="sagemaker-Type-ClusterAutoPatchConfigDetails-IdleWaitWindowInSeconds"></a>
The maximum time, in seconds, that automatic patching waits for instances to become idle after a scheduled patch starts. Automatic patching uncordons instances that don't become idle within this window, and they remain on the previous AMI version. The default is 86400 (24 hours).
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 2160000.
Required: No

 ** PatchingStrategy **   <a name="sagemaker-Type-ClusterAutoPatchConfigDetails-PatchingStrategy"></a>
The strategy used for applying patches to instances in the group.
+  `WhenIdle`: Cordons all instances and patches each instance as it becomes idle (no running jobs). Each instance is uncordoned immediately after patching and becomes available for new jobs. If instances do not become idle, they remain on the previous AMI version. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.
+  `WhenAllIdle`: Cordons all instances and waits for all to become idle before patching. All instances are uncordoned after patching completes. If not all instances become idle, no patching occurs and all instances remain on the previous AMI version.
+  `DrainFirst`: Designed for workloads that never become idle, such as inference. Cordons instances, evicts the running pods, and then patches each instance in batches. Each instance is uncordoned after patching. Use `DrainPolicy` to control how long to wait for pods to drain and what happens if the drain times out. Requires `MaximumBatchSize` in `DeploymentConfig`. Available only for clusters that use Amazon EKS as the orchestrator.
Type: String
Valid Values: `WhenIdle | WhenAllIdle | DrainFirst`
Required: No

## See Also
<a name="API_ClusterAutoPatchConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterAutoPatchConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterAutoPatchConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterAutoPatchConfigDetails)
