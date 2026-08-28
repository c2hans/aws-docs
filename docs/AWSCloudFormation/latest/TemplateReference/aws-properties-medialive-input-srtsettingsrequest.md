---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-srtsettingsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input SrtSettingsRequest
<a name="aws-properties-medialive-input-srtsettingsrequest"></a>

The settings associated with an SRT input.

The parent of this entity is Input.

## Syntax
<a name="aws-properties-medialive-input-srtsettingsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-srtsettingsrequest-syntax.json"></a>

```
{
  "[SrtCallerSources](#cfn-medialive-input-srtsettingsrequest-srtcallersources)" : {{[ SrtCallerSourceRequest, ... ]}},
  "[SrtListenerSettings](#cfn-medialive-input-srtsettingsrequest-srtlistenersettings)" : {{SrtListenerSettingsRequest}}
}
```

### YAML
<a name="aws-properties-medialive-input-srtsettingsrequest-syntax.yaml"></a>

```
  [SrtCallerSources](#cfn-medialive-input-srtsettingsrequest-srtcallersources): {{
    - SrtCallerSourceRequest}}
  [SrtListenerSettings](#cfn-medialive-input-srtsettingsrequest-srtlistenersettings): {{
    SrtListenerSettingsRequest}}
```

## Properties
<a name="aws-properties-medialive-input-srtsettingsrequest-properties"></a>

`SrtCallerSources`  <a name="cfn-medialive-input-srtsettingsrequest-srtcallersources"></a>
The list of SRT caller sources for this input. Use this when MediaLive is the caller connecting to upstream SRT listeners.
*Required*: No
*Type*: Array of [SrtCallerSourceRequest](aws-properties-medialive-input-srtcallersourcerequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtListenerSettings`  <a name="cfn-medialive-input-srtsettingsrequest-srtlistenersettings"></a>
Configuration for SRT listener input. Use this when MediaLive is the listener accepting connections from upstream SRT callers.
*Required*: No
*Type*: [SrtListenerSettingsRequest](aws-properties-medialive-input-srtlistenersettingsrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
