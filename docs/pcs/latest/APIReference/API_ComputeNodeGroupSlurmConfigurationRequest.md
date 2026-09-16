---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroupSlurmConfigurationRequest.html
---

# ComputeNodeGroupSlurmConfigurationRequest
<a name="API_ComputeNodeGroupSlurmConfigurationRequest"></a>

Additional options related to the Slurm scheduler.

## Contents
<a name="API_ComputeNodeGroupSlurmConfigurationRequest_Contents"></a>

 ** gresCustomSettings **   <a name="PCS-Type-ComputeNodeGroupSlurmConfigurationRequest-gresCustomSettings"></a>
The additional Slurm `gres.conf` records for the compute node group. Each item is a map of `gres.conf` attribute names to values that describes one `gres.conf` record, such as a GPU topology, MIG, MPS, or custom GRES entry. AWS PCS adds the `NodeName=` prefix and merges these records with the GPU record it derives from the instance type.
Type: Array of string to string maps
Required: No

 ** scaleDownIdleTimeInSeconds **   <a name="PCS-Type-ComputeNodeGroupSlurmConfigurationRequest-scaleDownIdleTimeInSeconds"></a>
The time (in seconds) before an idle node is scaled down. If not specified, the cluster-level setting applies. This overrides the cluster-level `scaleDownIdleTimeInSeconds` setting. A value of `-1` removes the override and applies the cluster-level setting to this compute node group. Requires Slurm version 25.11 or later.
Type: Integer
Valid Range: Minimum value of -1. Maximum value of 10000000.
Required: No

 ** slurmCustomSettings **   <a name="PCS-Type-ComputeNodeGroupSlurmConfigurationRequest-slurmCustomSettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
Type: Array of [SlurmCustomSetting](API_SlurmCustomSetting.md) objects
Required: No

## See Also
<a name="API_ComputeNodeGroupSlurmConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ComputeNodeGroupSlurmConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ComputeNodeGroupSlurmConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ComputeNodeGroupSlurmConfigurationRequest)
