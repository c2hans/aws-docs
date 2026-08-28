---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiotrackselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioTrackSelection
<a name="aws-properties-medialive-channel-audiotrackselection"></a>

Information about the audio track to extract.

The parent of this entity is AudioSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-audiotrackselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiotrackselection-syntax.json"></a>

```
{
  "[DolbyEDecode](#cfn-medialive-channel-audiotrackselection-dolbyedecode)" : {{AudioDolbyEDecode}},
  "[Tracks](#cfn-medialive-channel-audiotrackselection-tracks)" : {{[ AudioTrack, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiotrackselection-syntax.yaml"></a>

```
  [DolbyEDecode](#cfn-medialive-channel-audiotrackselection-dolbyedecode): {{
    AudioDolbyEDecode}}
  [Tracks](#cfn-medialive-channel-audiotrackselection-tracks): {{
    - AudioTrack}}
```

## Properties
<a name="aws-properties-medialive-channel-audiotrackselection-properties"></a>

`DolbyEDecode`  <a name="cfn-medialive-channel-audiotrackselection-dolbyedecode"></a>
Configure decoding options for Dolby E streams carried in PCM streams tagged with SMPTE-337.
*Required*: No
*Type*: [AudioDolbyEDecode](aws-properties-medialive-channel-audiodolbyedecode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tracks`  <a name="cfn-medialive-channel-audiotrackselection-tracks"></a>
Selects one or more unique audio tracks from within a source.
*Required*: No
*Type*: Array of [AudioTrack](aws-properties-medialive-channel-audiotrack.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
