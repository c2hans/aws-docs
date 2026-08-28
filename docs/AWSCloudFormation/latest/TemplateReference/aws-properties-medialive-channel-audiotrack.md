---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiotrack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioTrack
<a name="aws-properties-medialive-channel-audiotrack"></a>

Information about one audio track to extract. You can select multiple tracks.

The parent of this entity is AudioTrackSelection.

## Syntax
<a name="aws-properties-medialive-channel-audiotrack-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiotrack-syntax.json"></a>

```
{
  "[PremixSettings](#cfn-medialive-channel-audiotrack-premixsettings)" : {{AudioPreMixerSettings}},
  "[Track](#cfn-medialive-channel-audiotrack-track)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiotrack-syntax.yaml"></a>

```
  [PremixSettings](#cfn-medialive-channel-audiotrack-premixsettings): {{
    AudioPreMixerSettings}}
  [Track](#cfn-medialive-channel-audiotrack-track): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-audiotrack-properties"></a>

`PremixSettings`  <a name="cfn-medialive-channel-audiotrack-premixsettings"></a>
The optional audio pre-mixer settings for this track. When specified, the service applies channel remixing, gain adjustment, and loudness normalization to this track before interleaving.
*Required*: No
*Type*: [AudioPreMixerSettings](aws-properties-medialive-channel-audiopremixersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Track`  <a name="cfn-medialive-channel-audiotrack-track"></a>
1-based integer value that maps to a specific audio track
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
