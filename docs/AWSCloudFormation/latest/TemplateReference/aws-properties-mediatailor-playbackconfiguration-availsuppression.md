---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-playbackconfiguration-availsuppression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::PlaybackConfiguration AvailSuppression
<a name="aws-properties-mediatailor-playbackconfiguration-availsuppression"></a>

The configuration for avail suppression, also known as ad suppression. For more information about ad suppression, see [Ad Suppression](https://docs.aws.amazon.com/mediatailor/latest/ug/ad-behavior.html).

## Syntax
<a name="aws-properties-mediatailor-playbackconfiguration-availsuppression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-playbackconfiguration-availsuppression-syntax.json"></a>

```
{
  "[FillPolicy](#cfn-mediatailor-playbackconfiguration-availsuppression-fillpolicy)" : {{String}},
  "[Mode](#cfn-mediatailor-playbackconfiguration-availsuppression-mode)" : {{String}},
  "[Value](#cfn-mediatailor-playbackconfiguration-availsuppression-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-playbackconfiguration-availsuppression-syntax.yaml"></a>

```
  [FillPolicy](#cfn-mediatailor-playbackconfiguration-availsuppression-fillpolicy): {{String}}
  [Mode](#cfn-mediatailor-playbackconfiguration-availsuppression-mode): {{String}}
  [Value](#cfn-mediatailor-playbackconfiguration-availsuppression-value): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-playbackconfiguration-availsuppression-properties"></a>

`FillPolicy`  <a name="cfn-mediatailor-playbackconfiguration-availsuppression-fillpolicy"></a>
Defines the policy to apply to the avail suppression mode. `BEHIND_LIVE_EDGE` will always use the full avail suppression policy. `AFTER_LIVE_EDGE` mode can be used to invoke partial ad break fills when a session starts mid-break.
*Required*: No
*Type*: String
*Allowed values*: `PARTIAL_AVAIL | FULL_AVAIL_ONLY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-mediatailor-playbackconfiguration-availsuppression-mode"></a>
Sets the ad suppression mode. By default, ad suppression is off and all ad breaks are filled with ads or slate. When Mode is set to `BEHIND_LIVE_EDGE`, ad suppression is active and MediaTailor won't fill ad breaks on or behind the ad suppression Value time in the manifest lookback window. When Mode is set to `AFTER_LIVE_EDGE`, ad suppression is active and MediaTailor won't fill ad breaks that are within the live edge plus the avail suppression value.
*Required*: No
*Type*: String
*Allowed values*: `OFF | BEHIND_LIVE_EDGE | AFTER_LIVE_EDGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-mediatailor-playbackconfiguration-availsuppression-value"></a>
A live edge offset time in HH:MM:SS. MediaTailor won't fill ad breaks on or behind this time in the manifest lookback window. If Value is set to 00:00:00, it is in sync with the live edge, and MediaTailor won't fill any ad breaks on or behind the live edge. If you set a Value time, MediaTailor won't fill any ad breaks on or behind this time in the manifest lookback window. For example, if you set 00:45:00, then MediaTailor will fill ad breaks that occur within 45 minutes behind the live edge, but won't fill ad breaks on or behind 45 minutes behind the live edge.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
