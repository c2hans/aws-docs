---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-logconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration LogConfiguration
<a name="aws-properties-mediatailor-playbackconfiguration-logconfiguration"></a>

Defines where AWS Elemental MediaTailor sends logs for the playback configuration.

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-logconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-logconfiguration-syntax.json"></a>

```
{
  "[AdsInteractionLog](#cfn-mediatailor-playbackconfiguration-logconfiguration-adsinteractionlog)" : {{AdsInteractionLog}},
  "[EnabledLoggingStrategies](#cfn-mediatailor-playbackconfiguration-logconfiguration-enabledloggingstrategies)" : {{[ String, ... ]}},
  "[ManifestServiceInteractionLog](#cfn-mediatailor-playbackconfiguration-logconfiguration-manifestserviceinteractionlog)" : {{ManifestServiceInteractionLog}},
  "[PercentEnabled](#cfn-mediatailor-playbackconfiguration-logconfiguration-percentenabled)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-logconfiguration-syntax.yaml"></a>

```
  [AdsInteractionLog](#cfn-mediatailor-playbackconfiguration-logconfiguration-adsinteractionlog): {{
    AdsInteractionLog}}
  [EnabledLoggingStrategies](#cfn-mediatailor-playbackconfiguration-logconfiguration-enabledloggingstrategies): {{
    - String}}
  [ManifestServiceInteractionLog](#cfn-mediatailor-playbackconfiguration-logconfiguration-manifestserviceinteractionlog): {{
    ManifestServiceInteractionLog}}
  [PercentEnabled](#cfn-mediatailor-playbackconfiguration-logconfiguration-percentenabled): {{Integer}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-logconfiguration-properties"></a>

`AdsInteractionLog`  <a name="cfn-mediatailor-playbackconfiguration-logconfiguration-adsinteractionlog"></a>
Settings for customizing what events are included in logs for interactions with the ad decision server (ADS).
*Required*: No
*Type*: [AdsInteractionLog](aws-properties-mediatailor-playbackconfiguration-adsinteractionlog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnabledLoggingStrategies`  <a name="cfn-mediatailor-playbackconfiguration-logconfiguration-enabledloggingstrategies"></a>
The method used for collecting logs from AWS Elemental MediaTailor. `LEGACY_CLOUDWATCH` indicates that MediaTailor is sending logs directly to Amazon CloudWatch Logs. `VENDED_LOGS` indicates that MediaTailor is sending logs to CloudWatch, which then vends the logs to your destination of choice. Supported destinations are CloudWatch Logs log group, Amazon S3 bucket, and Amazon Data Firehose stream.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManifestServiceInteractionLog`  <a name="cfn-mediatailor-playbackconfiguration-logconfiguration-manifestserviceinteractionlog"></a>
Settings for customizing what events are included in logs for interactions with the origin server.
*Required*: No
*Type*: [ManifestServiceInteractionLog](aws-properties-mediatailor-playbackconfiguration-manifestserviceinteractionlog.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PercentEnabled`  <a name="cfn-mediatailor-playbackconfiguration-logconfiguration-percentenabled"></a>
The percentage of session logs that MediaTailor sends to your configured log destination. For example, if your playback configuration has 1000 sessions and `percentEnabled` is set to `60`, MediaTailor sends logs for 600 of the sessions to CloudWatch Logs. MediaTailor decides at random which of the playback configuration sessions to send logs for. If you want to view logs for a specific session, you can use the [debug log mode](https://docs.aws.amazon.com/mediatailor/latest/ug/debug-log-mode.html).
Valid values: `0` - `100`
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
