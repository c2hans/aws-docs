---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UserSettings.html
---

# UserSettings
<a name="API_UserSettings"></a>

A collection of settings that apply to users in a domain. These settings are specified when the `CreateUserProfile` API is called, and as `DefaultUserSettings` when the `CreateDomain` API is called.

 `SecurityGroups` is aggregated when specified in both calls. For all other settings in `UserSettings`, the values specified in `CreateUserProfile` take precedence over those specified in `CreateDomain`.

## Contents
<a name="API_UserSettings_Contents"></a>

 ** AutoMountHomeEFS **   <a name="sagemaker-Type-UserSettings-AutoMountHomeEFS"></a>
Indicates whether auto-mounting of an EFS volume is supported for the user profile. The `DefaultAsDomain` value is only supported for user profiles. Do not use the `DefaultAsDomain` value when setting this parameter for a domain.
SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesn't apply this setting to shared spaces.
Type: String
Valid Values: `Enabled | Disabled | DefaultAsDomain`
Required: No

 ** CanvasAppSettings **   <a name="sagemaker-Type-UserSettings-CanvasAppSettings"></a>
The Canvas app settings.
SageMaker applies these settings only to private spaces that SageMaker creates for the Canvas app.
Type: [CanvasAppSettings](API_CanvasAppSettings.md) object
Required: No

 ** CodeEditorAppSettings **   <a name="sagemaker-Type-UserSettings-CodeEditorAppSettings"></a>
The Code Editor application settings.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
Type: [CodeEditorAppSettings](API_CodeEditorAppSettings.md) object
Required: No

 ** CustomFileSystemConfigs **   <a name="sagemaker-Type-UserSettings-CustomFileSystemConfigs"></a>
The settings for assigning a custom file system to a user profile. Permitted users can access this file system in Amazon SageMaker AI Studio.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
Type: Array of [CustomFileSystemConfig](API_CustomFileSystemConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** CustomPosixUserConfig **   <a name="sagemaker-Type-UserSettings-CustomPosixUserConfig"></a>
Details about the POSIX identity that is used for file system operations.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
Type: [CustomPosixUserConfig](API_CustomPosixUserConfig.md) object
Required: No

 ** DefaultLandingUri **   <a name="sagemaker-Type-UserSettings-DefaultLandingUri"></a>
The default experience that the user is directed to when accessing the domain. The supported values are:
+  `studio::`: Indicates that Studio is the default experience. This value can only be passed if `StudioWebPortal` is set to `ENABLED`.
+  `app:JupyterServer:`: Indicates that Studio Classic is the default experience.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1023.
Required: No

 ** ExecutionRole **   <a name="sagemaker-Type-UserSettings-ExecutionRole"></a>
The execution role for the user.
SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesn't apply this setting to shared spaces.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** JupyterLabAppSettings **   <a name="sagemaker-Type-UserSettings-JupyterLabAppSettings"></a>
The settings for the JupyterLab application.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
Type: [JupyterLabAppSettings](API_JupyterLabAppSettings.md) object
Required: No

 ** JupyterServerAppSettings **   <a name="sagemaker-Type-UserSettings-JupyterServerAppSettings"></a>
The Jupyter server's app settings.
Type: [JupyterServerAppSettings](API_JupyterServerAppSettings.md) object
Required: No

 ** KernelGatewayAppSettings **   <a name="sagemaker-Type-UserSettings-KernelGatewayAppSettings"></a>
The kernel gateway app settings.
Type: [KernelGatewayAppSettings](API_KernelGatewayAppSettings.md) object
Required: No

 ** RSessionAppSettings **   <a name="sagemaker-Type-UserSettings-RSessionAppSettings"></a>
A collection of settings that configure the `RSessionGateway` app.
Type: [RSessionAppSettings](API_RSessionAppSettings.md) object
Required: No

 ** RStudioServerProAppSettings **   <a name="sagemaker-Type-UserSettings-RStudioServerProAppSettings"></a>
A collection of settings that configure user interaction with the `RStudioServerPro` app.
Type: [RStudioServerProAppSettings](API_RStudioServerProAppSettings.md) object
Required: No

 ** SecurityGroups **   <a name="sagemaker-Type-UserSettings-SecurityGroups"></a>
The security groups for the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.
Optional when the `CreateDomain.AppNetworkAccessType` parameter is set to `PublicInternetOnly`.
Required when the `CreateDomain.AppNetworkAccessType` parameter is set to `VpcOnly`, unless specified as part of the `DefaultUserSettings` for the domain.
Amazon SageMaker AI adds a security group to allow NFS traffic from Amazon SageMaker AI Studio. Therefore, the number of security groups that you can specify is one less than the maximum number shown.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-0-9a-zA-Z]+`
Required: No

 ** SharingSettings **   <a name="sagemaker-Type-UserSettings-SharingSettings"></a>
Specifies options for sharing Amazon SageMaker AI Studio notebooks.
Type: [SharingSettings](API_SharingSettings.md) object
Required: No

 ** SpaceStorageSettings **   <a name="sagemaker-Type-UserSettings-SpaceStorageSettings"></a>
The storage settings for a space.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
Type: [DefaultSpaceStorageSettings](API_DefaultSpaceStorageSettings.md) object
Required: No

 ** StudioWebPortal **   <a name="sagemaker-Type-UserSettings-StudioWebPortal"></a>
Whether the user can access Studio. If this value is set to `DISABLED`, the user cannot access Studio, even if that is the default experience for the domain.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** StudioWebPortalSettings **   <a name="sagemaker-Type-UserSettings-StudioWebPortalSettings"></a>
Studio settings. If these settings are applied on a user level, they take priority over the settings applied on a domain level.
Type: [StudioWebPortalSettings](API_StudioWebPortalSettings.md) object
Required: No

 ** TensorBoardAppSettings **   <a name="sagemaker-Type-UserSettings-TensorBoardAppSettings"></a>
The TensorBoard app settings.
Type: [TensorBoardAppSettings](API_TensorBoardAppSettings.md) object
Required: No

## See Also
<a name="API_UserSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UserSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UserSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UserSettings)
