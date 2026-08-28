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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
