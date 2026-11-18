---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ImageBuilderAgentAccessConfig.html
---

# ImageBuilderAgentAccessConfig
<a name="API_ImageBuilderAgentAccessConfig"></a>

The configuration for agent access on an image builder. Agent access enables AI agents to interact with desktop applications during streaming sessions to the image builder.

## Contents
<a name="API_ImageBuilderAgentAccessConfig_Contents"></a>

 ** ScreenImageFormat **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfig-ScreenImageFormat"></a>
The image format for agent screen captures.
+ PNG - PNG format.
+ JPEG - JPEG format.
Type: String
Valid Values: `PNG | JPEG`
Required: Yes

 ** ScreenResolution **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfig-ScreenResolution"></a>
The screen resolution for the agent streaming environment.
+ W\_1280xH\_720 - 1280 x 720 pixels.
Type: String
Valid Values: `W_1280xH_720`
Required: Yes

 ** Settings **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfig-Settings"></a>
The list of agent access settings that define permissions for each agent action. You must specify at least one setting, and at least one agent action must be enabled.
Type: Array of [AgentAccessSetting](API_AgentAccessSetting.md) objects
Required: Yes

 ** S3BucketArn **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfig-S3BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots are stored. Required when ScreenshotsUploadEnabled is true.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:s3:::[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]$`
Required: No

 ** ScreenshotsUploadEnabled **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfig-ScreenshotsUploadEnabled"></a>
Specifies whether screenshot uploads to Amazon S3 are enabled for agent sessions.
Type: Boolean
Required: No

 ** UserControlMode **   <a name="WorkSpacesApplications-Type-ImageBuilderAgentAccessConfig-UserControlMode"></a>
The user control mode for agent sessions. This setting determines how users can interact with agent sessions.
+ VIEW\_ONLY - Users can view and observe agent actions as they happen.
+ VIEW\_STOP - Users can view agent actions and stop the agent if needed.
+ DISABLED - Users cannot view or stop the agent session.
Type: String
Valid Values: `VIEW_ONLY | VIEW_STOP | DISABLED`
Required: No

## See Also
<a name="API_ImageBuilderAgentAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ImageBuilderAgentAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ImageBuilderAgentAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ImageBuilderAgentAccessConfig)
