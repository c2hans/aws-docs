---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-stage-participantrecordinghlsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Stage ParticipantRecordingHlsConfiguration
<a name="aws-properties-ivs-stage-participantrecordinghlsconfiguration"></a>

Object specifying a configuration of participant HLS recordings for individual participant recording.

## Syntax
<a name="aws-properties-ivs-stage-participantrecordinghlsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-stage-participantrecordinghlsconfiguration-syntax.json"></a>

```
{
  "[TargetSegmentDurationSeconds](#cfn-ivs-stage-participantrecordinghlsconfiguration-targetsegmentdurationseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ivs-stage-participantrecordinghlsconfiguration-syntax.yaml"></a>

```
  [TargetSegmentDurationSeconds](#cfn-ivs-stage-participantrecordinghlsconfiguration-targetsegmentdurationseconds): {{Integer}}
```

## Properties
<a name="aws-properties-ivs-stage-participantrecordinghlsconfiguration-properties"></a>

`TargetSegmentDurationSeconds`  <a name="cfn-ivs-stage-participantrecordinghlsconfiguration-targetsegmentdurationseconds"></a>
Defines the target duration for recorded segments generated when recording a stage participant. Segments may have durations longer than the specified value when needed to ensure each segment begins with a keyframe. Default: 6.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
