---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-videoselectorpid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel VideoSelectorPid
<a name="aws-properties-medialive-channel-videoselectorpid"></a>

Selects a specific PID from within a video source.

The parent of this entity is VideoSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-videoselectorpid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-videoselectorpid-syntax.json"></a>

```
{
  "[Pid](#cfn-medialive-channel-videoselectorpid-pid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-videoselectorpid-syntax.yaml"></a>

```
  [Pid](#cfn-medialive-channel-videoselectorpid-pid): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-videoselectorpid-properties"></a>

`Pid`  <a name="cfn-medialive-channel-videoselectorpid-pid"></a>
Selects a specific PID from within a video source.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
