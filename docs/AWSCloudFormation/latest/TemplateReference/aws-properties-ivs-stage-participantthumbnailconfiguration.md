---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-stage-participantthumbnailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Stage ParticipantThumbnailConfiguration
<a name="aws-properties-ivs-stage-participantthumbnailconfiguration"></a>

Object specifying a configuration of thumbnails for recorded video from an individual participant.

## Syntax
<a name="aws-properties-ivs-stage-participantthumbnailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-stage-participantthumbnailconfiguration-syntax.json"></a>

```
{
  "[RecordingMode](#cfn-ivs-stage-participantthumbnailconfiguration-recordingmode)" : {{String}},
  "[Storage](#cfn-ivs-stage-participantthumbnailconfiguration-storage)" : {{[ String, ... ]}},
  "[TargetIntervalSeconds](#cfn-ivs-stage-participantthumbnailconfiguration-targetintervalseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ivs-stage-participantthumbnailconfiguration-syntax.yaml"></a>

```
  [RecordingMode](#cfn-ivs-stage-participantthumbnailconfiguration-recordingmode): {{String}}
  [Storage](#cfn-ivs-stage-participantthumbnailconfiguration-storage): {{
    - String}}
  [TargetIntervalSeconds](#cfn-ivs-stage-participantthumbnailconfiguration-targetintervalseconds): {{Integer}}
```

## Properties
<a name="aws-properties-ivs-stage-participantthumbnailconfiguration-properties"></a>

`RecordingMode`  <a name="cfn-ivs-stage-participantthumbnailconfiguration-recordingmode"></a>
Thumbnail recording mode. Default: `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `INTERVAL | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Storage`  <a name="cfn-ivs-stage-participantthumbnailconfiguration-storage"></a>
Indicates the format in which thumbnails are recorded. `SEQUENTIAL` records all generated thumbnails in a serial manner, to the media/thumbnails/high directory. `LATEST` saves the latest thumbnail in media/latest\_thumbnail/high/thumb.jpg and overwrites it at the interval specified by `targetIntervalSeconds`. You can enable both `SEQUENTIAL` and `LATEST`. Default: `SEQUENTIAL`.
*Required*: No
*Type*: Array of String
*Allowed values*: `SEQUENTIAL | LATEST`
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetIntervalSeconds`  <a name="cfn-ivs-stage-participantthumbnailconfiguration-targetintervalseconds"></a>
The targeted thumbnail-generation interval in seconds. This is configurable only if `recordingMode` is `INTERVAL`. Default: 60.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
