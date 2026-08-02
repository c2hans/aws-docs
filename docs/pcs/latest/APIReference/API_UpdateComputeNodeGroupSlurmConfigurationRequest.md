---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateComputeNodeGroupSlurmConfigurationRequest.html
---

# UpdateComputeNodeGroupSlurmConfigurationRequest
<a name="API_UpdateComputeNodeGroupSlurmConfigurationRequest"></a>

Additional options related to the Slurm scheduler.

## Contents
<a name="API_UpdateComputeNodeGroupSlurmConfigurationRequest_Contents"></a>

 ** scaleDownIdleTimeInSeconds **   <a name="PCS-Type-UpdateComputeNodeGroupSlurmConfigurationRequest-scaleDownIdleTimeInSeconds"></a>
The time (in seconds) before an idle node is scaled down. If not specified, the cluster-level setting applies. This overrides the cluster-level `scaleDownIdleTimeInSeconds` setting. A value of `-1` removes the override and applies the cluster-level setting to this compute node group. Requires Slurm version 25.11 or later.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000000.
Required: No

 ** slurmCustomSettings **   <a name="PCS-Type-UpdateComputeNodeGroupSlurmConfigurationRequest-slurmCustomSettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
Type: Array of [SlurmCustomSetting](API_SlurmCustomSetting.md) objects
Required: No

## See Also
<a name="API_UpdateComputeNodeGroupSlurmConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/UpdateComputeNodeGroupSlurmConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/UpdateComputeNodeGroupSlurmConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/UpdateComputeNodeGroupSlurmConfigurationRequest)
