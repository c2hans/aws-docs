---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-adsinteractionlog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AdsInteractionLog
<a name="aws-properties-mediatailor-playbackconfiguration-adsinteractionlog"></a>

Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).

For more information about ADS logs, inlcuding descriptions of the event types, see [MediaTailor ADS logs description and event types](https://docs.aws.amazon.com/mediatailor/latest/ug/ads-log-format.html) in AWS Elemental MediaTailor User Guide.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-adsinteractionlog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-adsinteractionlog-syntax.json"></a>

```
{
  "[ExcludeEventTypes](#cfn-mediatailor-playbackconfiguration-adsinteractionlog-excludeeventtypes)" : {{[ String, ... ]}},
  "[PublishOptInEventTypes](#cfn-mediatailor-playbackconfiguration-adsinteractionlog-publishoptineventtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-adsinteractionlog-syntax.yaml"></a>

```
  [ExcludeEventTypes](#cfn-mediatailor-playbackconfiguration-adsinteractionlog-excludeeventtypes): {{
    - String}}
  [PublishOptInEventTypes](#cfn-mediatailor-playbackconfiguration-adsinteractionlog-publishoptineventtypes): {{
    - String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-adsinteractionlog-properties"></a>

`ExcludeEventTypes`  <a name="cfn-mediatailor-playbackconfiguration-adsinteractionlog-excludeeventtypes"></a>
Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublishOptInEventTypes`  <a name="cfn-mediatailor-playbackconfiguration-adsinteractionlog-publishoptineventtypes"></a>
Indicates that MediaTailor emits `RAW_ADS_RESPONSE` logs for playback sessions that are initialized with this configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
