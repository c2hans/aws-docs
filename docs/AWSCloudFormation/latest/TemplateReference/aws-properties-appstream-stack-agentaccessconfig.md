---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appstream-stack-agentaccessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack AgentAccessConfig
<a name="aws-properties-appstream-stack-agentaccessconfig"></a>

The configuration for agent access on a stack. Agent access enables AI agents to interact with desktop applications during streaming sessions.

## Syntax
<a name="aws-properties-appstream-stack-agentaccessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appstream-stack-agentaccessconfig-syntax.json"></a>

```
{
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

```
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

`S3BucketArn`  <a name="cfn-appstream-stack-agentaccessconfig-s3bucketarn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where agent screenshots are stored. Required when ScreenshotsUploadEnabled is true.
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
The list of agent access settings that define permissions for each agent action. You must specify at least one setting.
*Required*: Yes
*Type*: Array of [AgentAccessSetting](aws-properties-appstream-stack-agentaccesssetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserControlMode`  <a name="cfn-appstream-stack-agentaccessconfig-usercontrolmode"></a>
The user control mode for agent sessions. This setting determines how users can interact with agent sessions.
*Required*: No
*Type*: String
*Allowed values*: `VIEW_ONLY | VIEW_STOP | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
