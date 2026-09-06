---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EFSFileSystemConfig.html
---

# EFSFileSystemConfig
<a name="API_EFSFileSystemConfig"></a>

The settings for assigning a custom Amazon EFS file system to a user profile or space for an Amazon SageMaker AI Domain.

## Contents
<a name="API_EFSFileSystemConfig_Contents"></a>

 ** FileSystemId **   <a name="sagemaker-Type-EFSFileSystemConfig-FileSystemId"></a>
The ID of your Amazon EFS file system.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 21.
Pattern: `(fs-[0-9a-f]{8,})`
Required: Yes

 ** FileSystemPath **   <a name="sagemaker-Type-EFSFileSystemConfig-FileSystemPath"></a>
The path to the file system directory that is accessible in Amazon SageMaker AI Studio. Permitted users can access only this directory and below.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\/\S*`
Required: No

## See Also
<a name="API_EFSFileSystemConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EFSFileSystemConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EFSFileSystemConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EFSFileSystemConfig)
