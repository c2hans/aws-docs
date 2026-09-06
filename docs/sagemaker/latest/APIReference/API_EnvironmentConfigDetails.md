---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EnvironmentConfigDetails.html
---

# EnvironmentConfigDetails
<a name="API_EnvironmentConfigDetails"></a>

The configuration details for the restricted instance groups (RIG) environment.

## Contents
<a name="API_EnvironmentConfigDetails_Contents"></a>

 ** FSxLustreConfig **   <a name="sagemaker-Type-EnvironmentConfigDetails-FSxLustreConfig"></a>
Configuration settings for an Amazon FSx for Lustre file system to be used with the cluster.
Type: [FSxLustreConfig](API_FSxLustreConfig.md) object
Required: No

 ** S3OutputPath **   <a name="sagemaker-Type-EnvironmentConfigDetails-S3OutputPath"></a>
The Amazon S3 path where output data from the restricted instance group (RIG) environment will be stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_EnvironmentConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EnvironmentConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EnvironmentConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EnvironmentConfigDetails)
