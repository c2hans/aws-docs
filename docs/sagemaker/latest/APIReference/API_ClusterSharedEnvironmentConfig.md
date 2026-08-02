---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterSharedEnvironmentConfig.html
---

# ClusterSharedEnvironmentConfig
<a name="API_ClusterSharedEnvironmentConfig"></a>

The shared environment configuration for the restricted instance groups (RIG).

## Contents
<a name="API_ClusterSharedEnvironmentConfig_Contents"></a>

 ** FSxLustreConfig **   <a name="sagemaker-Type-ClusterSharedEnvironmentConfig-FSxLustreConfig"></a>
Configuration settings for an Amazon FSx for Lustre file system in the shared environment.
Type: [FSxLustreConfig](API_FSxLustreConfig.md) object
Required: Yes

 ** FSxLustreDeletionPolicy **   <a name="sagemaker-Type-ClusterSharedEnvironmentConfig-FSxLustreDeletionPolicy"></a>
The deletion policy for the Amazon FSx for Lustre file system in the shared environment.
Type: String
Valid Values: `DeleteIfNotUsed | Keep`
Required: Yes

## See Also
<a name="API_ClusterSharedEnvironmentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterSharedEnvironmentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterSharedEnvironmentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterSharedEnvironmentConfig)
