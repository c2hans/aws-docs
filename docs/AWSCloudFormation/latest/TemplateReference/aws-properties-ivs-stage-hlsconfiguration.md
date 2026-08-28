---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-stage-hlsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Stage HlsConfiguration
<a name="aws-properties-ivs-stage-hlsconfiguration"></a>

Object specifying an HLS configuration for individual participant recording.

## Syntax
<a name="aws-properties-ivs-stage-hlsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-stage-hlsconfiguration-syntax.json"></a>

```
{
  "[ParticipantRecordingHlsConfiguration](#cfn-ivs-stage-hlsconfiguration-participantrecordinghlsconfiguration)" : {{ParticipantRecordingHlsConfiguration}}
}
```

### YAML
<a name="aws-properties-ivs-stage-hlsconfiguration-syntax.yaml"></a>

```
  [ParticipantRecordingHlsConfiguration](#cfn-ivs-stage-hlsconfiguration-participantrecordinghlsconfiguration): {{
    ParticipantRecordingHlsConfiguration}}
```

## Properties
<a name="aws-properties-ivs-stage-hlsconfiguration-properties"></a>

`ParticipantRecordingHlsConfiguration`  <a name="cfn-ivs-stage-hlsconfiguration-participantrecordinghlsconfiguration"></a>
Object specifying a configuration of participant HLS recordings for individual participant recording.
*Required*: No
*Type*: [ParticipantRecordingHlsConfiguration](aws-properties-ivs-stage-participantrecordinghlsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
