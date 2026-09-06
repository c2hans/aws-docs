---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-stage-thumbnailconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Stage ThumbnailConfiguration
<a name="aws-properties-ivs-stage-thumbnailconfiguration"></a>

An object representing a configuration of thumbnails for recorded video.

## Syntax
<a name="aws-properties-ivs-stage-thumbnailconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-stage-thumbnailconfiguration-syntax.json"></a>

```
{
  "[ParticipantThumbnailConfiguration](#cfn-ivs-stage-thumbnailconfiguration-participantthumbnailconfiguration)" : {{ParticipantThumbnailConfiguration}}
}
```

### YAML
<a name="aws-properties-ivs-stage-thumbnailconfiguration-syntax.yaml"></a>

```
  [ParticipantThumbnailConfiguration](#cfn-ivs-stage-thumbnailconfiguration-participantthumbnailconfiguration): {{
    ParticipantThumbnailConfiguration}}
```

## Properties
<a name="aws-properties-ivs-stage-thumbnailconfiguration-properties"></a>

`ParticipantThumbnailConfiguration`  <a name="cfn-ivs-stage-thumbnailconfiguration-participantthumbnailconfiguration"></a>
Object specifying a configuration of thumbnails for recorded video from an individual participant.
*Required*: No
*Type*: [ParticipantThumbnailConfiguration](aws-properties-ivs-stage-participantthumbnailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
