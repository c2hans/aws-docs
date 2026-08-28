---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-smpte2110receivergroupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input Smpte2110ReceiverGroupSettings
<a name="aws-properties-medialive-input-smpte2110receivergroupsettings"></a>

Include this parameter if the input is a SMPTE 2110 input, to identify the stream sources for this input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-smpte2110receivergroupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-smpte2110receivergroupsettings-syntax.json"></a>

```
{
  "[Smpte2110ReceiverGroups](#cfn-medialive-input-smpte2110receivergroupsettings-smpte2110receivergroups)" : {{[ Smpte2110ReceiverGroup, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-input-smpte2110receivergroupsettings-syntax.yaml"></a>

```
  [Smpte2110ReceiverGroups](#cfn-medialive-input-smpte2110receivergroupsettings-smpte2110receivergroups): {{
    - Smpte2110ReceiverGroup}}
```

## Properties
<a name="aws-properties-medialive-input-smpte2110receivergroupsettings-properties"></a>

`Smpte2110ReceiverGroups`  <a name="cfn-medialive-input-smpte2110receivergroupsettings-smpte2110receivergroups"></a>
The list of SMPTE 2110 receiver groups for this input. Each receiver group is a collection of video, audio, and ancillary streams that you want to group together.
*Required*: No
*Type*: Array of [Smpte2110ReceiverGroup](aws-properties-medialive-input-smpte2110receivergroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
