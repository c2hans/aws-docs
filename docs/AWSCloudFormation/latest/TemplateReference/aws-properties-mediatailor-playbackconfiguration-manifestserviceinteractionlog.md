---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration ManifestServiceInteractionLog
<a name="aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog"></a>

Settings for customizing what events are included in logs for interactions with the origin server.

For more information about manifest service logs, including descriptions of the event types, see [MediaTailor manifest logs description and event types](https://docs.aws.amazon.com/mediatailor/latest/ug/log-types.html) in AWS Elemental MediaTailor User Guide.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog-syntax.json"></a>

```
{
  "[ExcludeEventTypes](#cfn-mediatailor-playbackconfiguration-manifestserviceinteractionlog-excludeeventtypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog-syntax.yaml"></a>

```
  [ExcludeEventTypes](#cfn-mediatailor-playbackconfiguration-manifestserviceinteractionlog-excludeeventtypes): {{
    - String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog-properties"></a>

`ExcludeEventTypes`  <a name="cfn-mediatailor-playbackconfiguration-manifestserviceinteractionlog-excludeeventtypes"></a>
Indicates that MediaTailor won't emit the selected events in the logs for playback sessions that are initialized with this configuration.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
