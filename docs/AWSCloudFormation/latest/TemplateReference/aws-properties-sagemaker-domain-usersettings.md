---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-domain-usersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Domain UserSettings
<a name="aws-properties-sagemaker-domain-usersettings"></a>

A collection of settings that apply to users of Amazon SageMaker Studio. These settings are specified when the [CreateUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateUserProfile.html) API is called, and as `DefaultUserSettings` when the [CreateDomain](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateDomain.html) API is called.

`SecurityGroups` is aggregated when specified in both calls. For all other settings in `UserSettings`, the values specified in `CreateUserProfile` take precedence over those specified in `CreateDomain`.

## Syntax
<a name="aws-properties-sagemaker-domain-usersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-domain-usersettings-syntax.json"></a>

```
{
  "[AutoMountHomeEFS](#cfn-sagemaker-domain-usersettings-automounthomeefs)" : {{String}},
  "[CodeEditorAppSettings](#cfn-sagemaker-domain-usersettings-codeeditorappsettings)" : {{CodeEditorAppSettings}},
  "[CustomFileSystemConfigs](#cfn-sagemaker-domain-usersettings-customfilesystemconfigs)" : {{[ CustomFileSystemConfig, ... ]}},
  "[CustomPosixUserConfig](#cfn-sagemaker-domain-usersettings-customposixuserconfig)" : {{CustomPosixUserConfig}},
  "[DefaultLandingUri](#cfn-sagemaker-domain-usersettings-defaultlandinguri)" : {{String}},
  "[ExecutionRole](#cfn-sagemaker-domain-usersettings-executionrole)" : {{String}},
  "[JupyterLabAppSettings](#cfn-sagemaker-domain-usersettings-jupyterlabappsettings)" : {{JupyterLabAppSettings}},
  "[JupyterServerAppSettings](#cfn-sagemaker-domain-usersettings-jupyterserverappsettings)" : {{JupyterServerAppSettings}},
  "[KernelGatewayAppSettings](#cfn-sagemaker-domain-usersettings-kernelgatewayappsettings)" : {{KernelGatewayAppSettings}},
  "[RSessionAppSettings](#cfn-sagemaker-domain-usersettings-rsessionappsettings)" : {{RSessionAppSettings}},
  "[RStudioServerProAppSettings](#cfn-sagemaker-domain-usersettings-rstudioserverproappsettings)" : {{RStudioServerProAppSettings}},
  "[SecurityGroups](#cfn-sagemaker-domain-usersettings-securitygroups)" : {{[ String, ... ]}},
  "[SharingSettings](#cfn-sagemaker-domain-usersettings-sharingsettings)" : {{SharingSettings}},
  "[SpaceStorageSettings](#cfn-sagemaker-domain-usersettings-spacestoragesettings)" : {{DefaultSpaceStorageSettings}},
  "[StudioWebPortal](#cfn-sagemaker-domain-usersettings-studiowebportal)" : {{String}},
  "[StudioWebPortalSettings](#cfn-sagemaker-domain-usersettings-studiowebportalsettings)" : {{StudioWebPortalSettings}}
}
```

### YAML
<a name="aws-properties-sagemaker-domain-usersettings-syntax.yaml"></a>

```
  [AutoMountHomeEFS](#cfn-sagemaker-domain-usersettings-automounthomeefs): {{String}}
  [CodeEditorAppSettings](#cfn-sagemaker-domain-usersettings-codeeditorappsettings): {{
    CodeEditorAppSettings}}
  [CustomFileSystemConfigs](#cfn-sagemaker-domain-usersettings-customfilesystemconfigs): {{
    - CustomFileSystemConfig}}
  [CustomPosixUserConfig](#cfn-sagemaker-domain-usersettings-customposixuserconfig): {{
    CustomPosixUserConfig}}
  [DefaultLandingUri](#cfn-sagemaker-domain-usersettings-defaultlandinguri): {{String}}
  [ExecutionRole](#cfn-sagemaker-domain-usersettings-executionrole): {{String}}
  [JupyterLabAppSettings](#cfn-sagemaker-domain-usersettings-jupyterlabappsettings): {{
    JupyterLabAppSettings}}
  [JupyterServerAppSettings](#cfn-sagemaker-domain-usersettings-jupyterserverappsettings): {{
    JupyterServerAppSettings}}
  [KernelGatewayAppSettings](#cfn-sagemaker-domain-usersettings-kernelgatewayappsettings): {{
    KernelGatewayAppSettings}}
  [RSessionAppSettings](#cfn-sagemaker-domain-usersettings-rsessionappsettings): {{
    RSessionAppSettings}}
  [RStudioServerProAppSettings](#cfn-sagemaker-domain-usersettings-rstudioserverproappsettings): {{
    RStudioServerProAppSettings}}
  [SecurityGroups](#cfn-sagemaker-domain-usersettings-securitygroups): {{
    - String}}
  [SharingSettings](#cfn-sagemaker-domain-usersettings-sharingsettings): {{
    SharingSettings}}
  [SpaceStorageSettings](#cfn-sagemaker-domain-usersettings-spacestoragesettings): {{
    DefaultSpaceStorageSettings}}
  [StudioWebPortal](#cfn-sagemaker-domain-usersettings-studiowebportal): {{String}}
  [StudioWebPortalSettings](#cfn-sagemaker-domain-usersettings-studiowebportalsettings): {{
    StudioWebPortalSettings}}
```

## Properties
<a name="aws-properties-sagemaker-domain-usersettings-properties"></a>

`AutoMountHomeEFS`  <a name="cfn-sagemaker-domain-usersettings-automounthomeefs"></a>
Indicates whether auto-mounting of an EFS volume is supported for the user profile. The `DefaultAsDomain` value is only supported for user profiles. Do not use the `DefaultAsDomain` value when setting this parameter for a domain.
SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesn't apply this setting to shared spaces.
*Required*: No
*Type*: String
*Allowed values*: `Enabled | Disabled | DefaultAsDomain`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeEditorAppSettings`  <a name="cfn-sagemaker-domain-usersettings-codeeditorappsettings"></a>
The Code Editor application settings.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
*Required*: No
*Type*: [CodeEditorAppSettings](aws-properties-sagemaker-domain-codeeditorappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomFileSystemConfigs`  <a name="cfn-sagemaker-domain-usersettings-customfilesystemconfigs"></a>
The settings for assigning a custom file system to a user profile. Permitted users can access this file system in Amazon SageMaker AI Studio.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
*Required*: No
*Type*: Array of [CustomFileSystemConfig](aws-properties-sagemaker-domain-customfilesystemconfig.md)
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomPosixUserConfig`  <a name="cfn-sagemaker-domain-usersettings-customposixuserconfig"></a>
Details about the POSIX identity that is used for file system operations.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
*Required*: No
*Type*: [CustomPosixUserConfig](aws-properties-sagemaker-domain-customposixuserconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultLandingUri`  <a name="cfn-sagemaker-domain-usersettings-defaultlandinguri"></a>
The default experience that the user is directed to when accessing the domain. The supported values are:
+ `studio::`: Indicates that Studio is the default experience. This value can only be passed if `StudioWebPortal` is set to `ENABLED`.
+ `app:JupyterServer:`: Indicates that Studio Classic is the default experience.
*Required*: No
*Type*: String
*Maximum*: `1023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-sagemaker-domain-usersettings-executionrole"></a>
The execution role for the user.
SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesn't apply this setting to shared spaces.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterLabAppSettings`  <a name="cfn-sagemaker-domain-usersettings-jupyterlabappsettings"></a>
The settings for the JupyterLab application.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
*Required*: No
*Type*: [JupyterLabAppSettings](aws-properties-sagemaker-domain-jupyterlabappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JupyterServerAppSettings`  <a name="cfn-sagemaker-domain-usersettings-jupyterserverappsettings"></a>
The Jupyter server's app settings.
*Required*: No
*Type*: [JupyterServerAppSettings](aws-properties-sagemaker-domain-jupyterserverappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KernelGatewayAppSettings`  <a name="cfn-sagemaker-domain-usersettings-kernelgatewayappsettings"></a>
The kernel gateway app settings.
*Required*: No
*Type*: [KernelGatewayAppSettings](aws-properties-sagemaker-domain-kernelgatewayappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RSessionAppSettings`  <a name="cfn-sagemaker-domain-usersettings-rsessionappsettings"></a>
A collection of settings that configure the `RSessionGateway` app.
*Required*: No
*Type*: [RSessionAppSettings](aws-properties-sagemaker-domain-rsessionappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RStudioServerProAppSettings`  <a name="cfn-sagemaker-domain-usersettings-rstudioserverproappsettings"></a>
A collection of settings that configure user interaction with the `RStudioServerPro` app.
*Required*: No
*Type*: [RStudioServerProAppSettings](aws-properties-sagemaker-domain-rstudioserverproappsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroups`  <a name="cfn-sagemaker-domain-usersettings-securitygroups"></a>
The security groups for the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.
Optional when the `CreateDomain.AppNetworkAccessType` parameter is set to `PublicInternetOnly`.
Required when the `CreateDomain.AppNetworkAccessType` parameter is set to `VpcOnly`, unless specified as part of the `DefaultUserSettings` for the domain.
Amazon SageMaker AI adds a security group to allow NFS traffic from Amazon SageMaker AI Studio. Therefore, the number of security groups that you can specify is one less than the maximum number shown.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `32 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SharingSettings`  <a name="cfn-sagemaker-domain-usersettings-sharingsettings"></a>
Specifies options for sharing Amazon SageMaker AI Studio notebooks.
*Required*: No
*Type*: [SharingSettings](aws-properties-sagemaker-domain-sharingsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpaceStorageSettings`  <a name="cfn-sagemaker-domain-usersettings-spacestoragesettings"></a>
The storage settings for a space.
SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.
*Required*: No
*Type*: [DefaultSpaceStorageSettings](aws-properties-sagemaker-domain-defaultspacestoragesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StudioWebPortal`  <a name="cfn-sagemaker-domain-usersettings-studiowebportal"></a>
Whether the user can access Studio. If this value is set to `DISABLED`, the user cannot access Studio, even if that is the default experience for the domain.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StudioWebPortalSettings`  <a name="cfn-sagemaker-domain-usersettings-studiowebportalsettings"></a>
Studio settings. If these settings are applied on a user level, they take priority over the settings applied on a domain level.
*Required*: No
*Type*: [StudioWebPortalSettings](aws-properties-sagemaker-domain-studiowebportalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
