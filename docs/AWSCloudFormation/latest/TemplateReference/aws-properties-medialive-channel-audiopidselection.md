---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiopidselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioPidSelection
<a name="aws-properties-medialive-channel-audiopidselection"></a>

Used to extract audio by The PID.

The parent of this entity is AudioSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-audiopidselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiopidselection-syntax.json"></a>

```
{
  "[Pid](#cfn-medialive-channel-audiopidselection-pid)" : {{Integer}},
  "[Pids](#cfn-medialive-channel-audiopidselection-pids)" : {{[ AudioPid, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiopidselection-syntax.yaml"></a>

```
  [Pid](#cfn-medialive-channel-audiopidselection-pid): {{Integer}}
  [Pids](#cfn-medialive-channel-audiopidselection-pids): {{
    - AudioPid}}
```

## Properties
<a name="aws-properties-medialive-channel-audiopidselection-properties"></a>

`Pid`  <a name="cfn-medialive-channel-audiopidselection-pid"></a>
Select the audio by this PID.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pids`  <a name="cfn-medialive-channel-audiopidselection-pids"></a>
Selects one or more unique packet identifiers (PIDs) from within a source. When using PIDs, you can specify per-PID audio pre-mixer settings.
*Required*: No
*Type*: Array of [AudioPid](aws-properties-medialive-channel-audiopid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
