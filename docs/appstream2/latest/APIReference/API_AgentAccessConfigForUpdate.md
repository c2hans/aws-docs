---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AgentAccessConfigForUpdate.html
---

# AgentAccessConfigForUpdate
<a name="API_AgentAccessConfigForUpdate"></a>

The configuration for updating agent access on a stack. This type supports partial updates, so you only need to specify the fields you want to change.

## Contents
<a name="API_AgentAccessConfigForUpdate_Contents"></a>

 ** S3BucketArn **   <a name="WorkSpacesApplications-Type-AgentAccessConfigForUpdate-S3BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots are stored.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:s3:::[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]$`
Required: No

 ** ScreenImageFormat **   <a name="WorkSpacesApplications-Type-AgentAccessConfigForUpdate-ScreenImageFormat"></a>
The image format for agent screen captures.
Type: String
Valid Values: `PNG | JPEG`
Required: No

 ** ScreenResolution **   <a name="WorkSpacesApplications-Type-AgentAccessConfigForUpdate-ScreenResolution"></a>
The screen resolution for the agent streaming environment.
Type: String
Valid Values: `W_1280xH_720`
Required: No

 ** ScreenshotsUploadEnabled **   <a name="WorkSpacesApplications-Type-AgentAccessConfigForUpdate-ScreenshotsUploadEnabled"></a>
Indicates whether screenshot uploads to Amazon S3 are enabled for agent sessions.
Type: Boolean
Required: No

 ** Settings **   <a name="WorkSpacesApplications-Type-AgentAccessConfigForUpdate-Settings"></a>
The list of agent access settings that define permissions for each agent action.
Type: Array of [AgentAccessSetting](API_AgentAccessSetting.md) objects
Required: No

 ** UserControlMode **   <a name="WorkSpacesApplications-Type-AgentAccessConfigForUpdate-UserControlMode"></a>
The user control mode for agent sessions. This setting determines how users can interact with agent sessions.
Type: String
Valid Values: `VIEW_ONLY | VIEW_STOP | DISABLED`
Required: No

## See Also
<a name="API_AgentAccessConfigForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AgentAccessConfigForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AgentAccessConfigForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AgentAccessConfigForUpdate)
