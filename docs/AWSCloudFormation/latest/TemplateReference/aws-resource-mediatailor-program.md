---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediatailor-program.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program
<a name="aws-resource-mediatailor-program"></a>

Creates a program within a channel. For information about programs, see [Working with programs](https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-programs.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-resource-mediatailor-program-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediatailor-program-syntax.json"></a>

```
{
  "Type" : "AWS::MediaTailor::Program",
  "Properties" : {
      "[AdBreaks](#cfn-mediatailor-program-adbreaks)" : {{[ AdBreak, ... ]}},
      "[AudienceMedia](#cfn-mediatailor-program-audiencemedia)" : {{[ AudienceMedia, ... ]}},
      "[ChannelName](#cfn-mediatailor-program-channelname)" : {{String}},
      "[LiveSourceName](#cfn-mediatailor-program-livesourcename)" : {{String}},
      "[ProgramName](#cfn-mediatailor-program-programname)" : {{String}},
      "[ScheduleConfiguration](#cfn-mediatailor-program-scheduleconfiguration)" : {{ScheduleConfiguration}},
      "[SourceLocationName](#cfn-mediatailor-program-sourcelocationname)" : {{String}},
      "[VodSourceName](#cfn-mediatailor-program-vodsourcename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-mediatailor-program-syntax.yaml"></a>

```
Type: AWS::MediaTailor::Program
Properties:
  [AdBreaks](#cfn-mediatailor-program-adbreaks): {{
    - AdBreak}}
  [AudienceMedia](#cfn-mediatailor-program-audiencemedia): {{
    - AudienceMedia}}
  [ChannelName](#cfn-mediatailor-program-channelname): {{String}}
  [LiveSourceName](#cfn-mediatailor-program-livesourcename): {{String}}
  [ProgramName](#cfn-mediatailor-program-programname): {{String}}
  [ScheduleConfiguration](#cfn-mediatailor-program-scheduleconfiguration): {{
    ScheduleConfiguration}}
  [SourceLocationName](#cfn-mediatailor-program-sourcelocationname): {{String}}
  [VodSourceName](#cfn-mediatailor-program-vodsourcename): {{String}}
```

## Properties
<a name="aws-resource-mediatailor-program-properties"></a>

`AdBreaks`  <a name="cfn-mediatailor-program-adbreaks"></a>
Property description not available.
*Required*: No
*Type*: Array of [AdBreak](aws-properties-mediatailor-program-adbreak.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudienceMedia`  <a name="cfn-mediatailor-program-audiencemedia"></a>
An AudienceMedia object contains an Audience and a list of AlternateMedia.
*Required*: No
*Type*: [Array](aws-properties-mediatailor-program-audiencemedia.md) of [AudienceMedia](aws-properties-mediatailor-program-audiencemedia.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelName`  <a name="cfn-mediatailor-program-channelname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LiveSourceName`  <a name="cfn-mediatailor-program-livesourcename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProgramName`  <a name="cfn-mediatailor-program-programname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ScheduleConfiguration`  <a name="cfn-mediatailor-program-scheduleconfiguration"></a>
Schedule configuration parameters. A channel must be stopped before changes can be made to the schedule.
*Required*: No
*Type*: [ScheduleConfiguration](aws-properties-mediatailor-program-scheduleconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceLocationName`  <a name="cfn-mediatailor-program-sourcelocationname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VodSourceName`  <a name="cfn-mediatailor-program-vodsourcename"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-mediatailor-program-return-values"></a>

### Ref
<a name="aws-resource-mediatailor-program-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediatailor-program-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediatailor-program-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
Property description not available.

`DurationMillis`  <a name="DurationMillis-fn::getatt"></a>
The duration of the live program in seconds.

`ScheduledStartTime`  <a name="ScheduledStartTime-fn::getatt"></a>
Property description not available.
