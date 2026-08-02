---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSlurmConfigurationRequest.html
---

# ClusterSlurmConfigurationRequest
<a name="API_ClusterSlurmConfigurationRequest"></a>

Additional options related to the Slurm scheduler.

## Contents
<a name="API_ClusterSlurmConfigurationRequest_Contents"></a>

 ** accounting **   <a name="PCS-Type-ClusterSlurmConfigurationRequest-accounting"></a>
The accounting configuration includes configurable settings for Slurm accounting.
Type: [AccountingRequest](API_AccountingRequest.md) object
Required: No

 ** cgroupCustomSettings **   <a name="PCS-Type-ClusterSlurmConfigurationRequest-cgroupCustomSettings"></a>
Additional Cgroup-specific configuration that directly maps to Cgroup settings.
Type: Array of [CgroupCustomSetting](API_CgroupCustomSetting.md) objects
Required: No

 ** scaleDownIdleTimeInSeconds **   <a name="PCS-Type-ClusterSlurmConfigurationRequest-scaleDownIdleTimeInSeconds"></a>
The time (in seconds) before an idle node is scaled down.
Default: `600`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000000.
Required: No

 ** slurmCustomSettings **   <a name="PCS-Type-ClusterSlurmConfigurationRequest-slurmCustomSettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
Type: Array of [SlurmCustomSetting](API_SlurmCustomSetting.md) objects
Required: No

 ** slurmdbdCustomSettings **   <a name="PCS-Type-ClusterSlurmConfigurationRequest-slurmdbdCustomSettings"></a>
Additional SlurmDBD-specific configuration that directly maps to SlurmDBD settings.
Type: Array of [SlurmdbdCustomSetting](API_SlurmdbdCustomSetting.md) objects
Required: No

 ** slurmRest **   <a name="PCS-Type-ClusterSlurmConfigurationRequest-slurmRest"></a>
The Slurm REST API configuration for the cluster.
Type: [SlurmRestRequest](API_SlurmRestRequest.md) object
Required: No

## See Also
<a name="API_ClusterSlurmConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ClusterSlurmConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ClusterSlurmConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ClusterSlurmConfigurationRequest)
