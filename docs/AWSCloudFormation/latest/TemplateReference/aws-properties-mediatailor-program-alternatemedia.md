---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-alternatemedia.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program AlternateMedia
<a name="aws-properties-mediatailor-program-alternatemedia"></a>

A playlist of media (VOD and/or live) to be played instead of the default media on a particular program.

## Syntax
<a name="aws-properties-mediatailor-program-alternatemedia-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-alternatemedia-syntax.json"></a>

```
{
  "[AdBreaks](#cfn-mediatailor-program-alternatemedia-adbreaks)" : {{[ AdBreak, ... ]}},
  "[ClipRange](#cfn-mediatailor-program-alternatemedia-cliprange)" : {{ClipRange}},
  "[DurationMillis](#cfn-mediatailor-program-alternatemedia-durationmillis)" : {{Integer}},
  "[LiveSourceName](#cfn-mediatailor-program-alternatemedia-livesourcename)" : {{String}},
  "[ScheduledStartTimeMillis](#cfn-mediatailor-program-alternatemedia-scheduledstarttimemillis)" : {{Integer}},
  "[SourceLocationName](#cfn-mediatailor-program-alternatemedia-sourcelocationname)" : {{String}},
  "[VodSourceName](#cfn-mediatailor-program-alternatemedia-vodsourcename)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-alternatemedia-syntax.yaml"></a>

```
  [AdBreaks](#cfn-mediatailor-program-alternatemedia-adbreaks): {{
    - AdBreak}}
  [ClipRange](#cfn-mediatailor-program-alternatemedia-cliprange): {{
    ClipRange}}
  [DurationMillis](#cfn-mediatailor-program-alternatemedia-durationmillis): {{Integer}}
  [LiveSourceName](#cfn-mediatailor-program-alternatemedia-livesourcename): {{String}}
  [ScheduledStartTimeMillis](#cfn-mediatailor-program-alternatemedia-scheduledstarttimemillis): {{Integer}}
  [SourceLocationName](#cfn-mediatailor-program-alternatemedia-sourcelocationname): {{String}}
  [VodSourceName](#cfn-mediatailor-program-alternatemedia-vodsourcename): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-program-alternatemedia-properties"></a>

`AdBreaks`  <a name="cfn-mediatailor-program-alternatemedia-adbreaks"></a>
Ad break configuration parameters defined in AlternateMedia.
*Required*: No
*Type*: Array of [AdBreak](aws-properties-mediatailor-program-adbreak.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClipRange`  <a name="cfn-mediatailor-program-alternatemedia-cliprange"></a>
Property description not available.
*Required*: No
*Type*: [ClipRange](aws-properties-mediatailor-program-cliprange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DurationMillis`  <a name="cfn-mediatailor-program-alternatemedia-durationmillis"></a>
The duration of the alternateMedia in milliseconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LiveSourceName`  <a name="cfn-mediatailor-program-alternatemedia-livesourcename"></a>
The name of the live source for alternateMedia.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduledStartTimeMillis`  <a name="cfn-mediatailor-program-alternatemedia-scheduledstarttimemillis"></a>
The date and time that the alternateMedia is scheduled to start, in epoch milliseconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLocationName`  <a name="cfn-mediatailor-program-alternatemedia-sourcelocationname"></a>
The name of the source location for alternateMedia.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VodSourceName`  <a name="cfn-mediatailor-program-alternatemedia-vodsourcename"></a>
The name of the VOD source for alternateMedia.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
