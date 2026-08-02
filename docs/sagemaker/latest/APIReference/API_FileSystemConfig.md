---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FileSystemConfig.html
---

# FileSystemConfig
<a name="API_FileSystemConfig"></a>

The Amazon Elastic File System storage configuration for a SageMaker AI image.

## Contents
<a name="API_FileSystemConfig_Contents"></a>

 ** DefaultGid **   <a name="sagemaker-Type-FileSystemConfig-DefaultGid"></a>
The default POSIX group ID (GID). If not specified, defaults to `100`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** DefaultUid **   <a name="sagemaker-Type-FileSystemConfig-DefaultUid"></a>
The default POSIX user ID (UID). If not specified, defaults to `1000`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.
Required: No

 ** MountPath **   <a name="sagemaker-Type-FileSystemConfig-MountPath"></a>
The path within the image to mount the user's EFS home directory. The directory should be empty. If not specified, defaults to */home/sagemaker-user*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\/.*`
Required: No

## See Also
<a name="API_FileSystemConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/FileSystemConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/FileSystemConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/FileSystemConfig)
