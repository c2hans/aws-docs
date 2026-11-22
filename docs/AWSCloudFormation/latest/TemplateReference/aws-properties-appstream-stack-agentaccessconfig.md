---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-agentaccessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack AgentAccessConfig

The configuration for agent access on a stack. Agent access enables AI agents to interact with desktop applications during streaming sessions.

## Syntax
<a name="aws-properties-appstream-stack-agentaccessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-agentaccessconfig-syntax.json"></a>

```json
{
  "[KmsKeyArn](#cfn-appstream-stack-agentaccessconfig-kmskeyarn)" : {{String}},
  "[ReplaySessionEnabled](#cfn-appstream-stack-agentaccessconfig-replaysessionenabled)" : {{Boolean}},
  "[S3BucketArn](#cfn-appstream-stack-agentaccessconfig-s3bucketarn)" : {{String}},
  "[ScreenImageFormat](#cfn-appstream-stack-agentaccessconfig-screenimageformat)" : {{String}},
  "[ScreenResolution](#cfn-appstream-stack-agentaccessconfig-screenresolution)" : {{String}},
  "[ScreenshotsUploadEnabled](#cfn-appstream-stack-agentaccessconfig-screenshotsuploadenabled)" : {{Boolean}},
  "[Settings](#cfn-appstream-stack-agentaccessconfig-settings)" : {{[ AgentAccessSetting, ... ]}},
  "[UserControlMode](#cfn-appstream-stack-agentaccessconfig-usercontrolmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-appstream-stack-agentaccessconfig-syntax.yaml"></a>

```yaml
  [KmsKeyArn](#cfn-appstream-stack-agentaccessconfig-kmskeyarn): {{String}}
  [ReplaySessionEnabled](#cfn-appstream-stack-agentaccessconfig-replaysessionenabled): {{Boolean}}
  [S3BucketArn](#cfn-appstream-stack-agentaccessconfig-s3bucketarn): {{String}}
  [ScreenImageFormat](#cfn-appstream-stack-agentaccessconfig-screenimageformat): {{String}}
  [ScreenResolution](#cfn-appstream-stack-agentaccessconfig-screenresolution): {{String}}
  [ScreenshotsUploadEnabled](#cfn-appstream-stack-agentaccessconfig-screenshotsuploadenabled): {{Boolean}}
  [Settings](#cfn-appstream-stack-agentaccessconfig-settings): {{
    - AgentAccessSetting}}
  [UserControlMode](#cfn-appstream-stack-agentaccessconfig-usercontrolmode): {{String}}
```

## Properties
<a name="aws-properties-appstream-stack-agentaccessconfig-properties"></a>

`KmsKeyArn`  <a name="cfn-appstream-stack-agentaccessconfig-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the customer managed symmetric encryption KMS key that encrypts Replay Session artifacts while WorkSpaces Applications processes them. The key must be in the same Region as the stack, and ReplaySessionEnabled must be true.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:kms:[a-z0-9\-]+:\d{12}:key/[A-Za-z0-9\-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplaySessionEnabled`  <a name="cfn-appstream-stack-agentaccessconfig-replaysessionenabled"></a>
Indicates whether Replay Session is enabled for agent sessions. WorkSpaces Applications delivers a video combining session screenshots, a transcript, and a report for each session. Requires the COMPUTER\_VISION agent action.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3BucketArn`  <a name="cfn-appstream-stack-agentaccessconfig-s3bucketarn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots and Replay Session artifacts are stored. Required when ScreenshotsUploadEnabled or ReplaySessionEnabled is true.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:s3:::[a-z0-9][a-z0-9.\-]{1,61}[a-z0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScreenImageFormat`  <a name="cfn-appstream-stack-agentaccessconfig-screenimageformat"></a>
The image format for agent screen captures.
*Required*: Yes
*Type*: String
*Allowed values*: `PNG | JPEG`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScreenResolution`  <a name="cfn-appstream-stack-agentaccessconfig-screenresolution"></a>
The screen resolution for the agent streaming environment.
*Required*: Yes
*Type*: String
*Allowed values*: `W_1280xH_720`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScreenshotsUploadEnabled`  <a name="cfn-appstream-stack-agentaccessconfig-screenshotsuploadenabled"></a>
Indicates whether screenshot uploads to Amazon S3 are enabled for agent sessions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-appstream-stack-agentaccessconfig-settings"></a>
The list of agent access settings that define permissions for each agent action. You must specify at least one setting, and at least one agent action must be enabled.
*Required*: Yes
*Type*: Array of [AgentAccessSetting](aws-properties-appstream-stack-agentaccesssetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserControlMode`  <a name="cfn-appstream-stack-agentaccessconfig-usercontrolmode"></a>
The user control mode for agent sessions. This setting determines how users can interact with agent sessions.
*Required*: No
*Type*: String
*Allowed values*: `VIEW_ONLY | VIEW_STOP | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
