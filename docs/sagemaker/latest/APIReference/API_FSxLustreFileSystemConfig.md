---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FSxLustreFileSystemConfig.html
---

# FSxLustreFileSystemConfig
<a name="API_FSxLustreFileSystemConfig"></a>

The settings for assigning a custom Amazon FSx for Lustre file system to a user profile or space for an Amazon SageMaker Domain.

## Contents
<a name="API_FSxLustreFileSystemConfig_Contents"></a>

 ** FileSystemId **   <a name="sagemaker-Type-FSxLustreFileSystemConfig-FileSystemId"></a>
The globally unique, 17-digit, ID of the file system, assigned by Amazon FSx for Lustre.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `(fs-[0-9a-f]{8,})`
Required: Yes

 ** FileSystemPath **   <a name="sagemaker-Type-FSxLustreFileSystemConfig-FileSystemPath"></a>
The path to the file system directory that is accessible in Amazon SageMaker Studio. Permitted users can access only this directory and below.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\/\S*`
Required: No

## See Also
<a name="API_FSxLustreFileSystemConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FSxLustreFileSystemConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FSxLustreFileSystemConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FSxLustreFileSystemConfig)
