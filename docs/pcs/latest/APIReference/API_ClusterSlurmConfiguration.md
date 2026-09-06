---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSlurmConfiguration.html
---

# ClusterSlurmConfiguration
<a name="API_ClusterSlurmConfiguration"></a>

Additional options related to the Slurm scheduler.

## Contents
<a name="API_ClusterSlurmConfiguration_Contents"></a>

 ** accounting **   <a name="PCS-Type-ClusterSlurmConfiguration-accounting"></a>
The accounting configuration includes configurable settings for Slurm accounting.
Type: [Accounting](API_Accounting.md) object
Required: No

 ** authKey **   <a name="PCS-Type-ClusterSlurmConfiguration-authKey"></a>
The shared Slurm key for authentication, also known as the **cluster secret**.
Type: [SlurmAuthKey](API_SlurmAuthKey.md) object
Required: No

 ** cgroupCustomSettings **   <a name="PCS-Type-ClusterSlurmConfiguration-cgroupCustomSettings"></a>
Additional Cgroup-specific configuration that directly maps to Cgroup settings.
Type: Array of [CgroupCustomSetting](API_CgroupCustomSetting.md) objects
Required: No

 ** jwtAuth **   <a name="PCS-Type-ClusterSlurmConfiguration-jwtAuth"></a>
The JWT authentication configuration for Slurm REST API access.
Type: [JwtAuth](API_JwtAuth.md) object
Required: No

 ** scaleDownIdleTimeInSeconds **   <a name="PCS-Type-ClusterSlurmConfiguration-scaleDownIdleTimeInSeconds"></a>
The time (in seconds) before an idle node is scaled down.
Default: `600`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000000.
Required: No

 ** slurmCustomSettings **   <a name="PCS-Type-ClusterSlurmConfiguration-slurmCustomSettings"></a>
Additional Slurm-specific configuration that directly maps to Slurm settings.
Type: Array of [SlurmCustomSetting](API_SlurmCustomSetting.md) objects
Required: No

 ** slurmdbdCustomSettings **   <a name="PCS-Type-ClusterSlurmConfiguration-slurmdbdCustomSettings"></a>
Additional SlurmDBD-specific configuration that directly maps to SlurmDBD settings.
Type: Array of [SlurmdbdCustomSetting](API_SlurmdbdCustomSetting.md) objects
Required: No

 ** slurmRest **   <a name="PCS-Type-ClusterSlurmConfiguration-slurmRest"></a>
The Slurm REST API configuration for the cluster.
Type: [SlurmRest](API_SlurmRest.md) object
Required: No

## See Also
<a name="API_ClusterSlurmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/ClusterSlurmConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/ClusterSlurmConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/ClusterSlurmConfiguration)
