---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AgentAccessConfig.html
---

# AgentAccessConfig

The configuration for agent access on a stack. Agent access enables AI agents to interact with desktop applications during streaming sessions.

## Contents
<a name="API_AgentAccessConfig_Contents"></a>

 ** ScreenImageFormat **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-ScreenImageFormat"></a>
The image format for agent screen captures.
Type: String
Valid Values: `PNG | JPEG`
Required: Yes

 ** ScreenResolution **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-ScreenResolution"></a>
The screen resolution for the agent streaming environment.
Type: String
Valid Values: `W_1280xH_720`
Required: Yes

 ** Settings **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-Settings"></a>
The list of agent access settings that define permissions for each agent action. You must specify at least one setting, and at least one agent action must be enabled.
Type: Array of [AgentAccessSetting](API_AgentAccessSetting.md) objects
Required: Yes

 ** KmsKeyArn **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer managed symmetric encryption KMS key that encrypts Replay Session artifacts while WorkSpaces Applications processes them. The key must be in the same Region as the stack, and ReplaySessionEnabled must be true.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:kms:[a-z0-9\-]+:\d{12}:key/[A-Za-z0-9\-]+$`
Required: No

 ** ReplaySessionEnabled **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-ReplaySessionEnabled"></a>
Indicates whether Replay Session is enabled for agent sessions. WorkSpaces Applications delivers a video combining session screenshots, a transcript, and a report for each session. Requires the COMPUTER\_VISION agent action.
Type: Boolean
Required: No

 ** S3BucketArn **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-S3BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots and Replay Session artifacts are stored. Required when ScreenshotsUploadEnabled or ReplaySessionEnabled is true.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:s3:::[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]$`
Required: No

 ** ScreenshotsUploadEnabled **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-ScreenshotsUploadEnabled"></a>
Indicates whether screenshot uploads to Amazon S3 are enabled for agent sessions.
Type: Boolean
Required: No

 ** UserControlMode **   <a name="WorkSpacesApplications-Type-AgentAccessConfig-UserControlMode"></a>
The user control mode for agent sessions. This setting determines how users can interact with agent sessions.
Type: String
Valid Values: `VIEW_ONLY | VIEW_STOP | DISABLED`
Required: No

## See Also
<a name="API_AgentAccessConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AgentAccessConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AgentAccessConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AgentAccessConfig)
