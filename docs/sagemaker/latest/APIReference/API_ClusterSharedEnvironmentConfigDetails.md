---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterSharedEnvironmentConfigDetails.html
---

# ClusterSharedEnvironmentConfigDetails
<a name="API_ClusterSharedEnvironmentConfigDetails"></a>

The shared environment configuration details for the restricted instance groups (RIG).

## Contents
<a name="API_ClusterSharedEnvironmentConfigDetails_Contents"></a>

 ** CurrentFSxLustreConfig **   <a name="sagemaker-Type-ClusterSharedEnvironmentConfigDetails-CurrentFSxLustreConfig"></a>
The current Amazon FSx for Lustre file system configuration in the shared environment.
Type: [FSxLustreConfig](API_FSxLustreConfig.md) object
Required: No

 ** CurrentFSxLustreDeletionPolicy **   <a name="sagemaker-Type-ClusterSharedEnvironmentConfigDetails-CurrentFSxLustreDeletionPolicy"></a>
The current deletion policy for the Amazon FSx for Lustre file system in the shared environment.
Type: String
Valid Values: `DeleteIfNotUsed | Keep`
Required: No

 ** DesiredFSxLustreConfig **   <a name="sagemaker-Type-ClusterSharedEnvironmentConfigDetails-DesiredFSxLustreConfig"></a>
The desired Amazon FSx for Lustre file system configuration in the shared environment.
Type: [FSxLustreConfig](API_FSxLustreConfig.md) object
Required: No

 ** DesiredFSxLustreDeletionPolicy **   <a name="sagemaker-Type-ClusterSharedEnvironmentConfigDetails-DesiredFSxLustreDeletionPolicy"></a>
The desired deletion policy for the Amazon FSx for Lustre file system in the shared environment.
Type: String
Valid Values: `DeleteIfNotUsed | Keep`
Required: No

## See Also
<a name="API_ClusterSharedEnvironmentConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterSharedEnvironmentConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterSharedEnvironmentConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterSharedEnvironmentConfigDetails)
