---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ImageBuilderAgentAccessConfigForUpdate.html
---

# ImageBuilderAgentAccessConfigForUpdate
<a name="API_ImageBuilderAgentAccessConfigForUpdate"></a>

The configuration for updating agent access on an image builder. This type supports partial updates, so you only need to specify the fields you want to change. Fields that you omit keep their stored values.

## Contents
<a name="API_ImageBuilderAgentAccessConfigForUpdate_Contents"></a>

 ** S3BucketArn **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfigForUpdate-S3BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots are stored. If ScreenshotsUploadEnabled is false after the merge, the stored bucket ARN is removed.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:s3:::[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]$`
Required: No

 ** ScreenImageFormat **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfigForUpdate-ScreenImageFormat"></a>
The image format for agent screen captures.
+ PNG - PNG format.
+ JPEG - JPEG format.
Type: String
Valid Values: `PNG | JPEG`
Required: No

 ** ScreenResolution **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfigForUpdate-ScreenResolution"></a>
The screen resolution for the agent streaming environment.
+ W\_1280xH\_720 - 1280 x 720 pixels.
Type: String
Valid Values: `W_1280xH_720`
Required: No

 ** ScreenshotsUploadEnabled **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfigForUpdate-ScreenshotsUploadEnabled"></a>
Specifies whether screenshot uploads to Amazon S3 are enabled for agent sessions.
Type: Boolean
Required: No

 ** Settings **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfigForUpdate-Settings"></a>
The list of agent access settings that define permissions for each agent action. These settings are merged with the stored settings by agent action. A setting that you specify replaces the stored setting for the same agent action. The merged settings must have at least one agent action enabled.
Type: Array of [AgentAccessSetting](API_AgentAccessSetting.md) objects
Required: No

 ** UserControlMode **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfigForUpdate-UserControlMode"></a>
The user control mode for agent sessions. This setting determines how users can interact with agent sessions.
+ VIEW\_ONLY - Users can view and observe agent actions as they happen.
+ VIEW\_STOP - Users can view agent actions and stop the agent if needed.
+ DISABLED - Users cannot view or stop the agent session.
Type: String
Valid Values: `VIEW_ONLY | VIEW_STOP | DISABLED`
Required: No

## See Also
<a name="API_ImageBuilderAgentAccessConfigForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ImageBuilderAgentAccessConfigForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ImageBuilderAgentAccessConfigForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ImageBuilderAgentAccessConfigForUpdate)
