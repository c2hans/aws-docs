---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CustomFileSystemConfig.html
---

# CustomFileSystemConfig
<a name="API_CustomFileSystemConfig"></a>

The settings for assigning a custom file system to a user profile or space for an Amazon SageMaker AI Domain. Permitted users can access this file system in Amazon SageMaker AI Studio.

## Contents
<a name="API_CustomFileSystemConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** EFSFileSystemConfig **   <a name="sagemaker-Type-CustomFileSystemConfig-EFSFileSystemConfig"></a>
The settings for a custom Amazon EFS file system.
Type: [EFSFileSystemConfig](API_EFSFileSystemConfig.md) object
Required: No

 ** FSxLustreFileSystemConfig **   <a name="sagemaker-Type-CustomFileSystemConfig-FSxLustreFileSystemConfig"></a>
The settings for a custom Amazon FSx for Lustre file system.
Type: [FSxLustreFileSystemConfig](API_FSxLustreFileSystemConfig.md) object
Required: No

 ** S3FileSystemConfig **   <a name="sagemaker-Type-CustomFileSystemConfig-S3FileSystemConfig"></a>
Configuration settings for a custom Amazon S3 file system.
Type: [S3FileSystemConfig](API_S3FileSystemConfig.md) object
Required: No

## See Also
<a name="API_CustomFileSystemConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CustomFileSystemConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CustomFileSystemConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CustomFileSystemConfig)
