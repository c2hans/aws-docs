---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterAutoPatchConfig.html
---

# ClusterAutoPatchConfig
<a name="API_ClusterAutoPatchConfig"></a>

The configuration for automatic patching of the instance group. When configured, the system automatically applies security patch AMI updates to the instance group.

## Contents
<a name="API_ClusterAutoPatchConfig_Contents"></a>

 ** PatchingStrategy **   <a name="sagemaker-Type-ClusterAutoPatchConfig-PatchingStrategy"></a>
The strategy for applying patches to instances in the group.
+  `WhenIdle`: Cordons all instances and patches each instance as it becomes idle (no running jobs). Each instance is uncordoned immediately after patching and becomes available for new jobs. If instances do not become idle, they remain on the previous AMI version. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.
+  `WhenAllIdle`: Cordons all instances and waits for all to become idle before patching. All instances are uncordoned after patching completes. If not all instances become idle, no patching occurs and all instances remain on the previous AMI version.
Type: String
Valid Values: `WhenIdle | WhenAllIdle`
Required: Yes

 ** DeploymentConfig **   <a name="sagemaker-Type-ClusterAutoPatchConfig-DeploymentConfig"></a>
The deployment configuration for rolling patch updates, including rollback settings and batch sizes. Only applicable when using a rolling patching strategy.
Type: [DeploymentConfiguration](API_DeploymentConfiguration.md) object
Required: No

 ** PatchSchedule **   <a name="sagemaker-Type-ClusterAutoPatchConfig-PatchSchedule"></a>
The schedule for automatic patching, including the next patch date.
Type: [ClusterPatchSchedule](API_ClusterPatchSchedule.md) object
Required: No

## See Also
<a name="API_ClusterAutoPatchConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterAutoPatchConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterAutoPatchConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterAutoPatchConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
