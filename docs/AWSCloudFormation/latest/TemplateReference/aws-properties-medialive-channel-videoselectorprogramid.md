---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-videoselectorprogramid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel VideoSelectorProgramId
<a name="aws-properties-medialive-channel-videoselectorprogramid"></a>

Used to extract video by the program ID.

The parent of this entity is VideoSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-videoselectorprogramid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-videoselectorprogramid-syntax.json"></a>

```
{
  "[ProgramId](#cfn-medialive-channel-videoselectorprogramid-programid)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-videoselectorprogramid-syntax.yaml"></a>

```
  [ProgramId](#cfn-medialive-channel-videoselectorprogramid-programid): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-videoselectorprogramid-properties"></a>

`ProgramId`  <a name="cfn-medialive-channel-videoselectorprogramid-programid"></a>
Selects a specific program from within a multi-program transport stream. If the program doesn't exist, MediaLive selects the first program within the transport stream by default.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
