---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DefaultSpaceSettings.html
---

# DefaultSpaceSettings
<a name="API_DefaultSpaceSettings"></a>

The default settings for shared spaces that users create in the domain.

SageMaker applies these settings only to shared spaces. It doesn't apply them to private spaces.

## Contents
<a name="API_DefaultSpaceSettings_Contents"></a>

 ** CustomFileSystemConfigs **   <a name="sagemaker-Type-DefaultSpaceSettings-CustomFileSystemConfigs"></a>
The settings for assigning a custom file system to a domain. Permitted users can access this file system in Amazon SageMaker AI Studio.
Type: Array of [CustomFileSystemConfig](API_CustomFileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** CustomPosixUserConfig **   <a name="sagemaker-Type-DefaultSpaceSettings-CustomPosixUserConfig"></a>
Details about the POSIX identity that is used for file system operations.
Type: [CustomPosixUserConfig](API_CustomPosixUserConfig.md) object
Required: No

 ** ExecutionRole **   <a name="sagemaker-Type-DefaultSpaceSettings-ExecutionRole"></a>
The ARN of the execution role for the space.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** JupyterLabAppSettings **   <a name="sagemaker-Type-DefaultSpaceSettings-JupyterLabAppSettings"></a>
The settings for the JupyterLab application.
Type: [JupyterLabAppSettings](API_JupyterLabAppSettings.md) object
Required: No

 ** JupyterServerAppSettings **   <a name="sagemaker-Type-DefaultSpaceSettings-JupyterServerAppSettings"></a>
The JupyterServer app settings.
Type: [JupyterServerAppSettings](API_JupyterServerAppSettings.md) object
Required: No

 ** KernelGatewayAppSettings **   <a name="sagemaker-Type-DefaultSpaceSettings-KernelGatewayAppSettings"></a>
The KernelGateway app settings.
Type: [KernelGatewayAppSettings](API_KernelGatewayAppSettings.md) object
Required: No

 ** SecurityGroups **   <a name="sagemaker-Type-DefaultSpaceSettings-SecurityGroups"></a>
The security group IDs for the Amazon VPC that the space uses for communication.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** SpaceStorageSettings **   <a name="sagemaker-Type-DefaultSpaceSettings-SpaceStorageSettings"></a>
The default storage settings for a space.
Type: [DefaultSpaceStorageSettings](API_DefaultSpaceStorageSettings.md) object
Required: No

## See Also
<a name="API_DefaultSpaceSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DefaultSpaceSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DefaultSpaceSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DefaultSpaceSettings)
